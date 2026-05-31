---
categories:
- 视频总结
date: 2021-08-20
subtitle: CephFS_Code_Walkthrough_-_rstats
tags:
- CephFS
- 分布式存储
title: "'CephFS Code Walkthrough: rstats'"
updated: 2021-08-21
---




CephFS R-Stats 实现讨论会议纪要

### 会议主题
本次会议深入探讨了 Ceph 文件系统（CephFS）中递归树统计（R-Stats）的实现细节，以及其在文件系统检查中的应用。

### 主要议题
1. **R-Stats 的定义与用途**：
   - R-Stats 用于递归前向 scrubbing 过程中检查统计数据的一致性。
   - 提出使用快照 R-Stats 来检测两个文件系统树之间的变更。

2. **Scrubbing 的启动方式**：
   - Scrubbing 可针对常规目录或内部 MDS 目录启动，若无递归标志，仅验证目录的一层。

3. **R-Stats 的维护与结构**：
   - 维护依赖于 `frag_info` 和 `nest_info` 结构，这些结构嵌入在 `fnode_t` 容器结构中。
   - `frag_info` 维护单个目录片段的信息，`nest_info` 累积深度超过一层的条目统计。

4. **R-Stats 的传播**：
   - 从叶节点向文件系统根节点传播，涉及路径上所有 `fnode` 对象的更新。
   - 传播是懒惰的，不即时发生。

5. **挑战与问题**：
   - R-Stats 传播涉及大量锁定，是并发问题。
   - 快照目录的 RC 时间更新存在 bug。

### 决定事项
- 承认 R-Stats 在文件系统检查和快照变更检测中的重要性。
- 需要解决 R-Stats 传播中的锁定和并发问题。

### 后续行动计划
- 调查和修复快照目录的 RC 时间更新 bug。
- 研究优化 R-Stats 传播过程中的锁定机制，提高效率和可靠性。

### 会议总结
会议强调了 R-Stats 在 CephFS 中的关键作用，并明确了后续改进的方向。