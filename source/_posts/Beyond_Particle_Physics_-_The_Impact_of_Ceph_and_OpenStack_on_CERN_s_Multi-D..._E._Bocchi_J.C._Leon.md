---
title: Beyond Particle Physics- The Impact of Ceph and OpenStack on CERNs Multi-D... E. Bocchi & J.C. Leon
date: 2025-01-26
updated: 2025-01-26
tags:
- Ceph
- OpenStack
- CERN
categories: 
- "视频总结"
subtitle: Beyond_Particle_Physics_-_The_Impact_of_Ceph_and_OpenStack_on_CERN_s_Multi-D..._E._Bocchi_J.C._Leon
---
### 会议纪要：CERN的Ceph与OpenStack集成及新数据中心介绍

CERN的SEF集群操作员Enrico和云技术负责人Jose在Auditorium C介绍了CERN的Ceph与OpenStack集成、新数据中心的构建与运营，以及跨数据中心的更高可用性存储方案。

### 会议要点：

1. **CERN的背景与任务**：
   - CERN是全球最大的粒子物理实验室，运营大型强子对撞机（LHC），需要处理、存储和分发海量数据。
   - CERN的存储需求包括数据重建、存储、分发，以及备份和归档。

2. **Ceph在CERN的应用**：
   - CERN使用Ceph作为后端存储，支持HPC集群、对象存储、块存储和文件系统存储。
   - Ceph用于存储加速器监控数据、探测器数据、备份和归档，以及全球数据分发。

3. **OpenStack与Ceph的集成**：
   - CERN的云基础设施基于OpenStack，提供计算、存储和网络资源。
   - OpenStack与Ceph集成，支持虚拟机镜像、块存储（RBD）、文件共享（Manila）和对象存储（RADOS Gateway）。

4. **新数据中心的构建**：
   - 新数据中心的构建是为了应对LHC高亮度扩展带来的计算需求增长。
   - 新数据中心设计时考虑了物理基础设施的优化，采用了高密度的JBOD、NVMe存储和AMD单插槽处理器。

5. **跨数据中心的更高可用性存储方案**：
   - CERN正在探索RGW Multisite和Ceph Stretch Clusters，以实现跨数据中心的存储一致性。
   - CERN正在招聘一名初级存储工程师，专注于AIML工作负载。

6. **Ceph元数据管理的挑战**：
   - CERN的Ceph集群管理了数十亿个iNode，元数据管理面临挑战。
   - CERN正在探索Emerald pinning和多文件系统（Multi FS）解决方案。

7. **用户界面与可用性改进**：
   - CERN正在简化用户界面，隐藏底层基础设施复杂性。

8. **未来工作与社区合作**：
   - CERN希望通过社区合作，分享经验并学习其他Ceph运营商的最佳实践。

### 决定事项与后续行动计划：

1. 继续优化Ceph元数据管理。
2. 完善RGW Multisite和Stretch Clusters的监控与故障切换机制。
3. 简化用户界面。
4. 招聘新成员，专注于AIML工作负载。

### 会议总结：

本次会议详细介绍了CERN如何利用Ceph和OpenStack构建大规模存储解决方案，并讨论了新数据中心的构建和跨数据中心存储的一致性等问题。会议还强调了Ceph元数据管理的挑战以及CERN在用户界面和可用性改进方面的努力。