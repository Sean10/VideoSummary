---
title: "2020-02-05 :: Ceph Developer Monthly"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期与时间**: [具体日期]
- **参与者**: Liam, Josh, 及其他相关人员
- **主要议题**: Ceph项目的状态更新、功能开发进展、监控系统改进、自动化部署及未来计划

#### 讨论内容
1. **状态更新**
   - 目前主要进行的是一些小的修复和改进，包括监控系统的进展，如添加节点导出器和Prometheus的工作正在进行中。
   - 部署FSS（File System Storage）的工作也在进行中，但还有一些紧急问题需要解决，特别是在 orchestrator 模块中。

2. **监控系统改进**
   - 讨论了关于如何处理主机和主机名的模糊性问题，提出了一个方案来确保主机名的一致性，以便更好地集成到CRUSH map中。
   - 需要增加基于每个主机的IP或完全限定域名的能力，以便在不依赖DNS的情况下进行通信。

3. **自动化部署**
   - 讨论了关于Ansible playbook的使用，用于自动化Ceph集群的部署和转换过程。
   - 强调了在监控方面和故障处理方面仍存在的主要差距。

4. **功能开发进展**
   - 讨论了NFS网关的开发状态，目前仍在进行中，但尚未有人关注rgw NFS网关。
   - 密码更改功能即将完成，正在进行最后的QA测试。

5. **未来计划**
   - 计划在接下来的一个月内推动用户启用telemetry模块，目标是达到500或1000个活跃的集群。
   - 讨论了关于cephalic的在线会议计划，建议分块进行，以便更有效地讨论各个议题。

#### 决定事项
- 确认了Ceph集群的监控和自动化部署的改进方向。
- 确定了密码更改功能的最终测试和部署计划。
- 计划推动用户启用telemetry模块，并设定了具体的目标。

#### 后续行动计划
- 继续推进监控系统和自动化部署的改进工作。
- 完成密码更改功能的QA测试并部署。
- 推动用户启用telemetry模块，并通过邮件列表和社交媒体进行宣传。
- 安排cephalic的在线会议，分块讨论各个议题。

#### 其他
- 讨论了关于Ceph客户端版本和功能比特的命名问题，建议未来不再使用命名版本，而是直接使用功能比特来标识支持的功能。

会议结束时，所有参与者对未来的工作计划表示了肯定，并期待下一次的在线会议。