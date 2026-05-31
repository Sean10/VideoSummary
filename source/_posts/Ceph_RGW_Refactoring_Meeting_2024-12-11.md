---
title: Ceph RGW Refactoring Meeting 2024-12-11
date: 2024-12-11
updated: 2024-12-11
tags:
- Ceph
- RGW
- 分布式存储
categories: 
- "视频总结"
subtitle: Ceph_RGW_Refactoring_Meeting_2024-12-11
---

会议纪要

### 会议主题

Ceph RGW 多区域（Multisite）和元数据同步讨论

### 参会人员

Cena, Casey, Yehuda 等

### 会议时间

未知



#### 主要议题

1. **多区域（Multisite）复制策略的讨论**
   - **当前问题**：多区域复制（Multisite Replication）在实现上存在一些混淆，特别是在对称复制（symmetric replication）和增量复制（incremental sync）之间的选择。
   - **讨论内容**：
     - 当前实现要求两个桶（bucket）完全一致，但有些用户希望使用复制作为数据流动，而不是确保两个桶完全相同。
     - 新的多区域组（Multisite Group）实现允许根据同步策略（sync policy）选择性地复制对象，而不是强制全量同步。
     - AWS 的桶复制策略（bucket replication policy）不支持全量同步，只对新上传的对象进行复制。
   - **决定**：
     - 需要进一步讨论是否支持全量同步和增量同步的混合模式，以及如何在多区域组（Multisite Group）和多区域（Multisite）之间进行选择。
     - 需要明确多区域组（Multisite Group）和多区域（Multisite）的使用场景，特别是灾难恢复（Disaster Recovery）的需求。

2. **元数据同步（Metadata Sync）的优化**
   - **当前问题**：元数据同步在多区域组（Multisite Group）中存在不必要的负载，特别是当其他区域组（Zone Group）并不关心某些桶的元数据时。
   - **讨论内容**：
     - 当前实现会将所有桶的元数据复制到所有区域组，这可能导致不必要的负载和竞争条件。
     - 建议优化元数据同步，只同步相关区域组（Zone Group）的元数据。
   - **决定**：
     - 需要进一步讨论如何在元数据同步中避免不必要的负载，特别是在区域组（Zone Group）之间的同步。

3. **同步策略（Sync Policy）与全局同步（Global Sync）的冲突**
   - **当前问题**：同步策略（Sync Policy）允许在同一区域组（Zone Group）内进行不对称同步，这可能导致数据不一致。
   - **讨论内容**：
     - 同步策略（Sync Policy）允许用户在同一区域组内进行不对称同步，但这与全局同步（Global Sync）的目标相冲突。
     - 建议在区域组（Zone Group）级别进行全局同步，而桶级别的同步策略（bucket replication policy）应仅用于跨区域组（Zone Group）的同步。
   - **决定**：
     - 需要进一步讨论是否应该禁用同步策略（Sync Policy）中的不对称同步，以确保区域组（Zone Group）内的数据一致性。

4. **桶索引清理（Bucket Index Cleanup）的讨论**
   - **当前问题**：桶索引清理的实现需要考虑不同区域组（Zone Group）之间的同步状态。
   - **讨论内容**：
     - 当前实现只考虑同一区域组（Zone Group）内的同步状态，未考虑跨区域组的同步。
     - 建议在清理桶索引时，确保所有相关区域组（Zone Group）都已完成同步。
   - **决定**：
     - 需要进一步讨论如何在跨区域组（Zone Group）的情况下进行桶索引清理，并确保数据一致性。



#### 后续行动计划

1. **多区域（Multisite）复制策略的进一步讨论**：
   - 需要撰写设计文档，明确全量同步和增量同步的混合模式，以及多区域组（Multisite Group）和多区域（Multisite）的使用场景。
   - 讨论是否支持多区域组（Multisite Group）内的不对称同步。

2. **元数据同步的优化**：
   - 进一步讨论如何在元数据同步中避免不必要的负载，特别是在区域组（Zone Group）之间的同步。

3. **同步策略（Sync Policy）与全局同步（Global Sync）的冲突**：
   - 讨论是否禁用同步策略（Sync Policy）中的不对称同步，以确保区域组（Zone Group）内的数据一致性。

4. **桶索引清理的进一步讨论**：
   - 讨论如何在跨区域组（Zone Group）的情况下进行桶索引清理，并确保数据一致性。



**下次会议时间**：待定