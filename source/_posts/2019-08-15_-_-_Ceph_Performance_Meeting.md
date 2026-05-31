---
categories:
- 视频总结
date: 2019-08-15
subtitle: 2019-08-15_-_-_Ceph_Performance_Meeting
tags:
- 性能
- 存储集群
title: "'2019-08-15 :: Ceph Performance Meeting'"
updated: 2019-08-16
---




本次Ceph性能会议纪要概述了Ceph社区在性能优化、QoS功能实现、兼容性等方面的工作进展和讨论。

**一、本周工作进展**

* **BlueStore优化**：
    * Igor提交了优化BlueStore中设备空间利用的pull request，通过简化空间管理流程提高效率。
    * Sam提交了关于BlueStore QoS功能的pull request，并分析了BlueStore的NVMe性能，发现并发性对性能有显著影响。
    * Jinping提交了关于BlueStore锁定的pull request，旨在减少锁定，提高性能。
    * Egor提交了关于BlueStore性能优化的pull request，包括减少锁获取和更新finisher。
    * Adam继续推进BlueStore的优化工作，包括将IOU ring相关的工作移到后台运行，并对Object存储进行了优化。
    * Sonia探索了使用4K块大小的BlueStore性能，并进行Alligator aging测试的改进。
* **BlueStore QoS功能**：
    * 讨论了如何实现BlueStore的QoS功能，以满足不同用户的需求。
    * 讨论了如何通过节流值控制不同用户的I/O请求。
* **BlueStore与RBD的兼容性**：
    * 讨论了如何确保BlueStore与RBD的兼容性。
    * 讨论了如何处理不同存储引擎之间的性能差异。

**二、决定的事项**

* 审查Igor的优化pull request。
* 将跟踪点集成到CDT中，并进行QoS实验。
* 继续推进BlueStore的优化工作，并与社区进行讨论。
* 与社区讨论4K块大小对BlueStore性能的影响。

**三、后续行动计划**

* 继续优化BlueStore的性能。
* 实现BlueStore的QoS功能。
* 确保BlueStore与RBD的兼容性。
* 对不同存储引擎进行性能测试。
* 改进BlueStore的Alligator aging测试。
* 进行更多关于4K块大小对BlueStore性能影响的测试。

**总结**

本周Ceph社区在BlueStore性能优化、QoS功能实现等方面取得了进展，并讨论了后续的工作计划。社区将继续努力，为用户提供更好的存储解决方案。