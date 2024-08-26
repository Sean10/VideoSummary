---
title: "Ceph User + Dev Monthly Meeting 2024-05-23"
date: 2024-05-31
updated: 2024-05-31
tags:
categories:
- "视频总结"
subtitle: tech
---


---
title: "Ceph User + Dev Monthly Meeting 2024-05-23"
date: 2024-05-31
updated: 2024-05-31
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Ceph社区的调查反馈，特别是关于Orchestration和Performance的调查结果。会议旨在通过互动讨论，收集社区成员的实时反馈，以便更好地理解用户需求并改进Ceph的功能和性能。

#### 关键讨论点
1. **Orchestration反馈**
   - **部署目标**：大多数用户使用裸机（bare metal）进行部署，较少使用容器。
   - **Orchestration系统**：SEF ADM是最受欢迎的Orchestration系统，其次是自制的Orchestration系统。
   - **用户反馈**：SEF ADM被认为简单可靠，但存在某些命令过于复杂和日志难以调试的问题。自制Orchestration系统则被赞赏为提供了更多的控制和信任。

2. **Performance反馈**
   - **集群事件影响**：监控同步、OSD不可用等事件对性能有显著影响。
   - **EC插件使用**：大多数用户使用默认的EC插件，如jerasure和reed_sol_van。
   - **Op调度器**：mclock是常用的Op调度器，但存在文档不足和需要手动调优的问题。

3. **Telemetry模块**：约50%的用户未启用Telemetry模块，主要原因是缺乏对功能的了解和对隐私安全的担忧。

4. **用户建议和反馈**
   - **改进建议**：用户提出了对SEF ADM的自动化程度、日志调试、OSD创建过程的具体改进建议。
   - **技术讨论**：涉及SEF ADM是否应支持非容器化部署的讨论，以及Telemetry模块的数据安全和隐私问题。

#### 决定事项
- **改进方向**：社区将根据调查反馈，特别是在Orchestration和Performance方面的具体问题，进行针对性的改进。
- **文档更新**：将更新和改进相关文档，特别是关于mclock和SEF ADM的使用指南。

#### 后续行动计划
- **跟踪问题**：社区成员被鼓励提出具体的问题和反馈，通过创建Tracker来跟踪和解决这些问题。
- **社区参与**：鼓励更多的社区成员参与到用户委员会中，特别是那些对特定主题（如stretch clusters）有兴趣的成员。
- **持续反馈**：会议结束后，调查问卷将继续开放一段时间，以便收集更多的反馈。

#### 结论
会议强调了社区反馈的重要性，并承诺将根据这些反馈进行改进，以提高Ceph的性能和用户体验。同时，鼓励社区成员积极参与，共同推动Ceph的发展。