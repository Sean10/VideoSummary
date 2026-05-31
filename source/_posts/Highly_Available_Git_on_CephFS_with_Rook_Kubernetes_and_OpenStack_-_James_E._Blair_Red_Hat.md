---
categories:
- 视频总结
date: 2019-05-24
subtitle: Highly_Available_Git_on_CephFS_with_Rook_Kubernetes_and_OpenStack_-_James_E._Blair_Red_Hat
tags:
- CephFS
- Rook
- Kubernetes
- OpenStack
- 高可用性
title: "Highly Available Git on CephFS with Rook, Kubernetes, and OpenStack - James E. Blair, Red Hat"
updated: 2019-05-24
---



在本次会议中，James E. Blair（Red Hat CTO办公室）和OpenStack社区代表共同探讨了如何使用CephFS、Rook、Kubernetes和OpenStack实现高度可用的Git服务。

**会议内容**：

* **Open Dev项目介绍**： Open Dev是一个为OpenStack开发的软件开发环境，使用免费软件进行开发和系统运营。Git T服务是Open Dev项目的重要组成部分。
* **Git T服务优化**： 目前Git T服务运行在独立的虚拟机上，难以扩展和规模扩展。计划将Git T服务迁移到CephFS，使用Percona XtraDB Cluster作为数据库，Elasticsearch集群用于全文索引，并利用Kubernetes进行管理。
* **自动化部署**： 使用Kubernetes on OpenStack项目进行自动化部署，利用Rook进行Ceph集群的部署和管理。
* **Ceph集群部署**： 使用Rook的Flex存储驱动程序在Kubernetes上部署Ceph集群，使用Rook的Operator简化Ceph集群的部署和管理，并使用BlueStore存储驱动程序提高性能。
* **其他部署**： 使用Percona XtraDB Cluster作为数据库，并使用Kubernetes部署Git T应用程序。
* **行动计划**： 完成Git T服务的迁移和优化，继续使用Rook和Ceph进行部署和管理，探索使用Ceph作为Percona XtraDB Cluster的后端存储。

**改进后的总结**：

在本次会议中，James E. Blair介绍了如何利用CephFS、Rook、Kubernetes和OpenStack实现高度可用的Git服务。他详细讨论了如何使用这些技术优化Git T服务，实现自动化部署和Ceph集群的部署管理。此外，他还介绍了如何使用BlueStore存储驱动程序提高性能，并探索使用Ceph作为Percona XtraDB Cluster的后端存储。

**相关关键词**：

- CephFS
- Rook
- Kubernetes
- OpenStack
- 高可用性
- Git服务
- 自动化部署
- Ceph集群
- BlueStore
- Percona XtraDB Cluster