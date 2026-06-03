---
title: "Ceph Crimson/SeaStore 2021-07-21"
date: 2021-07-21
updated: 2021-08-24
tags:
  - "Ceph"
  - "性能优化"
  - "分布式存储"
  - "CRUSH算法"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 关键细节
- **上周工作回顾**：
  - 对与scrub相关的逻辑进行了审查和调整，将其提取到独立的队列中，以减少crimson的影响并解决由refractory引入的一些回归问题。
  - 提交了sister patch的第三个版本，增加了ceph ctl和控制接口到siege。
  - 审查了一些gears，提供了类似magic的支持，但在测试中遇到了一些不可复现的问题。

- **本周工作计划**：
  - 继续优化buffer list cstr，解决因空carriage buffer指针导致的低效问题。
  - 进行crimson的性能分析，特别是在使用4k随机读取时，观察到每操作的周期数显著增加。
  - 探索使用spin lock替代semaphore的可能性，以提高性能。

#### 讨论的主要议题
- **性能优化**：
  - 讨论了semaphore的使用对性能的影响，特别是在高并发情况下的效率问题。
  - 探讨了使用spin lock替代semaphore的可能性，以减少等待时间。

- **测试方法**：
  - 讨论了使用fio和rbd进行性能测试的有效性，以及如何避免客户端库对测试结果的影响。

#### 决定的事项
- **性能测试策略**：
  - 决定使用fio和rbd进行更深入的性能测试，确保客户端和服务器端在不同的核心上运行，以避免资源争用。

- **代码优化**：
  - 决定进一步探索和实施spin lock替代semaphore的方案，以提高系统的整体性能。

#### 后续行动计划
- **性能测试**：
  - 使用fio和rbd进行更全面的性能测试，特别是在高并发和不同负载条件下的测试。

- **代码优化**：
  - 实施spin lock替代semaphore的方案，并进行性能对比测试，以验证优化效果。

- **持续监控**：
  - 持续监控系统的性能，特别是在引入新优化后的表现，确保没有引入新的性能问题。

#### 错误、误解或遗漏的信息
- 原始字幕中提到的“fixes”和“investigations”部分在总结中未体现。
- 原始字幕中提到的关于性能测试的详细讨论，如fio和rbd的使用方法，在总结中简化了。

#### 相关关键词
- Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage, block storage, file system storage, consistency, decentralization, performance, bluestore, bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW, RESTful API, authentication, authorization, encryption, erasure coding, replication, snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, dashboard, management, orchestration, automation, integration, containerization, Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, network, topology, failure domain, recovery, resilience, load balancing, caching, compression, deduplication, tiering, performance tuning, benchmarking, testing, validation