---
title: "Ceph Performance Meeting 2021-12-09"
date: 2021-12-13
updated: 2021-12-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题
1. **Pull Requests (PRs) 更新**
   - **新PR**: 启动新的MD日志段，以处理高负载情况下的预期段大小问题。Patrick正在审查，需要进行单元测试。
   - **关闭的PRs**:
     - Sage实现了管理器中Gill处理的优化，主要是线程争用问题。
     - 设置最小Alex大小为最佳I/O大小，针对具有较大分配大小的设备。
   - **更新PRs**:
     - TTL缓存实现，是旧PR的新版本。
     - Whip主平衡器PR，Josh Solomon提交，Laura审查，需要对文档进行一些调整。
     - 引入基于Huge Page的读缓冲区，Igor审查，需要更多信息。
     - BlueFS的细粒度锁定，Adam提交，正在进行新测试。
     - 使Bob fsck更少内存消耗，Igor提交，正在进行更多讨论和更新。
     - OSD优化PG移除，Igor提交，正在进行更多讨论和更新。

2. **Bob fsck内存使用问题**
   - Adam提出了对改进后的Bob fsck过程的担忧，担心在某些特定情况下可能会有共享blob错误通过fsck过程。
   - Igor解释了改进后的Bob fsck不会提供错误检测，但在某些情况下可能会标记一些仍然良好的blob为潜在损坏。
   - 讨论了在容器环境中运行OSD的内存限制问题，以及如何避免内存不足导致的崩溃。

3. **TC Malloc线程缓存大小配置**
   - Adam提议将TC Malloc线程缓存大小设置为可配置选项，而不是使用环境变量。
   - 讨论了在perf glue代码中直接处理TC Malloc线程缓存大小的可能性，以及如何在全局配置中处理。

4. **内存分配器讨论**
   - 讨论了不同内存分配器（如TC Malloc和Libsy Malloc）的内存碎片问题。
   - 提到了Crimson中使用C-star分配器的情况，以及可能的改进方向。

#### 决定事项
- 需要进一步讨论和测试Bob fsck的内存使用问题，特别是在容器环境中的应用。
- 确定将TC Malloc线程缓存大小设置为可配置选项，并考虑在perf glue代码中处理。
- 讨论了在Crimson中使用TC Malloc替代Libsy Malloc的可能性，特别是在BlueStore和AlienStore中。

#### 后续行动计划
- 继续审查和测试相关PRs。
- 进一步讨论和优化Bob fsck的内存使用问题。
- 确定TC Malloc线程缓存大小的配置方式，并在perf glue代码中实现。
- 探索在Crimson中使用TC Malloc替代Libsy Malloc的可能性。

#### 下次会议议题
- 讨论OSD同步写性能问题。
- 讨论更广泛的自性能优化话题。

**会议结束时间**: 会议持续了一个小时，所有议题均已讨论完毕。下次会议将继续讨论未尽事宜。