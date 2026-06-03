---
title: "Ceph RGW Refactoring Meeting 2025-09-10"
date: 2025-09-10
updated: 2025-09-15
tags:
  - "Ceph"
  - "分布式存储"
  - "RGW"
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
### **Ceph 社区会议纪要 - 版本规划讨论**

#### **会议概览**
本次会议主要围绕 Ceph Umbrella 版本的规划进行讨论，涵盖了多个关键功能的开发进度、优先级和未来计划。会议重点关注了 D4N、DDUP、快照、S3 功能增强等核心议题，并明确了部分功能的预期交付时间。

#### **关键讨论议题**

#### **1. D4N（分布式数据驱动网络）**
- **当前状态**：Pria 正在进行性能优化工作，预计这些改进将包含在 Umbrella 版本中。
- **下一步计划**：实现分布式缓存，这是下一个重要的 MVP。
- **进展**：目前仅支持单节点缓存，未来将扩展为分布式架构。

#### **2. DDUP（去重）**
- **最新进展**：Full DDUP PR 已提交并处于测试阶段，预计很快合并。Rate Limiting 功能也已开发完成，待文档审核后合并。Small Object Dedup 正在开发中，预计会在 Umbrella 版本中提供。
- **用户收益**：功能可同时显示标准对象去重和小对象去重的节省空间，帮助用户评估是否启用小对象去重。

#### **3. 快照**
- **现状**：目前无人全职负责，代码需 rebase 并修复单元测试，需进行回归测试，确保不影响版本控制功能。
- **潜在价值**：快照不仅适用于备份场景，还可能支持其他用例。

#### **4. 有序桶列表**
- **进展**：Eric 和 Matt 正在推进，但目前缺乏公开的设计文档或代码更新。

#### **5. 客户管理策略**
- **状态**：Pritha 和 Raja 正在开发相关 API，进展顺利，预计可按时交付。

#### **6. AWS 组织 API**
- **计划**：扩展 Account Quota 和 Service Control Policies 功能，支持多级账户管理，目前处于设计阶段。

#### **7. S3 Vectors**
- **现状**：仍处于设计阶段，目标是在后续版本中提供基础 API。

#### **8. 桶日志**
- **新增功能**：Nitia 正在开发 EC Pools 支持，需改为异步刷新临时日志，预计在 New 版本中落地。

#### **其他重要讨论**

#### **OMAP Data Logs 弃用**
- 社区提议在 Umbrella 版本中标记 OMAP Data Logs 为弃用，为用户提供迁移时间。

#### **版本发布计划**
- **Tentacle RC1** 已发布，正在收集用户反馈，可能需进一步修复后再发布正式版。
- **Umbrella 版本优先级**：确定包含 D4N 优化、Full DDUP、Small Object Dedup。待定：快照、有序桶列表。排除：S3 Vectors、Host Offload。

#### **社区协作建议**
- 通过 EtherPad 或邮件列表公开功能规划，鼓励更多开发者参与讨论和贡献。

#### **后续行动计划**
- **D4N**：Pria 完成性能优化后提交代码。
- **DDUP**：合并 Full DDUP 和 Rate Limiting PR，推进 Small Object Dedup 开发。
- **快照**：寻找开发者负责 rebase 和测试。
- **有序桶列表**：联系 Eric/Matt 获取进展更新。
- **OMAP 弃用**：发布公告并更新文档。
- **社区沟通**：将功能列表通过邮件公开，征求社区意见。

#### **保留关键词（中英对照）**
- Ceph, distributed storage, CRUSH algorithm, OSD, RADOS, PG, replication, erasure coding (EC), snapshots, versioning, S3 API, bucket logging, deduplication (DDUP), performance tuning.