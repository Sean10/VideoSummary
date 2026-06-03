---
title: "CDS Hammer (Day 2) - Quota Discussion"
date: 2014-10-30
updated: 2014-10-30
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议主题**： 讨论Ceph分布式存储系统中CephFS配额支持的实现以及配额与子树的关系

**会议时间**： 2023年11月（具体日期未知）

**参会人员**： Sage, Yanchon, Josh, John Craig, Lee（通过聊天室）

**会议内容**：

**1. 配额支持讨论**

* Sage介绍了CephFS配额支持的实现方案，包括如何在目录创建时集成文件parents，并查找所有配额信息和状态。
* 指出配额实现可能不够精确，需要进一步改进。
* 讨论了在创建操作频繁发生时配额可能被超限的问题。

**2. 子树配额跟踪**

* Sage提到当前子树配额跟踪存在一些问题，例如在文件重命名时配额信息不会更新，导致配额无法正确执行。
* 提出使用“subtree”概念来跟踪文件属于哪个配额，确保检查正确的配额。

**3. 配额与子卷**

* Josh建议将配额与子卷结合，以便在目录上设置配额并创建快照。
* 讨论了使用现有的“snap realm”数据结构来跟踪inode成员资格，并使用“sub volume”概念来限制操作。

**4. 测试和改进**

* Sage建议添加测试用例来验证配额功能，并确保它能够在达到配额限制时阻止写入操作。
* 讨论了对配额实现进行改进的建议，例如处理截断操作和优化统计信息传播。

**5. 决策**

* 会议决定将配额与子卷结合，并使用现有的“snap realm”数据结构来跟踪inode成员资格。
* 决定添加测试用例来验证配额功能，并对配额实现进行改进。

**后续行动计划**：

* Sage将添加测试用例来验证配额功能。
* Sage将对配额实现进行改进，例如处理截断操作和优化统计信息传播。
* John Craig将研究使用更严格的目录结构来限制配额的方法。

**关键词**：

* CephFS配额
* subtree
* sub volume
* snap realm
* inode
* MTS
* quota enforcement
* truncate operation
* Ceph
* 分布式存储
* CRUSH algorithm
* high availability
* scalability
* object storage
* block storage
* file system storage
* consistency
* decentralization
* performance
* bluestore
* bluefs
* rocksdb
* OSD
* MON
* MDS
* PG
* RADOS
* librados
* libcephfs
* cephfs
* rbd
* radosgw
* RGW
* RESTful API
* authentication
* authorization
* encryption
* erasure coding
* replication
* snapshots
* clones
* thin provisioning
* iSCSI
* Fibre Channel
* NFS
* CIFS
* POSIX
* monitoring
* dashboard
* management
* orchestration
* automation
* integration
* containerization
* Kubernetes
* Docker
* virtualization
* cloud computing
* AWS
* Azure
* Google Cloud
* hybrid cloud
* multi-cloud
* storage cluster
* node
* disk
* SSD
* HDD
* JBOD
* SAN
* NAS
* network
* topology
* failure domain
* recovery
* resilience
* load balancing
* caching
* compression
* deduplication
* tiering
* performance tuning
* benchmarking
* testing
* validation