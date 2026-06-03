---
title: "CDS Infernalis (Day 2.2) -- LMDB backend for Ceph"
date: 2015-03-06
updated: 2015-03-07
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议主题**： SEF（Storage Efficiency Framework）的LMDB键值存储后端方案讨论

**参会人员**： Patrick、John（Intel）、Shinin、会议主持人

**会议内容**：

1. **方案概述**：
   - John介绍了LMDB（Lightning Memory-Mapped Database）作为SEF的键值存储后端方案。
   - 当前SEF的QAL（Quota and Accounting Layer）实现存在问题，如读写放大率高，且需要将日志写入R Disc。
   - 该方案将包括：
     1. 实现`rmdb`存储类，继承自`qdb`，实现基本操作如get、delete和put。
     2. 集成`rmdb`作为子模块，支持自动配置和自动生成。
     3. 精炼`QB`接口，集成一些高级API，如合并操作、前缀迭代器等。

2. **方案讨论**：
   - 会议认为尝试LMDB是值得的，可以了解其在键值存储中的表现。
   - 目前SSD设置的性能问题主要在于RSM的压缩和读写放大。
   - 建议不要过于依赖文件存储和键值存储的对比，因为它们的应用场景和性能特点不同。
   - 新存储方案的目标是通用性，可在磁盘和SSD上良好运行，但不适合PCI附加的快速闪存等特定场景。

3. **行动计划**：
   - 尝试实现LMDB和LMDB接口，以便了解其在键值存储中的表现。
   - 考虑将LMDB集成到监控器中，特别是读取方面。
   - 使用现有的OSD测试工具进行测试，而不是尝试模拟OSD的工作负载。

4. **其他讨论**：
   - 讨论了在liberatus中是否需要构建键值接口，以及如何实现。
   - 讨论了如何测试监控器特定的数据库，以及是否可以使用现有的测试工具。

**结论**：

会议认为尝试LMDB作为SEF的键值存储后端方案是值得的，并制定了相应的行动计划。

[改进后的中文总结内容结束]