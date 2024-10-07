---
title: "Ceph Performance Meeting 2022-01-06"
date: 2022-01-11
updated: 2022-01-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议主要讨论了Ceph项目的多个Pull Request (PR)，包括新提交的PR、已关闭的PR以及正在进行中的PR。会议还涉及了一些技术讨论和后续行动计划。

#### 主要议题
1. **新提交的PR**
   - **PR 4479**：使用线程局部指针变量保存shard。目前尚未有详细审查，但Ronan已开始进行初步评论。
   - **PR 4466**：重写硬件文档。Dan已批准，但会议中提出了关于文档中关于核心需求的建议，建议更细致地说明在NVMe驱动器上可能需要更多核心以提高性能。

2. **已关闭的PR**
   - Igor的PR，主要清理onode代码中的pinning。该PR已由Yuri合并，被认为是良好的清理工作。
   - 一个关于优化对象内存分配的PR，基于收到的反馈，作者决定关闭该PR。

3. **正在进行中的PR**
   - 管理器TTL缓存的实现更新。
   - Josh的主要平衡器工作，正在进行中，计划通过tautology进行测试。
   - Igor的PR，旨在减少shared blob FSDK的RAM使用。Adam进行了大量审查，会议中讨论了如何更好地控制内存使用。

4. **其他讨论**
   - 关于omap benchmark的讨论，提出了是否需要重写以更好地适应现有OSD环境。
   - Casey汇报了rgw性能相关的PR进展，特别是关于beast前端的变化。
   - Gabby汇报了关于分配器更改的修复工作进展。

#### 决定事项
- 对于新提交的PR，鼓励团队成员进行审查。
- 对于硬件文档的更新，建议更细致地说明核心需求。
- 对于omap benchmark，建议在下次会议中进一步讨论。

#### 后续行动计划
- 继续审查和更新PR，确保代码质量和性能优化。
- 安排下一次会议，讨论omap benchmark和可能的技术改进。
- 关注并评估新提交的PR，特别是那些可能影响性能和稳定性的PR。

#### 其他备注
- 会议中提到的一些技术讨论需要Adam和Igor的参与，因此相关议题将推迟到他们参与的下次会议。
- 会议还提到了一些性能优化和内存管理的潜在改进，这些将在后续的开发和测试中进一步探索。

#### 会议结束
会议在讨论了所有议题后结束，感谢所有参与者的贡献，并期待下周的会议。