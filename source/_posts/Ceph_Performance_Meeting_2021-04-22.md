---
title: "Ceph Performance Meeting 2021-04-22"
date: 2021-04-23
updated: 2021-04-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议是Ceph开发团队的定期会议，主要讨论了近期的工作进展、待处理的Pull Requests（PRs）以及一些技术细节。会议开始时，主持人欢迎大家回归，并简要回顾了过去几周的工作情况。

#### 主要议题
1. **Pull Requests（PRs）讨论**
   - 讨论了两个新的PR，均与o-node pinning和trimming相关。一个是Igor提交的，另一个是Adam提交的，但Adam本周不在，因此未能深入讨论。Igor建议对两个方案进行独立审查。
   - 更新了关于RGW压缩和roxdb内存分配的PR，Gabriel的PR需要进一步的审查和测试。

2. **技术细节讨论**
   - Gabriel讨论了在roxdb中进行对象计数的挑战，提出了使用估计大小和节点遍历的方法来改进进度显示。
   - 讨论了如何从PG map中获取对象计数信息，以及如何改进osd的启动过程显示。

3. **Crimson存储优化**
   - 介绍了Crimson存储的最新进展，包括与IBM的合作和性能优化。目前Crimson在处理小随机读写方面更高效，但仍需解决多核利用率的问题。

#### 决定事项
- 对Igor和Adam的PR进行独立审查，计划在下一次性能会议上进一步讨论。
- Gabriel将继续测试和改进roxdb中的对象计数和进度显示方法。
- 继续推进Crimson存储的多核优化工作。

#### 后续行动计划
- 对Gabriel的PR进行详细审查和性能测试。
- 继续研究和优化Crimson存储的多核利用率。
- 下一次会议将讨论PR的进一步审查结果和Crimson存储的进展。

#### 其他事项
- 确认了关于backfill和recovery reservations的邮件列表讨论的澄清。
- 会议结束时，主持人提醒大家下周再见，并祝大家一周愉快。

本次会议有效地总结了近期的工作进展，并为接下来的工作指明了方向。