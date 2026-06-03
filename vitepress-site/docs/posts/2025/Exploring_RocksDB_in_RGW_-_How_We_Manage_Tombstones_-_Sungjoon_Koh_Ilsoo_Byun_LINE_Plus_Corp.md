---
title: "Exploring RocksDB in RGW- How We Manage Tombstones - Sungjoon Koh & Ilsoo Byun, LINE Plus Corp"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "RocksDB"
  - "RGW"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：Ceph与RocksDB性能优化讨论

**会议时间**：下午  
**会议主题**：Ceph存储系统中RocksDB性能优化与Tombstone问题处理  
**会议主持**：Ishion（负责公司私有云存储服务）  
**参会人员**：Ceph研发团队成员、存储服务相关人员



#### 1. **会议背景**
   - **公司存储服务**：LINE Plus Corp 提供多种存储服务，包括块存储、文件存储和对象存储，主要基于Ceph分布式存储系统，管理超过30个集群，物理存储容量超过700PB。
   - **Ceph应用场景**：Ceph不仅用于Line Messenger服务，还支持其他多种业务需求。

#### 2. **RocksDB在Ceph中的角色**
   - **RocksDB的作用**：RocksDB作为Ceph内部元数据存储，负责存储RADOS对象的OMAP（Object Map）数据。OMAP通过RocksDB的键值对形式存储，支持点查询和范围查询。
   - **OMAP与RocksDB的关系**：OMAP存储在RocksDB中，每个对象的OMAP键由对象ID和OMAP名称组成。范围查询操作在RGW（RADOS Gateway）中频繁使用，尤其是在列出桶内对象时。

#### 3. **Tombstone问题及其影响**
   - **Tombstone的产生**：当对象被删除时，RocksDB中的对应记录会被标记为删除（Tombstone），但不会立即物理删除。随着时间推移，这些Tombstone会积累在RocksDB的SST文件中，导致性能下降。
   - **Tombstone的影响**：在执行范围查询时，RocksDB需要跳过大量Tombstone，导致CPU使用率飙升，OSD（对象存储守护进程）响应变慢，甚至完全无响应。
   - **实际案例**：某次范围查询操作导致OSD CPU使用率达到100%，持续4小时，严重影响集群性能。

#### 4. **Tombstone问题的深入分析**
   - **RocksDB迭代机制**：RocksDB在执行范围查询时，会遍历SST文件中的键值对。当遇到Tombstone时，RocksDB需要跳过这些删除标记，导致大量I/O和字符串解析操作，消耗大量CPU资源。
   - **Tombstone的分布**：分析发现，大量Tombstone集中在少数几个前缀（Prefix）下，尤其是与桶索引相关的键值对。
   - **Tombstone的来源**：Tombstone不仅来自对象删除操作，还可能来自多部分上传（Multipart Upload）操作，这些操作会在RocksDB中生成大量临时键值对，最终被删除。

#### 5. **解决方案与优化措施**
   - **手动压缩（Compaction）**：通过手动触发RocksDB的压缩操作，可以有效清理Tombstone，恢复OSD性能。但手动压缩无法持续解决问题，且可能影响写入性能。
   - **基于Skip Count的自动化压缩**：通过监控RocksDB的Skip Count（跳过Tombstone的次数），可以预测哪些OSD可能面临性能问题，并自动触发压缩操作。
   - **前缀范围压缩（Prefix-based Compaction）**：针对Tombstone集中在特定前缀下的问题，提出在桶索引级别进行压缩，而不是在整个OSD级别进行压缩。

#### 6. **后续行动计划**
   - **优化压缩策略**：开发基于前缀的压缩功能，减少压缩操作的范围，避免对系统资源的过度消耗。
   - **社区讨论与贡献**：将前缀范围压缩方案提交到Ceph社区，与社区开发者共同讨论和优化。
   - **持续监控与改进**：继续监控RocksDB的性能指标，特别是Tombstone的分布和Skip Count，确保系统稳定运行。