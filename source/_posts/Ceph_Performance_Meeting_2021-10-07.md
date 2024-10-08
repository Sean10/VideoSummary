---
title: "Ceph Performance Meeting 2021-10-07"
date: 2021-10-08
updated: 2021-10-09
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是关于Ceph存储系统的开发进展和讨论。会议开始于两周前的一个拉取请求（Pull Request, PR）总结之后，主要回顾了过去两周内的PR动态和相关讨论。

#### 主要议题和讨论内容
1. **新PR和更新**
   - 一个关于优先级现金（priority cash）的缓存年龄分箱（cash age binning）的更新实现。
   - 讨论了LRU缓存实现中的问题，特别是在roxdb块缓存中的一些更改可能导致轻微的损坏。

2. **已关闭的PR**
   - 一个关于Prometheus管理器模块的PR，提供了禁用缓存的能力。
   - 一个旧版本的缓存分箱PR被关闭，取而代之的是一个更新和重新基于的版本。

3. **更新中的PR**
   - Neha对管理器TTL缓存实现的审查，以及基于她反馈的进一步讨论和更新。
   - Igor的PG移除优化PR，之前有测试失败的记录，目前仍在计划中。
   - 关于头解码优化的讨论，由Iliad进行审查，有一些额外的讨论和更新。
   - 一个关于从日志中移除子树映射的大PR，由于其复杂性，需要更多的设计文档和讨论。

4. **其他讨论**
   - 关于内存使用问题的讨论，特别是在某些节点上发现的大量不可释放内存，可能与创建和销毁大量cgroup时的上游内核bug有关。
   - 缓存年龄分箱的性能影响讨论，虽然有时会有性能提升，但也可能会有损失，主要原因是高估了缓存omap数据的重要性。

#### 决定事项
- 继续审查和测试缓存年龄分箱的实现，特别是解决可能导致SIG故障的问题。
- 对于大且复杂的PR，如子树映射移除，需要更多的设计文档和讨论，可能考虑分解为更小的部分。

#### 后续行动计划
- 继续进行缓存年龄分箱的测试和审查，确保其稳定性和性能。
- 对于大PR，如子树映射移除，准备设计文档和进一步的讨论，可能分解为更小的可管理部分。
- 关注内存使用问题，特别是与cgroup相关的内核bug，可能需要进一步的研究和解决。

#### 其他
- 讨论了关于缓存行为的未来改进和可能的优化方向，包括考虑预分配内存和更静态的内存管理策略。
- 探讨了应用程序提供缓存提示的可能性，以优化缓存行为。

#### 会议结束
会议在讨论了所有议题后结束，没有其他待讨论的事项。会议参与者将在后续的会议中继续跟进这些议题。