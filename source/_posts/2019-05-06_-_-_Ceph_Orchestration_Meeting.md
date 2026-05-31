---
categories:
- 视频总结
date: 2019-05-28
subtitle: 2019-05-06_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 编排
- 分布式存储
- 安全性
title: "'2019-05-06 :: Ceph Orchestration Meeting'"
updated: 2019-05-28
---



### 会议纪要

**会议时间**： 2023年（具体日期未提及）

**会议主题**： Ceph分布式存储及Orchestrator相关议题讨论

**参会人员**： 未知

**会议内容**：

**1. Ceph安全服务（Iscsi）问题**

- 讨论了上周五提交的关于Iscsi服务类型的一个bug。
- 提出了一个临时解决方案：复制管理员角色并移除Iscsi作用域，从而避免执行相关代码。
- 认为这个解决方案似乎可行，但需要进一步测试。
- 讨论了手动配置Safe Eyes CoS URL作为另一种解决方案。
- 强调了这是一个BEC（Base Exception Class）问题，需要尽快修复。

**2. Orchestrator相关**

- 讨论了关于Orchestrator合同的问题，以及如何解决冲突。
- 提出了一个建议：将所有Orchestrator请求合并到一个pull request中，以简化集成过程。
- 认为这个建议是合理的，但需要进一步讨论和测试。

**3. 其他事项**

- 讨论了Ansible Orchestrator的pull request，以及如何处理冲突。
- 讨论了将证书放入Manager的流程。
- 讨论了监控等后续工作。

**行动计划**：

- 对Iscsi服务类型的bug进行进一步测试和修复。
- 讨论、测试并实施Orchestrator pull request合并方案。
- 处理Ansible Orchestrator的pull request冲突。
- 完成证书放入Manager的流程。
- 继续进行监控等后续工作。

**后续会议**：

- 下次会议定于周三或下周召开。

**改进点**：

- 原总结中未提及Orchestrator合同的具体问题和解决方案，改进后的总结增加了这一点。
- 原总结中对于Iscsi服务类型bug的描述较为简略，改进后的总结提供了更详细的解决方案。
- 增加了后续会议的安排，使总结更加完整。