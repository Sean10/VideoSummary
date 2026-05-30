---
title: "  Ceph Science Working Group 2022-05-24  "
date: 2022-05-26
updated: 2022-05-26
tags:
- Ceph
- 分布式存储
- scrubbing
- 高可用性
- 自动化
- 性能优化
categories:
- "视频总结"
subtitle: Ceph_Science_Working_Group_2022-05-24
---



本次Ceph科学工作组会议主要讨论了Ceph分布式存储系统在大型集群中面临的scrubbing问题，以及与HP Apollos硬件相关的问题。会议涵盖了以下关键议题：

1. **scrubbing问题**：针对Ceph在大型集群中遇到的scrubbing问题，特别是与HP Apollos硬件相关的问题，讨论了磁盘类型、对象大小和测试数据量等因素。
2. **参数调整**：分析了默认的scrubbing和deep scrubbing参数是否适合当前的工作负载和硬件配置，并提出了调整这些参数以适应更大文件和磁盘容量的可能性。
3. **监控阈值调整**：讨论了硬件限制导致的scrubbing警告，以及如何通过调整监控阈值来减少这些警告。
4. **RAID控制器影响**：讨论了RAID控制器对磁盘一致性检查的影响。
5. **自动调整参数**：提出了基于OSD的大小和工作负载自动调整默认scrubbing参数的想法。
6. **版本更新**：分享了Ceph版本更新的信息，包括Octopus版本将支持CentOS 7，并讨论了升级到Pacific版本的计划。
7. **Cephalocon活动**：提到了Cephalocon活动，包括虚拟参与的可能性和相关的技术展示。
8. **集中式日志记录**：讨论了集中式日志记录的使用情况，特别是Elasticsearch和Loki的使用，以及它们在Ceph环境中的潜在应用。
9. **性能问题**：讨论了一个特定的性能问题，涉及Power9节点上的性能下降。

会议确定了以下行动计划：

- 研究并调整scrubbing参数以适应大型磁盘和工作负载。
- 检查RAID控制器设置，以确定其是否影响scrubbing性能。
- 探索自动调整scrubbing参数的方法。
- 计划升级到Ceph的Pacific版本，并关注Octopus版本对CentOS 7的支持。
- 准备参与Cephalocon活动，包括技术展示和虚拟参与的安排。
- 评估集中式日志记录解决方案，如Elasticsearch和Loki，以提高Ceph环境的可管理性。
- 调查Power9节点性能问题的根本原因，并寻找解决方案。