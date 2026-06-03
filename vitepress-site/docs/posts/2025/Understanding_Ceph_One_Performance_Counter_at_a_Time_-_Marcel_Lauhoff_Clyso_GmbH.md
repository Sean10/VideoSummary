---
title: "Understanding Ceph One Performance Counter at a Time - Marcel Lauhoff, Clyso GmbH"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：理解Ceph性能计数器

**会议主题**: 通过性能计数器逐步理解Ceph的工作原理

**主讲人**: Marcel Lauhoff, Clyso GmbH

**会议内容概述**:

Marcel Lauhoff分享了他通过性能计数器来理解Ceph工作原理的学习历程。他通过一系列实验，展示了如何利用性能计数器分析Ceph的操作和延迟，并开发了一种直观的理解方法。

**主要议题**:

1. **性能计数器的定义与类型**:
   - 性能计数器是运行时捕获的服务度量，在Ceph中称为perf counters，在其他上下文中通常称为metrics。
   - 类型包括：Gauge（表示可测量的值）、Counter（递增的值）、Histogram（带有桶的计数器）、Long Running Average（长期平均值）。

2. **实验与分析**:
   - 通过简单的S3 PUT操作，分析了操作类型和延迟，发现涉及多个操作，包括写入和设置扩展属性。
   - 通过S3基准测试，分析了不同操作的延迟分布，发现读取操作的延迟分布有两个峰值。

3. **延迟分析**:
   - 使用OSD的性能计数器分析读取、写入和读写操作的延迟。
   - 使用直方图分析延迟分布，发现不同大小的操作延迟差异较大。

4. **工具与方法**:
   - 使用Admin Socket和Perf Dump获取性能计数器。
   - 使用Histogram分析深入了解操作的延迟分布。

**决定事项**:
- 探索如何将性能计数器与Prometheus、Grafana等监控工具集成。
- 开发一个类似“top”工具的网络连接监控工具。

**后续行动计划**:
- 研究将Ceph的性能计数器导出到Prometheus等监控系统中。
- 深入研究BlueStore的性能计数器。
- 开发网络连接监控工具。

**会议总结**:
Marcel通过性能计数器展示了如何逐步理解Ceph的工作原理，强调了性能计数器在开发和调试中的重要性，并提出了进一步的研究和工具开发计划。