---
title: "Remote Replication in MicroCeph- RBD and Beyond - Utkarsh Bhatt, Canonical"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "RBD"
  - "Ceph"
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：MicroCeph 中 RBD 远程复制功能的介绍与应用

**会议时间**：2023年12月4日  
**主讲人**：Utkarsh Bhatt (Canonical)  
**主题**：MicroCeph 中的 RBD 镜像远程复制功能



#### 1. **会议背景与目标**
   - **MicroCeph** 是 Canonical 推出的一款简化版 Ceph 管理工具，旨在降低 Ceph 的使用门槛。
   - 会议重点介绍了 RBD 镜像远程复制功能，并计划将此功能扩展到 RADOS Gateway (RGW) 和 CephFS。

#### 2. **主讲人介绍**
   - Utkarsh Bhatt 曾在华为从事专有存储产品开发，后转向开源存储领域，尤其专注于 Ceph。
   - 他对 Ceph 的复杂性和强大功能有深入理解，并致力于通过 MicroCeph 简化 Ceph 的使用。

#### 3. **MicroCeph 的哲学**
   - MicroCeph 的目标是让 Ceph 的使用变得更加简单，即使是对存储或 Ceph 不熟悉的用户也能轻松上手。
   - MicroCeph 并非 Ceph 的简化版或缩减版，而是通过智能化的默认配置和简化的操作流程，帮助用户快速部署和管理 Ceph 集群。
   - 用户可以根据需求进行高级配置，MicroCeph 提供了灵活的参数调整选项。

#### 4. **RBD 远程复制功能**
   - **RBD 镜像远程复制**是 Ceph 中用于将 RBD 镜像数据复制到另一个 Ceph 集群的功能，适用于备份、灾难恢复等场景。
   - 复制模式支持 **池模式**（整个池的镜像复制）和 **镜像模式**（单个镜像的复制），并且可以选择 **日志模式** 或 **快照模式**。
   - 复制的实现依赖于 **RBD 镜像守护进程 (RBD Mirror Daemon)**，用户可以在启用复制前后启动该守护进程。

#### 5. **演示环节**
   - 演示了如何配置集群间的远程连接、启用复制、查看复制状态、故障切换、恢复同步以及禁用复制等操作。
   - 使用两个虚拟集群进行演示，展示了 RBD 镜像远程复制功能的实际操作。

#### 6. **未来计划**
   - 计划扩展远程复制功能到 **RADOS Gateway (RGW)** 和 **CephFS**。
   - 将引入 **多站点复制**，MicroCeph 将自动处理 Realms 和 Zone Groups 的配置。
   - 未来还将增加 **监控和告警** 功能，帮助运维人员实时了解复制状态。

#### 7. **Q&A 环节**
   - 回答了关于 MicroCeph 目标用户的问题，指出 MicroCeph 旨在让非专业用户也能轻松使用 Ceph。

#### 8. **后续行动计划**
   - 继续开发和完善 MicroCeph 的远程复制功能，尤其是扩展到 RGW 和 CephFS。
   - 增加监控和告警功能，提升运维人员的操作体验。
   - 欢迎社区贡献者参与 MicroCeph 的开发，Canonical 提供了开源项目支持。