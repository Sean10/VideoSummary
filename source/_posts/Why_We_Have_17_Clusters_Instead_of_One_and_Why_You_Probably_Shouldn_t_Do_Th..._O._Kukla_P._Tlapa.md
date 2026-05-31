---
title: Why We Have 17 Clusters Instead of One (and Why You Probably Shouldn’t Do Th... O. Kukla & P. Tlapa
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 分布式存储
- 可扩展性
- 高可用性
- 云计算
categories: 
- "视频总结"
subtitle: Why_We_Have_17_Clusters_Instead_of_One_and_Why_You_Probably_Shouldn_t_Do_Th..._O._Kukla_P._Tlapa
---

### Ceph分布式存储解决方案会议纪要

#### 1. 会议基本信息
- **演讲人**：Peter和Andre（CDN77存储团队）
- **主题**：大规模Ceph集群的设计、实现与挑战
- **背景**：CDN77为全球约10亿用户提供内容分发服务，存储需求庞大且复杂。

#### 2. 核心问题与需求
- **数据规模**：约20PB混合数据，对象数量达数百亿且持续增长。
- **技术挑战**：高性能读取、高可用性、扩展性、数据分布性。
- **需求**：作为CDN源站存储，需支持高吞吐读取，单OSD故障不影响整体集群，未来发展需支持2-3个数量级的增长，数据映射到S3桶。

#### 3. 解决方案设计
- **架构概述**：17个独立Ceph集群（14个HDD集群 + 3个SSD集群），双数据中心部署，避免单点故障。
- **负载均衡**：基于Nginx的定制一致性哈希模块（chash）分发请求，使用客户端对象的CRC32哈希前4字符作为桶名，确保均匀分布。
- **硬件配置**：单节点配置包括24核EPYC CPU、512GB RAM、30×24TB HDD + 6×NVMe。

#### 4. 实施中的挑战与经验
- **管理复杂度**：多集群操作、Bucket列表操作困难。
- **扩展性问题**：新增集群需手动迁移数据。
- **生产环境问题**：Bucket命名长度初始设置错误，版本统计差异，Lifecycle策略导致性能峰值。

#### 5. 关键结论与未来计划
- **方案评估**：满足高性能、可扩展S3端点的需求，但管理开销大，扩展需谨慎。
- **改进方向**：探索自动化工具、研究更高效的EC方案。

#### 6. Q&A环节摘要
- **灾备恢复**：依赖双数据中心设计，故障时切换至备用集群，数据从对端DC同步。
- **扩展建议**：优先扩容现有集群。

#### 7. 后续行动
- **短期**：优化监控指标。
- **长期**：评估Ceph Multicite以简化多集群管理。

**备注**：如需进一步技术细节，请联系演讲团队。

**关键词保留**：Ceph, CRUSH, RADOS, RGW, OSD, RocksDB, EC (Erasure Coding), replication, bucket, S3 endpoint.