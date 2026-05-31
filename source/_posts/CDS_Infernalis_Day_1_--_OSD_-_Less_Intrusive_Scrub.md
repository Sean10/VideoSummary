---
categories:
- 视频总结
date: 2015-03-06
subtitle: CDS_Infernalis_Day_1_--_OSD_-_Less_Intrusive_Scrub
tags:
- Ceph
- OSD
- 性能优化
title: "'CDS Infernalis (Day 1) -- OSD: Less Intrusive Scrub'"
updated: 2015-03-06
---




CDS Infernalis (Day 1) 会议的议题集中在Ceph中OSD的scrub功能优化上，旨在减少其对系统性能的影响。以下是会议的主要内容和决定事项：

**会议主题**： 讨论并优化Ceph中OSD的scrub选项，减少其对系统性能的影响。

**关键细节**：

- **scrub优化目标**： 减少scrub操作对系统性能的影响，提高效率。
- **主要议题**：
  - **减少scrub对性能的影响**： 通过随机化scrub调度时间、选择更细粒度的scrub操作、提高scrub操作优先级等措施来减少scrub对系统性能的影响。
  - **统一工作队列**： 完成统一工作队列的实现，以便更好地管理scrub操作。
  - **scrub调度策略**： 优化scrub调度策略，使其更加智能，例如根据负载情况进行动态调整。
  - **优先级问题**： 解决优先级反转问题，确保scrub操作在关键时刻能够获得足够的资源。
  - **scrub窗口大小**： 调整scrub窗口大小，例如将窗口大小设置为单个对象，以减少调度开销。

**决定的事项**：

- 完成统一工作队列的实现。
- 随机化scrub调度时间，例如将深度scrub间隔设置为一周加减四天。
- 选择更细粒度的scrub操作，例如在chunk级别进行决策。
- 提高scrub操作优先级，确保其在关键时刻能够获得足够的资源。
- 调整scrub窗口大小，例如将窗口大小设置为单个对象。
- 实现scrub操作限制，例如限制scrub操作的速度（例如每秒处理的对象数量或每秒处理的字节数）。
- 添加健康警告，当无法在指定时间内完成scrub操作时，向管理员发出警告。

**后续行动计划**：

- Sam将负责完成统一工作队列的实现。
- 其他研发人员将根据会议讨论结果，进一步优化scrub操作。
- 添加健康警告功能。
- 评估scrub操作限制的效果。

**关键词**：

- scrub
- OSD
- unified work queue
- priority inversion
- throttling
- quality of service