---
title: CephFS Basics & Whats New. Greg Farnum from IBM
date: 2025-05-08
updated: 2025-05-09
tags:
- CephFS
- Ceph
categories: 
- "视频总结"
subtitle: CephFS_Basics_What_s_New._Greg_Farnum_from_IBM
---

### 会议纪要：CephFS 基础知识与新发展

**会议时间**：未知  
**会议主持人**：Greg Farnum，IBM Ceph 工程经理  
**参会人员**：Ceph 开发团队及相关人员



#### 会议主题：

1. **CephFS 架构回顾**
2. **CephFS 新特性介绍**
3. **未来开发计划**



#### 主要讨论内容：

1. **CephFS 架构概述**：
   - CephFS 是基于 RADOS 构建的分布式文件系统，包括 Monitor（MON）、Manager（MGR）、Object Storage Daemon（OSD）、Metadata Server（MDS）等组件。
   - MDS 负责维护文件系统层次结构，但不直接存储数据，所有数据存储在 RADOS 集群中。
   - MDS 通过内存缓存处理大量元数据请求，支持动态负载均衡和缓存迁移。

2. **CephFS 数据路径**：
   - CephFS 客户端通过 MDS 获取文件元数据，然后直接与 OSD 交互进行数据读写。
   - MDS 不参与实际数据传输，仅负责元数据管理和权限控制。

3. **CephFS 新特性**：
   - **快照功能**：类似 RBD 的快照功能，支持目录级别的快照，创建速度快、成本低。
   - **递归统计**：支持递归统计目录下的文件数量和总大小。
   - **客户端加密**：数据在发送到 Ceph 服务器之前进行加密。
   - **Samba VFS 插件优化**：通过代理守护进程提升 Samba 与 CephFS 的集成性能。

4. **即将推出的功能**：
   - **快照一致性改进**：支持多客户端并发操作下的快照一致性。
   - **硬链接支持改进**：解决硬链接在快照中的问题。
   - **元数据日志优化**：提升元数据操作的性能。

5. **CephFS Manager 和 Volumes 插件改进**：
   - 优化 Ceph Manager 插件的隔离性。
   - Volumes 插件支持更方便的快照、克隆和子卷管理。

6. **未来开发计划**：
   - **快速克隆**：实现元数据级别的文件克隆。
   - **QoS 支持**：引入用户空间客户端的 QoS 支持。
   - **CephFS Mirror 改进**：优化灾难恢复效率。



#### 决定事项：

1. 继续优化 CephFS 的快照一致性和硬链接支持。
2. 推进元数据日志的进一步优化。
3. 加速 CephFS 与 Samba、NFS 等协议的集成优化。



#### 后续行动计划：

1. 开发团队：推进快照一致性改进、硬链接支持优化和元数据日志优化。
2. 集成团队：与 Kubernetes、OpenStack 等平台团队合作，测试和验证 Volumes 插件的改进。
3. 性能测试团队：针对 CephFS 的新特性进行性能测试，确保新功能在大规模环境下的稳定性。



#### 会议总结：

本次会议重点介绍了 CephFS 的新特性和未来开发计划，包括快照、递归统计、客户端加密等功能，以及性能优化和集成改进。开发团队将继续优化 CephFS 的性能和功能，以提升用户体验和大规模部署的稳定性。