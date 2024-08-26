---
title: "CephFS Code Walkthrough: rstats"
date: 2021-08-20
updated: 2021-08-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要：CephFS R-Stats 实现讨论

#### 会议主题
本次会议主要讨论了Ceph文件系统（CephFS）中递归树统计（R-Stats）的实现细节及其在文件系统检查（File System Check）中的应用。

#### 主要议题
1. **R-Stats 的定义与用途**：
   - R-Stats 用于在递归前向 scrubbing 过程中检查统计数据的一致性。
   - 提出了使用快照 R-Stats 来检测两个文件系统树（即两个快照之间）的变更。

2. **Scrubbing 的启动方式**：
   - Scrubbing 可以针对常规目录或内部 MDS 目录启动，但不使用递归标志时，仅验证目录的一层。

3. **R-Stats 的维护与结构**：
   - R-Stats 的维护依赖于 `frag_info` 和 `nest_info` 结构，这些结构嵌入在 `fnode_t` 容器结构中。
   - `frag_info` 维护单个目录片段的信息，而 `nest_info` 累积深度超过一层的条目统计。

4. **R-Stats 的传播**：
   - R-Stats 从叶节点（目录或文件）向文件系统根节点传播。
   - 传播是懒惰的，不即时发生，涉及路径上所有 `fnode` 对象的更新。

5. **挑战与问题**：
   - R-Stats 的传播涉及大量锁定，是一个复杂的并发问题。
   - 快照目录的 RC 时间更新存在 bug，正在调查中。

#### 决定事项
- 确认了 R-Stats 在文件系统检查和快照变更检测中的重要性。
- 需要进一步解决 R-Stats 传播中的锁定和并发问题。

#### 后续行动计划
- 继续调查和修复快照目录的 RC 时间更新 bug。
- 研究优化 R-Stats 传播过程中的锁定机制，以提高效率和可靠性。

#### 会议结束
会议结束时，主持人询问是否有其他问题，并表示如果没有更多问题将结束分享。