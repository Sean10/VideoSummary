---
title: Ceph as a NAS Platform Are We Architecturally Ready?
date: 2026-04-02
updated: 2026-04-03
tags:
- NFS
- 分布式存储
categories: 
- 视频总结
subtitle: Ceph_as_a_NAS_Platform_Are_We_Architecturally_Ready
---

## 概述

本次演讲由 SE（Ceph）开发工程师 Mohit 主讲，探讨 Ceph 是否已在架构层面准备好作为一个完整的 NAS 平台，而不仅仅是 NFS/Samba 等文件服务的存储后端。

## 背景与问题的提出

在典型的企业部署场景中，Ceph 被用于构建大规模可扩展的存储平台。对象存储（object storage）和块存储（block storage）工作负载可以直接运行在 Ceph 之上，充分获得 Ceph 架构和运维层面的全部优势。

然而，当涉及文件工作负载，尤其是 NFS 和 Samba 时，传统的架构模型往有所不同：NFS 和 Samba 协议服务运行在 Ceph 外部，独立部署，Ceph 仅作为存储后端提供支撑。这种方式技术上可行，但在架构层面引发了一个值得深思的问题：

**Ceph 是否已经在架构上准备好成为一个真正的 NAS 平台，而不仅仅是这些服务的存储后端？**

## 为什么这个问题重要

尽管对象存储和云原生架构快速发展，NFS 和 Samba 依然是大量文件工作负载的主要访问协议，广泛应用于：

- 虚拟机存储
- 共享应用存储
- 数据分析流水线
- 用户主目录
- 工程代码仓库

企业级 NAS 解决方案的需求不仅仅是文件系统本身，还包括：

1. **协议与多样化客户端生态**：稳定的 NFS/Samba 协议服务，与 Active Directory、LDAP 等身份服务的清晰集成，以及对锁语义和多样客户端的支持。
2. **高可用性与数据保护**：透明故障转移、强数据完整性，snapshots、备份和数据保护是基线要求，而非可选项。
3. **性能与 scalability**：文件环境中 metadata 性能往比原始吞吐量更关键，平台需在小负载、混合负载和高负载下均无瓶颈。
4. **运维成熟度**：简单的运维自动化和生命周期管理。

## Ceph 文件系统的演进历程

### 阶段一：cephfs 文件系统

cephfs 已在生产环境稳定运行多年，基于高度可扩展的 MDS 架构，提供强一致性（consistency）和 scalability，是 NFS/Samba 服务的强大存储后端。

### 阶段二：NFS 原生协议支持（Reef 版本）

Reef 版本引入了 NFS 编排（orchestration）的原生支持，实现了：

- NFS 服务的容器化（containerization）部署
- 通过 cephadm CLI 进行端到端生命周期自动化（滚动升级、功能启用等）
- 将协议服务作为 Ceph 内部的一等公民组件进行管理

这是一次重要的架构转变：从外部独立运行的协议服务，转变为 Ceph 原生管理的组件。

### 阶段三：SMB 原生协议支持（Squid 版本）

Squid 版本进一步引入了 SMB 编排的原生支持：

- SMB 服务的完整生命周期管理
- 与 Active Directory 的清晰集成
- 通过 cephadm 统一管理

## 架构全景：从用户层到 RADOS

当前 Ceph NAS 平台的完整架构栈（从上至下）：

| 层次 | 说明 |
|------|------|
| 用户层 | Linux 客户端通过 NFS 挂载，Windows 客户端通过 SMB 访问 |
| 协议层 | NFS 和 Samba 服务容器化部署于 Ceph 内部，由 cephadm CLI 统一管理 |
| Ceph 编排层 | cephadm 提供全功能自动化，配置存储于 RADOS 层而非节点本地，保证集群范围内的配置一致性 |
| cephfs 层 | 生产稳定的分布式文件系统，为 NFS/Samba 提供强大存储后端 |
| RADOS 层 | 提供所有架构和运维层面的底层保障 |

关键架构优势：配置不再存储于节点级别，而是存储于 RADOS 层，确保了配置的一致性（consistency）和集群范围内的感知能力。

## 部署演示：启用 NFS 与 Samba 服务

演讲者现场演示了完整的部署流程，分为以下阶段：

### 第一阶段：cephfs 就绪

1. 启动 MDS 服务
2. 创建 cephfs 卷（主卷，供 NFS/Samba 工作负载使用）
3. 分别为 NFS 和 Samba 创建独立的 subvolume group 和 subvolume，实现独立管理

### 第二阶段：协议配置

1. 启用 NFS 和 Samba 的 MGR 模块
2. 创建 NFS 集群（指定节点标签，自动完成服务部署）
3. 创建 SMB 集群（支持用户模式和 Active Directory 模式，演示使用用户模式）

### 第三阶段：Export 与 Share创建

1. 获取 NFS subvolume 路径，创建 NFS export（支持按需创建多个 export）
2. 创建 SMB share

### 第四阶段：客户端挂载验证

- Linux 客户端：使用标准 mount 命令挂载 NFS export
- Windows 客户端：通过网络驱动器映射 SMB share（使用创建集群时设置的用户名密码）

演示成功验证了 NFS 和 SMB 服务均可正常使用。

## 生命周期管理的三种方式

Ceph 提供三种方式对 NFS/Samba 服务进行完整的生命周期管理：

1. **Dashboard（图形界面）**：通过 Ceph Dashboard 以少量点击完成 NFS/Samba 的配置与管理
2. **命令式 CLI**：使用 cephadm CLI 命令集进行精细化操作
3. **声明式 Spec 文件**：将所有配置写入一个 spec 文件，一次性激活 NFS/Samba 服务，适合大规模环境

## 架构就绪性结论

从 cephfs 的演进历程和现场演示可以得出明确结论：

**Ceph 现在已经在架构上准备好支持 NFS 和 Samba 协议，不再是外部支持，而是内部原生支持，并具备完整的自动化管理能力。**

Ceph 已满足企业级 NAS 平台的核心要求：
- high availability
- 简单的运维自动化
- 数据保护（snapshots 等）
- 完整的生命周期管理

## 核心要点总结

1. **Ceph 已成为完整集成的 NAS 解决方案**：从部署、升级、配置到下线，所有典型 NAS 平台支持的操作均可通过 Ceph 原生完成。

2. **历史遗留问题得到解决**：过去企业部署 Ceph 时，对象和块工作负载可获得 Ceph 的全部架构优势，而文件工作负载（NFS/Samba）只能在外部独立运行。现在，通过 Ceph 对这些服务的原生支持，文件工作负载同样可以获得 Ceph 完整的架构和运维优势。

3. **架构转变的意义**：Ceph 不再仅仅是文件服务的存储后端，而是一个真正统一的、原生管理 NFS 和 Samba 的 NAS 平台。
