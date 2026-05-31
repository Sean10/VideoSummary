---
title: "  2019-01-31 :: Ceph Performance meeting  "
date: 2019-02-04
updated: 2019-02-05
tags:
- 性能
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
categories:
- "视频总结"
subtitle: 2019-01-31_-_-_Ceph_Performance_meeting
---



**会议纪要**

**会议时间**： 2023年[具体日期]

**参会人员**： Sage, Ma Jian Pang, Cruising, Radek, Keefe, Braddock, Adam, Casey, Nick, Matt, French等

**会议主题**：

* 确认和讨论Ceph分布式存储项目中的最新进展和问题。
* 讨论Ceph在容器工作负载中的性能问题，特别是创建文件系统时的延迟。
* 探讨Ceph-RBD的性能和未来发展方向。

**关键细节和讨论议题**：

* **批量处理和发送消息工作**： Ma Jian Pang的工作得到Sage的赞赏，并计划进行测试。
* **memstore优化**： Radek开发的Science Star变体旨在消除不必要的锁定和原子操作，并利用Crimson测试阶段的特性。与会者对此表示兴奋，并期待进一步进展。
* **IObject集成**： Adam将IObject集成到RGW中，以优化性能，并建议将RGW特定的更改拆分为单独的PR。
* **性能问题**： Nick报告了在创建文件系统时遇到的问题，特别是在使用XFS的情况下，与会者讨论了可能的解决方案，如将零填充转换为丢弃操作。
* **Ceph-RBD性能**： Nick正在重新编写FIO CBT基准测试，以简化测试过程并提高效率。与会者讨论了Ceph-RBD的不同实现，包括RBD fuse和TCM。

**决定的事项**：

* Sage将尝试测试Ma Jian Pang的工作。
* Radek将继续开发Science Star。
* Adam将集成IObject到RGW。
* Nick将重新编写FIO CBT基准测试。
* 讨论将关于操作和SMDs的讨论主题添加到下周会议议程。

**后续行动计划**：

* Sage、Radek、Adam和Nick将继续他们的工作。
* 将讨论操作和SMDs的议题添加到下周会议议程。
* 尝试使用其他文件系统（如ext4和XFS）来避免XFS的延迟问题。

**备注**：

* 会议中提到了以下计算机科学/ceph相关领域英文关键词：
    * batch handling
    * send message
    * memstore
    * crimson
    * science star
    * intrusive data structures
    * RGW
    * IObject
    * XFS
    * Ceph-RBD
    * FIO CBT benchmarks