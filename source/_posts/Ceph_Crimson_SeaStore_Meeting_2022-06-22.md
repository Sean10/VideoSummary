---
title: "Ceph Crimson/SeaStore Meeting 2022-06-22"
date: 2022-06-27
updated: 2022-06-28
tags:
categories:
- "视频总结"
subtitle: tech
---


会议重点概括：

1. Ying Jin报告了意外的trim spike问题，并提到改进的GC策略减少了写放大、冲突，并提升了性能。同时，她正在研究SSD内部写放大的评估方法，并计划进一步优化设备分层。

2. Airmen提到他正在处理一个关于元数据生成的Pull Request (PR)，主要涉及清理工作和计算函数的修正。他还在解决开启Voiced时遇到的写入问题，通过更改代码确保在关闭segment时写入tail信息。

3. 对于ZNS设备的segment管理，讨论了在关闭segment后无法重新打开的情况，因为大多数设备不支持重新打开已关闭的segment。还讨论了在crimson中模拟block segment manager的行为，以及如何根据不同的存储设备选择合适的写入管理器。

4. Joe May正在处理根据评论修复问题的PR，并研究解决根本原因。他还提到了有关gcc 11的问题影响Ceph的构建，以及与Python绑定相关的问题。

5. 讨论了Ceph CRIMSON OSD的性能分析结果，特别是在垃圾回收(GC)过程中发现的一些关键性能瓶颈，如空间回收过程的时间增加，以及可能的优化点。

后续行动计划：

- Ying Jin将继续她的PR工作，并对设备分层进行进一步研究。

- Airmen将对元数据生成的PR进行最终修改，并继续解决开启Voiced时的写入问题。

- 团队同意需要添加对象数据块到缓存中以确保在进行GC时的数据一致性。

- Joe May将继续处理修复问题并研究与GCC 11和Python绑定相关的构建问题。

- 根据性能分析结果，团队决定调查和优化cache数据结构及其查找方式，以提高GC过程的效率。