---
title: 56 Weeks Later- Becoming a Jack of All Trades
date: 2025-06-24
updated: 2025-06-24
tags:
- Ceph
- 性能优化
- 分布式存储
categories: 
- "视频总结"
subtitle: 56_Weeks_Later_-_Becoming_a_Jack_of_All_Trades
---

### 56 Weeks Later- Becoming a Jack of All Trades
**会议主题**：Crimson OSD 架构性能测试进展与贡献回顾
**主讲人**：Ian Palos Perez（IBM SEF 团队成员）
**日期**：近期会议

#### 核心讨论内容
##### Crimson OSD 架构概述
- **传统 Classic OSD**：多线程架构，依赖线程间同步原语（如互斥锁）共享资源，包括 `messenger`、`PG`（Placement Groups）、`ObjectStore`。
- **Crimson OSD**：基于 `seastar` 框架，采用异步通信与同步计算模型，使用 C++20 特性，单 `reactor` 绑定单 CPU 核心，避免显式锁和资源共享。

##### 性能测试结果
- **随机读写性能**：Crimson 在随机读性能上显著优于 Classic，但在随机写性能上仍有优化空间。
- **Reactor 配置**：测试了单 `reactor` 与双 `reactor` 绑定核心的策略，性能差异与工作负载相关。

##### 关键贡献
- **CPU 核心绑定策略**：开发工具支持将 `reactor` 绑定到指定 CPU 核心，优化 OSD 分布。
- **I/O 成本评估工具**：基于硬件能力提供性能指标，使用 `pandas` 分析数据并生成报告。
- **Messenger 性能分析**：对比 Crimson 异步 `messenger` 与 Classic 同步 `messenger`，发现 16 核心为性能拐点，高并发下存在资源争用。
- **自动化测试工具**：为 SEF 基准测试工具开发回归测试生成器，确保代码变更不影响基线性能。

#### 未来计划与优化方向
- **Crimson 深度优化**：分析 `coroutines` 在 `seastar` 中的执行效率，减少 `messenger` 路径的延迟。
- **遗留代码改进**：探索 Classic 代码的潜在优化点。
- **社区协作**：呼吁开发者参与性能分析工具链的扩展。

#### 行动项
- 完善 `reactor` 绑定策略对 AMD 的支持
- 提交 `messenger` 资源争用分析报告
- 集成实时监控工具到 Crimson 测试框架

#### 备注
- 保留关键词：Crimson、seastar、reactor、PG、OSD、messenger、coroutines、NUMA、IOPS。

**会议结束**