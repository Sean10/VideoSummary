---
title: "Disaster Recovery User Story"
date: 2025-06-24
updated: 2025-06-24
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
本次会议主要讨论了英国MRC分子生物学实验室（LMB）在CephFS存储系统中遭遇的严重故障及其恢复过程。以下是会议的关键细节和主要议题：

**关键议题与讨论内容**

1. **背景与系统架构**：LMB使用CephFS作为主要存储方案，备份集群（Pebbles）由36个节点组成，包括17PB数据，采用SAS硬盘和NVMe存储，并使用Erasure Coding和Replication。

2. **故障现象**：MDS卡在`laggy replay`状态，日志分析显示Journal损坏，可能与异步写入和RADOS Clone操作有关。

3. **恢复方案对比**：
   - **完整恢复**：通过备份Journal、恢复元数据、重建文件系统、验证与上线等步骤进行。
   - **快速恢复**：仅重置Session Map和运行`scan-links`，适用于假设元数据池未损坏的情况。

4. **后续改进**：调整配置、禁用异步写入、升级Ceph Squid、优化备份策略等。

**决策与行动计划**

- 短期行动：禁用异步写入、验证备份Journal完整性。
- 长期计划：迁移至Ceph Squid、测试稳定性、编写自动化恢复脚本。
- 风险提示：快速恢复方案需谨慎评估元数据池的健康状态。

**遗留问题与后续讨论**

- 是否需要在其他场景中调整恢复流程？
- 如何进一步优化`scan-extents`和`scan-inodes`的并行效率？

会议强调了CephFS在处理大规模数据存储和备份时的挑战，以及如何通过有效的故障恢复策略和数据管理来保证数据的完整性和可用性。

结束了



**标签**：
- Ceph
- 存储恢复
- 数据一致性
- 系统故障
- 备份策略