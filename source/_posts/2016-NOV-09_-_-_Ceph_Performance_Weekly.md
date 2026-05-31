---
categories:
- 视频总结
date: 2017-01-11
subtitle: 2016-NOV-09_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- RocksDB
- 性能优化
- 分布式存储
- 测试
title: "'2016-NOV-09 :: Ceph Performance Weekly'"
updated: 2017-01-12
---


本次会议主要讨论了Ceph分布式存储和RocksDB的性能优化进展。以下是会议的关键内容：

**一、Ceph分布式存储项目进展**

*   **内存池调整**： 部分请求正在将数据移动到Blue Store的独立内存池中，以便更好地跟踪内存使用情况。
*   **Crush锁移除**： Adam提交的请求可能有助于移除Crush锁，提高性能。
*   **RocksDB优化**： Dan正在进行相关工作，值得期待。
*   **Blue Store性能优化**： 已合并新的Rocks TBE配置应用程序设置，使用更大的缓冲区以减少RocksDB的写入压力。
*   **并行事务提交**： Blue Store的并行事务提交功能正在开发中。
*   **性能回归**： 由于RocksDB编译时优化导致的性能下降已修复。

**二、RocksDB性能测试及优化**

*   **RocksDB与Jetta Scale对比**： 进行了RocksDB和Jetta Scale的性能对比测试，发现RocksDB在非稳定状态下性能更好，但在稳定状态下性能较差。
*   **Sharding逻辑问题**： 发现Sharding逻辑存在错误，导致性能下降。
*   **RocksDB优化方向**：
    *   减少数据集大小，降低压缩频率。
    *   优化读取操作，提高全读场景下的性能。
    *   考虑使用更小的对象大小，减少碎片化。

**三、后续行动计划**

*   继续进行RocksDB与Jetta Scale的性能对比测试，包括多OST和全读场景。
*   修复Sharding逻辑错误。
*   优化RocksDB的读取操作和对象大小设置。
*   探索其他RocksDB优化方案。

**四、其他事项**

*   预计将在今年内尝试使用RDMA进行数据同步。
*   邀请其他团队成员分享性能测试数据。

本次会议内容涵盖了内存池调整、Sharding逻辑问题、RocksDB优化等多个方面，为Ceph项目的进一步发展奠定了基础。