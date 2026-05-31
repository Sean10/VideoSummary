---
title: Ceph Telemetry - The Why, What, and How - Yaarit Hatuka, IBM
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 开源
categories: 
- "视频总结"
subtitle: Ceph_Telemetry_-_The_Why_What_and_How_-_Yaarit_Hatuka_IBM
---

### 会议纪要：Ceph Telemetry 项目回顾

**会议时间**：上午  
**主讲人**：Yit  
**主题**：Ceph Telemetry 项目回顾



#### **会议概述**
Yit 讲解了 Ceph Telemetry 项目的目的、功能、数据收集方式以及对 Ceph 社区的价值。Telemetry 是 Ceph 的一个内置模块，用于自动收集和传输 Ceph 集群的匿名数据，以帮助开发者了解 Ceph 的使用情况和性能表现。



#### **会议主要议题**

1. **Telemetry 的定义和目的**
   - Telemetry 是一种自动记录和传输数据的技术，Ceph Telemetry 项目通过收集 Ceph 集群的匿名数据，帮助开发者了解 Ceph 的使用情况、发现新问题并优先处理。
   - 用户可以通过 Telemetry 数据验证其安装的 Ceph 集群是否存在常见问题，并了解其他用户如何使用 Ceph 的功能。

2. **Telemetry 的数据收集**
   - Telemetry 模块自 Mimic 版本（2019 年）引入，已有约 3,500 个集群参与数据上报，总存储容量达到 1.7 EB。
   - 数据收集分为多个通道，包括基本通道、崩溃通道、设备通道等，用户可根据需求选择开启。

3. **数据隐私与安全性**
   - Telemetry 数据是匿名的，不包含敏感信息。
   - 用户可通过 CLI 命令或 Ceph Dashboard 选择加入 Telemetry，并可随时查看上报的数据。

4. **Telemetry 数据的应用**
   - 开发者通过 Telemetry 数了解用户如何使用 Ceph 功能、发现新 Bug 并优先修复。
   - 用户通过 Telemetry 数据验证其集群的配置是否合理，了解其他用户的使用情况。
   - 崩溃处理：Telemetry 收集的崩溃数据通过自动化流程与 Ceph 的 Bug 跟踪系统（Redmine）同步，帮助开发者快速定位和修复问题。

5. **Telemetry 的公共仪表盘**
   - Telemetry 数据通过公共仪表盘展示，用户可以查看集群的版本分布、存储容量、设备健康状况等信息。
   - 仪表盘还提供了对 Rook、Ceph 版本、存储类利用率等详细分析。

6. **未来计划**
   - 继续优化 Telemetry 数据收集和分析流程，增加更多功能。
   - 鼓励更多用户参与 Telemetry 项目，以帮助 Ceph 社区更好地了解用户需求并改进产品。



#### **决定事项与后续行动计划**

1. **继续优化 Telemetry 功能**：
   - 增加对 ODF 安装信息、RBD 镜像功能使用情况的数据收集。
   - 改进崩溃数据处理流程，提高 Bug 修复的效率。

2. **推广 Telemetry 项目**：
   - 通过社区活动和文档更新，鼓励更多用户加入 Telemetry 项目。

3. **定期更新公共仪表盘**：
   - 确保 Telemetry 数据能够及时反映 Ceph 社区的最新动态，并提供更详细的分析报告。



#### **会议总结**
Ceph Telemetry 项目通过自动收集和分析 Ceph 集群的匿名数据，为开发者和用户提供了宝贵的洞察力。通过 Telemetry，开发者可以更快地发现和修复问题，用户可以验证其集群配置并了解其他用户的使用情况。未来，Ceph 社区将继续优化 Telemetry 功能，并鼓励更多用户参与，以推动 Ceph 项目的持续改进。



**会议结束时间**：10 秒超时  
**会议反馈**：会议内容丰富，参会者对 Telemetry 项目表现出浓厚兴趣，并提出了关于数据收集和功能改进的问题。