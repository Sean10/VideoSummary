---
title: Ordered Bucket Index Shards in RGW - Eric Ivancich, IBM
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- RGW
- 分布式存储
categories: 
- "视频总结"
subtitle: Ordered_Bucket_Index_Shards_in_RGW_-_Eric_Ivancich_IBM
---

在这次Ceph会议中，IBM的Eric Ivancich详细介绍了RGW（Rados Gateway）中的有序桶索引分片（Ordered Bucket Index Shards）的相关内容。以下是会议的要点总结：

### 会议基本信息
- **演讲人**：Eric Ivancich (IBM)
- **背景**：Eric在Ceph领域有超过十年的工作经验，曾就职于Cohort FS（后被Red Hat收购），现属于IBM存储团队。

### 核心讨论内容

#### 1. RGW桶索引基础
- **当前架构**：
  - RGW维护包含桶元数据的系列对象，包括桶入口点、桶实例对象和分片。
- **Resharding机制**：
  - 每个分片最多容纳约100,000个对象。
  - 动态重分片阈值触发扩容/缩容。

#### 2. 哈希分片索引现状
- **工作原理**：
  - 对对象名进行哈希计算，取模确定目标分片。
- **优点**：
  - 恒定时间计算分片位置。
  - 对象分布相对均匀。
- **缺点**：
  - 重分片是全局操作。
  - 桶列表操作复杂且I/O密集。

#### 3. 有序分片索引提案
- **核心改进**：
  - 维护分片间的词典序。
  - 使用OMAP记录分片切割点。
- **优势**：
  - 桶列表I/O大幅降低。
  - 支持局部重分片。
- **挑战**：
  - 热点问题。
  - 分片定位复杂度增加。
  - 版本桶的特殊约束。

#### 4. 技术实现细节
- **分片命名方案**：
  - 改用分层命名。
  - 通过模拟测试验证。
- **性能考量**：
  - 通过缓存减少bucket instance object的频繁读取。
  - 对RocksDB的OMAP操作影响需进一步评估。

#### 5. 路线图
- **目标版本**：
  - Ceph Octopus的次版本发布。
  - 下游RHCS 9.1版本集成。

### Q&A重点摘要
- **分片数量限制**：
  - OMAP限制100,000键值对。
  - 超大规模解决方案可能采用混合索引。
- **迁移策略**：
  - 通过`radosgw-admin`命令将现有哈希分片转换为有序分片。
  - 支持配置新建桶的默认分片策略。
- **性能影响**：
  - CPU开销：插入/删除操作可能涉及对数时间复杂度的排序。
  - RocksDB压缩：需关注频繁插入是否导致额外压缩开销。
- **切割点确定**：
  - 动态确定。
  - 当前需全扫描分片，未来可能开发专用CLS操作。

### 行动计划
- **短期**：
  - 完成Octopus版本的有序分片索引实现。
  - 完善版本桶的特殊情况处理。
- **长期**：
  - 评估混合索引方案的可行性。
  - 优化超大规模桶的支持能力。

### 关键术语
- Ceph/RGW/CRUSH algorithm
- object storage/block storage/file system storage
- OSD/MON/MDS/PG
- RADOS/librados/libcephfs
- cephfs/rbd/radosgw (RGW)
- RESTful API/authentication/authorization
- erasure coding/replication/snapshots/clones
- thin provisioning/iSCSI/Fibre Channel
- NFS/CIFS/POSIX
- Kubernetes/Docker/containerization
- AWS/Azure/Google Cloud/hybrid cloud/multi-cloud
- SSD/HDD/JBOD/SAN/NAS
- failure domain/recovery/resilience
- caching/compression/deduplication/tiering