---
title: "Ceph Performance Meeting 2021-12-09"
date: 2021-12-09
updated: 2021-12-14
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 主要议题

1. **Pull Requests (PRs) 更新**
   - 讨论了多个PR的进展情况，包括MD日志段优化、Gill处理优化、Alex大小设置、TTL缓存实现、Whip主平衡器、基于Huge Page的读缓冲区、BlueFS细粒度锁定、Bob fsck内存消耗优化、OSD PG移除优化等。
   - 重点讨论了Bob fsck的内存使用问题，担心在特定情况下可能会有共享blob错误通过fsck过程。

2. **Bob fsck内存使用问题**
   - Adam提出对改进后的Bob fsck过程的担忧，担心某些情况下可能会有共享blob错误通过fsck过程。
   - Igor解释了改进后的Bob fsck不会提供错误检测，但在某些情况下可能会标记一些仍然良好的blob为潜在损坏。
   - 讨论了在容器环境中运行OSD的内存限制问题，以及如何避免内存不足导致的崩溃。

3. **TC Malloc线程缓存大小配置**
   - Adam提议将TC Malloc线程缓存大小设置为可配置选项，而不是使用环境变量。
   - 讨论了在perf glue代码中直接处理TC Malloc线程缓存大小的可能性，以及如何在全局配置中处理。

4. **内存分配器讨论**
   - 讨论了不同内存分配器（如TC Malloc和Libsy Malloc）的内存碎片问题。
   - 提到了Crimson中使用C-star分配器的情况，以及可能的改进方向。

#### 决定事项
- 需要进一步讨论和测试Bob fsck的内存使用问题，特别是在容器环境中的应用。
- 确定将TC Malloc线程缓存大小设置为可配置选项，并考虑在perf glue代码中处理。
- 讨论了在Crimson中使用TC Malloc替代Libsy Malloc的可能性，特别是在BlueStore和AlienStore中。

#### 后续行动计划
- 继续审查和测试相关PRs。
- 进一步讨论和优化Bob fsck的内存使用问题。
- 确定TC Malloc线程缓存大小的配置方式，并在perf glue代码中实现。
- 探索在Crimson中使用TC Malloc替代Libsy Malloc的可能性。

#### 下次会议议题
- 讨论OSD同步写性能问题。
- 讨论更广泛的自性能优化话题。

**会议结束时间**: 会议持续了一个小时，所有议题均已讨论完毕。下次会议将继续讨论未尽事宜。

[原文中关键词保留，如Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage, block storage, file system storage, consistency, decentralization, performance, bluestore, bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW, RESTful API, authentication, authorization, encryption, erasure coding, replication, snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, dashboard, management, orchestration, automation, integration, containerization, Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, network, topology, failure domain, recovery, resilience, load balancing, caching, compression, deduplication, tiering, performance tuning, benchmarking, testing, validation]