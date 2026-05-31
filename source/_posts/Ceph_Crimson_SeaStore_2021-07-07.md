---
categories:
- 视频总结
date: 2021-08-24
subtitle: Ceph_Crimson_SeaStore_2021-07-07
tags:
- Ceph
- 分布式存储
title: "Ceph Crimson/SeaStore 2021-07-07"
updated: 2021-08-25
---




在2021年7月7日的Ceph Crimson/SeaStore会议中，研发团队主要讨论了以下几个关键议题：

1. **Crimson项目的清理和讨论**：Aaron分享了Crimson项目中的随机清理工作，并讨论了与Jihan关于扩展分配管理器的PR。

2. **IOCTL和控制支持的补丁更新**：Aaron正在开发Ceph的IOCTL和控制支持的下一个补丁版本，并已提交并接收了一些评审意见。

3. **Extent内容的更新问题**：Aaron报告了一个关于Extent内容更新的问题，特别是在并发操作中，可能导致错误的地址获取。

4. **MLIS案例分析**：Riddick分享了关于MLIS案例的分析，指出问题可能与消息处理有关，特别是在OSD重启时可能发生的竞态条件。

5. **Extent Placement Manager的修改**：讨论了如何处理Extent的写入和日志记录。

6. **C-Store性能分析**：正在进行C-Store的性能分析，并尝试添加矩阵以帮助诊断性能问题。

会议中的决定事项包括：

- Aaron将继续优化Extent内容的更新问题，并寻找更稳定的解决方案。
- Riddick将继续分析MLIS案例，特别是关注消息处理和OSD重启时的竞态条件。
- 对于Extent Placement Manager的修改，将继续进行多设备支持的实现。

后续行动计划包括：

- Aaron将提交更新的补丁版本，并继续在Segment Manager中实现接口。
- Riddick将深入研究MLIS案例，并寻找可能的解决方案。
- 所有参会者将继续关注各自负责的模块，确保Ceph的稳定性和性能优化。

此外，会议还讨论了消息处理的防御性编程以及如何在集群中处理可能的错误消息。



改进点：
- 确保所有关键议题、讨论内容、决定事项和后续行动计划都被包含在总结中。
- 保留了原字幕中的英文关键词，如Crimson、MLIS、Extent Placement Manager等。
- 简化了部分描述，以提高可读性。