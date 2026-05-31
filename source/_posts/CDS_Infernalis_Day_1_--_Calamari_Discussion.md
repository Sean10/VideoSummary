---
title: "  CDS Infernalis (Day 1) -- Calamari Discussion  "
date: 2015-03-06
updated: 2015-03-07
tags:
- Ceph
- 分布式存储
categories:
- "视频总结"
subtitle: CDS_Infernalis_Day_1_--_Calamari_Discussion
---
本次会议主要讨论了Calamari客户端的重命名以及如何在智能API中实现高级故事。以下是会议内容的详细总结：

**1. Calamari客户端重命名**

*   由于“Calamari”名称容易引起混淆，决定将其重命名为“Rana”。
*   “Rana”将成为上游仓库，并作为UI的参考实现。
*   “Rana”将继续使用MIT许可证，并按与Calamari相同的节奏发布版本。
*   预计在“Hammer”版本发布后约一个月推出“Rana”的第一个版本。

**2. 高级故事实现**

*   讨论了如何在智能API中实现高级故事，并通过Calamari API的现有功能进行深入分析。
*   以“管理员可以不中断I/O扩展存储池的PG数”为例，展示了如何通过API进行更新操作。
*   分析了Calamari架构中涉及的各个组件，包括：
    *   Calamari REST API：负责处理HTTP请求和验证。
    *   Thulu服务：负责将REST请求映射到Seth命令。
    *   Salt：用于节点控制和配置管理。
    *   Python模块：用于与Seth集群交互。

**3. 其他议题**

*   讨论了如何实现“管理员收到OSD可能失败的警报”的功能。
*   提出了使用Smartmon工具或其他工具来实现此功能的想法。
*   鼓励社区成员加入邮件列表或提交问题跟踪器，以提供反馈和贡献。

**行动计划**

*   Gregory将创建问题跟踪器条目，以跟踪Calamari客户端重命名和高级故事实现的工作。
*   社区成员可以加入邮件列表或提交问题跟踪器，以提供反馈和贡献。
*   讨论了如何实现“管理员收到OSD可能失败的警报”的功能，并鼓励社区成员提供反馈。

**改进点**

*   原总结中未提及“Rana”将作为UI的参考实现，以及“Rana”的发布节奏与Calamari相同。
*   原总结中未详细说明Calamari架构中涉及的组件及其功能。
*   原总结中未提及使用Smartmon工具或其他工具实现OSD警报功能的讨论。