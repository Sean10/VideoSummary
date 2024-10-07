---
title: "Ceph Crimson/SeaStor OSD 2020-07-29"
date: 2020-07-29
updated: 2020-07-30
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **Messenger 相关问题**：上周在测试基于病理的结构测试时发现了一些问题，今天再次运行测试时发现心跳（heartbeat）部分出现了崩溃，目前正在调查中。
- **FBA Ping 审查**：正在审查 Sam 的 FBA Ping，但仍在努力解决中。
- **恢复和回填测试**：正在寻找真正的测试失败案例，特别是与恢复和回填（recovery and backfill）相关的测试，以及阈值测试。
- **经典扫描（Classic Scrubbing）**：已经更新了文档，并开始运行独立的测试套件。
- **内部节点插入和分裂实现**：上周完成了内部节点插入和分裂的实现，目前正在跟踪树层次结构在递归分裂过程中的变化。
- **单元测试**：正在为回填（backfill）准备单元测试，包括一个基本随机的测试案例，用于生成大量副本间的差异，确保这些差异被消除。
- **Tommy 的状态**：Tommy 正在根据 Sam 的评论更新 PR，并处理网络问题。
- **Crimson 中断机制**：上周在开发 Crimson 中断机制，但因其他工作进展不大，本周将继续开发。

#### 讨论的主要议题
- **测试和调试**：讨论了各种测试的进展和遇到的问题，包括心跳崩溃、恢复和回填测试、经典扫描等。
- **代码审查和实现**：审查了 FBA Ping 和内部节点插入和分裂的实现，以及树层次结构的跟踪。
- **单元测试和基础设施**：讨论了为回填准备的单元测试和相关的基础设施。

#### 决定的事项
- **继续调查心跳崩溃问题**：需要进一步调查和重现心跳崩溃的问题。
- **继续审查和更新 FBA Ping**：需要继续审查并根据 Sam 的评论更新 FBA Ping。
- **继续开发 Crimson 中断机制**：本周将继续开发 Crimson 中断机制。

#### 后续的行动计划
- **调查心跳崩溃**：继续调查并重现心跳崩溃的问题。
- **审查和更新 FBA Ping**：继续审查并根据 Sam 的评论更新 FBA Ping。
- **开发 Crimson 中断机制**：本周将继续开发 Crimson 中断机制。
- **准备单元测试**：继续为回填准备单元测试，并确保测试案例能够生成并消除副本间的差异。

#### 其他
- **网络问题**：Tommy 遇到了网络问题，会议中等待其重新加入。
- **链接分享**：分享了一个链接，用于解释单元测试的基础设施和实现细节。

### 结束语
感谢所有参与者的贡献和讨论，期待后续的进展和成果。