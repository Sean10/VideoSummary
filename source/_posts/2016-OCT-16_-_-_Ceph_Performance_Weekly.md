---
categories:
- 视频总结
date: 2017-01-11
subtitle: 2016-OCT-16_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- BlueStore
- RocksDB
- 性能优化
title: "'2016-OCT-16 :: Ceph Performance Weekly'"
updated: 2017-01-12
---



**会议纪要**

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Alan、Ben、Igor、Sage、Somnath等

**会议主题**： Ceph社区近期工作进展及讨论

**一、关键进展**

* **内存管理**： Alan提交了实现slab containers的PR，旨在减少内存碎片，并识别代码中存在的低效操作，从而更好地管理内存分配。
* **BlueStore**：
    * Sage对BlueStore进行重构，预计将带来性能提升。
    * Igor开始为异步消息传递实现RDMA，这是XIO消息传递开发的一个替代方案。
    * 优化了RocksDB的日志设置，可能对BlueStore产生积极影响。
    * 移除了BlueStore的事务提交，提高了性能。
    * Sage进行了异步消息传递的性能优化，性能提升了40%。
    * PG级别的快照和事务性能得到提升。
    * BlueStore的紫色压缩设置和快速编码功能已合并。
* **RocksDB**：
    * Sage对RocksDB进行优化，减少了IO元数据更新的频率，提高了性能。
    * 压缩设置已合并。
* **其他**：
    * RC锁定工作进展顺利。
    * Zipkin跟踪工作有望合并。
    * Slab容器工作继续进行。
    * Sandisk的ZetaScale集成工作取得进展，已在4K随机I/O方面超越了BlueStore。

**二、讨论的主要议题**

* **RocksDB行为**： Sage对RocksDB的行为进行了深入研究，并分享了测试结果。结果表明，使用大缓冲区可以提高性能，尤其是在使用NVMe设备时。
* **文件系统性能**： Ben分享了使用Ceph BlueStore和RocksDB进行性能测试的结果，并提出了关于文件描述符限制的问题。
* **ZetaScale**： Sage介绍了Sandisk的ZetaScale集成工作，并分享了测试结果。

**三、决定的事项**

* 继续优化RocksDB和BlueStore。
* 对异步消息传递进行更多测试和评估。
* 对ZetaScale集成工作进行更多研究。

**四、后续行动计划**

* Alan将进一步完善slab containers的PR。
* Sage将继续优化RocksDB和BlueStore。
* Ben将调查文件描述符限制问题。
* Igor将继续开发RDMA异步消息传递。
* Ben将分享更多性能测试结果。
* Sage将分享更多关于ZetaScale集成工作的信息。

**五、其他**

* 会议中提到了一些计算机科学/ceph相关领域英文原文的关键词，例如：
    * slab containers
    * memory fragmentation
    * RDMA
    * async messenger
    * RocksDB
    * compaction
    * file descriptors
    * ZetaScale