---
categories:
- 视频总结
date: 2019-04-09
subtitle: 2019-03-28_-_Ceph_Performance_meeting
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
title: "'2019-03-28 :: Ceph Performance meeting'"
updated: 2019-04-10
---



### 会议纪要

**会议时间**： 未知
**参会人员**： 未知（可能包括Ben、Adam、Casey等人）
**会议主题**： Ceph RGW性能优化与相关议题讨论

**会议内容**：

* **RGW性能优化**：
    * Ben报告了与Beast和SEO相关的异步工作进展，并提及了对云服务支持的重构。
    * 讨论了QoS（服务质量）在多站点环境下的应用，特别是bucket动态重启的挑战及其设计方案。
    * 探讨了CPU资源限制和提升RGW性能的方法，包括减少线程数量以降低内存消耗和上下文切换开销。
    * 讨论了性能测量方法，如使用wall clock profiler进行性能分析。
    * 分析了nvme驱动和RBD对性能的影响，以及压缩技术对RGW性能的潜在影响。
* **其他议题**：
    * 提及了默认使用debug Amos zero而不是debug iboga miss one的决策。
    * 讨论了librettos库中用于禁用blue store压缩的flag。
* **决定事项**：
    * 推进RGW性能优化工作，包括异步重构、QoS优化、减少线程数量等。
    * 使用wall clock profiler工具进行性能分析。
    * 默认使用debug Amos zero。
* **后续行动计划**：
    * Ben将继续推进RGW性能优化工作。
    * 其他参会人员将根据各自职责推进相关工作。

**备注**：

* 会议中提到了Ceph RGW、Beast、SEO、QoS、nvme、RBD、librettos、blue store、debug Amos zero等关键词。