---
title: "Ceph Performance Meeting 2018-10-18"
date: 2018-10-18
updated: 2018-10-19
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "RocksDB"
categories:
  - "会议纪要"
outline: deep
---
会议纪要：

**会议时间**： 2018年10月18日
**参会人员**： Nick、Radek、Sage、Josh、Greg、Steve、Angie、Peter、Doug等
**会议主题**： Ceph分布式存储项目开发进展及讨论
**关键细节**：

* **Pull Requests**：
    * Radek提交了一个针对边界代码的优化请求，通过减少容器分配的内存需求来提高效率。
    * Radek还提交了一个针对编译器优化的请求，特别是对于Ceph列表中空数据部分的优化。
    * Sage合并了Radek提交的字符串处理代码。
    * Radek提出了一个关于调试信息的讨论，包括是否应该保留调试信息以及如何减少调试信息的数量。
    * 其他Pull Requests包括缓存大小增加、DMA问题、RBD性能优化等。
* **调试信息**：
    * 会议讨论了调试信息的重要性以及如何减少调试信息的数量。
    * 一些建议包括引入缓存机制、减少不必要的字符串操作以及重新评估日志记录策略。
* **RocksDB**：
    * 讨论了将RocksDB缓存集成到mempool基础设施中的可行性。
    * 讨论了关于RocksDB内存分配策略的改进。
* **Ceph性能**：
    * 讨论了Ceph性能优化，包括RBD性能优化、对象存储性能优化等。
    * 讨论了如何减少CPU使用率以及如何提高性能。
**决定的事项**：
* 接受Radek提交的关于边界代码和编译器优化的Pull Requests。
* 继续讨论调试信息的问题，并尝试减少调试信息的数量。
* 将RocksDB缓存集成到mempool基础设施中。
* 继续优化Ceph性能。
**后续行动计划**：
* Nick将跟进关于调试信息的问题。
* Radek将继续优化RBD性能。
* Sage将继续合并PullRequests。
* 其他团队成员将继续进行Ceph性能优化工作。

**备注**：

* 会议中提到了一些计算机科学/ceph相关领域英文关键词，例如：
    * Pull Requests
    * RocksDB
    * mempool
    * RBD
    * EC
    * SSD
    * CPU
    * latency
    * throughput
    * workload

[标签]
- Ceph
- 分布式存储
- 性能优化
- RocksDB
- 调试信息