---
title: "2019-07-08 :: Ceph Orchestration Meeting"
date: 2019-07-11
updated: 2019-07-12
tags:
  - "Ceph"
  - "分布式存储"
  - "编排"
  - "Rook"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2023年11月某日

**参会人员**： Christopher、Joyce、Eric、其他人

**会议主题**： Ceph 编排器会议

**会议内容**：

**1. Christopher自我介绍**

- Christopher来自Souza公司，曾在SUSE公司工作六年，现加入Theft Team，主要负责容器、Rook以及编排工作。

**2. Group Drive Group项目介绍**

- 该项目旨在实现驱动器组的概念，允许将多个驱动器分组管理，例如按型号或大小分组。
- 目前项目实现较为基础，需要进一步完善。
- 讨论了将驱动器组逻辑移至Volume层，以实现更灵活的管理。

**3. Python Common包**

- 该包是一个Python库，用于在Ceph组件之间共享代码，是SSH orchestrator等项目的关键组件。
- 讨论了检查代码的必要性。

**4. Dashboard集成**

- Keva正在开发将orchestrator界面集成到dashboard的功能，初始将从主机开始。

**5. Rook项目进展**

- 讨论了Rook项目的进展，包括PVS on cloud platforms spec、监控器放置、cmd reporter等。

**6. 其他议题**

- 讨论了将manager rook模块集成到monitoring storage classes in prometheus的可能性。
- 计划在周三讨论该议题。

**行动计划**：

- Christopher将完善Group Drive Group项目。
- Keva继续开发Dashboard集成功能。
- 讨论Rook项目的具体进展。
- 在周三讨论将manager rook模块集成到monitoring storage classes in prometheus的可能性。

**备注**：

- 会议中提到了一些计算机科学/ceph相关领域的英文关键词，如orchestrator、volume、drive group、monitor、Rook、prometheus等。