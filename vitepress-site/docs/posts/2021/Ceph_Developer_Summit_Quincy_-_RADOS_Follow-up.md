---
title: "Ceph Developer Summit Quincy: RADOS Follow-up"
date: 2021-04-20
updated: 2021-04-21
tags:
  - "Ceph"
  - "分布式存储"
  - "RADOS"
  - "BlueStore"
categories:
  - "视频总结"
outline: deep
---
Ceph开发者峰会Quincy的RADOS跟进会议纪要：

本次会议是CDS Raiders会议的后续会议，旨在回顾CDS讨论的项目，并根据优先级将其整理到Trello看板中。会议主要讨论了以下议题：

1. **Trello看板整理**：
   - 讨论了在Etherpad中列出的项目，并确保这些项目已正确转移到Trello看板上。
   - 主要议题包括仪表盘改进、崩溃遥测面板、BlueStore或Split Cache改进等。

2. **BlueStore与Split Cache改进**：
   - 讨论了由于BlueStore书籍的可用性问题，上次会议未能详细讨论的改进措施。
   - 计划在性能会议上进一步讨论这些改进，并已将相关文档链接添加到Etherpad。

3. **Manager改进**：
   - 讨论了一系列Manager的改进措施，包括短期和长期目标。
   - 特别提到了改进进度模块和Insights，这些已有单独的Trello卡片。

4. **Autoscaler改进**：
   - 讨论了Autoscaler的改进，包括创建单独的自动配置文件，用户可以根据工作负载选择合适的配置。

5. **Cluster Log Messages**：
   - 决定不存储所有低请求消息在集群日志中，而是将其定向到Manager日志。
   - 讨论了控制监控器中修剪率的更适应性方法。

6. **其他技术细节**：
   - 讨论了结构化配置文件、自动认证密钥轮换、Autoscaler改进、QoS（Quality of Service）等。
   - 特别提到了MClock调度器的默认使用，以及自动化基线测量的需求。

会议决定事项包括：
- 确认了各个项目的优先级和实施细节。
- 决定将某些项目的改进细节转移到Trello看板，以便更好地管理和跟踪。
- 确定了某些项目的短期和长期目标，并计划在后续的性能会议中进一步讨论。

后续行动计划包括：
- 继续在Trello看板上跟踪和管理各个项目的进展。
- 对于某些未详细讨论的项目，计划在后续的性能会议或CDM会议上进一步讨论。
- 确保所有项目的改进措施得到适当的文档记录和用户支持。

会议还讨论了一些小的改进项目，这些项目适合新手开发者参与。例如，设备错误和OSD崩溃的映射，提出了进一步的集成和改进建议。