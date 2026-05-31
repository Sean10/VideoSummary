---
title: " Rook Deployed Scalable NFS Clusters Exporting CephFS - Patrick Donnelly & Jeff Layton, Red Hat, Inc. "
date: 2019-05-24
updated: 2019-05-24
tags:
- Ceph
- 分布式存储
- Rook
- Kubernetes
- NFS
categories:
- "视频总结"
subtitle: Rook_Deployed_Scalable_NFS_Clusters_Exporting_CephFS_-_Patrick_Donnelly_Jeff_Layton_Red_Hat_Inc.
---

### 会议纪要

**会议时间**： 2023年11月（具体日期未知）

**参会人员**： Patrick Donnelly（Red Hat SEPA fest 技术负责人）、Jeff Lee（Red Hat 存储专家）

**会议主题**： 深入探讨使用 Rook 在 Kubernetes 上部署可扩展的 NFS 集群，并导出 CephFS，介绍 SEPA fest 技术及其与 Ceph 的集成。

**会议内容**：

**1. SEPA fest 简介**

* SEPA fest 是基于对象存储的 POSIX 分布式文件系统。
* 特点：MDS 集群化，元数据存储分离，客户端直接访问数据，无需与 MDS 交互，客户端和 MDS 共同维护元数据分布式缓存，确保数据一致性。
* 主要客户端：step views 和内核客户端。

**2. 使用 Rook 部署 NFS 集群**

* 部署原因：部分客户端可能无法直接处理 Ceph，需要通过网关进行转换，网络安全，例如防火墙保护集群数据，OpenStack Manila 等场景需要隔离数据访问。
* 目标：实现主动/主动部署，线性扩展集群，容器化部署，避免使用第三方软件，使用 NFS Ganesha 作为 NFS 服务器。

**3. Ceph 集群与 NFS 网关**

* Ceph 集群支持主动/被动网关，但性能扩展性较差。
* 希望实现主动/主动部署，实现线性扩展。

**4. NFS 协议**

* NFS 协议历史悠久，早期版本无状态，需要附加协议处理。
* NFSv4 和 NFSv4.1 引入会话层和会话恢复机制。
* Ganesha 使用 Ratius 存储跟踪客户端状态，支持会话恢复。

**5. 复杂性挑战**

* 网络文件系统（NFS）和集群文件系统（SEPA fest）都使用基于租约的会话机制，需要处理会话超时和租约过期等问题。
* 需要处理 IP 迁移，当 NFS Ganesha 服务器失败时，需要将 IP 地址迁移到新的服务器。

**6. 解决方案**

* 使用 Rook 和 Kubernetes 进行部署和管理。
* 利用 Kubernetes 的 IP 迁移功能。
* 通过 Rook 部署和管理 Ganesha 容器。
* 使用 Dashboard API 配置 Ganesha 导出。

**7. 未来工作**

* 支持基于子卷的主动/主动部署。
* 支持迁移到新的 IP 地址。
* 优化子卷的 grace 期。
* 与 SMB 集成。

**行动计划**：

* 完善 Rook 和 Kubernetes 的集成。
* 优化 Ganesha 的配置和管理。
* 在 Ceph 中实现基于子卷的主动/主动部署。
* 研究与 SMB 的集成方案。

**总结**：

本次会议讨论了使用 Rook 和 Kubernetes 在 Ceph 上部署可扩展的 NFS 集群，并导出 CephFS 的方案。会议分析了相关技术和挑战，明确了未来工作方向和行动计划，为 Ceph 的存储功能扩展提供了新的思路。