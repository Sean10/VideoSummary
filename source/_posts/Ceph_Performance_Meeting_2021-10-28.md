---
title: "Ceph Performance Meeting 2021-10-28"
date: 2021-11-03
updated: 2021-11-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **新拉取请求（Pull Requests, PRs）**:
  - 设置最小分配大小为某些设备的最佳I/O大小。讨论了新设备类型可能需要大于4K的分配单元，但不一定必须，涉及性能与空间浪费的权衡。
  - Igor提出的改进共享Blob fsck过程，使其更节省RAM。从12GB减少到0.5GB，显著改善了内存使用。
  - Mark Cogan关于db store的工作，增加了配置选项以设置单线程性能调优参数。

- **更新PRs**:
  - 优化PG peering延迟的PR，Neha将重新定位到master分支。
  - MDS移除子树映射从日志的PR，设计文档已提供，仍在进行中。
  - 优化对象内存分配使用池的旧PR，Gabriel增加了讨论，涉及内存分配的优化。

#### 讨论的主要议题
- **内存分配优化**:
  - 讨论了如何通过预分配区域或重用对象来优化内存分配，减少动态分配的需求。
  - 提到了使用栈分配、固定大小缓冲区（如4K或8K）以及slab分配器的可能性。
  - 讨论了是否应该重新设计协议，以支持更高效的内存使用和减少碎片化。

- **性能瓶颈**:
  - 提到了messenger组件可能存在的性能瓶颈，建议从这里开始优化。
  - 讨论了如何通过减少动态分配和优化数据结构来改善性能。

#### 决定的事项
- 需要进一步调查和优化内存分配策略，特别是对于高频使用的对象和请求。
- 选择一个简单的组件（如messenger）开始优化，以验证假设和方法的有效性。

#### 后续行动计划
- 继续讨论和优化内存分配策略，特别是对于编码/解码过程。
- 开始对messenger组件进行优化，以减少其性能开销。
- 收集更多的性能数据和墙钟分析，以帮助确定进一步优化的领域。

会议强调了通过小步骤开始，逐步改进系统性能的重要性，并鼓励团队成员继续探索和实验这些优化策略。