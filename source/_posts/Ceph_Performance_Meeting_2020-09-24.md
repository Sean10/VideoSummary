---
title: "Ceph Performance Meeting 2020-09-24"
date: 2020-09-25
updated: 2020-09-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
1. **新拉取请求 (Pull Requests)**:
   - Adam Core Adam提交了一个新的PR，旨在为每个列族 (column family) 提供独立的RocksDB块缓存 (block caches)。
   - 另一个新的PR是关于并发检索设备数据的软卷 (soft volume)，标记为性能相关。

2. **更新拉取请求**:
   - 动态级别 (dynamic levels) 在RocksDB中的实现。
   - RGW中的D3N缓存更改，经过QA测试，但可能需要进一步的工作。

3. **优化放置组 (Placement Group) 移除**:
   - Mark提到了一个优化放置组移除的PR，编号为37314，包含一些修复，如重用集合列表的下一个位置和立即从缓存中移除已删除的节点。

4. **RocksDB性能分析**:
   - 讨论了RocksDB的写前日志 (write ahead log) 和内存表 (mem table) 的行为，特别是关于如何处理PG日志和对象节点的同步问题。

5. **未来行动计划**:
   - Gabi将继续研究RocksDB代码，探索是否可以实现一个可丢弃的内存表。
   - 重新评估和测试移除PG日志对性能的影响。

#### 讨论的主要议题
- **RocksDB的缓存和写前日志行为**: 讨论了如何优化RocksDB的缓存和写前日志，以减少IOPS和延迟。
- **PG日志的处理**: 探讨了PG日志的存储和处理方式，以及如何在不牺牲一致性的前提下提高性能。

#### 决定的事项
- **继续研究和优化RocksDB的使用**: Gabi将继续深入研究RocksDB的内部机制，特别是内存表和写前日志的处理。
- **重新测试PG日志的影响**: 计划重新运行移除PG日志的实验，以评估当前代码的性能影响。

#### 后续行动计划
- **Gabi的研究工作**: Gabi将在接下来的几天内继续研究RocksDB，特别是探索创建一个可丢弃的内存表的可能性。
- **性能测试**: 重新进行性能测试，特别是移除PG日志的实验，以评估当前代码的性能表现。
- **会议跟进**: 下次会议将讨论Gabi的研究进展和性能测试的结果。

### 结论
本次会议主要讨论了RocksDB的优化和PG日志的处理，确定了Gabi将继续深入研究RocksDB的内部机制，并计划重新进行性能测试以评估移除PG日志的影响。会议还提到了未来可能的改进方向，包括优化内存表和写前日志的处理。