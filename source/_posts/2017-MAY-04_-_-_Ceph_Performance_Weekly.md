---
title: " 2017-MAY-04 :: Ceph Performance Weekly "
date: 2017-05-17
updated: 2017-05-17
tags:
- 性能优化
- 分布式存储
- RocksDB
- BlueStore
categories:
- "视频总结"
subtitle: 2017-MAY-04_-_-_Ceph_Performance_Weekly
---

### 会议纪要

**会议时间**： 2023年11月X日

**参会人员**： Chris, Mark, James (Alibaba), Josh, Sage, Andy (kestrels), Stu, Ali (Alibaba), Johnson (Alibaba)

**会议主题**： Ceph分布式存储项目进展及讨论

**会议内容**：

**1. Ceph性能优化**

* **RocksDB读前加速**： Mark介绍通过启用RocksDB读前加速功能，在压缩过程中提高性能的方法，将读取时间从95%降低到18%，等待时间从82%降低到18%。
* **编码/解码框架迁移**： Sage提交PR移除旧编码/解码代码并迁移到新框架，提高性能和可维护性。
* **BlueStore优化**： Sage提交PR将BlueStore放置在共享设备中间，讨论了数据放置位置对性能的影响。
* **锁优化**： 讨论了锁优化，包括消除重复块位置和锁冲突。
* **CRC缓存**： Andy (kestrels) 提交PR改进CRC缓存，提高性能。
* **自适应限流**： 讨论自适应限流机制优化性能和降低延迟。
* **OST性能优化**： Johnson (Alibaba) 提出优化OST性能的方案。
* **游戏时钟**： 讨论游戏时钟的实现和性能。

**2. Ceph恢复**

* **阿里巴巴团队**： 分享恢复优化工作，包括同步恢复和部分恢复，讨论性能提升和优化方向。
* **异步恢复**： Josh分享异步恢复工作，讨论与阿里巴巴团队的协作。

**3. 其他**

* **OST性能优化**： Johnson (Alibaba) 提出优化OST性能的方案。
* **游戏时钟**： 讨论游戏时钟的实现和性能。

**行动计划**：

* Mark将继续优化RocksDB读前加速功能。
* Sage将继续改进BlueStore和CRC缓存。
* Andy (kestrels) 将完善CRC缓存PR。
* Josh将优化异步恢复机制。
* Johnson (Alibaba) 将继续优化OST性能。
* 阿里巴巴团队将继续优化Ceph恢复功能。

**下次会议**：

* 时间：2023年11月X日
* 内容：Ceph分布式存储项目进展及讨论

**备注**：

* 会议中提到了一些计算机科学/ceph相关领域英文原文的关键词，如RocksDB, BlueStore, CRC, PG, OST, RBD等。
* 会议纪要仅供参考，具体细节可能需要查阅相关PR和邮件。