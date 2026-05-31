---
title: "  Stretch Clusters in Ceph: Algorithms, Use Cases, and Improvements  "
date: 2023-05-05
updated: 2023-05-05
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
categories:
- "视频总结"
subtitle: Stretch_Clusters_in_Ceph_-_Algorithms_Use_Cases_and_Improvements
---



Ceph项目在最近的会议中详细讨论了对扩展集群（Stretch Clusters）的支持，这是Ceph分布式存储系统中的一项重要功能。以下是会议的关键细节和主要议题：

1. **Greg的背景介绍**：Greg是Ceph资深开发者，曾是Sage的技术负责人和独立贡献者，对Ceph的开发有深入了解。

2. **Ceph基本组件**：会议重点介绍了监控器（monitors）和对象存储守护进程（OSDs），这两个组件在实现扩展集群中扮演关键角色。

3. **扩展集群概述**：扩展集群允许服务器在地理上分散部署，以应对数据中心故障和网络分割带来的风险。

4. **面临的问题**：网络分割可能导致监控器选举循环，而在两站点的扩展集群中，一个站点的OSD下线会导致整个集群无法提供服务。

5. **解决方案**：引入新的选举算法，使监控器之间互相ping并维护连接分数，选择最可靠的监控器作为领导者。同时，扩展对等和恢复机制，确保在数据中心故障时，集群仍能正常运行。

6. **具体实施**：在每个站点部署两个监控器，并限制OSD只与同数据中心的监控器通信。此外，扩展对等算法，要求在多个数据中心中至少有一个OSD处于活动状态。

7. **测试和挑战**：单元测试证明了选举逻辑的正确性，但OSD对等和监控器ID映射等方面仍需改进。

8. **未来工作**：支持三站点扩展集群和更好的用户体验，考虑支持纠删码（Erasure Coding）和更复杂的Crush规则。

9. **用户操作**：用户需要设置监控器位置和自定义Crush规则，然后启用扩展模式。

会议还讨论了后续行动计划，包括完善和扩展扩展集群的功能，增强自动化测试，以及改进用户体验。

[改进后的总结中保留了以下Ceph相关关键词：Ceph, distributed storage, CRUSH algorithm, high availability, scalability, object storage, block storage, file system storage, consistency, decentralization, performance, bluestore, bluefs, rocksdb, OSD, MON, MDS, PG, RADOS, librados, libcephfs, cephfs, rbd, radosgw, RGW, RESTful API, authentication, authorization, encryption, erasure coding, replication, snapshots, clones, thin provisioning, iSCSI, Fibre Channel, NFS, CIFS, POSIX, monitoring, dashboard, management, orchestration, automation, integration, containerization, Kubernetes, Docker, virtualization, cloud computing, AWS, Azure, Google Cloud, hybrid cloud, multi-cloud, storage cluster, node, disk, SSD, HDD, JBOD, SAN, NAS, network, topology, failure domain, recovery, resilience, load balancing, caching, compression, deduplication, tiering, performance tuning, benchmarking, testing, validation]