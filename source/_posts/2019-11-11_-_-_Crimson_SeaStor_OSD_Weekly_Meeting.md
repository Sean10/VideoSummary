---
title: "  2019-11-11 :: Crimson SeaStor OSD Weekly Meeting  "
date: 2019-11-15
updated: 2019-11-16
tags:
- Ceph
- 分布式存储
- 性能优化
categories:
- "视频总结"
subtitle: 2019-11-11_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
---

会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 多位Ceph研发人员，包括Mishkin、Mia、Young Waller、Eric、Jason、Adam、Ben、Josh、Ilya等。

**会议主题**：

* Ceph存储系统近期更新及讨论
* 分布式存储Ceph的性能优化
* 内存管理策略讨论

**会议关键细节**：

1. **Ceph存储系统近期更新**：
   * PG Autoscaler更新：增加了最小默认PG数量，从4个增加到16个，以提升并行性和可扩展性。
   * RBD更新：实现了RBD复制的日志核心代码的第一部分。
   * OSD更新：增强了OSD的亲和性阶段。
   * MDS更新：MDS机会和MDS缓存内存限制得到更新。
   * RGW更新：将额外的过滤功能移动到CLS代码中。

2. **性能优化讨论**：
   * 透明大页面（THP）问题：讨论了THP可能导致内存使用过高的问题，并考虑通过限制THP使用来解决这个问题。
   * 内存分配器优化：讨论了TC malloc内存分配器的性能问题，并考虑使用内存池或对象池来优化内存分配。
   * 缓冲区管理：讨论了缓冲区管理的最佳实践，并考虑使用scatter-gather I/O来减少缓冲区管理的开销。

3. **决定的事项**：
   * 接受新的PG Autoscaler默认值。
   * 禁用novelist的arm range和novelist。
   * 降低默认的max OMAP增加量。
   * 实施Eric的PR以减少bucket列表中的chard条目数。
   * 继续测试和优化THP和TC malloc。
   * 考虑使用内存池或对象池来优化内存分配。

4. **后续行动计划**：
   * 继续跟进THP和TC malloc的优化。
   * 完成RBD复制的日志核心代码。
   * 实施新的PG Autoscaler默认值。
   * 禁用novelist的arm range和novelist。
   * 降低默认的max OMAP增加量。
   * 完成其他待办事项。

**会议总结**：

本次会议讨论了Ceph存储系统近期更新、性能优化策略以及内存管理策略。会议达成了多项决定，并制定了后续行动计划，以进一步提升Ceph存储系统的性能和稳定性。