---
title: "Ceph RGW Refactoring Meeting 2026-04-29"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
  - "Erasure Coding"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2026 年 4 月 29 日举行，主要围绕三个议题展开：LC（Lifecycle）metrics 性能计数器 PR 审查、erasure coding 场景下的 object packing 设计探讨，以及 LC 删除逻辑的安全性改进。

## 议题一：LC Metrics 作为 Perf Counters

### PR 概述

Matthew 提交了两个 PR，第一个是将 LC metrics 添加为 perf counters。该 PR 已在内部使用 100,000 个 bucket 和Ceph exporter 进行测试，scrape 全部 bucket 耗时约 5 秒，性能表现良好。

PR 还新增了以下内容：
- 针对 transition 和 aborted MPU 删除操作的额外 metrics
- 包含 PromQL 示例的详细文档，对运维人员尤为实用

### 性能讨论

针对 Bloomberg 团队关于使用 `ceph daemon` scrape metrics 性能的顾虑，Matthew 说明：

- `ceph daemon` 本质上是 Python 脚本，处理大数据集时速度较慢
- 默认使用 JSON pretty格式输出，处理耗时较长
- 改用 compact JSON（`--format json`）后，100,000 个 bucket 约需 10 秒，仍在 Prometheus 默认 15 秒 scrape 间隔内
- 推荐迁移至 Ceph exporter 以获得更好性能

### LC List 改进建议

与会者建议在 LC list 中增加 completion time 字段（目前只显示开始时间和状态）。Matthew 表示这可能需要 CLS 变更，团队正在评估如何以最小改动实现更多 LC 统计信息，划作为独立 PR 推进。

## 议题二：LC 版本对象批量删除优化

Matthew 的第二个 PR 将版本对象（versioned objects）分组，通过 multi-delete 调用批量处理，以减少 OLH contention，提升版本删除性能。

### 代码复用确认

经讨论确认，该 PR 已将 multi-delete 逻辑重构为公共函数，供 multi-object delete handler、S3 handler 和 lifecycle policy 共同调用，避免了代码重复和维护问题。

### 测试覆盖

讨论了现有 LC 测试对版本对象的覆盖情况。Casey 确认 QA 测试中已通过 debug 配置选项将 LC 周期缩短至约 10 秒，cloud transition QA 测试也有类似配置。建议重点确认针对 non-current rules 的测试用例覆盖了足够多的版本数量。

## 议题三：Erasure Coding 场景下的 Object Packing 设计

### 背景与问题

Gaby 提出了两个与 erasure coding 相关的设计问题。

**问题一：stripe_max_size 配置**

manifest 中的 `stripe_max_size` 默认为 4MB，对 replication 合理，但对 erasure coding 不够高效。以 EC 4+2 为例，4 MB stripe 会导致每个 OSD 只写入 1 MB 数据加 1 MB parity，空间利用率低。建议将 stripe size 设为 `k * 4 MB`（即 16 MB），使每个 OSD 写入 4 MB，提升效率。此优化仅影响大于 4 MB 的对象。

**问题二：Write Coalescing（写合并）**

针对 erasure coding 场景下小对象写入效率低的问题，Gaby 提出延迟 ACK + 写合并方案：

- 在收到 PUT 请求后，开启一个短暂时间窗口（约 100 微秒至 1 毫秒）
- 在窗口内收集多个 PUT 请求，打包为单次 EC 写操作
- 由于未向客户端发送 ACK，窗口内崩溃不会造成数据丢失

### 关键问题讨论

**客户端并发行为**：与会者指出客户端行为是混合的——单线程应用会串行发送请求，但大规模部署下会有大量并发。multipart upload 本身也会并行上传 part。Gabby 明确此优化主要针对 1 KB 至 64 KB 的小对象。

**延迟影响**：有与会者担心额外延迟会影响用户对 Ceph 性能的感知。Gabby 解释，在高负载场景下，虽然单次请求延迟略有增加，但系统整体吞吐量会显著提升，平均性能更好。在低负载时，可通过运行时统计自适应关闭合并模式。

**Write-back Cache 方案**：Matt Benjamin 提出可借鉴 D4N（Boston University研究项目）的思路，使用稳定的 write-back cache 作为 ingest buffer，先将数据写入缓存，再异步打包写出，可立即完成 IO 而无需等待窗口。Gabby 表示 write-back cache 需要非易失性内存或日志设施，延迟 ACK 方案则是一种"免费"的缓冲机制，两者可以互补。

### Object Packing 设计细节

Gabby 详细介绍了 object packing 的设计目标：

**当前 EC 小对象写入的问题**（以 4 KB 对象、EC 4+2 为例）：
- 数据被分片写入 4 个 OSD，每个 OSD 写 1 KB 数据 + 3 KB 填充 + parity
- 6 个 OSD 共消耗 24 KB 空间，效率极低
- 读取时需要访问全部 4 个 EC 成员

**Fast EC 的改进**：将小对象完整写入单个 member OSD，其余 OSD 存储空对象，读取只需访问一个 OSD，但写入仍较昂贵。

**Object Packing 方案**：
- 将多个小对象打包进一个大容器对象（如 16 MB）
- 每个小对象有一个空的 head object，manifest 指向 packed 对象中的偏移量
- 读取时：先读 head object 获取 manifest，再读 packed 对象中对应数据（额外一次 hop）
- 写入效率大幅提升：原本 7 次独立 EC 写变为 1 次，理论上可降低写入开销约 1000 倍

**额外 hop 的权衡**：与会者指出额外一次网络往返会增加读延迟。Gabby 对比了现状——当前 EC 读取已需访问多个 OSD，用户已接受这种模式。Fast EC 解决了这个问题，建议未来设计以 Fast EC 为基础假设。

**PG split 问题**：即使初始时 head object 和 data object 在同一 OSD，PG split 或 rebalance 后两者可能分离，维护局部性代价较高，目前 CRUSH 模型不支持此类约束。

### 后续行动

- Gabby 希望与 Max 安排专项会议，确保 object packing 设计对 RGW 友好（同时兼顾 CephFS）
- 欢迎与会者在会后提供更多反馈和深入思考

## 议题四：LC 删除逻辑安全性改进

### 问题背景

Igor 报告了当前 LC 跳过逻辑 PR 中存在的潜在数据安全问题。在以下三种异常对象状态下，LC 可能错误删除数据：

1. latest 版本被标记为 non-current
2. 对象没有 current 版本
3. 对象存在多个 current 版本

### 具体风险场景

以"多个 current 版本"为例：当前 PR逻辑会删除最顶层的 current 版本，跳过其余版本。但若后续通过 object re-index 修正了对象状态，之前已被删除的版本将无法恢复，造成数据丢失。

### 改进方案

Igor 提出更安全的处理策略：**当发现对象版本状态与 bucket 状态不一致时，完全跳过该对象，不执行任何 LC 操作**，并记录日志提示运维人员手动检查修复。修复完成后，LC 可正常处理该对象。

与会者一致认同此方案更安全，数据丢失风险更低。Igor 将据此修改 PR 并提交新的 commit。

## 总结

本次会议主要推进了以下工作：

- LC metrics perf counters PR 获得进一步审查，性能验证通过，待更多 reviewer 参与
- 版本对象批量删除 PR 代码结构得到确认，测试覆盖待补充
- Erasure coding 场景下的 object packing 设计方向初步明确，write coalescing 和 write-back cache 两种思路均值得探索
- LC 删除安全逻辑将改为对异常状态对象完全跳过，避免潜在数据丢失
