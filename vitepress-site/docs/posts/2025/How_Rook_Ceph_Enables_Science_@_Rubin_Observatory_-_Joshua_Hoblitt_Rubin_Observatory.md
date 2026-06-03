---
title: "How Rook/Ceph Enables Science @ Rubin Observatory - Joshua Hoblitt, Rubin Observatory"
date: 2025-11-19
updated: 2025-11-19
tags:
  - "Ceph"
  - "Rook"
  - "Kubernetes"
  - "分布式存储"
categories:
  - "会议纪要"
  - "技术文章"
outline: deep
---
Rubin Observatory 的首席 DevOps 工程师 Joshua Hoblitt 在其演讲中详细介绍了 Rubin Observatory 如何利用 Ceph 和 Rook 技术实现其存储架构的统一，以支持天文数据的高吞吐和高可用需求。

**Rubin Observatory 背景**

Rubin Observatory 是一个由 NSF/DOE 联合资助的项目，位于智利 Cerro Pachón 山上。其科学目标包括研究暗物质、太阳系测绘、银河系映射等。每晚观测会产生约 20TB 的原始数据，并包含数百万次瞬变事件警报。

**数据流架构**

Rubin Observatory 的数据流包括从 LSST Camera 捕获数据，经过数据采集系统（DAC）处理，再通过诊断集群节点转换为 FITS 格式并压缩。数据主要通过 RGW 写入 USDF，同时也复制到本地的 RGW 实例，并通过 Kafka 通知导入 OODS。

**选择 Ceph 和 Rook 的原因**

Rubin Observatory 选择 Ceph 和 Rook 的原因包括：

- **统一存储**：Ceph 支持 RBD、CephFS 和 RGW，提供了一种统一的存储解决方案。
- **高可用性**：Ceph 通过 CRUSH 算法和 PG 实现分布式冗余，确保数据的高可用性。
- **扩展性**：Ceph 可轻松扩展至千级 OSD，满足 Rubin Observatory 的存储需求。
- **Kubernetes 集成**：Rook 提供了 Kubernetes 原生集成，简化了部署和管理过程。
- **GitOps 支持**：Rook 与 GitOps 实践相结合，实现配置版本化和自动化。

**当前存储集群状态**

Rubin Observatory 的存储集群已启用 OSD 加密，并计划部署 1,100+ OSD。集群使用了 RBD、RGW 和 CephFS，同时通过 NFS-Ganesha 提供文件共享功能。

**挑战与优化**

Rubin Observatory 面临的主要挑战包括性能敏感型负载和 NFS 性能。对于性能敏感型负载，如 InfluxDB 和 Kafka，目前仍使用本地 NVMe 存储。NFS 性能问题可能与使用的 NFS-Ganesha 版本有关。

**GitOps 工作流**

Rubin Observatory 使用 GitOps 模型进行存储管理。所有 Rook 资源都存储在公共 Git 仓库中，通过 PR 提交到 `dev` 分支，并自动同步到生产环境。

**后续行动计划**

Rubin Observatory 计划继续优化性能，测试新的 NFS-Ganesha 版本，并评估使用 CephFS 直挂替代 NFS 的可能性。此外，Rubin Observatory 还计划扩展其存储集群，并考虑组织 Rook 研讨会，帮助团队更好地使用 Kubernetes。

**关键词保留**：Ceph, Rook, OSD, CRUSH, RGW, CephFS, RBD, EC, GitOps, Kubernetes