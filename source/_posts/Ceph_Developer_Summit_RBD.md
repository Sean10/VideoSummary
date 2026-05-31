---
title: Ceph Developer Summit RBD
date: 2025-09-11
updated: 2025-09-11
tags:
- Ceph
- RBD
- 分布式存储
- 存储集群
categories: 
- "技术会议总结"
subtitle: Ceph_RBD_Developer_Summit
---

## Ceph Developer Summit RBD 会议纪要

### 会议概述
- **会议主题**：Ceph RBD (RADOS Block Device) 开发者峰会
- **主持人**：未具名（推测为Ceph RBD核心开发者）
- **主要议题**：讨论Umbrella发布周期中RBD的开发重点，特别是快照镜像功能（snapshot-based mirroring）的改进

### 核心讨论内容

#### 快照镜像功能
- **当前状态**：该功能尚未上游化，已有专用集成分支（非个人fork）
- **目标调整**：由于发布周期缩短，上游合并可能延后至Umbrella之后
- **关键限制**：目前组镜像仅支持"静态组"（static groups），无法在启用镜像时增减成员镜像

#### 主要开发项目
- **高优先级项目**：
  - 半动态组支持（Semi-dynamic groups）
  - 镜像API处理程序重写
  - 基于RADOS watch的通知机制
  - 引入组快照状态机制
  - 跨存储池组镜像支持
- **数据同步正确性问题**：
  - 克隆镜像同步问题
  - discard操作传播问题
- **测试工具开发**：
  - 模糊测试器（Fuzzer）开发

#### CLI改进
- **RBD disk-usage命令增强**
- **时间戳显示一致性**

#### 内核客户端
- **延续Tentacle工作**：
  - upmap读取均衡器
  - CRUSH多步重试规则

### 开放讨论
- **镜像调度时间分配**
- **强制提升（force promote）限制**
- **弃用计划**

### 后续行动计划
- **快照镜像功能**：优先实现半动态组支持，继续API处理程序重写工作，完成RADOS watch通知机制
- **同步问题修复**：解决克隆镜像同步的数据损坏问题，完善discard操作传播机制
- **工具开发**：启动模糊测试器开发，协调开发者月度会议讨论时间戳标准
- **文档与体验**：完善disk-usage命令文档，评估时间戳显示改进方案

### 未决问题
- 组快照状态机制是否归类为通用项
- 时间戳标准化方案选择

### 会议结论
Umbrella发布周期将聚焦快照镜像功能的稳定性和扩展性改进，特别是对一致性组的支持。同步问题修复和测试工具开发将显著提升功能可靠性，而CLI改进则侧重用户体验优化。