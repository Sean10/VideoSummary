---
title: "2020-05-28 :: Ceph Tech Talk - What's New In Octopus"
date: 2020-05-28
updated: 2020-05-29
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期**: 2023年5月28日
- **主题**: Seth Tech Talk - Ceph Octopus 版本更新及新功能介绍
- **主讲人**: Josh Durgan (Red Hat) 和 Lance Kramer (Sousa)
- **参会人员**: Ceph 社区成员及技术爱好者

#### 讨论内容
1. **Ceph Octopus 版本更新**
   - **发布时间**: Octopus 版本于2020年3月发布，下一个版本 Pacific 预计于2021年3月发布。
   - **支持与升级**: 支持从 Luminous、Mimic 和 Nautilus 升级到 Octopus，但 Luminous 需要先升级到 Mimic 或 Nautilus。

2. **主要改进与新功能**
   - **可操作性提升**:
     - **Orchestrator API**: 实现统一部署和管理，支持容器化部署，简化集群管理。
     - **Ceph Dashboard**: 界面布局调整，增强用户管理功能，改进 OSD 部署流程。
   - **性能与稳定性**:
     - **BlueStore 优化**: 改进预取和压缩机制，优化内存使用和TRIM行为。
     - **健康监控**: 新增网络监控健康警报，改进内部健康警报处理。
   - **多站点支持**:
     - **RBD 镜像**: 基于快照的灾难恢复，减少 I/O 开销。
     - **Garbage Collection**: 使用简单块用于垃圾回收，减少 RocksDB 瓶颈。
   - **生态系统集成**:
     - **Ceph CSI 和 Rook**: 增强与 Kubernetes 的集成，支持更多存储模式和操作。

3. **用户提问与回答**
   - **驱动器故障处理**: Ceph Orchestrator 目前不直接处理驱动器故障，但有计划自动化这一过程。
   - **SMR 磁盘支持**: 目前不支持，但 Pacific 版本将引入新的后端存储以支持 SMR 磁盘。

#### 后续行动计划
- **持续优化**: 继续改进 Ceph Orchestrator 的功能，特别是在自动化驱动器故障处理方面。
- **新功能开发**: 开发支持 SMR 磁盘的新后端存储，预计在 Pacific 版本中实现。
- **社区参与**: 鼓励用户参与 Ceph 的 telemetry 和 crash reporting，以帮助改进产品。

#### 结论
本次会议详细介绍了 Ceph Octopus 版本的新功能和改进，强调了其在可操作性、性能和多站点支持方面的进步。同时，讨论了未来版本的发展方向和社区参与的重要性。