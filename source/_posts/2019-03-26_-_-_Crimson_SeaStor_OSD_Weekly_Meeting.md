---
title: "  2019-03-26:: Crimson SeaStor OSD Weekly Meeting  "
date: 2019-04-15
updated: 2019-04-15
tags:
- Ceph
- 性能优化
- 分布式存储
- OSD
categories:
- "视频总结"
subtitle: 2019-03-26_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
---



### 改进后的中文总结内容

在2019年3月26日的Ceph Crimson SeaStor OSD每周会议上，研发人员和内容审核专家讨论了Ceph分布式存储系统性能优化与Crimson OSD项目的进展。以下是对会议内容的总结：

#### 会议纪要

#### 会议时间：
[请填写会议时间]

#### 参会人员：
[请填写参会人员名单]

#### 会议主题：
Ceph 分布式存储系统性能优化与 crimson OSD 项目的进展讨论

#### 关键细节：

* **Crimson OSD 项目**：
    * 已完成初步的 crimson OSD 实现，但部分功能尚未完善。
    * 性能测试显示，在某些场景下，crimson OSD 的性能优于经典 OSD，但需要进一步优化。
    * 优化方向包括减少线程切换，提高指令缓存命中率，优化内存使用。
    * 下一步计划是完成 crimson OSD 的全部功能，进行更全面的性能测试，并与经典 OSD 进行公平的比较。

* **经典 OSD 优化**：
    * 优化目标为提高 CPU 使用效率和减少内存占用。
    * 使用 perf stat 工具进行性能分析，观察 CPU 使用率、内存占用等指标。
    * 下一步计划是调整 placement group 的数量，提高经典 OSD 的并行处理能力。

#### 讨论的主要议题：

* **Crimson OSD 性能优化**：
    * 如何减少线程切换，提高指令缓存命中率。
    * 如何优化内存使用，减少内存占用。
    * 如何与经典 OSD 进行公平的比较。

* **经典 OSD 优化**：
    * 如何提高 CPU 使用效率。
    * 如何减少内存占用。
    * 如何调整 placement group 的数量。

#### 决定的事项：

* 完成 crimson OSD 的全部功能。
* 进行更全面的性能测试，并与经典 OSD 进行公平的比较。
* 调整 classic OSD 的 placement group 数量，提高其并行处理能力。
* 使用 perf stat 工具进行性能分析，观察 CPU 使用率、内存占用等指标。

#### 后续行动计划：

* Crimson OSD 项目负责人：完成 crimson OSD 的全部功能，并进行性能测试。
* Classic OSD 项目负责人：调整 classic OSD 的 placement group 数量，并进行性能测试。
* 全体成员：关注 crimson OSD 和 classic OSD 的性能优化工作，提供反馈和建议。

会议中，与会者还讨论了以下关键点：

* 如何通过优化 crimson OSD 的解码阶段来提高性能。
* 如何使用 perf stat 工具进行性能分析，并如何使用它来比较 crimson OSD 和经典 OSD 的性能。
* 如何通过调整 placement group 的数量来优化经典 OSD 的性能。
* 如何在 crimson OSD 中使用应用程序队列来提高性能。

会议强调了性能优化和 crimson OSD 项目的进展对 Ceph 分布式存储系统的重要性。与会者决定采取进一步的行动，以提高 Ceph 的性能和可靠性。