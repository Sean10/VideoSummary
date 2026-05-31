---
title: " 2016-JUN-21 -- Ceph Tech Talks: Bluestore "
date: 2016-06-23
updated: 2016-06-23
tags:
- Ceph
- BlueStore
- 分布式存储
- 性能优化
categories:
- "视频总结"
---

subtitle: 2016-JUN-21_--_Ceph_Tech_Talks_-_Bluestore

### 会议纪要

**会议时间**： 2016年6月21日

**会议主题**： Ceph Tech Talks - Bluestore 后端存储介绍

**参会人员**： Sage (主讲人) 及其他 Ceph 团队成员

**会议内容**：

**一、会议背景**

* Ceph 是一个可扩展、高性能的分布式存储系统，提供对象、块和文件存储接口。
* Ceph 的存储后端是 Rados，它使用文件系统来存储数据。
* 传统的文件存储方式存在性能瓶颈和复杂性，因此需要新的存储后端。

**二、讨论的主要议题**

1. **文件存储的局限性**：
    * POSIX 接口限制，无法提供原子性事务。
    * 文件系统遍历效率低，不适合大量对象存储。
    * 需要使用复杂的目录结构来模拟对象存储。

2. **新存储 (New Store)**：
    * 使用 RocksDB 作为键值数据库来存储元数据。
    * 对象数据存储在 POSIX 文件中。
    * 存在日志和文件系统日志的双重开销，性能不佳。

3. **蓝存储 (Blue Store)**：
    * 结合了新存储和块设备的特点。
    * 使用 RocksDB 存储元数据。
    * 对象数据直接写入块设备。
    * 提供原子性事务、高效的对象枚举、克隆和压缩功能。

**三、决定的事项**

* 将 Blue Store 作为 Rados 的候选存储后端。
* 在 Jewel 和最新 master 版本中提供 Blue Store 的实验性支持。
* 进行性能测试和优化。
* 将 Blue Store 集成到 Kraken 版本中，作为默认存储后端。

**四、后续行动计划**

* 完善元数据编码效率。
* 支持 ZetaScale 作为 RocksDB 的替代方案。
* 优化压缩和检查和功能。
* 添加池级别属性，支持不同的数据存储策略。
* 开发 SMR 硬盘支持。
* 支持 SPDK，优化 NVMe 设备性能。

**五、关键术语**

* Ceph
* Rados
* RocksDB
* POSIX
* Blue Store
* New Store
* 原子性事务
* 对象枚举
* 克隆
* 压缩
* 检查和
* BlueFS
* RocksDB
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
* checksum
* inline compression
