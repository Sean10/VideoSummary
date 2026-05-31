---
categories:
- 视频总结
date: 2021-11-04
subtitle: Ceph_Performance_Meeting_2021-11-04
tags:
- Ceph
- 分布式存储
- 测试
- CI/CD
title: Ceph Performance Meeting 2021-11-04
updated: 2021-11-05
---


### 会议纪要

#### 会议概述
本次Ceph性能会议主要讨论了Ceph项目的最新进展，包括新提交的PR（Pull Request）、已关闭的PR以及性能测试相关的话题。会议重点关注了BlueStore的细粒度锁定、请求超时问题优化、性能测试CI的现状和改进建议等议题。

#### 主要议题
1. **新PR讨论**
   - **Adam的BlueStore fine grain locking PR**：这是一个重新尝试引入的PR，讨论了其复杂性和潜在的性能提升。
   - **优化请求超时问题**：Casey提交了一个新的PR，通过引入自定义分配器等方法优化了请求超时问题，显著提升了性能，并讨论了CPU使用率的变化和后续的测试计划。

2. **性能测试CI工作**
   - 讨论了当前性能测试CI的现状和存在的问题，特别是关于Classic PRs的性能测试未自动运行的问题。
   - 提出了扩展测试工作负载的建议，包括引入FIO测试，并讨论了如何改进和扩展现有的性能测试框架。
   - 讨论了多节点测试的必要性和可行性，以及如何处理非默认配置（如禁用数据CRC）的问题。

3. **其他更新和讨论**
   - 讨论了其他几个PR的更新情况，包括优化内存使用、配置调整等。
   - 提到了一些长期未有进展的PR，强调了继续讨论和评估的重要性。

#### 决定事项
- 确认了需要进一步调查为何带有性能标签的Classic PRs未自动运行性能测试。
- 决定扩展性能测试框架，首先引入FIO测试，并考虑多节点测试的可行性。
- 讨论了性能测试中非默认配置的问题，建议根据PR的具体内容决定是否启用某些配置。

#### 后续行动计划
- 调查并解决Classic PRs性能测试未自动运行的问题。
- 扩展性能测试框架，引入FIO测试，并考虑多节点测试。
- 继续讨论和评估长期未有进展的PR，确保项目的持续改进和发展。

#### 其他事项
- 确认了下一次会议将讨论Crimson相关的内容，再下一次会议将讨论Balancer的包装器。

#### 会议结束
会议在讨论了所有议题后结束，感谢所有参与者的贡献，并期待下一次会议的讨论。

[改进后的总结内容中包含的Ceph相关关键词]
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