---
categories:
- 视频总结
date: 2023-05-18
subtitle: Ceph_Performance_Tuning_-_From_Bluestore_to_RBD_-_Mark_Nelson_Clyso_GmbH
tags:
- Ceph性能调优
- Bluestore
- RBD
- 分布式存储
- Ceph性能
title: Ceph Performance Tuning- From Bluestore to RBD - Mark Nelson, Clyso GmbH
updated: 2023-05-19
---



在本次会议中，Mark Nelson，Ceph性能团队成员，深入探讨了Ceph性能调优的重要性和具体方法。以下是对会议内容的总结：

**会议要点**：

1. **性能概述**： Mark Nelson首先介绍了Ceph性能的复杂性，强调了理解性能问题背后的行为和原因的重要性。他引用了Neil Stevenson的话：“性能取决于具体情况”。

2. **性能调优工具**： 
   - 介绍了CBT（Ceph Benchmarking Tool），一个用于性能测试的工具，支持多种测试工具如fio, hsbench等。
   - 提到了正在开发的仪表板，用于更直观地展示测试结果。

3. **性能优化案例**：
   - **硬件问题**： SSD固件升级解决高Q等待时间问题。
   - **软件问题**： PG计数对性能的影响，低PG计数导致资源争用和性能下降。
   - **RBD快照修剪**： 优化共享blob的处理，减少CPU使用率。
   - **OSD线程优化**： 减少线程数在资源有限的情况下提高效率。
   - **PG日志与RocksDB交互**： 调整RocksDB参数和实验性日志原型，改善随机写性能。

4. **结论与建议**：
   - 强调了理解性能问题背后的行为和原因的重要性。
   - 鼓励关注Ceph社区的博客和文档，以获取更多性能调优的信息和案例。

**后续行动计划**：

- 继续开发和完善性能调优工具，如CBT和仪表板。
- 探索和实施更多的性能优化措施，特别是在硬件和软件交互方面。
- 加强社区合作，分享和讨论性能调优的最佳实践。

**可能的错误、误解或遗漏**：

- 原始字幕内容中缺少了一些关键信息，如CBT的具体功能和使用方法。
- 会议中提到的仪表板原型可能尚未发布或完全可用。

**改进后的中文总结**：

在本次会议中，Mark Nelson深入探讨了Ceph性能调优的重要性和具体方法。他强调了理解性能问题背后的行为和原因的重要性，并介绍了CBT（Ceph Benchmarking Tool）等性能调优工具。他还分享了一些性能优化案例，包括硬件和软件问题，并提出了后续行动计划，包括工具开发和社区合作。