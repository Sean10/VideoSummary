---
title: "Ceph Science Working Group 2022-05-24"
date: 2022-05-26
updated: 2022-05-26
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要：

1. 讨论了Ceph分布式存储系统在大型集群中遇到的scrubbing问题，特别是与HP Apollos硬件相关的问题。探讨了磁盘类型（旋转磁盘、闪存或NVMe）、对象大小（小对象或大对象）以及测试数据量（约25PB）。

2. 分析了默认的scrubbing和deep scrubbing参数是否适合当前的工作负载和硬件配置。提出可能需要调整这些参数以适应更大的文件和磁盘容量。

3. 提到了由于硬件限制（如磁盘容量和I/O性能）导致的scrubbing警告，并讨论了如何通过调整监控阈值来减少这些警告。

4. 讨论了RAID控制器的影响，特别是它们可能对整个磁盘的一致性检查（如Dell的patrol reads）产生的影响。

5. 提出了基于OSD的大小和工作负载自动调整默认scrubbing参数的想法，并考虑了实现这一功能的可能性。

6. 分享了有关Ceph版本更新的信息，特别是Octopus版本将支持CentOS 7，并讨论了升级到Pacific版本的计划。

7. 提到了Cephalocon活动，包括虚拟参与的可能性和相关的技术展示。

8. 讨论了集中式日志记录的使用情况，特别是Elasticsearch和Loki的使用，以及它们在Ceph环境中的潜在应用。

9. 最后，讨论了一个特定的性能问题，涉及Power9节点上的性能下降，这可能是由于网络接口问题或内核客户端与OSD之间的连接中断所致。

行动计划：
- 研究并调整scrubbing参数以适应大型磁盘和工作负载。
- 检查RAID控制器设置，以确定其是否影响scrubbing性能。
- 探索自动调整scrubbing参数的方法，可能通过开发脚本或工具来实现。
- 计划升级到Ceph的Pacific版本，并关注Octopus版本对CentOS 7的支持。
- 准备参与Cephalocon活动，包括技术展示和虚拟参与的安排。
- 评估集中式日志记录解决方案，如Elasticsearch和Loki，以提高Ceph环境的可管理性。
- 调查Power9节点性能问题的根本原因，并寻找解决方案。