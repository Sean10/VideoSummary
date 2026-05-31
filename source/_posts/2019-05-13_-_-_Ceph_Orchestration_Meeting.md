---
categories:
- 视频总结
date: 2019-05-28
subtitle: 2019-05-13_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 编排
- Kubernetes
- Rook
title: "'2019-05-13:: Ceph Orchestration Meeting'"
updated: 2019-05-28
---



### 会议纪要

**会议时间**： 2023年5月13日

**会议主题**： Orchestrator 团队会议

**会议内容**：

1. **独立模式（Standalone Mode）讨论**
   - Rook 4.5 版本中曾包含独立模式，但后续废弃，转而使用 Kubernetes 进行编排。
   - 独立模式面临挑战，需要重新实现 Kubernetes 的许多功能，例如集群管理、资源分配等。
   - Orchestrator 团队已具备中央组件，简化了部分功能。

2. **Rook 1.0.1 版本发布**
   - 由于主要版本发布后出现了一些升级问题，例如主机网络与 0.9 版本升级不兼容，将推出 1.0.1 版本进行修复。
   - 期望在第二天发布此补丁版本，并计划后续推出 1.0.2 版本。

3. **Cephalocon 会议地点**
   - Cephalocon 会议地点（Red Hat Office）目前不可用，因为会议室被董事会会议占用。
   - Mike Perez 正在寻找替代地点，包括酒店或附近的场地。
   - 需要进一步跟进并确认会议地点。

4. **Kubecon 会议**
   - Rook 将在 Kubecon 上进行演讲和展示，需要志愿者协助在展位上为用户解答问题。

5. **其他事项**
   - 有关会议地点的具体信息，将通过电子邮件进一步确认。
   - 下次会议将在下周举行。

**行动计划**：

- Travis 负责发布 Rook 1.0.1 版本。
- Mike Perez 负责寻找 Cephalocon 会议地点。
- 团队成员准备 Kubecon 会议的相关工作。

[改进说明]

- 在总结中增加了对独立模式（Standalone Mode）的详细讨论，包括其废弃的原因和面临的挑战。
- 对 Rook 1.0.1 版本的发布计划进行了补充，明确了修复升级问题的具体内容。
- 对 Cephalocon 会议地点的问题进行了详细说明，包括当前面临的困难和解决方案。
- 增加了 Kubecon 会议的相关信息，包括 Rook 的参与方式和团队成员的职责。