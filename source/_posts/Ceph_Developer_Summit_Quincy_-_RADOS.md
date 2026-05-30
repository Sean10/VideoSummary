---
title: "  Ceph Developer Summit Quincy: RADOS  "
date: 2021-04-07
updated: 2021-04-07
tags:
- Ceph
- Dashboard
- Rados
- Distributed Storage
- CephFS
- RADOSGW
- Monitoring
- Automation
categories:
- "视频总结"
subtitle: Ceph_Developer_Summit_Quincy_-_RADOS
---


## 改进后的中文总结内容

本次Ceph开发者峰会Quincy会议主要讨论了Ceph分布式存储系统中的RADOS组件及其相关议题。以下是会议的主要内容和决定事项：

### 主要议题

1. **Dashboard和RADOS当前状态及下一步计划**：
   - Ernesto和Alfonso展示了Dashboard的功能和未来改进方向，强调了收集用户反馈的重要性。
   - 讨论了Dashboard中特定功能的实现，如OSD创建和过滤器的使用。

2. **Crash Telemetry面板审查**：
   - 讨论了收集和审查集群崩溃数据的机制，建议将崩溃数据审查纳入日常bug清理流程。

3. **Immutable Content优化**：
   - 讨论了在Ceph中处理不可变对象的挑战，如空间放大和枚举问题，提出了将对象打包成大容量的解决方案。

4. **Ceph Manager改进**：
   - 讨论了扩展Manager的策略，如将模块分离到不同的进程中，创建共享池以提高效率。

5. **避免集群日志消息通过Paxos**：
   - 讨论了通过Paxos存储集群日志消息的问题，提出了将日志信息重定向到Manager日志的解决方案。

6. **简化文档编写**：
   - 讨论了简化选项文档编写的必要性，提出了使用YAML文件和Python脚本自动生成文档的方案。

7. **自动化认证密钥轮换**：
   - 讨论了实现自动化密钥轮换的挑战，提出了两种可能的解决方案。

### 决定事项

- 继续收集用户对Dashboard的反馈，并根据反馈进行改进。
- 改进崩溃数据审查流程，并优化每日邮件报告。
- 探索在RGW层实现对象打包支持的可能性。
- 实施Manager模块的分离和共享池的创建。
- 重定向集群日志消息到Manager日志，以减轻Paxos的负担。
- 使用YAML文件和Python脚本自动生成选项文档。
- 研究并实现自动化密钥轮换的解决方案。

### 后续行动计划

- 继续收集和分析用户对Dashboard的反馈。
- 实施崩溃数据审查流程的改进。
- 探索并实现对象打包支持。
- 实施Manager模块的分离和共享池的创建。
- 重定向集群日志消息到Manager日志。
- 使用YAML文件和Python脚本自动生成选项文档。
- 研究并实现自动化密钥轮换的解决方案。

本次会议重点关注了Ceph分布式存储系统中RADOS组件的改进，包括Dashboard功能、崩溃数据审查、对象存储优化、Manager模块扩展、日志管理、文档编写自动化和认证密钥轮换等方面。会议提出了具体的改进方案和后续行动计划，旨在提升Ceph系统的可用性、可靠性和易用性。