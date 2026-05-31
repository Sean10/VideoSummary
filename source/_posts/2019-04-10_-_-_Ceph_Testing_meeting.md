---
categories:
- 视频总结
date: 2019-04-12
subtitle: 2019-04-10_-_-_Ceph_Testing_meeting
tags:
- Ceph
- 测试
- 分布式存储
- OpenStack
title: "'2019-04-10 :: Ceph Testing meeting'"
updated: 2019-04-12
---



### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： 未知

**会议主题**： Ceph 存储集群测试与部署

**会议内容**：

**1. 近期工作回顾**

- 会议回顾了过去几周的工作情况，由于部分成员缺席，对具体工作进展了解有限。
- Kiran 分享了在测试环境中的 Rock Orchestrator 部署经验，但未明确其整合方案。

**2. Jenkins 测试**

- 目前上游 Jenkins 测试主要依靠 Jenkins Slave 系统自动执行，如 Alfredo 创建的系统。
- David Galloway 负责管理 Jenkins 环境。
- 讨论了如何将测试集成到 Jenkins 中，并触发相关操作。

**3. 部署测试**

- 讨论了将测试部署到虚拟机中的方法，包括使用电话设置虚拟机、部署集群和执行测试。
- 目前上游尚无直接将测试部署到虚拟机中的方案，但可以考虑参考 Jenkins 测试方案。

**4. smoke 测试**

- 讨论了 smoke 测试的执行方式，包括在 Jenkins 上运行和针对不同分支执行。
- 认为在 Jenkins 上运行 smoke 测试可以提供快速反馈，并减少人工干预。

**5. OpenStack 部署测试**

- 讨论了在 OpenStack 上进行部署测试的方法，包括使用 OpenStack API 和创建镜像。
- 认为需要实现类似功能，以便在测试环境中使用 OpenStack。

**6. Other**

- 讨论了不同测试套件的执行时间，以及如何优化测试流程。
- 认为需要进一步研究 smoke 测试的执行时间，以便提高测试效率。

**后续行动计划**：

- Kiran 将分享 Rock Orchestrator 部署经验。
- David Galloway 将介绍 Jenkins 环境设置。
- 尝试将 smoke 测试集成到 Jenkins 中。
- 研究在 OpenStack 上进行部署测试的方法。
- 优化测试流程，提高测试效率。

**备注**：

- 会议中涉及部分计算机科学/ceph相关领域英文原文的关键词，如：Rock Orchestrator、Jenkins、smoke 测试、OpenStack、Alfredo、David Galloway、PR、CI/CD、虚拟机等。