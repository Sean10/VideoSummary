---
title: The SMB Report Card - John Mulligan, IBM
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 存储
categories: 
- "视频总结"
subtitle: The_SMB_Report_Card_-_John_Mulligan_IBM
---

John Mulligan（IBM）在会议上介绍了IBM团队在Ceph项目中集成SMB（Server Message Block）支持的最新进展。SMB是一种广泛用于Windows系统的文件共享协议，支持Windows、macOS和Linux。团队的主要目标是提供一个使用Ceph原生工具的SMB集成方案，并通过Ceph的orchestration层实现一致的部署和管理。

### 会议内容概述

* **SMB在Ceph中的集成**：讨论了将SMB支持集成到Ceph中，特别是CephFS（Ceph File System），并提供与现有Ceph工具（如Cephadm）的无缝集成。
* **现有工作与挑战**：过去已有用户通过Samba在Ceph上运行SMB，但缺乏统一的文档和最佳实践。团队决定重新激活VFS CephFS模块，并与其他上游项目（如Samba和Kubernetes）合作，以改进SMB在Ceph中的集成。
* **开发进展**：开发了一个新的SMB管理模块，类似于现有的NFS模块，提供CLI命令和未来可能的Dashboard集成。支持Active Directory集成，并提供声明式和命令式两种管理方式。
* **演示展示**：John进行了一个演示，展示了如何在Ceph上创建SMB集群和共享，并通过Windows和Linux客户端进行访问。
* **未来计划**：短期计划包括添加Dashboard支持、优化性能和扩展Active Directory配置支持。长期计划包括支持并发SMB和NFS在同一子卷上运行、改进CephFS VFS模块等。

### 决定事项

* 团队将继续完善SMB在Ceph中的集成，特别是通过Cephadm的orchestration层提供更简化的管理体验。
* 未来将添加Dashboard支持，并优化性能以应对Samba的内存密集型操作。

### 后续行动计划

* 鼓励社区用户测试并反馈SMB集成功能，提交bug报告和功能请求。
* 团队将继续与Samba和Kubernetes等上游项目合作，改进Ceph的SMB支持。

### 相关标签

- Ceph
- SMB
- Storage
- Linux
- File System