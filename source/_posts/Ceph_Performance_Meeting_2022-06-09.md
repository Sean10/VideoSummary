---
categories:
- 视频总结
date: 2022-06-27
subtitle: Ceph_Performance_Meeting_2022-06-09
tags:
- Ceph
- 性能优化
- 分布式存储
- CRUSH算法
title: "Ceph Performance Meeting 2022-06-09"
updated: 2022-06-28
---



在2022年6月9日的Ceph性能会议上，讨论了多个与Ceph分布式存储性能优化相关的问题和改进措施：

1. **Snap Mapper改进**：
   - **项目1**：提出了将Snap Mapper从RocksDB中移除，改为内存数据结构，并在系统关闭时将其保存到文件中。这旨在减少系统关闭时间，并在启动时节省时间。
   - **项目2**：通过批量处理删除请求来减少与RocksDB的交互次数，从而降低性能开销。
   - **项目3**：将Snap Marker从单一大型实体更改为每个PG维护自己的Snap Mapper集合，以减少锁冲突并提高性能。

2. **TRACING改进**：
   - 提交了一个新的TRACING补丁，已合并到主分支，并显示出良好的性能指标。

3. **其他讨论**：
   - 讨论了CPT Toothology Proof Testing的问题，以及如何解决其偶尔不提供结果的问题。
   - 探讨了使用CSTAR（Control TCMalek Thread Cache Size）配置选项来控制TCMalek线程缓存大小。
   - 讨论了将旧映射基准测试功能添加到Google测试套件的存储测试中，以帮助了解OMAP和RocksDB的开销。

4. **后续行动**：
   - 继续审查和合并PR（Pull Requests）。
   - 进一步研究Snap Mapper的历史和代码。
   - 调整和优化Shard向上Q在OSD中的行为。

会议重点关注了Ceph性能优化，特别是Snap Mapper的改进，以及如何通过不同的方法来提升Ceph系统的整体性能和可扩展性。