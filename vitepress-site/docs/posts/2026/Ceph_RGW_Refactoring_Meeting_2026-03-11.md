---
title: "Ceph RGW Refactoring Meeting 2026-03-11"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2026 年 3 月 11 日举行，涵盖四个主要议题：小对象内联存储优化、multipart upload 数据丢失问题修复、Keystone 角色注入 IAM policy，以及 multi-site 复制流量负载均衡问题。

## 议题一：小对象内联存储（Tiny RGW Objects Packing）

**提出者：Gaby**

当前 RGW 对于小于 512 字节的对象，仍会在磁盘上分配 block 存储数据。在 erasure coding 场景下（例如 4+2 配置），一个 256 字节的对象实际会消耗约 24 KB 的存储空间，代价极高。即便是 replication 模式，也需要支付 4 KB 的最小 block 开销。

**核心思路：**

观察到 RGW 对象的 manifest 本身约为 320 字节。若对象数据小于该阈值，可以将数据直接存储在 xattr（扩展属性）中，并省去 manifest，实现"零额外开销"的存储。在 BlueStore 中，xattr 存储于 RocksDB 的 Omap 中，不受 block 对齐限制，因此字节级别的数据存储是可行的。

**讨论要点：**

- 实际使用场景确实存在：ProtonMail 将邮件作为 object 存储于 RGW，Spark 等引擎使用小对象作为文件标记，S3 用户也可能将小文件直接存为对象。
- 阈值建议在 320 字节到 512 字节之间，具体数值待定。
- 对 versioned bucket 无影响，每个版本有独立的 head object 和 xattr。
- 主要挑战是**向后兼容性**：新版本 RGW 写入的内联对象，旧版本无法识别。建议通过 zone feature flag 机制，在集群完成升级后再启用该特性，防止混版本集群出现读取异常。

**结论：** 思路可行，需进一步确定阈值并设计兼容性保护机制。

## 议题二：Multipart Upload 数据丢失问题

**提出者：Casey（会议主持）**

**问题描述：**

客户报告了一个数据丢失的复现路径：第一次 complete multipart upload 请求在恰好 10 分钟后超时，客户端重试并发起新的 complete multipart upload，覆盖了原始的 multipart head object，导致原始上传的 tail objects 被垃圾回收删除。

10 分钟的超时与 RGW 使用的 CLS lock 时长一致——该锁用于保护 multipart upload 操作，但时间锁在到期后即失去保护效果，存在竞态窗口。

**根因分析：**

- multipart meta object 与最终 head object 分属不同 RADOS object，无法原子化操作。
- multipart meta object 存储于 extra data pool，与 head object 不在同一 pool，因此无法通过 object locator key 强制同 PG。
- 当前 PR尝试通过 compare-and-swap（CMPX）方式拒绝覆盖 head object，但存在局限性：OSD 对不存在对象的 CLS read 行为不确定，且仍有其他竞态路径。

**讨论的解决方案：**

1. **CLS 实现类 CMPX 语义**：在 CLS 中实现类似 compare-and-swap 的操作，但存在向后兼容问题，RGW 需要感知 OSD 是否支持该特性。
2. **持续约 CLS lock**：参考 multi-site 中的做法，在 complete/abort multipart upload 期间每隔约 5 分钟续约一次锁，防止锁过期。这是目前最被认可的方向。
3. **返回限流错误码**：当锁竞争时，将 500 错误改为限流错误码，引导客户端退避重试，减少竞争。
4. **引用计数防止 GC**：通过 ref count 阻止 tail objects 被垃圾回收，但被认为实现复杂度过高，不可行。

**关于并发量的担忧：**

有人担心为每个 multipart upload 请求启动续约 coroutine 会导致大量并发 coroutine。Casey 指出，complete multipart upload 本身已受 max concurrent requests 限制，续约 coroutine 数量上限与此相同，且 coroutine 本身轻量，影响可控。

**结论：** Casey 将原型实现"持续续约 CLS lock"方案，同时考虑将锁竞争时的错误码改为限流码。

## 议题三：Keystone 角色注入 IAM Policy

**提出者：Supriti（来自 Place，首次参会）**

**背景：**

当前 RGW 使用 Keystone 进行用户认证，仅判断用户是否具有 admin/reader 等角色，认证通过后角色信息即被丢弃，无法用于细粒度的访问控制。

**方案：**

将 Keystone 返回的角色列表注入到 IAM policy 的 environment（多值 map）中，在 policy 解析时通过条件键（condition key）进行匹配。例如：

