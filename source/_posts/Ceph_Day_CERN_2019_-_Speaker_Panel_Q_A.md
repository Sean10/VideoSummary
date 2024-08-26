---
title: "Ceph Day CERN 2019: Speaker Panel Q/A"
date: 2020-08-25
updated: 2020-08-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph存储系统的功能讨论与用户反馈

#### 参会人员：Ceph专家、CSC代表Peter Reverend、Ceph集群操作员等

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 主要议题及讨论内容：

1. **Ceph Dashboard支持多CRUSH规则的问题**
   - 讨论了Ceph Dashboard是否支持多CRUSH规则（multiple CRUSH rules）。
   - 确认可以在Ceph Dashboard中修改池属性，但不确定是否可以直接在Dashboard中创建新的CRUSH规则。
   - 提到Ceph团队正在不断更新和优化Dashboard的基本功能。

2. **Safe Day Nordic活动信息**
   - Peter Reverend询问Safe Day Nordic活动的举办地点。
   - 确认活动将在挪威、瑞典、冰岛、芬兰等地举行，预计在11月底。

3. **Ceph集群的Telemetry功能启用情况**
   - 调查了参会者中Ceph集群是否启用了Telemetry功能。
   - 讨论了启用Telemetry的顾虑和问题，包括数据隐私和网络安全。
   - 提到Telemetry数据目前被发送到上游Ceph实验室的机器，存储在PostgreSQL数据库中，只有少数开发人员有权访问。
   - 强调Telemetry数据不包含敏感信息，未来可能会有摘要报告发送给相关人员。

4. **CephFS的多站点使用情况**
   - 讨论了CephFS在多站点环境中的使用情况。
   - 提到Ceph目前没有专门的多站点特性，但可以通过扩展RADOS集群来实现。
   - 强调在多站点环境中，需要特别注意网络链接的质量和服务的实时性。

5. **Ceph集群的运行和配置问题**
   - 讨论了Ceph集群的运行情况和配置问题，包括启用Telemetry功能的具体操作和配置HTTP代理的可能性。

#### 决定事项：

- 确认Ceph Dashboard支持多CRUSH规则的修改，但创建新规则的功能尚不确定。
- 确认Safe Day Nordic活动的举办地点和时间。
- 讨论了Telemetry功能的启用情况和相关顾虑，强调数据安全和隐私保护。
- 讨论了CephFS在多站点环境中的使用和注意事项。

#### 后续行动计划：

- 进一步确认Ceph Dashboard中创建新CRUSH规则的功能，并更新相关文档。
- 继续优化Telemetry功能，解决用户的顾虑，并确保数据安全和隐私保护。
- 提供更多关于CephFS多站点使用的指导和最佳实践。
- 更新和完善Ceph相关文档，包括Telemetry功能的详细说明和配置指南。

#### 备注：

- 会议中提到的关键词和术语包括Ceph Dashboard、CRUSH rules、Telemetry、CephFS、RADOS cluster等。
- 会议记录了参会者的反馈和建议，为Ceph的进一步开发和优化提供了重要参考。