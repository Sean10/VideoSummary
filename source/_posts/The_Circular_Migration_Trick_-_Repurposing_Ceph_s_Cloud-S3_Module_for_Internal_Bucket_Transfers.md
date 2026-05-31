---
title: The Circular Migration Trick- Repurposing Cephs Cloud-S3 Module for Internal Bucket Transfers
date: 2025-06-24
updated: 2025-06-24
tags:
- Ceph
- 存储优化
categories: 
- "视频总结"
subtitle: The_Circular_Migration_Trick_-_Repurposing_Ceph_s_Cloud-S3_Module_for_Internal_Bucket_Transfers
---

本次会议的主题是探讨如何利用Ceph的Cloud-S3模块实现内部存储桶的数据传输，以优化数据管理和降低存储成本。以下是会议的关键要点：

### 会议概述

OxyLabs的DevOps工程师Lus分享了该公司在Ceph存储架构中的实践经验，包括如何使用RADOS Gateway (RGW)、CephFS和RBD，以及通过Cloud S3模块实现数据生命周期管理。

### 关键议题与讨论

#### OxyLabs的Ceph使用背景

- **核心架构**：基于Kubernetes的裸金属集群用于Web Scraping，存储层采用Ceph，包括RBD、CephFS和RGW。
- **集群规模**：4PB存储，380+ OSD（3x副本），1B+对象，混合使用HDD和SSD，成本优化至80%利用率。

#### 数据暴露问题

- **挑战**：客户依赖CephFS，但新数据平台基于RGW，导致数据需在CephFS和RGW间重复存储（6x~12x副本），每月额外消耗200TB存储。
- **临时方案**：引入SFTP-Go工具实现数据迁移和生命周期管理，但面临S3挂载性能问题。

#### 利用Ceph Cloud S3模块的解决方案

- **核心思路**：通过配置RGW自身为Cloud端点，实现内部存储桶间数据传输。
- **实施步骤**：创建压缩池或纠删码池，配置存储类，设置生命周期策略，自动迁移旧数据至归档存储桶。
- **优势**：基于Ceph原生功能，无需第三方工具，支持数据分层和减少冗余存储。

#### 注意事项与优化

- **关键配置调整**：调整RGW生命周期处理性能，处理时间窗口，多部分上传清理。
- **安全提示**：归档存储桶的密钥信息会暴露在zonegroup placement list中，需谨慎管理。

### 决议与行动计划

1. 推广Cloud S3模块的“自引用”模式，补充案例至社区文档。
2. 优化生命周期策略，结合标签和存储类实现更细粒度数据管理。
3. 探索私有云方案，整合虚拟化技术和Ceph多集群协作。

通过本次会议，展示了Ceph在混合存储场景下的灵活性和可扩展性，并通过Cloud S3模块的创造性使用，解决了数据冗余和成本问题。未来将进一步提升生命周期策略的性能和安全性，并推动社区文档的完善。