```
条件：keystone:roles 包含 "reader"
效果：允许对特定 bucket 执行只读操作
```

已提交 ADR 文档和 PR，并包含单元测试（复用 IAM 现有测试框架）。

**讨论要点：**

- 建议为条件键添加命名前缀（如 `X-RGW-`）以避免与其他系统冲突，Supriti 已使用 `keystone:roles` 格式。
- 对外部 policy linter/validator 的兼容性可能存在影响，但属于工具侧问题。
- 关于未来扩展到基于 Keystone user ID 的访问控制，与会者认为需要进一步评估用例合理性，暂不纳入本次 PR。

**结论：** 方案简洁，社区反馈正面，将推进 PR 合并，user ID 粒度控制留待后续讨论。

## 议题四：OLH Epoch 一致性修复（Versioned Bucket）

**提出者：Jane**

**问题描述：**

在 versioned bucket 场景下，观察到 non-current 版本的 OLH（Object Lifecycle Head）entry epoch 新于 current 版本，导致后续 link OLH 操作无法将正确版本提升为 current。该问题在本地 zone 和 multi-site 复制场景下均可复现，触发条件为 S3 客户端流量、LC（Lifecycle）删除或 `radosgw-admin object rm` 命令。

**根因：**

执行 unlink instance 时，代码始终将 OLH entry 的 epoch 更新为最新值，导致 epoch 与其所指向的 instance 的实际 epoch 不一致，进而阻止更早版本被正确提升。

**修复方案：**

保持 OLH entry 的 epoch 与其所指向的 instance epoch 一致；pending log 中的 epoch 仍使用操作发生时的最新 epoch，以维持日志的时序回放能力。

这意味着 OLH epoch 可能在删除最新版本后"回退"到更早的值，这是预期行为——确保后续 link 操作能够正确比较并提升新版本。

**关于 epoch 单位的讨论：**

早期 PR 已将 OLH data entry epoch 和 candidate epoch 统一转换为基于时间戳的格式，因此两者比较单位一致，不存在混用问题。

**测试覆盖：**

当前测试使用 `radosgw-admin object rm` 复现问题，S3 delete 请求无法复现（原因待查）。Casey 建议后续补充 S3 delete 路径的测试用例。

**结论：** Igor 和团队内部已讨论确认，方案合理，待补充测试覆盖后合并。

## 议题五：Multi-site 复制流量负载均衡（DNS 服务发现场景）

**提出者：Ogazon**

**问题背景：**

multi-site 复制底层使用 libcurl 拉取数据。libcurl 在解析 DNS 端点时，默认只取单个 IP 并维持久连接，导致在使用 DNS 服务发现（而非负载均衡器）的场景下，复制流量集中打到少数几个 RGW 节点，形成热点。

**三种典型部署模式：**

1. **枚举所有 RGW 实例 IP**：流量均匀分布，无热点，但运维成本高。
2. **单端点 + 负载均衡器**：流量均匀，但负载均衡器成本高且引入额外复杂度。
3. **单端点 + DNS 服务发现**（当前用户场景）：libcurl 只解析到单个 IP，导致流量不均。

**提出的解决方案：**

在 RGW 侧主动将 DNS 端点解析为所有可用 IP，利用 libcurl 的 `--connect-to` 选项，在发起请求时指定目标 IP，并在 RGW 层实现轮询（round-robin）逻辑，将复制流量均匀分发到所有节点。

初步 POC 测试结果显示，使用该方案后复制流量可均匀分布到所有 RGW 实例。

**实现挑战：**

当前 RGW 将 endpoint 表示为单一 URL字符串，需要对 RGW 内部的 HTTP 客户端代码进行一定程度的重构，以支持传递 `connect-to` hint 给 libcurl。

**结论：** 问题动机充分，方案思路清晰，实现细节较复杂。Casey 表示将尝试在 PR 上留下反馈，下次会议继续深入讨论。

## 后续行动计划

| 负责人 | 行动项 |
|--------|--------|
| Casey | 原型实现 multipart upload CLS lock 持续续约方案 |
| Casey | 评估将锁竞争错误码改为限流码 |
| Supriti | 推进 Keystone 角色注入 IAM policy 的 PR合并 |
| Jane | 补充 OLH epoch 修复的 S3 delete 路径测试用例 |
| Ogazon | 整理 DNS 服务发现负载均衡 PR，下次会议深入讨论 |
| Gabby | 进一步调研小对象内联存储的实际使用规模及阈值选择 |
