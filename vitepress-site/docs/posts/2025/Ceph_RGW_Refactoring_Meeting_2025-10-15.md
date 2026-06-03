---
title: "Ceph RGW Refactoring Meeting 2025-10-15"
date: 2025-10-15
updated: 2025-10-16
tags:
  - "Ceph"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
### 会议关键信息

- **主持人**: Joseph
- **主要参会人员**: Casey, Adam, Eric 等核心开发成员
- **讨论版本**: Tentacle 版本发布相关事项

### 主要讨论议题

#### 1. Tentacle 版本发布阻塞问题

- **讨论点**：关于几个已合并/新开的 PR 中报告的与**replication lifecycle**相关的 bug 是否应阻塞 Tentacle 发布，特别是涉及**data loss from garbage collection bypass**的严重问题。
- **决策结果**：不阻塞 Tentacle 发布，但会在**release notes**中明确标注已知问题。严重修复将通过标准**backport流程**进入后续点版本。
- **判断标准**：非回归性问题且已在Squid版本中存在。

#### 2. 技术债务与测试问题

- **未初始化条件(uninit condition)问题**：
  - 在多环境中重现（Fedora/Ubuntu）。
  - 可能与**Valgrind**版本或**TC Malik**相关。
  - 行动计划：在Folio 7(CentOS 9)环境复现，尝试构建禁用TC Malik的版本。
- **S3测试迁移**：
  - Adam 的PR正在将**S3 tests**移入Ceph主仓库。
  - 待解决问题：分支参数传递。
  - 迁移影响：现有PR需要重新针对Ceph repo提交，各版本分支需对应同步。

### 行动计划

1. **版本发布**：
   - 推进Tentacle最终版发布。
   - 在release notes中添加已知问题说明。
   - 严重bug修复进入后续点版本。
2. **问题排查**：
   - Casey继续调查uninit condition问题。
   - Adam完善S3测试迁移PR。
3. **测试迁移**：
   - 完成S3测试到主仓库的迁移。
   - 协调各版本分支同步。

### 保留关键词

- Ceph
- distributed storage
- CRUSH algorithm
- high availability
- scalability
- object storage
- block storage
- file system storage
- consistency
- decentralization
- performance
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
- authentication
- authorization
- encryption
- erasure coding
- replication
- snapshots
- clones
- thin provisioning
- iSCSI
- Fibre Channel
- NFS
- CIFS
- POSIX
- monitoring
- dashboard
- management
- orchestration
- automation
- integration
- containerization
- Kubernetes
- Docker
- virtualization
- cloud computing
- AWS
- Azure
- Google Cloud
- hybrid cloud
- multi-cloud
- storage cluster
- node
- disk
- SSD
- HDD
- JBOD
- SAN
- NAS
- network
- topology
- failure domain
- recovery
- resilience
- load balancing
- caching
- compression
- deduplication
- tiering
- performance tuning
- benchmarking
- testing
- validation