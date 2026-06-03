---
title: "2019-03-14 :: Ceph Performance meeting"
date: 2019-04-15
updated: 2019-04-15
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年3月14日

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph分布式存储项目性能更新与讨论

**会议内容**：

**一、PR更新与讨论**

1. **新PR**：
    - 一项关于信使应用的PR报告了显著的增长，值得进一步研究。
    - 一项针对异步连接的优化PR，专门优化回环连接。
    - 一项针对MDS的PR，将不必要的标准列表使用转换为标准向量。
    - 一项更新EM时钟的PR，可能包含性能提升。
    - 一项改进对象映射性能的PR。
    - 一项异步信使优化PR，等待知识更新。
    - 一项信使PR，批量处理和发送消息，但性能测试未改善。
    - 一项Rgw性能PR，包含修复和优化。
    - 一项Lib RB多缓存回线程PR，与PR 6.6.7.5有所重叠。

2. **未决PR**：
    - 多个信使优化PR，正在持续优化中。
    - 蓝办公室读取周期性丢弃功能和蓝存储PR，可能不会很快落地。

**二、性能瓶颈与优化**

1. **信使线程**：
    - 在低CPU使用场景下，信使线程在日志代码中锁定，消耗大量CPU资源。
    - 考虑减少日志记录，或使用更高效的日志记录方式。
    - 探讨使用自旋锁替换互斥锁的可能性。

2. **对象生命周期与内存管理**：
    - 在代码中创建和删除大量临时对象，导致性能开销。
    - 寻找避免创建和删除对象的方法，优化对象生命周期。

**三、外部库优化**

1. **外部库依赖**：
    - 讨论了Ceph对外部库的依赖，特别是加密库。
    - 考虑使用自定义版本的加密库，以获得更好的性能。
    - 讨论了不同平台和硬件对性能的影响。

2. **OpenSSL优化**：
    - 探讨了使用OpenSSL异步接口和同步接口对性能的影响。
    - 考虑使用OpenSSL的SSE4.2加速功能。

**四、其他讨论**

1. **Keystone PKI令牌**：
    - 讨论了Keystone PKI令牌的使用，以及可能的替代方案。
    - 考虑使用OpenSSL的CMS支持。

**五、后续行动计划**

1. 继续跟踪和审查未决PR。
2. 研究信使线程和对象生命周期优化方案。
3. 探索外部库优化方案。
4. 准备Nautilus发布。

**六、会议总结**

本次会议讨论了Ceph项目的最新进展，包括PR更新、性能瓶颈优化和外部库优化。会议明确了后续行动计划，并确定了下一步工作重点。会议重点关注了信使线程的性能瓶颈、对象生命周期与内存管理优化，以及外部库的优化策略。

会议中提到的关键Ceph相关关键词包括：Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage, block storage, file system storage, consistency, decentralization, performance, bluestore, bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW, RESTful API, authentication, authorization, encryption, erasure coding, replication, snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, dashboard, management, orchestration, automation, integration, containerization, Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, network, topology, failure domain, recovery, resilience, load balancing, caching, compression, deduplication, tiering, performance tuning, benchmarking, testing, validation。