---
title: "2019-09-16 :: Ceph Orchestration Meeting"
date: 2019-09-16
updated: 2019-09-21
tags:
  - "Ceph"
  - "编排"
  - "Rook"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
会议纪要

**会议时间**： 2019年9月某日

**参会人员**： 会议记录者，Jonathan，DePaul，Percept，Travie，Adam Freeman等

**会议主题**： 讨论Ceph项目的进展、问题及后续行动计划。

**关键细节**：

* **Estate Orchestrator**： Jonathan提到已将Estate Orchestrator的更改推送到分支，以便继续工作。他还提到了PR 3026，该PR使得completions可组合，这对于桌面和仪表板非常重要。
* **Nautilus模块阻塞**： 由于存在tracker issue 41737，Nautilus模块遇到了阻塞。该问题与两个端口有关，需要在master分支中修复。
* **Rook 1.0**： Rook 1.0已发布，目前看起来一切顺利。计划在本周进行补丁发布。
* **Orchestrator问题**： 讨论了关于polls的持续时间和reclaim策略的问题。决定更改默认策略以保留规则，并考虑在self中启用secure pull deletion标志。
* **Rook CI**： 讨论了Rook CI的未来。短期内，将更新旧的Jenkins实例。长期目标是实现自动化，类似于F CIA。会议决定将讨论移至上游，并与Greg和Adam Freeman一起讨论。

**决定事项**：

* 将修复Nautilus模块的tracker issue 41737。
* 计划进行Rook 1.0的补丁发布。
* 更改默认策略以保留规则，并考虑在self中启用secure pull deletion标志。
* 将Rook CI讨论移至上游，并与Greg和Adam Freeman一起讨论。

**后续行动计划**：

* Jonathan将继续工作在Estate Orchestrator上。
* 讨论修复Nautilus模块的tracker issue 41737。
* 计划进行Rook 1.0的补丁发布。
* 讨论并实施新的reclaim策略。
* 讨论并实施Rook CI的自动化。
* 将讨论移至上游，并与Greg和Adam Freeman一起讨论。

**关键词**：

- Estate Orchestrator
- PR 3026
- Nautilus
- Rook 1.0
- Orchestrator
- polls
- reclaim策略
- Rook CI