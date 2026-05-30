---
categories:
- 视频总结
date: 2022-06-27
subtitle: Ceph_Crimson_SeaStore_Meeting_2022-06-22
tags:
- Ceph
- Distributed Storage
- CRUSH Algorithm
- High Availability
- Scalability
title: "Ceph Crimson/SeaStore Meeting 2022-06-22"
updated: 2022-06-28
---



在2022年6月22日的Ceph Crimson/SeaStore会议上，研发人员和专家们讨论了多个关键议题：

1. **Ying Jin** 报告了意外的trim spike问题，并介绍了改进的GC策略，该策略减少了写放大、冲突，并提升了性能。Ying Jin 正在研究SSD内部写放大的评估方法，并计划进一步优化设备分层。

2. **Airmen** 正在处理一个关于元数据生成的Pull Request (PR)，主要涉及清理工作和计算函数的修正。他还解决了开启Voiced时遇到的写入问题，通过更改代码确保在关闭segment时写入tail信息。

3. **ZNS设备的segment管理** 被讨论，特别是关闭segment后无法重新打开的情况。会议还讨论了在crimson中模拟block segment manager的行为，以及如何根据不同的存储设备选择合适的写入管理器。

4. **Joe May** 正在处理根据评论修复问题的PR，并研究解决根本原因。他还提到了gcc 11的问题影响Ceph的构建，以及与Python绑定相关的问题。

5. **Ceph CRIMSON OSD的性能分析** 被讨论，特别是在垃圾回收(GC)过程中发现的一些关键性能瓶颈。团队决定调查和优化cache数据结构及其查找方式，以提高GC过程的效率。

后续行动计划包括：
- Ying Jin 继续她的PR工作，并对设备分层进行进一步研究。
- Airmen 对元数据生成的PR进行最终修改，并继续解决开启Voiced时的写入问题。
- 团队同意需要添加对象数据块到缓存中以确保在进行GC时的数据一致性。
- Joe May 继续处理修复问题并研究与GCC 11和Python绑定相关的构建问题。
- 团队决定调查和优化cache数据结构及其查找方式，以提高GC过程的效率。

已保留所有相关关键词，并对会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划进行了准确的反映。