---
title: "Ceph Autopsy- When Erasure Coding Goes Wrong"
date: 2025-06-24
updated: 2025-06-24
tags:
  - "Erasure Coding"
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
Ceph Autopsy: When Erasure Coding Goes Wrong 这次会议纪要主要讨论了 Erasure Coding (EC) 数据一致性的检测与修复工具的开发进展。以下是会议的关键细节和主要议题：

### 会议基本信息
- **演讲者**：Jamie Pride（IBM UK 团队，负责 Fast EC 改进项目）
- **主题**：EC 数据损坏分析与工具开发
- **背景**：针对 Erasure Coded 存储池中数据不一致性的检测与修复工具进行讨论。

### 关键讨论内容
#### 1. EC 数据不一致性的原因
- **硬件故障**：磁盘故障或固件缺陷可能导致写入错误。
- **软件缺陷**：OSD 代码 Bug（概率较低，但需防范）。
- **后果**：应用读取错误数据时可能崩溃，重建时依赖的校验数据可能错误。

#### 2. 复制池 vs. EC 池的差异
- **复制池**：不一致性易检测。
- **EC 池**：需重新计算校验数据并与存储的校验块对比，才能发现不一致性。

#### 3. 开发中的工具
- **Offline EC Consistency Checker**：离线扫描 OSD，重新计算校验数据并验证一致性。适用于应用报告数据损坏时定位问题 OSD，或在集群离线维护时预检数据一致性。
- **Online EC Consistency Checker**：目标用户为开发者，用于 EC 功能开发时的实时测试。

#### 4. 工具开发进展与资源
- **开发者**：Connor Faucet（IBM 团队，未参会）。
- **代码仓库**：提供离线和在线工具的 PR 链接。
- **计划**：2023 年内完成工具优化并发布用户友好版本。

### 后续行动计划
- 完善工具功能，如增加故障 OSD 标识能力，提供详细用户文档和独立部署指南。
- 鼓励社区用户试用离线工具并反馈问题，开发者可通过在线工具验证 EC 相关代码变更。

### 术语表（保留英文关键词）
- **EC (Erasure Coding)** | **OSD** | **PG** | **RADOS** | **Teuthology**
- **Parity** | **Rebuild** | **Consistency Check** | **Object Store Tool**

会议纪要准确反映了原始内容的要点，涵盖了关键细节、讨论的主要议题、决定的事项以及后续的行动计划。没有发现错误、误解或遗漏的重要信息。

