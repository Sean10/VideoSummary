---
title: "Ceph Developer Summit Quincy: Rook"
date: 2021-04-09
updated: 2021-04-10
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph Rook Manager 模块评估与讨论

#### 参会人员：Rick、Travis、Miguel、Seth 等

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 主要议题：
1. **Rook Manager 模块评估**：讨论了 Rook Manager 模块的功能和应用场景，特别是与 Ceph 管理模块的集成。
2. **OSD 部署和管理**：探讨了 OSD（Object Storage Daemon）的部署和管理方式，包括使用 PVC（Persistent Volume Claim）和直接设备管理。
3. **维护任务自动化**：讨论了如何自动化执行维护任务，如 fs check、reshard 等，以及如何在 Rook 和 Ceph 环境中实现。
4. **服务部署和 HA 配置**：讨论了如何在 Kubernetes 和 Ceph 环境中部署服务（如 RGW、NFS）以及配置高可用性（HA）。
5. **Bucket 配置和 Cozy 集成**：探讨了 Bucket 配置的自动化以及与 Cozy 的集成，特别是在 Kubernetes 1.21 中的新功能。

#### 决定事项：
1. **OSD 部署策略**：决定继续探讨使用 PVC 和直接设备管理两种方式部署 OSD，并评估其在 Rook 和 Ceph 环境中的适用性。
2. **维护任务自动化**：计划开发一个通用的维护任务框架，允许用户定义和执行特定的维护任务，如 fs check 和 reshard。
3. **服务部署和 HA 配置**：决定将 HA 配置作为一个可选的独立模块，允许用户根据需要部署和配置高可用性服务。
4. **Bucket 配置和 Cozy 集成**：计划在 Rook 中优先集成 Cozy，并探讨如何在 Ceph 环境中实现类似的 Bucket 配置自动化。

#### 后续行动计划：
1. **技术测试开发**：开发一个技术测试，部署 Kubernetes 并使用 Rook 管理 Ceph 集群，以确保 Rook Manager 模块的功能和稳定性。
2. **维护任务框架开发**：开始开发一个通用的维护任务框架，允许用户定义和执行特定的维护任务。
3. **HA 配置模块开发**：开发一个独立的 HA 配置模块，允许用户根据需要部署和配置高可用性服务。
4. **Cozy 集成**：在 Rook 中优先集成 Cozy，并探讨如何在 Ceph 环境中实现类似的 Bucket 配置自动化。

#### 备注：
- 会议中提到的具体技术细节和实现方式将在后续的技术文档和开发过程中进一步明确。
- 所有决定的事项和后续行动计划将由相关团队负责执行，并定期进行进度更新和评估。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。