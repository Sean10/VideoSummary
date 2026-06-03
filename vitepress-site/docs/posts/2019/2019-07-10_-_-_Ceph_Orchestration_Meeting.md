---
title: "2019-07-10 :: Ceph Orchestration Meeting"
date: 2019-07-10
updated: 2019-07-12
tags:
  - "Ceph"
  - "编排"
  - "分布式存储"
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年7月10日

**参会人员**： Kiefer、Sebastian、Yuri、Nathan、Greg、Zach、Liam、Casey、Abby 等

**会议主题**： Ceph 项目开发讨论，包括 Orchestrator 功能改进、测试策略等。

**关键细节**：

* **Orchestrator 功能改进**：
    * Kiefer 正在开发一个新的 Orchestrator 功能，用于列出主机并展示主机库存。他计划在 Orchestrator 主页上添加一个新页面，列出所有主机，并展示每个主机的详细信息。
    * Christopher 正在研究如何将驱动器组添加到 Safe Dashboard 中，以提供更复杂的存储配置选项。
* **测试策略**：
    * Nathan 提出了测试 Rook Orchestrator 的问题，并讨论了如何将测试集成到现有的测试套件中。
    * Greg 提出了在测试中使用不同部署工具的抽象层，以便与现有的测试套件兼容。
    * David 讨论了 Nautilus 释放的情况，包括发现的问题和修复措施。
* **其他议题**：
    * Liam 讨论了将驱动器组添加到 Safe Dashboard 的合理性。
    * Sebastian 提出了使用 SSH Orchestrator 替代 Def Deploy 的可能性。

**决定的事项**：

* Kiefer 将继续开发新的 Orchestrator 功能，并将其集成到 Ceph 项目中。
* Christopher 将研究如何将驱动器组添加到 Safe Dashboard 中。
* Nathan 和 Greg 将继续研究测试 Rook Orchestrator 的策略。
* David 将继续修复 Nautilus 释放中发现的问题。

**后续行动计划**：

* Kiefer 将提供新的 Orchestrator 功能的截图和详细信息。
* Christopher 将提供关于将驱动器组添加到 Safe Dashboard 的更多细节。
* Nathan 和 Greg 将继续与社区讨论测试 Rook Orchestrator 的策略。
* David 将继续修复 Nautilus 释放中发现的问题。

**关键词**：

- Orchestrator
- Dashboard
- Inventory
- Hosts
- Testing
- Rook
- Def Deploy
- SSH
- Nautilus
- Ceph