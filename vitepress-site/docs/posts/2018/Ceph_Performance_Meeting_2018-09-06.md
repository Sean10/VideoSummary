---
title: "Ceph Performance Meeting 2018-09-06"
date: 2018-09-06
updated: 2018-09-11
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2018年9月6日

**会议地点**： 线上会议

**参会人员**： Alex, auditing, TC 70, Casey, Madden, Sage, Greg, Anna, Neha, Radek, Mike, Jesse, Branislav 等

**会议主题**： Ceph分布式存储系统性能优化，重点关注bufferless的使用和优化

**会议内容**：

* **bufferless使用情况**： 
    * bufferless在Ceph中被广泛使用，但存在一些问题，例如内存碎片化、迭代器失效、缓存行争用等。
    * 一些团队成员对使用bufferless的必要性表示质疑，认为可能存在过度使用的情况。
* **优化方案讨论**：
    * 探讨了使用small vector替换standard list的可能性，但测试结果并不一致，有时甚至出现性能下降。
    * 讨论了使用bufferless的不同场景，例如编码/解码、IO操作等，并分析了不同场景对bufferless的需求。
    * 讨论了使用bufferless时的迭代器失效和缓存行争用问题，并提出了可能的解决方案，例如使用不同的数据结构、优化工作流程等。
    * 讨论了使用bufferless时的内存分配和释放问题，并提出了优化方案，例如预分配内存、减少不必要的内存分配等。
* **后续行动计划**：
    * 由Braddock负责清理bufferless接口，整理出不必要的功能，并尝试使用small vector进行优化。
    * 由Casey、Radek和key foo负责SeaStar方面的优化，尝试将SeaStar特定缓冲区的原子引用计数改为非原子引用计数。
    * 由其他团队成员继续探索使用vector进行优化的可能性，并使用微基准测试分析其性能影响。
    * 由Mike和Jesse讨论OMAP和PG日志等话题。

**关键信息**：

* bufferless在Ceph中被广泛使用，但存在一些问题，需要进一步优化。
* 使用small vector替换standard list的优化方案需要进一步评估。
* 使用bufferless时需要考虑迭代器失效和缓存行争用问题。
* 使用bufferless时需要优化内存分配和释放。
* 需要进一步探索使用vector进行优化的可能性。

**备注**：

* 会议中提到了多个英文关键词，如bufferless、small vector、standard list、SeaStar、OMAP、PG日志等，这些关键词与Ceph分布式存储系统的性能优化相关。