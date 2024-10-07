---
title: "Ceph Month 2021: 5 more ways to break your ceph cluster"
date: 2021-06-14
updated: 2021-06-15
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议由Vito，421的创始人，主持，主题为“破坏你的Ceph集群的五种新方法及一个额外提示”。会议回顾了Vito几年前关于“破坏Ceph集群的十种方法”的演讲，并分享了新的研究成果和经验教训。

#### 讨论的主要议题
1. **自动化工具的误用**：
   - 案例分析：自动化脚本未正确检查监控器数量，导致监控器被错误移除，包括监控数据库，造成严重停机。
   - 教训：自动化工具的使用需谨慎，确保所有必要的检查和配置都已正确设置。

2. **监控器的重要性误解**：
   - 案例分析：用户错误地认为监控器可以随意移除和重新创建，导致系统监控功能受损。
   - 教训：监控器在Ceph集群中扮演关键角色，不应随意操作。

3. **配置错误**：
   - 案例分析：集群配置中的最小副本数设置不当，导致数据恢复困难或数据丢失。
   - 教训：建议始终使用至少三个副本以确保数据安全。

4. **升级不完全**：
   - 案例分析：未完全遵循升级指南进行升级，导致集群在一段时间后出现问题。
   - 教训：升级过程中应严格遵循官方指南，确保所有步骤都已完成。

5. **过早完成升级**：
   - 案例分析：在未完全升级所有守护进程的情况下，启用增强安全设置，导致服务连接问题。
   - 教训：升级应确保所有相关组件都已更新到最新状态。

6. **PG自动缩放器的盲目信任**：
   - 案例分析：集群在数据量增加后，PG自动缩放器错误地增加了放置组，导致数据错位。
   - 教训：应谨慎使用PG自动缩放器，并监控其行为以避免数据管理问题。

#### 决定的事项
- 强调了自动化工具、监控器管理、配置设置、升级过程和PG自动缩放器使用的重要性。
- 提醒用户应持续关注和学习Ceph的最佳实践和更新，以避免潜在的风险。

#### 后续行动计划
- 用户应重新评估和优化其Ceph集群的管理和配置，确保遵循最佳实践。
- 定期进行培训和知识更新，以提高对Ceph集群管理的理解和技能。

#### 会议结束
会议在讨论和解答与会者的疑问后结束，强调了持续学习和实践的重要性，以确保Ceph集群的稳定和高效运行。