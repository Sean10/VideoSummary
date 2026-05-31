---
categories:
- 视频总结
date: 2017-01-11
subtitle: 2016-OCT-12_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- BlueStore
- 性能优化
- RocksDB
- 分布式存储
title: "'2016-OCT-12 :: Ceph Performance Weekly'"
updated: 2017-01-12
---



### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Ramesh, Dan Lambright, Kevin, Alan, Sage, Tim, 等

**会议主题**： Ceph分布式存储系统，特别是BlueStore的性能优化

**会议内容**：

**一、本周工作进展**

1. **Ramesh** 优化了内存数据库存储接口，将键值存储从B树实现切换到通用映射，以提高性能。
2. **Dan Lambright** 尝试使用Ceph的PG映射功能，为PG信息提供了一种新的实现方式，有望提高性能。
3. **BlueStore性能优化**：
    * 通过减少内存结构的大小，降低对缓存节点的内存需求，本周关闭了许多与BlueStore相关的请求。
    * Sage提出了一种更新PG信息的方法，显著减少了数据写入量和提高了性能。
    * Tim试图将快速编码功能合并到BlueStore中，但遇到了冲突。

**二、讨论议题**

1. **BlueStore与文件存储的对比**：
    * BlueStore在随机读取方面存在性能问题，尤其是在IOPS大小为32时。
    * Sage提出了可能的解决方案，包括异步支持一次从Ceph MO数据结构中检索多个扩展，以及进行序列化操作。
    * 讨论了异步消息传递和快速调度器，以提高性能。

2. **RocksDB的写前日志（WAL）优化**：
    * 目前测试实验室出现问题，无法进行长时间测试。
    * 初步结果显示，增加日志数量或日志大小可以提高性能。
    * 需要进一步研究如何区分WAL数据与元数据，以及如何量化这些行为。

3. **其他议题**：
    * Ramesh正在研究将键值存储从B树实现切换到通用映射。
    * Dan Lambright正在尝试使用Ceph的PG映射功能。
    * Sage正在研究改进BlueStore的随机写入性能。

**三、决定事项**

1. 继续关注BlueStore的性能优化，特别是随机读取和序列读取性能问题。
2. 进一步研究RocksDB的WAL优化，包括增加日志数量或日志大小。
3. 完成Ramesh和Dan Lambright的工作，以提高性能。
4. Sage继续研究改进BlueStore的随机写入性能。

**四、后续行动计划**

1. Ramesh和Dan Lambright继续进行相关工作。
2. Sage研究改进BlueStore的随机写入性能。
3. Tim解决快速编码功能的合并冲突。
4. Kevin继续研究减少内存结构大小的工作。

**五、其他**

1. 讨论了BlueStore的分配策略，以及如何减少写放大和压缩。
2. 讨论了如何使用RocksDB的WAL来提高性能。
3. 讨论了如何使用更多的工具和指标来分析Ceph的性能。