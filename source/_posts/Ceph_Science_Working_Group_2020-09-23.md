---
categories:
- 会议纪要
date: 2020-09-24
subtitle: Ceph Science Working Group 2020-09-23 会议纪要
tags:
- Ceph
- 分布式存储
- 存储集群
- OpenStack
title: "Ceph Science Working Group 2020-09-23"
updated: 2020-09-25
---




本次会议是Ceph Science Working Group于2020年9月23日举行的小型聚会。会议主要由使用Ceph的研究系统管理员或大型集群辅助管理员组成，旨在讨论与Ceph相关的任何话题。以下是会议的关键细节、主要议题、决定事项以及后续行动计划：

#### 主要议题与讨论内容

1. **近期故障报告**
   - 讨论了近期一次长达四小时的全面停电事件，以及由此导致的集群恢复问题。

2. **Ceph Bug讨论**
   - 讨论了Ceph版本14.2.11和Octopus中的一些问题，如OSD map trimming逻辑错误和文件存储OSD清理问题。

3. **Octopus版本迁移经验**
   - 分享了从Luminous升级到Nautilus的经验，特别是关于S3网关的升级。

4. **OpenStack与S3集成**
   - 讨论了如何在OpenStack环境中集成S3，以及如何处理用户通过OpenStack管理S3凭证和配额的需求。

5. **大容量文件管理问题**
   - 讨论了处理包含大量小文件的S3 bucket时可能遇到的管理和性能问题。

6. **Ceph-CSI使用情况**
   - 讨论了Ceph CSI在Kubernetes环境中的使用情况，特别是与RBD和CephFS的集成。

#### 决定事项

- 对于Ceph版本14.2.11和Octopus中的已知问题，建议社区成员关注并参与修复。
- 对于大容量文件管理问题，建议进一步研究和测试可能的优化措施。

#### 后续行动计划

- 继续监控和报告Ceph版本中的bug和性能问题。
- 对于S3和OpenStack集成问题，建议进一步研究和分享最佳实践。
- 对于Ceph-CSI的使用，建议社区成员分享更多实际使用经验和配置建议。

#### 会议结束

会议在讨论了所有预定议题后结束，下一次会议计划在两个月后的11月25日举行。

[改进后的总结中保留的关键词包括：Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage, block storage, file system storage, consistency, decentralization, performance, bluestore, bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW, RESTful API, authentication, authorization, encryption, erasure coding, replication, snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, dashboard, management, orchestration, automation, integration, containerization, Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, network, topology, failure domain, recovery, resilience, load balancing, caching, compression, deduplication, tiering, performance tuning, benchmarking, testing, validation]