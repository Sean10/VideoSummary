---
title: "Ceph RGW Refactoring Meeting 2026-03-25"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
  - "Teuthology"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2026 年 3 月 25 日召开，主要讨论了三个议题：RGW list 请求的 CPU 时间限速方案、Teuthology 测试套件的修复策略，以及 copy object 压缩加密 bug 修复与 lifecycle transition 重构计划。

## 议题一：RGW List 请求限速——基于时间的 rate limiting

### 背景与问题

David 和 Sanjay 介绍了一个新的 PR，旨在为 RGW 的 list 请求引入基于 CPU 时间的 rate limiting 机制。

当前 RGW 已有针对 ops 数量和读写字节数（bandwidth）的限速，但对于 list 请求，这些指标不足以防止单个用户对集群造成冲击。核心原因在于：

- 当 list 请求携带 delimiter 参数时，RocksDB（OMap）需要执行大量 range scan，每次找到 delimiter 边界变化都需要发起一次新的数据库查询。
- 由于 Ceph 的 bucket sharding 机制，跨 shard 的查询更加复杂，无法预知需要跳过多少条目。
- 一个客户端请求可能导致数 MB/s 的 RocksDB IO，远超 ops/s 指标所能描述的范围。

### 方案讨论

与会者讨论了多种限速指标的优劣：

- **时间（time）**：最能反映请求对系统资源的实际消耗，包括 IO 等待和处理时间，但对用户而言不够直观，且受服务器负载影响。
- **RocksDB / OMap IOPS**：更贴近底层开销，但对用户完全不透明，难以解释限速原因。
- **ops 数量**：已有实现，但无法区分轻量与重量级 list 请求。

最终倾向于采用时间作为度量指标，理由是：
1. 用户可以感知请求耗时，具备一定可解释性。
2. 时间是对系统资源占用最综合的估算，未来 listing 性能优化（如 sharding 改进）也会自然反映在时间指标上，具备 future-proof 特性。
3. 实现方式与现有 bandwidth 限速类似，预算在操作完成后扣除，保证至少一次 list 操作始终可执行。

注意：应将该指标定义为"时间"而非"CPU 时间"，因为大量耗时实际发生在后端 IO（如 OMAP busy），不会体现在 RGW 进程的 CPU 使用率上。

### 版本兼容性关注

David 特别指出，该 PR 修改了存储限速配置的 JSON 结构版本号。若上游 main 分支同期有其他字段变更，将产生版本冲突，因此希望尽快明确该 PR 能否合入 main。

### 结论与后续行动

- 与会者达成基本共识，认为基于时间的 list 请求限速方案合理可行。
- 将请求 Mark Kogan（rate limiting 主要贡献者）对该 PR 进行 review。
- David 将在 PR 中补充本次讨论的结论摘要。

## 议题二：Teuthology RGW 测试套件修复

### 现状

RGW 测试套件（Teuthology）近期因 Rakuten 相关支持代码合入，出现大量测试失败，严重影响 PR 的 merge 验证流程。

主要失败来源：

- **ragweed**：依赖 boto2，已过时。Mark 有一个待合入的 PR 尝试通过 AI 生成兼容层来修复，但引入了不必要的抽象层，需要进一步评估。
- **Rocky 10 相关**：Redis 安装失败、cloud events 模块导入失败等问题，部分为 Rocky 特定问题。
- **upgrade 测试**：因Squid 和 Tentacle 缺少 Rocky 包，upgrade 测试套件整体失败。

### 讨论与决策

- **ragweed 处理方案**：优先测试 Mark 的 PR，若可用则合入；若不可用，则将 ragweed 从 `rgw verify`（基础测试套件）中移除，保留在 upgrade 套件中，避免阻塞日常 PR 验证。
- **ragweed 的价值评估**：与会者认为 ragweed 目前主要用于 upgrade 测试（如跨版本 multipart upload），但多年未新增测试用例，实际价值有限。
- **其他失败**：Oguzhan 将在 Slack 发布 Teuthology 运行分析摘要，并为各类失败创建 tracker issue，优先级标记为 urgent。
- 后续计划新增对最新 Ubuntu LTS 的测试支持，届时 Python 兼容性问题预计已基本解决。

### 后续行动

- 将 ragweed 从 `rgw verify` 测试套件中移除（由本次会议参与者作为 action item跟进）。
- 为各类 Teuthology 失败创建 tracker issue，标记为 urgent 优先级。
- 在 Slack 发布 Teuthology 运行分析摘要。

## 议题三：Copy Object 压缩加密 Bug 修复与 Lifecycle Transition 重构

### 背景

Matt 介绍了 PR #6725，该 PR 旨在为 lifecycle policy 的 transition 操作添加 recompression 和 re-encryption 支持（用于将对象迁移至新 storage pool）。

在编写 DPF（Data Processing Framework）过程中，发现 transition 与 copy object 存在大量重复逻辑，因此提议抽取公共基类，供两者共用。

同时，在测试中发现 copy object 对压缩和加密对象存在 bug（tracker issue #75650）：对压缩加密对象执行 copy object 会返回损坏数据。该 bug 在 main 分支于去年 11 月合入，尚未 backport 到 Tentacle。

### 方案讨论

- 与会者认同抽取共享 DPF 基类的方向，可减少代码重复，降低 bug 风险。
- 共享 DPF 未来还可用于 deduplication 场景（内存中解压缩并计算 fingerprint）。
- 建议优先单独提交一个 PR 修复 copy object 的压缩加密 bug，使 Teuthology 测试尽快恢复绿色，再推进 lifecycle 重构的泛化工作。

### 版本影响评估

- 该 bug仅存在于 main 分支，Tentacle 尚未受影响。
- 需确保在 Tentacle 预发布前完成修复，相关 backport tracker issue 已分配给 Marcus，尚未完成。
- 将新发现的 copy object bug 关联到现有 backport tracker，避免遗漏。

### 后续行动

- Matt 单独提交 PR 修复 copy object 压缩加密 bug。
- 在 PR 上tag Gabby（对共享 DPF 感兴趣）。
- 将新 copy object bug 关联到现有 backport tracker issue。

## 总结

本次会议在三个议题上均取得明确进展：list 请求时间限速方案获得共识并进入 review流程；Teuthology 测试套件有了清晰的修复路径；copy object 压缩加密 bug 将优先独立修复，lifecycle 重构工作同步推进。
