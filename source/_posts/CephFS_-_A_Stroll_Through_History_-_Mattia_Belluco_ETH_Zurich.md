---
title: CephFS- A Stroll Through History - Mattia Belluco, ETH Zurich
date: 2025-01-23
updated: 2025-01-24
tags: 
- Ceph
- CephFS
- 分布式存储
- CRUSH算法
- 高可用性
categories: 
- "视频总结"
subtitle: CephFS_-_A_Stroll_Through_History_-_Mattia_Belluco_ETH_Zurich
---

### 会议纪要：Ceph文件系统（CephFS）的历史与演进

**会议时间**：2023年  
**主讲人**：ETH Zurich的Mattia Belluco  
**主题**：CephFS的历史、演进及未来考虑



#### 1. **会议背景**
Belluco介绍了他在ETH Zurich的工作背景，该校是瑞士的领先科技大学，专注于科学计算领域的研究和应用。他所在的部门致力于科学计算服务，拥有40多位专家。



#### 2. **CephFS简介**
- **CephFS**是Ceph分布式存储系统中的文件系统层，提供POSIX兼容的文件系统服务。
- 基于RADOS和CRUSH算法，依赖MDS（元数据服务器）进行元数据管理。
- 自2010年起，CephFS支持Linux内核驱动，与Linux生态系统深度集成。



#### 3. **CephFS的演进**
Belluco详细介绍了CephFS在不同版本中的演进，包括：
- **Jewel（2016）**：CephFS被宣布为稳定版本，但缺乏快照支持。
- **Luminous（2017）**：引入BlueStore，支持Erasure Coded数据池，降低成本。
- **Mimic（2018）**：支持多MDS快照，MDS稳定性改进。
- **Nautilus（2019）**：CephFS数据扫描工具，支持灾难恢复，CephFS Shell。
- **Octopus（2020）**：改进Ceph Dashboard，支持CephFS管理，Emerald Pinning。
- **Pacific（2021）**：多文件系统支持，CephFS Mirror。
- **Quincy（2022）**：修复CephFS Manila漏洞，支持文件系统重命名。
- **Reef（2023）**：Crimson存储引擎，自动元数据负载均衡器。
- **Squid（最新版本）**：元数据树的写入锁定，支持文件系统名称交换。



#### 4. **CephFS集群设计与管理**
- 集群设计需根据生产负载优化硬件和配置。
- Ceph ADM简化了测试和基准测试流程，支持多MDS快速部署。
- Ceph社区提供了多种工具，如Ceph Deploy、Ceph Helm、Rook等，用于简化集群的部署和管理。



#### 5. **CephFS的日常运维与灾难恢复**
- CephFS具备自动重平衡、定期数据一致性检查等功能，简化了运维。
- CephFS提供了多种工具，如CephFS Journal Tool和CephFS Data Scan，用于恢复丢失的元数据和对象。



#### 6. **未来考虑**
- 进一步优化元数据处理和负载均衡。
- 增加自动化功能，如在线scrub调度机制。
- 优化容器化与云原生集成。



#### 7. **Q&A环节**
会议结束时，Belluco提供了联系方式，并欢迎与会者提出问题。

**总结**：本次会议详细回顾了CephFS从稳定版本发布以来的演进历程，重点介绍了各个版本的关键功能和改进。CephFS作为Ceph生态系统中的重要组成部分，未来将继续在性能优化、自动化管理和云原生集成方面进行深入发展。