---
categories:
- 视频总结
date: 2018-12-25
subtitle: Crimson_Seastar_OSD_Meeting_2018-12-25
tags:
- Ceph
- 分布式存储
- 性能优化
title: "Crimson/Seastar OSD Meeting 2018-12-25"
updated: 2018-12-25
---



### 会议纪要

**会议时间**： 2018年12月25日

**参会人员**： Michael、Rico、Chris、Jim、Lucy、TJ、Piggy、Riddle等

**会议主题**： 讨论Ceph分布式存储中消息传递机制、连接管理、性能优化等问题。

**关键细节**：

* **消息传递机制**：
    * Michael在修复回归问题时发现了大量失败，特别是在连接销毁时。
    * Rico提出需要修复代码，并隐藏异常。
    * Jim强调解决并发消息传递中的bug和异常的重要性。
    * Piggy和Riddle讨论了连接引用和数据结构的设计问题。
* **连接管理**：
    * Michael和Rico讨论了连接跨引用和数据结构的设计。
    * Piggy和Riddle讨论了连接引用的共享和修改。
    * Rico建议使用socket和输入输出字符串进行调试。
* **性能优化**：
    * Michael和Rico探讨了使用用户空间调度器的优缺点。
    * Piggy和Riddle讨论了单线程和多线程设计的选择。
    * Rico提出使用共享无锁设计来提高性能。
    * Jim提到使用Nvme设备时的性能优化。
* **后续行动计划**：
    * Michael将继续修复回归问题。
    * Rico将继续解决消息传递中的bug和异常。
    * Jim将继续调试消息传递机制。
    * Piggy和Riddle将继续优化连接管理。
    * Riddle将继续研究性能优化方案。

**讨论的主要议题**：

* 消息传递机制的设计和优化。
* 连接管理的设计和优化。
* 性能优化方案的选择。

**决定的事项**：

* 继续修复消息传递和连接管理中的bug。
* 优化性能。
* 研究单线程和多线程设计的选择。

**后续行动计划**：

* Michael修复回归问题。
* Rico解决消息传递中的bug。
* Jim调试消息传递机制。
* Piggy和Riddle优化连接管理。
* Riddle研究性能优化方案。

**备注**：

* 会议中提到了一些Ceph相关的关键词，如fulcrum、contest、mentos、shard、object store、OSD、PG、connection、socket等。
* 会议中涉及到的技术问题较为复杂，需要进一步研究和讨论。