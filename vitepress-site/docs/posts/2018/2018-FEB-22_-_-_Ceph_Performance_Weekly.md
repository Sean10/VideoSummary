---
title: "2018-FEB-22 :: Ceph Performance Weekly"
date: 2018-02-26
updated: 2018-02-27
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "RocksDB"
  - "缓存"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Peter, Mark, Assaf, David, John, Josh 等

**会议主题**： Ceph分布式存储性能优化与问题解决

**关键细节**：

* **性能优化**：
    * Peter修复了OP Tracker缓慢的问题，显著提升了性能。
    * Mark对标记压缩进行了优化，提高了插入和删除效率。
    * Assaf对RBD进行了优化，避免了不必要的内存分配。
    * John对PG日志进行了优化，提升了性能。
    * David解决了与流调试相关的性能问题。
    * Josh对个人对象恢复进行了优化。
* **问题解决**：
    * Peter通过减少缓存修剪频率，提高了性能。
    * Mark优化了BlueStore缓存，减少了内存占用。
    * Mark对BlueStore进行了重构，简化了代码结构。
    * Peter合并了配置归一化检查和配置选项观察者。
    * Assaf优化了对象映射，提高了性能。
    * John对BlueStore后端进行了更新。
    * Josh对BlueStore缓存进行了优化。
* **讨论议题**：
    * **BlueStore缓存**：
        * 讨论了BlueStore缓存存在的复杂性和性能问题，考虑移除BlueStore缓存，仅使用RocksDB缓存进行元数据存储。
        * 认为需要更多数据来了解RocksDB缓存中Bloom过滤器的大小和内存占用。
        * 讨论了禁用PG元项的Bloom过滤器，并部署测试集群来获取数据。
    * **缓存配置**：
        * 讨论了缓存配置的复杂性和用户理解难度，认为应该简化缓存配置，并提供一个用户友好的设置。
        * 认为可以尝试使用简单的启发式方法或更复杂的在线优化模型。
    * **其他**：
        * 讨论了FIO瓶颈和异步消息传递的性能问题。
        * 讨论了编码/解码和CRC计算的优化。
* **决定的事项**：
    * 继续测试和优化OP Tracker性能。
    * 继续优化标记压缩和BlueStore缓存。
    * 继续优化对象映射。
    * 继续优化PG日志。
    * 继续优化个人对象恢复。
    * 讨论BlueStore缓存的移除和RocksDB缓存的优化。
    * 讨论缓存配置的简化。
    * 讨论FIO瓶颈和异步消息传递的性能优化。
    * 收集更多数据来了解RocksDB缓存中Bloom过滤器的大小和内存占用。

**后续行动计划**：

* Peter将测试和优化OP Tracker性能。
* Mark将测试和优化标记压缩和BlueStore缓存。
* Assaf将测试和优化对象映射。
* John将测试和优化PG日志。
* Josh将测试和优化个人对象恢复。
* 讨论BlueStore缓存的移除和RocksDB缓存的优化。
* 讨论缓存配置的简化。
* 讨论FIO瓶颈和异步消息传递的性能优化。
* 收集更多数据来了解RocksDB缓存中Bloom过滤器的大小和内存占用。