---
categories:
- 视频总结
date: 2014-10-30
subtitle: CDS_Hammer_Day_2_-_OSD_-_Scrub_SnapTrim_IO_Prioritization
tags:
- Ceph
- OSD
title: "'CDS Hammer (Day 2) - OSD: Scrub / SnapTrim IO Prioritization'"
updated: 2014-10-31
---




会议纪要

会议时间：[请填写会议时间]

参会人员：Samuel（主讲人），其他研发人员

会议主题：分布式存储Ceph的 scrub 和 snap trim IO优先级优化

会议内容：

1. **背景介绍**：
   - Ceph中的所有操作都在线程池中执行，但不同线程池之间的相对优先级由操作系统决定，这可能导致不理想的优先级分配。
   - 为了优化IO优先级，提议将所有可能的IO操作整合到一个队列中，并使用更高效的队列管理方式。

2. **主要议题**：
   - **OSD内部机制**： OSD的绝大多数操作都在线程池中执行，但线程池之间的优先级分配存在问题。
   - **IO优先级**： 需要优化scrub、snap trim 和恢复等操作的IO优先级。
   - **恢复线程池**： 当前恢复线程池的线程数量与其他客户端线程数量相比过少，需要调整。
   - **优先级标记**： 在后台工作中添加IO优先级标记，将优先级管理提升到更高级别。

3. **关键细节**：
   - 使用更高效的队列管理方式，提高队列效率。
   - 调整恢复线程池的线程数量，优化恢复操作。
   - 将所有可能的IO操作整合到一个队列中，并使用优先级标记进行管理。
   - 将操作分解成更小的粒度，提高效率。

4. **决定事项**：
   - 将所有可能的IO操作整合到一个队列中，并使用优先级标记进行管理。
   - 调整恢复线程池的线程数量，优化恢复操作。
   - 将操作分解成更小的粒度，提高效率。

5. **后续行动计划**：
   - Samuel将在下个月完成相关代码调整。
   - 检查Lucerne，确认使用tagged union或boost variant。
   - 优化恢复操作，考虑使用更细粒度的操作分解。

**备注**：
- 会议中提到的“Firefly”是Ceph的一个版本，指的是Ceph 0.63版本。
- “tagged union”和“boost variant”是Ceph相关的技术术语，分别指Ceph中的一种数据结构和一种编程库。

**关键词**： scrub、snap trim、IO优先级、OSD、线程池、恢复操作、优先级标记、tagged union、boost variant