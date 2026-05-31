---
categories:
- 视频总结
date: 2018-10-17
subtitle: Ceph_Performance_Meeting_20180-9-20
tags:
- Ceph
- 分布式存储
- 性能优化
title: Ceph Performance Meeting 20180-9-20
updated: 2018-10-18
---



在Ceph性能会议中，与会人员讨论了一系列关于Ceph分布式存储系统的性能优化和内存分配的问题。以下是会议的关键细节和讨论的主要内容：

**关键细节**：

* **Pull Requests**： Sage移除了不再使用的死代码，并优化了MDS的性能；讨论了容器与slab分配的优化以及使用持久内存作为RBD持久缓存的改进。
* **内存分配问题**： 讨论了Ceph在内存分配方面的挑战，包括buffer列表的碎片化、对象池的使用以及TC Malloc分配器。
* **性能优化**： 讨论了Ceph在性能方面的挑战，包括CPU使用率、I/O吞吐量以及内存使用率。讨论了使用性能计数器、基准测试和QoS框架来优化性能。

**决定的事项**：

* Sage将负责合并PRS并解释相关改进。
* Mark将继续解决内存分配问题，并探索使用对象池和环形缓冲区的可行性。
* Marcus将创建一个“邪恶列表”，列出Ceph中存在内存分配问题的代码。
* Matt将负责使用性能计数器和基准测试来评估Ceph的性能。
* Shelby将负责使用QoS框架来优化Ceph的性能。

**后续行动计划**：

* Sage将合并PRS并更新相关代码。
* Mark将探索使用对象池和环形缓冲区的可行性，并解决内存分配问题。
* Marcus将创建一个“邪恶列表”。
* Matt将使用性能计数器和基准测试来评估Ceph的性能。
* Shelby将使用QoS框架来优化Ceph的性能。

**关键词**：

* Pull Requests
* Dead code
* Mutex
* Performance counter
* Heap allocation
* MDS
* Shard
* Persistent memory
* Buffer list
* Object pool
* TC Malloc
* Memory fragmentation
* Performance
* CPU utilization
* I/O throughput
* Quality of Service (QoS)
* Benchmark
* Black box testing