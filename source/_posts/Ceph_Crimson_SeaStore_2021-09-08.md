---
title: "Ceph Crimson/SeaStore 2021-09-08"
date: 2021-09-11
updated: 2021-09-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间：[具体日期]
#### 参会人员：[具体人员名单]

#### 主要议题：
1. **Segment Cleaner 问题审查**
   - 讨论了Segment Cleaner可能存在的问题，决定进一步详细审查。
   - 对handle split的修复可能解决了某个assert问题，但仍需进一步验证。

2. **性能分析与优化**
   - 使用Curve进行性能分析，发现rb allocate exchange占用了约20%的CPU周期。
   - 讨论了LBA树遍历的优化，建议使用二分查找以提高效率。
   - 计划通过perf counter分析迭代次数，以确定性能瓶颈。

3. **Bug修复与功能开发**
   - 讨论了多个Bug的修复情况，包括beetry相关问题和extent placement manager PR。
   - 提到了多设备支持工作的进展，以及对seastar教程的改进。

4. **监控与指标收集**
   - 讨论了收集和分析IO性能指标的方法，特别是reactor utilization的独特性。
   - 计划进一步优化写放大问题。

#### 决定事项：
- 对Segment Cleaner进行更详细的审查。
- 实施二分查找优化LBA树遍历。
- 通过perf counter分析迭代次数，以确定性能瓶颈。
- 继续进行Bug修复和功能开发。

#### 后续行动计划：
- 详细审查Segment Cleaner，并验证handle split修复的效果。
- 实施二分查找优化，并分析perf counter数据。
- 继续进行Bug修复和功能开发，特别是多设备支持工作。
- 收集和分析更多IO性能指标，优化写放大问题。

#### 其他备注：
- 会议中提到了使用perf counter进行性能分析的具体方法和预期结果。
- 讨论了seastar教程的改进和vstart的使用体验。

#### 会议结束：
- 会议在讨论了所有议题后结束，参会人员计划在下周继续跟进相关工作。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。