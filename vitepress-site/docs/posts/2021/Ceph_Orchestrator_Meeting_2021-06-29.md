---
title: "Ceph Orchestrator Meeting 2021-06-29"
date: 2021-08-24
updated: 2021-08-25
tags:
  - "Ceph"
  - "分布式存储"
  - "Rook"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议主题：OSD自我编排器中的实现

#### 参会人员：
- 会议主持人：[主持人姓名]
- 主要发言人：Chris（OCS操作界面负责人）
- 其他参会人员：[其他参会人员姓名]

#### 讨论议题：
1. **PV（持久卷）的获取与管理**
   - 如何将PV引入自我编排器（Self Orchestrator）。
   - 如何使用自我编排器在PV上创建OSD。

2. **现有问题与挑战**
   - 处理本地持久卷（Local Persistent Volumes）与PV及声明（Claims）的关系。
   - 在OCS（OpenShift Container Storage）中实现上述流程的挑战。

3. **技术细节与演示**
   - Chris演示了如何在OpenShift UI中通过OCS操作符创建PV和OSD。
   - 讨论了LSO（Local Storage Operator）的使用，包括节点磁盘的发现和存储类的创建。

4. **后续行动计划**
   - 探索LSO作为库的嵌入方式，而非独立操作符。
   - 讨论Rook支持多种存储类的PV，而不仅是LSO。
   - 考虑通过CSI（Container Storage Interface）标准管理本地硬件。

#### 决定事项：
- 明确Rook与LSO的集成方式，以及如何处理不同存储类的PV。
- 计划编写更具体的技术提案，以便深入讨论和实施。

#### 后续行动：
- 继续实验和研究LSO的嵌入方式。
- 编写具体的技术提案，以待下次会议讨论。
- 考虑CSI标准在本地存储管理中的应用。

#### 备注：
- 会议中提到了OpenEBS作为另一个本地存储管理选项，但目前主要关注LSO。
- 讨论了在Rook中实现对本地硬件的发现和管理，以及如何与现有的存储操作符（如LSO）协同工作。

#### 会议总结：
本次会议重点讨论了在Ceph Orchestrator中使用自我编排器创建OSD的过程，并探讨了与OpenShift和Rook集成的技术细节。会议还确定了后续行动计划，包括深入研究LSO的集成方式，编写技术提案，并考虑CSI标准在本地存储管理中的应用。