---
title: "  2019-06-03:: Ceph Orchestration Meeting  "
date: 2019-06-07
updated: 2019-06-07
tags:
- Ceph
- 分布式存储
- Rook
categories:
- "视频总结"
subtitle: 2019-06-03_-_-_Ceph_Orchestration_Meeting
---



会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 多位Ceph研发人员，包括负责分布式存储Ceph的研发人员、视频会议字幕翻译及总结人员等。

**会议主题**： 讨论Ceph Orchestrator和Nautilus的进展，以及相关技术挑战和解决方案。

**会议内容**：

**1. Dashboard讨论**

* 讨论将Dashboard集成到Orchestrator中的可行性，并确定Dashboard将主要关注集成到Orchestrator中。
* 讨论Dashboard的可用性和远程拨入的可能性，并计划在两周后的面对面会议中进一步讨论。

**2. Nautilus进展**

* 讨论Nautilus中Nathan提交的多个pull request。
* 讨论回滚Orchestrator更改的哲学，以及将更改回滚到master分支的目标。
* 讨论将Rook模块作为Rook模块添加到Octopus的可行性。

**3. AP状态管理**

* 讨论AP状态管理中的疑问和困难，特别是在没有使用AKS的情况下。
* 讨论默认配置和手动配置的问题。
* 讨论Rook允许创建多个对象存储区域，但没有允许它们跨集群工作的限制。
* 讨论最终用户对配置参数的控制。

**4. Orchestrator API一致性**

* 讨论不同Orchestrator之间API不一致性问题。
* 讨论是否应该将update操作仅实现于Rook和Kubernetes中，并使用其他Orchestrator的其他操作。
* 讨论如何使Dashboard能够处理不同Orchestrator的API调用。

**5. Rook API更新**

* 讨论Rook API的更新，包括添加新的命令和参数。
* 讨论如何处理Rook API中的update和remove操作。

**6. Rook治理**

* 讨论Jared提交的Rook治理更新PR，包括添加更多具有push访问权限的“所有者”。
* 讨论创建一个委员会来监督Rook项目。

**7. 41.1版本发布**

* 讨论即将发布的41.1版本，包括外部集群管理、OSD备份等功能。
* 讨论更新roadmap文档和功能板。

**后续行动计划**：

* 继续讨论Dashboard和Orchestrator的集成。
* 完成Nautilus的pull request。
* 解决AP状态管理中的问题。
* 实现Orchestrator API一致性。
* 更新Rook API。
* 完成Rook治理更新。
* 发布41.1版本。

**备注**：

* 会议中提到了多个英文关键词，例如“Orchestrator”、“Nautilus”、“Rook”、“AP”、“Kubernetes”等，这些关键词在会议讨论中占有重要地位。
* 会议纪要中尽量保留了原文的表述，以确保准确传达会议内容。