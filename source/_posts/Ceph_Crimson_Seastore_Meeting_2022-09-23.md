---
categories:
- 视频总结
date: 2022-09-23
subtitle: Ceph_Crimson_Seastore_Meeting_2022-09-23
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可伸缩性
- 对象存储
- 块存储
- 文件系统存储
- 一致性
- 去中心化
- 性能
- bluestore
- bluefs
- rocksdb
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- cephfs
- rbd
- radosgw
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 纠错码
- 复制
- 快照
- 克隆
- 虚拟化
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 多云
title: "Ceph Crimson/Seastore Meeting 2022-09-23"
updated: 2022-09-24
---




本次会议主要讨论了Ceph分布式存储系统中的技术议题。与会者探讨了多核分支的进展，特别是iOS的完成情况，并讨论了相关bug的修复。针对omap范围移除功能的优化，讨论了优化存储节点负载、内存拷贝效率、树状结构的调整和平衡，以及与系统稳定性和性能相关的问题。此外，会议还涉及了系统内部关键性错误修复和性能提升措施。在高填充率情况下设备的行为和对Ceph核心代码进行重构的可能性也得到了探讨。

关于Ceph存储节点在高填充率下的行为，讨论了存储使用率和垃圾回收对性能的影响。在bluestore和rocksdb方面，讨论了改进缓存的实现和range操作的性能问题。此外，还提到了对基于pin set的映射优化进行代码美化和性能测试的工作。

会议中提到的行动计划包括：
- 完成多核分支的iOS开发。
- 修复bug并优化omap范围移除功能。
- 改进bluestore和rocksdb的性能。
- 对基于pin set的映射优化进行代码美化和性能测试。

总体而言，本次会议聚焦于Ceph存储系统的性能优化和功能改进，涉及多个关键技术领域。