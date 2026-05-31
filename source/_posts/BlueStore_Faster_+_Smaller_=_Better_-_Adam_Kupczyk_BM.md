---
title: BlueStore, Faster + Smaller = Better - Adam Kupczyk, BM
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- BlueStore
- 性能优化
- 分布式存储
categories: 
- "视频总结"
subtitle: BlueStore_Faster_+_Smaller_=_Better_-_Adam_Kupczyk_BM
---

本次Ceph社区会议主要讨论了Bluestore存储引擎的最新技术进展、性能优化方案和未来开发路线。会议内容分为两部分：第一部分由Adam Kupczyk介绍了Bluestore的多项改进，第二部分由Ja Praash Madaka展示了其开发的性能分析工具。

### 关键技术讨论

1. **存储效率优化**
   - **压缩技术改进**：针对RBD场景下频繁覆写导致的压缩效率问题，提出了两种解决方案，其中方案一已经实现，可挽回10-15%的容量损失。
   - **小对象存储问题**：讨论了对微小对象的特殊编码方案，但暂未实施。

2. **性能优化**
   - **RocksDB WAL格式重构**：新格式合并IO操作，降低10-15%延迟，并修复了内存对齐问题。
   - **Discard操作增强**：实现多线程支持，并新增监控指标。

3. **元数据处理**
   - **Onode元数据重构**：采用C++ polymorphic allocators，消除blob独立存在性，减少锁竞争，提升事务处理效率。
   - **RocksDB提交优化**：发现WAL刷写与memtable排序可并行化，但当前实现存在数据损坏问题。

4. **内存管理**
   - **缓存体系改进**：推出与priority cache对齐的BlueFS缓存，解决内存碎片问题。
   - **分配器优化**：提案实现可加载的分配器分区，解决大容量磁盘内存占用问题。

5. **崩溃恢复**
   - **并行化恢复**：完全重写恢复机制，支持多线程加速，可达60倍提速。

### 创新工具展示

Ja Praash Madaka开发了基于perf_event_open的精准测量工具，用于硬件级PMU监控和代码块级粒度测量。

### 后续行动计划

- 三态磁盘分配器实现
- BlueFS priority cache集成
- EC clone_range优化为save/restore
- 小对象特殊编码方案评估

### 待解决问题

- RocksDB并行提交导致的数据损坏问题
- 内存碎片导致的缓存抖动现象
- 全闪存阵列下的碎片整理策略

### 特别致谢

- Pere Diasbu：突破性重构工作（bufferlist/onode）
- Mark Nelson：分层缓存概念设计
- Ja Praash Madaka：多项核心优化贡献

所有优化均遵循Ceph的consistency和decentralization核心原则，确保不影响现有PG分布和CRUSH algorithm行为。