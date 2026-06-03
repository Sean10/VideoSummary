---
title: "Q and A Panel"
date: 2025-06-23
updated: 2025-06-24
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

本次Ceph社区会议主要围绕Ceph分布式存储系统的最新进展、性能优化、文档改进、版本支持策略等方面进行了深入讨论。以下是对会议内容的详细总结：

## 会议概述

本次会议邀请了多位核心开发者参与，包括Bill、Jose等，他们分享了技术更新，并回答了社区成员的提问。

## 主要讨论议题

### 1. 性能优化与Crimson/EC整合
- **Crimson与EC的协同开发**：Crimson将直接使用Fast EC路径，避免重复开发，并将在未来全面支持EC。
- **NVMe与RBD的优化**：计划优化SPDK与RBD的集成，避免重复计算CRC，并探索librados线程与SPDK reactors的协同运行。

### 2. 文件系统与存储协议
- **SMB/NFS的并发访问问题**：目前SMB和NFS的锁机制不互通，导致跨协议访问冲突，社区正在讨论解决方案。
- **CephFS新VFS模块性能测试**：团队正在虚拟机和物理机环境进行基准测试，后续将公布性能对比数据。

### 3. 文档与用户体验改进
- **文档不足的问题**：社区成员反馈Ceph文档存在版本差异，BlueStore的性能计数器缺乏解释，团队鼓励用户通过GitHub Issue或Slack提交具体问题。
- **mclock调度器的优化**：`mclock`旨在简化参数配置，但初期实现存在硬编码问题，未来将提供更多灵活性。

### 4. Ceph Dashboard与存储浏览器
- **存储浏览器功能开发**：计划在Ceph Dashboard中集成对象存储浏览器，支持上传/删除对象。

### 5. 版本支持策略
- **长期支持（LTS）版本的缺失**：Ceph目前仅支持N-2版本，版本重叠期较短，未来目标：恢复春季/夏季发布周期。

## 关键决策与行动计划

1. **Crimson与EC的整合**：确保Fast EC路径在Crimson中稳定运行，并同步性能优化。
2. **NVMe/RBD优化**：测试SPDK与RBD的CRC计算优化方案。
3. **文档改进**：针对`mclock`、BlueStore计数器等补充文档。
4. **Ceph Dashboard存储浏览器**：推进自主开发的Angular集成方案。
5. **版本发布节奏调整**：缩短开发周期，确保"Umbrella"版本按时发布。

## 后续行动

- 社区成员可通过GitHub/Slack提交具体问题。
- 性能测试结果将在完成后公开。
- 下一次会议将讨论SMB/NFS锁机制的可行性方案。

## 关键词保留

Ceph、CRUSH、Crimson、EC、RBD、SPDK、BlueStore、mclock、PG、OSD、librados、libcephfs、cephfs、rbd、radosgw、RGW、RESTful API、authentication、authorization、encryption、erasure coding、replication、snapshots、clones、thin provisioning、iSCSI、Fibre Channel、NFS、CIFS、POSIX、monitoring、dashboard、management、orchestration、automation、integration、containerization、Kubernetes、Docker、virtualization、cloud computing、AWS、Azure、Google Cloud、hybrid cloud、multi-cloud、storage cluster、node、disk、SSD、HDD、JBOD、SAN、NAS、network、topology、failure domain、recovery、resilience、load balancing、caching、compression、deduplication、tiering、performance tuning、benchmarking、testing、validation