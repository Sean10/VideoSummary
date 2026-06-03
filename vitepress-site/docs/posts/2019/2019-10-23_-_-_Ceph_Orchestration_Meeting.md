---
title: "2019-10-23 :: Ceph Orchestration Meeting"
date: 2019-10-31
updated: 2019-11-01
tags:
  - "Ceph"
  - "编排"
  - "分布式存储"
  - "CephFS"
  - "存储集群"
categories:
  - "视频总结"
outline: deep
---
本次会议纪要主要讨论了Ceph分布式存储项目的进展、Orchestrator组件的介绍以及后续工作安排。以下是会议的关键细节和讨论议题：

1. **Drive Group预览功能**：
   - Keifa提到需要对Drive Group的预览功能进行审查，以便在合并后可以在仪表板上实现预览功能。
   - 该功能目前尚未实际使用，因此需要有人进行单元测试和实际应用。

2. **Inventory清理**：
   - II提到Inventory部分需要清理，但目前仍等待最新成员的审查。

3. **Orchestrator组件**：
   - Joshua Hesketh刚加入存储团队，正在学习Orchestrator组件。
   - Orchestrator组件是一个接口，用于创建、部署、移除服务以及获取运行在集群上的服务列表。
   - Orchestrator组件旨在构建Ceph和部署工具（如Rook、DeepSea等）之间的桥梁。
   - Orchestrator接口允许不同的orchestrator后端实现该接口，从而在Surf仪表板上实现部署任务。

4. **Dashboard支持**：
   - 如果部署工具没有Orchestrator模块，则无法通过内置的Chef仪表板进行部署。
   - Keifer正在为Dashboard添加新功能，例如从GUI部署新的OS Days，这需要通过Orchestrator模块实现。

5. **后续行动计划**：
   - Keifa将创建一个PR来读取pison comical，以开始更多choline模块的工作。
   - Joshua Hesketh将学习Orchestrator组件的文档，并了解其工作原理。
   - II将继续清理Inventory部分。

会议决定事项包括：
- Keifa将审查Drive Group预览功能，并在合并后进行测试。
- Joshua Hesketh将学习Orchestrator组件的文档，并了解其工作原理。
- II将继续清理Inventory部分。

后续行动计划包括：
- Keifa创建PR并开始更多choline模块的工作。
- Joshua Hesketh学习Orchestrator组件的文档。
- II清理Inventory部分。