---
title: "2016-SEP-07 :: Ceph Performance Weekly"
date: 2017-01-11
updated: 2017-01-12
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年X月X日
**会议地点**： 线上会议
**参会人员**： Sage, Percival, Charlie, Omar, Adam, Rich, Alan, Sila, Ken, 等
**会议主题**： 讨论Ceph项目中的性能优化工作，包括BlueStore的改进、编码优化以及Page统计的优化。

**关键细节**：

* **BlueStore改进**：
    * Sage在BlueStore的Short Extent Map方面取得了进展并进行了演示。
    * P Odors的CRUSH算法优化为Straw带来了性能提升。
    * 对象存储的IO Engine即将合并。
    * Canada end of it page更新。
* **编码优化**：
    * 探讨使用Group Barrington编码进行空间优化，以减少数据冗余。
    * 讨论针对特定数据类型和应用场景进行编码优化的方法。
    * 认为算法优化比微优化更重要，应优先考虑。
    * 将Page统计的优化视为下一个空间优化关键点。
* **Page统计优化**：
    * 讨论将Page统计更新分为两部分，分别针对频繁更新和不频繁更新的字段。
    * 认为可能需要使用merge operator来处理向后兼容性问题。
    * 认为将Page统计更新分割成单独的数据结构可能是一个可行的方案。

**讨论的主要议题**：

* 如何优化BlueStore的性能。
* 如何进行编码优化以减少数据冗余。
* 如何优化Page统计以减少空间占用。

**决定的事项**：

* Sage将审查P Odors的CRUSH优化代码，并与Sam一起审查。
* 进行BlueStore的Short Extent Map的测试。
* 进行Page统计的优化工作，并考虑使用merge operator来处理向后兼容性问题。

**后续行动计划**：

* Sage将审查P Odors的CRUSH优化代码，并与Sam一起审查。
* 进行BlueStore的Short Extent Map的测试。
* 进行Page统计的优化工作，并考虑使用merge operator来处理向后兼容性问题。
* 探索使用Group Barrington编码进行空间优化的方法。
* 分析Page统计中频繁更新和不频繁更新的字段，并考虑将其分割成单独的数据结构。

**其他事项**：

* 确定了Page统计中的一些字段可能不需要在每次事务中进行更新，可以懒加载或使用不同的数据结构进行处理。
* 认为将编码优化和Page统计优化进行排序，优先处理已知可以带来性能提升的优化。