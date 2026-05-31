---
categories:
- 视频总结
date: 2021-06-02
subtitle: Ceph_Developer_Monthly_2021-06-02
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 安全性
- 可扩展性
- 对象存储
- 块存储
- 文件系统存储
- 高可用性
- 性能
- BlueStore
- BlueFS
- RocksDB
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- CephFS
- RBD
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 复制
- 快照
- 克隆
- iSCSI
- NFS
- CIFS
- POSIX
- 监控
- Dashboard
- 编排
- 自动化
- 容器化
- Kubernetes
- Docker
- 虚拟化
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 多云
- 存储集群
- SSD
- HDD
- SAN
- NAS
- 网络
- 恢复
- 弹性
- 负载均衡
- 缓存
- 压缩
- 去重
- 分层
- 性能优化
- 测试
title: "Ceph Developer Monthly 2021-06-02"
updated: 2021-06-03
---



本次会议主要讨论了Ceph分布式存储系统的多个重要议题，包括故障条件处理、加密策略设计、Manager模块的性能优化以及OSD Map的缓存策略。

1. **故障条件处理**：讨论了当Ceph发现未找到对象时，进入backfill unfound状态的问题，以及重启primary OSD时可能出现的异常情况。会议决定对旧版本加强现有行为，避免崩溃，但不尝试修复。对于master版本，将记录缺失集中的对象，并在backfill过程中处理。

2. **加密策略设计**：讨论了Ceph中的加密策略，特别是SSE-S3的支持。会议决定开始实现SSE-S3，包括支持put bucket encryption API，并考虑使用Vault作为KMS。

3. **Manager模块的性能优化**：讨论了Manager模块在处理依赖关系时可能遇到的性能瓶颈。会议决定尝试合并所有模块到一个解释器中，以减少多进程通信开销，并关注Python新版本中的multi-isolated sub-interpreters的发展。

4. **OSD Map的缓存策略**：讨论了OSD Map的频繁更新可能导致性能问题。会议决定尝试使用缓存策略减少性能开销，并探索使用immutable对象和copy-on-write策略。

会议强调了增加测试覆盖和持续优化的重要性，并确定了各个主题的后续行动计划。