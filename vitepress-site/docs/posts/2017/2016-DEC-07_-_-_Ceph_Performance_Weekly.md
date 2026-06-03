---
title: "2016-DEC-07 :: Ceph Performance Weekly"
date: 2017-01-11
updated: 2017-01-12
tags:
  - "性能优化"
categories:
  - "会议纪要"
  - "Ceph"
  - "性能测试"
outline: deep
---
本次会议主要讨论了Ceph分布式存储系统的性能优化，涵盖了以下关键议题：

**一、关键功能跟踪点分析**

*   Steve提交了一个PR，用于在IO路径中添加关键功能的跟踪点，以帮助进行性能分析。
*   讨论如何改进缓冲区列表以避免不必要的复制。
*   Sage和Sam正在测试ZetaScale存储性能，并尝试将其集成到测试套件中。

**二、RBD性能测试**

*   Steve进行了RVD（RADOS erasure coding）与EC（Erasure Coding）的性能测试，结果显示RVD在大型顺序写操作中表现优异。
*   对于小型随机写操作，RVD性能较差，因为需要从主节点获取数据。
*   建议开发一个功能，允许客户端直接从各个碎片读取数据，以减少读取操作的延迟。

**三、ZetaScale存储性能测试**

*   Sage和Sam正在测试ZetaScale存储性能，并尝试将其集成到Ceph中。
*   测试了使用单个kv线程的版本和使用多个kv线程的版本。
*   预计ZetaScale可以减少RocksDB的压缩开销，并提高大型数据集的性能。

**四、IO路径性能分析**

*   Say提交了一个PR，用于生成LTTng跟踪点，以跟踪函数级延迟和OID跟踪点，以跟踪操作ID的飞行路径。
*   分析结果显示，网络延迟和DQ（dispatch queue）操作是影响性能的关键因素。
*   建议优化IO准备、IO队列和线程上下文切换，以减少延迟。

**五、后续行动计划**

*   继续进行RVD和ZetaScale的性能测试，并优化相关功能。
*   分析LTTng跟踪点数据，以识别性能瓶颈。
*   优化IO路径，减少延迟。
*   在下一个会议上分享更多测试结果。