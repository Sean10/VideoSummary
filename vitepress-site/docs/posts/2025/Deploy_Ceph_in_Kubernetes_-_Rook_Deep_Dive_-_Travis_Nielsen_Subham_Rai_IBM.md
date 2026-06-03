---
title: "Deploy Ceph in Kubernetes- Rook Deep Dive - Travis Nielsen & Subham Rai, IBM"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "Kubernetes"
  - "Rook"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：Rook 项目深入探讨

**会议时间**：Cephon 会议最后一天  
**主讲人**：Travis Nielsen (Rook 创始人及维护者) 和 Subham Rai (Rook 维护者)  
**会议主题**：Rook 项目的介绍、架构、功能、社区更新及未来规划



#### 1. **Rook 项目简介**
Rook 是一个 Kubernetes 操作符，用于自动化 Ceph 存储的部署、配置、升级和维护。它允许 Kubernetes 应用程序通过标准存储类、持久卷和持久卷声明来访问 Ceph 存储。

#### 2. **Rook 与 Ceph 的关系**
Rook 作为 Ceph 的 Kubernetes 集成层，负责管理 Ceph 集群的部署和维护。Ceph 提供分布式存储的核心功能，包括块存储、文件系统存储和对象存储。

#### 3. **Rook 架构**
Rook 采用三层架构：
   1. **Rook 操作符**：负责 Ceph 的部署和管理。
   2. **CSI 驱动程序**：为应用程序提供存储卷的挂载和管理。
   3. **Ceph 数据层**：Ceph 的核心组件（如 OSD、MON、MDS）运行在 Kubernetes Pod 中。

#### 4. **Rook 的功能**
   - **存储部署模式**：支持超融合模式、专用存储节点和外部 Ceph 集群。
   - **CSI 驱动程序功能**：支持拓扑感知、快照、克隆、卷扩展等功能。
   - **对象存储**：通过 Bucket 声明创建 S3 兼容的存储桶。

#### 5. **Rook 的维护与升级**
   - Rook 支持滚动升级，确保在升级过程中 Ceph 集群的高可用性。
   - 通过 Pod 干扰预算，Rook 确保在维护或升级时，Ceph 集群不会因节点故障而中断。
   - 灾难恢复场景中，Rook 确保数据的安全性。

#### 6. **Rook 工具**
   - **Rook Toolbox**：提供 Ceph 命令行工具，用于集群故障排查和日常维护。
   - **Rook Kubernetes 插件**：基于 Kubernetes 的扩展 CLI 工具，简化了集群状态检查和维护操作。
   - **Mon 仲裁恢复**：支持在 Mon 节点故障时恢复仲裁状态。

#### 7. **Rook 社区与更新**
   - Rook 是一个 CNCF 毕业项目，社区活跃，拥有超过 500 名贡献者和 3.4 亿次下载量。
   - 每 4 个月发布一次小版本更新，支持最新的 Ceph 版本。
   - Rook 1.15 和 1.16 版本新增了多项功能，包括 OSD 加密、Object Store CAS 存储、Ceph CSI 操作符等。

#### 8. **未来规划**
   - 将 Ceph 打造成 Kubernetes 的最佳存储平台，支持所有 Ceph 和 Kubernetes 的功能。
   - 重点发展领域：对象存储和数据复制。

#### 9. **问答环节**
   - 答疑环节涉及了外部 Ceph 集群的使用、性能对比、安全模型等问题。



**总结**：Rook 作为 Ceph 的 Kubernetes 集成层，提供了强大的存储管理能力，支持多种存储类型和部署模式。通过自动化和工具支持，Rook 简化了 Ceph 在 Kubernetes 环境中的使用和维护。未来，Rook 将继续扩展功能，提升与 Ceph 和 Kubernetes 的集成度，目标是成为云原生环境中的最佳存储解决方案。