---
categories:
- 视频总结
date: 2022-02-03
subtitle: Ceph_Performance_Meeting_2022-02-03
tags:
- Ceph
- 性能优化
- 内存管理
- 分布式存储
- CRUSH算法
- Quincy
- MClock
title: Ceph Performance Meeting 2022-02-03
updated: 2022-02-04
---


### 会议纪要

#### 关键细节
- 本次会议主要讨论了Ceph性能优化和内存管理相关议题。
- PR活动主要集中在Quincy特性开发上，没有新或关闭的PR。
- 有一个关于默认编译跟踪的PR被更新，RBD团队正在审查。
- 发现一个可能导致性能回归的PR，与跟踪功能相关，需要密切关注。

#### 讨论的主要议题
- **性能优化**: 讨论了通过调整配置和优化代码来减少内存使用和提高性能的方法。
- **MClock配置文件**: 讨论了不同MClock配置文件（高客户端IO、高恢复操作、平衡）及其对不同操作（如恢复和scrubbing）的影响。
- **Ceph性能测试**: 讨论了在大型集群上使用CBT进行性能测试的计划，特别是关于MClock和scrubbing的测试。

#### 决定的事项
- 决定在Giba集群上运行CBT以测试MClock配置文件和scrubbing性能。
- 决定进一步研究内存使用情况，特别是通过调整tc_malloc线程缓存和优化内存分配策略。

#### 后续行动计划
- Mark将设置Giba集群以便进行CBT测试。
- Ashwarya和Sridhar将使用此集群进行MClock和scrubbing的性能测试。
- 继续研究并优化内存使用，特别是通过改进内存分配和减少碎片化。
- 继续监控和分析可能导致性能回归的PR。
- 探索在客户端区域进行CRUSH计算的成本和可扩展性。
- 与SpeedyB和DigitalOcean合作，测试RocksDB性能改进。