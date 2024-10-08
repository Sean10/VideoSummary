---
title: "Troubleshooting and Debugging in the rook-ceph cluster"
date: 2022-11-23
updated: 2022-11-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Rook项目中的故障排查和调试方法，特别是如何处理Rook Ceph集群中的常见问题，并介绍了Crew插件的使用及其在故障排查中的应用。

#### 参会人员
- **Deepika Upadhyay**：Kotak的云存储工程师，Rook项目的核心贡献者。
- **Shubham Doshi**：Red Hat的软件工程师，Rook项目的核心贡献者。

#### 主要议题
1. **Rook Ceph集群中的常见故障**：
   - 监控器（monitors）失去Quorum，导致无法执行Ceph操作。
   - 网络故障或中断导致的卷报告“仍在使用”错误。
   - 高CPU利用率的Ceph组件问题。

2. **故障排查方法**：
   - 使用Rook操作日志和Kubernetes层进行初步故障排查。
   - 利用Crew插件进行更深入的调试，特别是在监控器失去Quorum的情况下。

3. **Crew插件介绍**：
   - Crew是一个基于Kubectl命令的工具，帮助用户管理和故障排查其Ceph集群。
   - 提供了自动化命令，如恢复Quorum和调试模式，简化了故障排查过程。

4. **未来工作计划**：
   - 计划增加在所有监控器都失效时恢复集群的功能。
   - 考虑增加备份和恢复支持，以防止Ceph集群CRD意外删除。
   - 自动化核心转储（core dump）的收集。

#### 决定事项
- 确认了Crew插件在Rook Ceph集群故障排查中的有效性。
- 确定了未来工作的方向，包括增强Crew插件的功能和自动化核心转储收集。

#### 后续行动计划
- 继续开发和完善Crew插件，以支持更多的故障排查场景。
- 与Telemetry团队合作，探讨如何集成核心转储收集到现有基础设施中。
- 鼓励社区成员提供反馈和建议，以改进Rook项目的故障排查工具和文档。

#### 其他信息
- 提供了Crew插件的安装和使用文档链接，方便用户自行安装和学习使用。
- 强调了社区合作的重要性，并欢迎任何形式的贡献和反馈。

#### 会议结束
感谢所有参与者的参与和贡献，期待在未来的社区活动中再次相聚。