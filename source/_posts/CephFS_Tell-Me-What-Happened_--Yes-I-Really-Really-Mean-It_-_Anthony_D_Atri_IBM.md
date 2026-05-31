---
title: CephFS Tell-Me-What-Happened --Yes-I-Really-Really-Mean-It - Anthony DAtri, IBM
date: 2025-11-19
updated: 2025-11-20
tags:
- CephFS
categories: 
- "视频总结"
subtitle: CephFS_Tell-Me-What-Happened_--Yes-I-Really-Really-Mean-It_-_Anthony_D_Atri_IBM
---

### **CephFS 审计日志需求讨论会议纪要**

#### **会议基本信息**

- **主持人**: Anthony Dri（IBM Ceph 支持团队成员，Ceph Ambassador）
- **缺席人员**: Daria、Veni Shanker（IBM Ceph 团队成员，原定主讲人）
- **会议主题**: Ceph 文件系统（CephFS）审计日志的需求与开发进展



#### **主要讨论内容**

1. **CephFS 调试挑战**
   - CephFS 调试面临困难，包括复杂的状态变更和操作追溯困难。
   - 命令执行顺序和完成状态对故障排查至关重要。

2. **现有问题诊断流程**
   - 通过 Ceph 用户邮件列表提交问题，但信息可能不完整。
   - 需要关键数据，如命令列表、MDS 状态、MDS map 历史、文件系统恢复记录和 Perf dump 数据。

3. **CephFS 审计日志方案（Audit Log）**
   - 记录所有命令的时序执行历史，包含命令、时间、状态和返回值。
   - 基于 SQLite 数据库，存储于 `.audit` RADOS pool。
   - 暂命名为 `auditman`，处于开发中，预计随 Ceph U 版本（代号 "Umbrella"）发布。

4. **Q&A 环节**
   - 目前为技术预览状态，建议关注上游 PR 或联系开发团队。
   - 当前优先级是 Tentacle 版本发布，审计日志功能将在之后推进。



#### **后续行动计划**

1. **开发跟踪**
   - 关注 Ceph 上游 PR 和 Umbrella 版本的合并进展。

2. **用户建议**
   - 使用终端日志工具记录操作历史。

3. **社区协作**
   - 通过邮件列表持续反馈需求，参与测试审计日志功能。



#### **关键词保留（Ceph 术语**）

- **核心组件**: CephFS, MDS, RADOS, Perf dump, disaster recovery
- **技术概念**: retention policy, backfill, SQLite, structured log, failover
- **版本计划**: Umbrella (U release), Tentacle

**会议结束时间**: [未记录具体时间]
**参会人员**: Ceph 社区成员、开发团队、存储工程师



**备注**: 本纪要基于 Anthony Dri 代汇报内容整理，部分技术细节需以最终代码实现为准。