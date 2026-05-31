---
categories:
- 视频总结
date: 2015-03-06
subtitle: CDS_Infernalis_Day_1_--_OSD_-_Erasure_Coding_Pool_Overwrite_Support
tags:
- Erasure Coding
- Ceph
- RBD
title: "'CDS Infernalis (Day 1) -- OSD: Erasure Coding Pool Overwrite Support'"
updated: 2015-03-07
---



### 会议纪要

**会议主题**： Erasure Coding (EC) 池覆盖支持讨论

**会议时间**： CDS Infernalis 会议第二天

**参会人员**： 多位 Ceph 开发者

**会议内容**：

**主要议题**：

* 讨论了在 Erasure Coding (EC) 池中实现覆盖支持的可能性，尤其是针对 Rados Block Device (RBD) 的应用。
* 分析了不同实现方案的优缺点，包括：
    * 回滚日志
    * 两阶段提交
    * 不支持覆盖
    * 改进 RBD 数据布局
    * 缓存层实现

**讨论结果**：

* 两阶段提交方案被认为具有确定性、可预测性和与 RAID 类似的行为，是一个值得尝试的方案。
* 回滚日志方案由于需要额外的写入操作，可能引入较大的延迟，因此被认为不如两阶段提交方案。
* 不支持覆盖被认为是最简单的方法，但可能无法满足某些应用的需求。
* 改进 RBD 数据布局和缓存层实现被认为是可行的方案，但需要进一步研究和评估。

**行动计划**：

* 由参会者之一负责实现两阶段提交方案或原型。
* 进一步研究其他方案的可行性和实现细节。
* 在决定最终方案之前，进行更多的讨论和评估。

**其他要点**：

* 实现覆盖支持需要修改 Ceph 的某些核心组件，例如 PG 信息和 OSD 类。
* 在实现覆盖支持之前，需要考虑数据一致性和可用性等问题。
* 需要评估不同方案的性能和可扩展性。

**关键词**：

* Erasure Coding (EC)
* 覆盖支持
* Rados Block Device (RBD)
* 回滚日志
* 两阶段提交
* PG 信息
* OSD 类