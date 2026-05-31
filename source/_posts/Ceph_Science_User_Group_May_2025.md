---
title: Ceph Science User Group May 2025
date: 2025-07-30
updated: 2025-07-30
tags:
- Ceph
- 分布式存储
- Cephadm
categories: 
- "视频总结"
subtitle: Ceph_Science_User_Group_May_2025
---

Ceph Science User Group 于 2023 年 5 月举行，会议涵盖了多个重要议题，以下是对会议内容的总结：

### 主题演讲：Ceph 在大规模高吞吐计算环境中的性能分析

演讲者 Tom（STFC）分享了 STFC 运行的 Ceph 集群 Echo 的性能分析结果。Echo 集群规模超过 100PB，主要为 LHC 实验提供存储支持。Tom 评估了将 RocksDB 从 HDD 迁移至 SSD 对性能的影响，发现：

- **Backfill 性能**：Hybrid OSD（使用 SSD 存储 RocksDB）的延迟显著降低，HDD 吞吐可达 200-250MB/s。HDD-only OSD 在延迟低于 100MB/s 时性能波动大。
- **写入操作**：Hybrid 配置下，HDD 的 IOPS 需求降低，写入更稳定。
- **读取操作**：RocksDB 位置对读取性能影响微乎其微，推测因数据缓存在内存中。

### 讨论议题

1. **Ceph RBD 故障排查**：讨论了 RBD 节点因内核 Bug 进入“半死”状态的问题，提出了避免 Mon 与 OSD 共置等临时方案。
2. **Cephadm vs 手动部署**：讨论了 Cephadm 和手动部署的优缺点，包括快速服务部署、解耦 OS 依赖、声明式 YAML 管理、黑盒操作、性能争议等。
3. **Quincy 17.2.9 紧急发布**：分享了 BlueFS 的 LSN 问题导致的 OSD 崩溃的修复内容，建议高风险集群尽快更新。

### 行动计划

1. **硬件采购**：Tom 将评估 SSD 对写入密集型场景的价值，提交成本效益分析。
2. **故障改进**：Matteo 计划升级内核并测试分离 Mon/OSD 部署。
3. **Cephadm 优化**：社区建议增强任务队列可视化。
4. **文档协作**：建立 GitHub 仓库归档会议幻灯片。

会议强调了 Ceph 在大规模高吞吐计算环境中的性能和稳定性，讨论了不同的部署和管理方案，并制定了后续的行动计划。