---
title: "Ceph Performance Meeting 2022-09-22"
date: 2022-09-26
updated: 2022-09-27
tags:
categories:
- "视频总结"
subtitle: tech
---


**会议纪要**：

1. **会议主题**：讨论Ceph分布式存储系统中的优化和性能改进。
2. **参会者**：Mark、Ronan、Adam等。
3. **主要讨论内容**：
   - Mark就上周取消的会议表示歉意，并提到他在准备与Adam讨论一些"令人兴奋的事情"。
   - Ronan询问了关于“Deep scrub”的讨论是否在邮件列表上进行，以及是否有其他私下的邮件交流。
   - Adam介绍了他最近的工作，包括对对象进行碎片整理以减少写入操作的数量，以及一个用于跟踪所有对象及其克隆的单一跟踪器的实现。
   - 提出了通过将负载从共享块转移到CPU密集型操作来改善性能的方法，并讨论了其潜在的改进效果。
   - 讨论了新的跟踪器方法如何有效地管理快照和克隆，以及如何简化数据结构。
   - 分析了新方法对CPU使用率和IOPS的影响，以及它如何减少空间放大和写入负载。
   - 提到了Jitter的概念，以及如何通过引入Jitter来平滑IO负载。
   - 讨论了在硬盘驱动器上进行快照和碎片整理的潜在影响，以及未来可能需要不同的方法。
   - 提到了rgw的HTTP 3前端的PR，以及它可能带来的性能提升。
   - 最后，讨论了当前Ceph集群部署的CPU使用情况，以及如何进一步降低开销。
4. **行动计划**：
   - 继续测试和优化Adam提出的方法。
   - 探讨将新方法集成到现有系统的可能性。
   - 分析新方法在硬盘驱动器上的性能表现。
   - 关注rgw的HTTP 3前端开发的进展，并评估其对性能的影响。
   - 计划下周继续讨论，并鼓励大家度过愉快的一周。