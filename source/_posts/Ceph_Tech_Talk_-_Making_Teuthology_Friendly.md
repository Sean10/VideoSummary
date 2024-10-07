---
title: "Ceph Tech Talk: Making Teuthology Friendly"
date: 2023-08-16
updated: 2023-08-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** 病理学（Pathology）项目的改进与实施

**主讲人：** Devansh，Google Summer of Code实习生，SEF项目成员

**会议时间：** [具体日期]

**会议地点：** [具体地点]

**参会人员：** [列出参会人员]

**会议内容：**

1. **项目介绍：**
   - **病理学（Pathology）** 是一个用于安全测试的Python框架，主要用于在远程主机上通过SSH运行测试。
   - **Pulpito** 是一个用于监控病理学测试基础设施的Web仪表板，包括测试队列和可用测试节点。

2. **现有问题：**
   - 病理学的命令行接口（CLI）复杂，包含大量命令和标志，对新用户不友好。
   - 用户需要手动配置多个参数，如仓库URL、分支名称和套件选项，容易导致错误。
   - 新用户难以发现和理解可用命令、选项及其含义，导致使用困难。

3. **解决方案：**
   - 开发**下一代Pulpito**，提供更直观的用户界面，允许用户通过仪表板直接调度或终止作业。
   - 实现了一个病理学API，并与下一代Pulpito集成，使用户无需SSH进入服务器即可管理作业。

4. **实施细节：**
   - 主要功能包括GitHub认证、作业调度和作业终止。
   - 通过仪表板，用户可以轻松配置和监控测试，提高团队生产力。

5. **演示：**
   - 展示了如何通过下一代Pulpito界面调度作业和终止作业。
   - 演示了作业调度的实时反馈和错误处理的流程。

6. **未来展望：**
   - 考虑将Paddles服务迁移到FastAPI，以利用其社区支持和内置功能。
   - 改进下一代Pulpito的用户体验，增加更多用户中心的功能，如作业历史记录和错误日志展示。

7. **感谢与反馈：**
   - 感谢导师Zach、Aishwarya和Junior在整个项目过程中的帮助。
   - 欢迎与会者提供反馈和建议，以进一步改进项目。

**后续行动计划：**
- 继续完善下一代Pulpito的功能。
- 探索将常用命令存储在数据库中的可能性。
- 增强错误日志的展示方式，提供更结构化的错误信息。

**会议结束语：**
- 感谢所有参与者的参与和反馈，期待继续改进和贡献于SEF项目。

**附件：**
- 演示视频链接
- 项目GitHub仓库链接

**会议记录人：** [记录人姓名]

**审核人：** [审核人姓名]

**日期：** [记录日期]