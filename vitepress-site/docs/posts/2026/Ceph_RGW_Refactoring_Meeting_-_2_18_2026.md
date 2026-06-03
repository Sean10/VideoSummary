---
title: "Ceph RGW Refactoring Meeting - 2/18/2026"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
  - "RADOS"
  - "OSD"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 RGW Refactoring Meeting 于 2026 年 2 月 18 日举行，主要讨论了两个议题：一是 RGW 中 objector（对象追踪器）introspection 功能当前存在的问题及修复方案；二是 Swift `X-Delete-After` header 的一个已知 bug 及对应 PR 的审查进展。


## 议题一：RGW objector 请求追踪问题（Gruno 主导）

### 背景

Ceph 提供了一个类似 OSD `dump ops` 的功能，可以通过 admin socket 查询 RGW gateway 当前正在向 RADOS 发送的所有请求（即 objector requests）。这对于生产环境排查 RADOS hang、定位阻塞的 PG 或 OSD 非常有价值。

然而，该功能在 RGW 上实际上是**不可用的**，而在 RBD、CephFS 等其他客户端上可以正常工作。

### 根本原因

RGW 当前初始化了**多个 librados 实例**：

- 一个用于 config store
- 一个用于实际的 S3 数据请求（最关键的一个）
- 一个用于 NeoRADOS（异步接口）
- 一个用于 realm watch（近期已有 PR 修复其导致的内存泄漏）

objector 的注册机制存在缺陷：第一个 librados 实例创建时会注册 admin socket hook，后续实例创建时由于 hook 已存在，会**静默忽略**，不再注册。因此，通过 admin socket 查询到的 objector 数据实际上只来自 config store 的 librados 实例，而非 S3 请求路径，导致该功能对 RGW 实际上形同虚设。

### 讨论方案

**方案一：合并所有 librados 实例为单一实例**

优点：架构更清晰，符合 RBD/CephFS 的做法。
缺点：改动量大，config store 可能需要独立后端，NeoRADOS 与 legacy RADOS 的合并也较为复杂，难以验证正确性。

**方案二：让 objector 支持多个 librados 实例**

即修改 objector，使其能够聚合多个实例的 ops，以 JSON array 或合并方式返回。
缺点：会改变现有 admin socket 命令的输出格式，可能影响依赖该格式的其他组件。

**方案三（最终共识）：为每个 librados 实例设置不同的 socket 名称**

在 librados 的 `rados.init` 和 `rados.connect` 之间，新增一个 API（如 `set_objector_admin_socket_name`），允许应用层在初始化时为每个 librados 实例指定唯一的 socket 名称。若不设置，则保持默认行为不变，对其他客户端（RBD、CephFS）无影响。

Gruno 已有一个 draft PR 演示了该方案的实现，测试验证可行。admin socket 的 `help` 命令可以发现所有已注册的 objector 命令，用户可通过 discovery 找到对应的命令名称。

**后续行动：**
- Gruno 将提交正式 PR，为 librados 添加 `set_objector_admin_socket_name` API
- 在 RGW 侧为各 librados 实例（NeoRADOS、legacy RADOS 等）分别设置不同名称


### 子议题：为 objector dump 添加 Transaction ID 关联

**问题描述**

当前 objector dump 输出的是 RADOS 层面的对象 ID，无法直接关联到 S3 bucket、S3 object 或 S3 user。同时，RGW 的请求日志（access log、ops log）只在请求**完成后**才写入，当后端 RADOS 阻塞时，无法通过日志追溯正在进行中的请求。

**提案**

在 objector 的 op 结构体中新增一个字段（caller ID / transaction ID），允许应用层在提交 RADOS op 时附带一个字符串标识（如 RGW 的 `trans_id`），从而将 RADOS 层的 op 与前端 S3 请求完整关联起来。

**讨论要点**

- Casey 对直接向 librados AIO 接口添加随机参数持保留意见，认为 librados 应保持稳定、通用的 API 设计。
- 有人提出复用现有的 Jaeger tracing 结构，但该结构仅在启用分布式 tracing 时生效，存在性能开销，不适合作为常规 introspection 手段。
- 最终共识：在 **op 结构体**上新增一个紧凑字段（字符串类型），通过新增一个 object operation 的 setter 函数暴露给应用层，而非修改 AIO 函数签名。RGW 侧在构建 RADOS op 时，从 RGW op 的 `trans_id` 中取值并设置，非 RGW 上下文的请求则不设置。
- 明确不应使用 thread local storage（存在协程调度导致值错误的问题）。
- 不应复用现有的 `T`（递增计数器）字段，以免破坏现有语义。

**后续行动：**
- Gruno 将为该功能单独创建一个 tracker，并在后续 PR 中讨论具体实现细节
- 两个 PR（socket 命名 + caller ID）保持独立，分开提交


## 议题二：Swift X-Delete-After 重复设置 Bug（David 主导）

### 问题描述

Swift 协议支持 `X-Delete-After` header，允许用户指定对象在若干分钟后自动删除。当前存在一个 bug：**若对同一对象两次设置该 header，只有第一次的值生效**，后续设置被忽略。

该 bug 已有对应 PR 开放约一年，实现方式是在 `cls_time_index` 的 insert 函数中，插入前先检查并删除已有的旧 key。

### 讨论要点

- `cls_time_index` 目前主要用于对象过期（object expiration）功能，S3 的 restore object（临时副本到期删除）也使用了该机制。
- 性能影响：每次 insert 多一次查找，但由于使用场景有限，性能代价可接受，正确性更重要。
- 测试覆盖：`source/test` 目录下有大量 CLS 客户端 API 的测试用例，但目前**缺少针对 `cls_time_index` 的单元测试**。

### 后续行动

- Casey 将在该 PR 中补充测试指导意见（action item）
- 鼓励 PR 作者补充针对 overwrite 场景的单元测试
- Swift 相关功能在社区关注度较低，需要更多人参与审查


## 总结

| 事项 | 负责人 | 状态 |
|------|--------|---|
| 提交 librados socket 命名 PR | Gruno | 待提交 |
| 创建 caller ID / transaction ID tracker | Gruno | 待创建 |
| 在 cls_time_index PR 中补充测试指导 | Casey | 待完成 |
| Swift X-Delete-After bug PR审查 | 团队 | 进行中 |
