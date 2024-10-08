---
title: "Ceph Orchestrator Meeting 2021-08-03"
date: 2021-08-23
updated: 2021-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Orchestrator 周会

#### 日期：[具体日期]

#### 参会人员：[参会人员名单]

#### 主要议题：

1. **容器镜像问题**
   - **问题描述**：在使用 OSPCI 部署 CephFS 时，团队原本使用 Ceph-Ansible 角色而非 Cephdm，通过创建 systemd 单元并使用 Ceph 提供的容器启动。在尝试将 Pacific beats 升级到 16.5 版本时，发现 CephFS 无法启动，原因可能是新容器构建基于 demon 基础镜像而非 daemon 镜像，导致 Dockerfile 缺少入口点，start nfs bash 脚本未被调用。
   - **讨论内容**：
     - 新容器格式缺少入口点，不适用于 CephFS。
     - 建议继续使用传统的 daemon 镜像，直到新的 Manila 部分准备就绪。
     - 讨论了旧容器镜像的维护问题，以及是否需要继续维护旧容器镜像。
   - **决定事项**：
     - 继续使用 6.0.4 版本的容器镜像作为稳定版本。
     - 确认 6.0.x 系列将继续维护，直到完全迁移到 Cepheidm。
   - **后续行动计划**：
     - 确认旧容器镜像的维护计划，确保新版本的稳定性和兼容性。
     - 继续监控新容器格式的测试和部署情况，确保无重大问题。

2. **LSO 项目更新**
   - **项目概述**：讨论了 LSO 项目的需求文档，计划与 LSO 团队合作，明确项目需求和目标。
   - **讨论内容**：
     - 创建了一个 Google Doc 用于团队间的协作和讨论。
     - 确认项目需要支持 vanilla Kubernetes，成为一个上游项目。
   - **决定事项**：
     - 继续完善需求文档，计划在本周五与 LSO 团队进行详细讨论。
   - **后续行动计划**：
     - 确保文档准备就绪，与 LSO 团队进行深入讨论。
     - 跟进与 Duncan 的会议，讨论产品管理相关事宜。

#### 其他议题：

- **Crimson 和 Encephalidium 容器镜像**：讨论了 Crimson 的容器镜像问题，确认其为不同的构建，带有特定的构建标志。

#### 会议总结：

会议主要解决了容器镜像的兼容性问题，并讨论了 LSO 项目的进展。团队将继续监控和维护相关容器镜像，确保项目的稳定推进。同时，LSO 项目的需求文档将继续完善，以便与团队进行更深入的讨论和合作。

#### 下一步行动：

- 确认并维护旧容器镜像的稳定性和兼容性。
- 完善 LSO 项目需求文档，准备与 LSO 团队进行详细讨论。
- 跟进与 Duncan 的会议，讨论产品管理相关事宜。

#### 会议结束：

感谢所有参与者的积极参与，期待下周的会议。

---

**注意**：以上内容根据会议记录整理，保留了关键的英文术语和技术细节，以确保信息的准确性和专业性。