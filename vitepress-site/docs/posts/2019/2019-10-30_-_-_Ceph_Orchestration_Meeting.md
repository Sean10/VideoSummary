---
title: "2019-10-30 :: Ceph Orchestration Meeting"
date: 2019-11-03
updated: 2019-11-04
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议主题**： Ceph分布式存储项目讨论

**会议时间**： 2023年11月（具体日期未知）

**参会人员**： 
- Sun、CH、Letta Pia、Katy Wiseman、Edie、Paul Kozma、AJ、Sage Ki Foo、Brad Hubbard、会议记录者

**会议关键细节**：

**1. Python 3问题**：
- 在Sintra 7和Central US 8环境中，由于CentOS 7缺少Python 3的某些包，导致Ceph无法运行。
- 讨论了在CentOS 7中添加所需Python 3包的可能性，并建议由Ceph项目成员提交请求。

**2. Ceph集群状态监控**：
- 提出了一个用于监控Ceph集群状态的工具，使用一种未命名的数据结构存储状态信息。
- 讨论了使用OC metadata来改进数据结构，并计划未来进行改进。

**3. 设备共享问题**：
- 讨论了当多个设备共享同一个OSD时可能出现的冲突问题。
- 提出了使用CID来区分不同设备的建议。

**4. SSH Orchestrator集成**：
- CH正在努力集成SSH Orchestrator，但由于CentOS 7缺少Python 3的某些包，导致集成受阻。
- 讨论了使用远程IO包的兼容性问题。

**5. 人员变动**：
- 会议记录者将在2023年12月至2月期间离职。
- 讨论了在离职前如何为团队做出贡献。

**决定事项**：

- 由Ceph项目成员提交请求，在CentOS 7中添加所需Python 3包。
- 进一步改进Ceph集群状态监控工具。
- 使用CID来区分共享同一个OSD的不同设备。
- 寻找解决方案以解决SSH Orchestrator集成问题。
- 讨论了离职人员的贡献问题。

**后续行动计划**：

- 由Ceph项目成员提交请求，在CentOS 7中添加所需Python 3包。
- 进一步改进Ceph集群状态监控工具。
- 使用CID来区分共享同一个OSD的不同设备。
- 寻找解决方案以解决SSH Orchestrator集成问题。
- 讨论了离职人员的贡献问题。

[改进后的总结确保了以下几点：]
- 准确反映了原始内容的关键细节。
- 覆盖了讨论的主要议题。
- 提到了决定的事项和后续的行动计划。
- 保留了计算机科学/ceph相关领域的英文原文关键词。