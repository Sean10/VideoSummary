---
title: A Harbor-side Chat on CephFS - Patrick Donnelly, IBM
date: 2025-11-19
updated: 2025-11-20
tags:
- CephFS
- 分布式存储
- 存储集群
- 高可用性
categories: 
- "视频总结"
subtitle: A_Harbor-side_Chat_on_CephFS_-_Patrick_Donnelly_IBM
---

### **CephFS 社区会议纪要：CephFS 最新进展与讨论**

#### **会议概览**
- **主持人**：Patrick Donnelly（前 CephFS 团队负责人，自 2016 年起参与 Ceph 项目）
- **主题**：介绍 Tentacle 和 Umbrella 版本的 CephFS 新功能，并开放讨论社区问题。
- **形式**：技术分享 + 自由问答。



#### **关键内容总结**

#### **1. Tentacle 版本新功能**
- **Case Insensitive Subtree 支持**：为目录树设置大小写不敏感，优化 Samba 在 CephFS 上的性能。
- **File Block Diff API**：对比文件快照间的数据块差异，优化备份效率。
- **可观测性增强**：包括 MDS Journal Replay 进度监控和数据 Scan 进度显示。
- **灾难恢复优化**：新增配置项禁用 Subvol 删除，记录 MDS Map 的创建时间。

#### **2. Umbrella 版本新功能**
- **Per-Subvol Metrics**：通过 Prometheus 或 Admin Socket 监控每个 Subvol 的 IO 指标。
- **用户态 FScrypt 支持**：兼容 Samba/NFS Ganesha，元数据和数据均加密。



#### **开放讨论重点**

- **性能与运维问题**：包括 CephFS Fuse 与 Kernel Driver 性能对比、Data Scan Cleanup 卡顿、MDS Journal Trimming 延迟等。
- **架构与设计**：讨论 MDS Cache/Journals/Metadata Pool 关系、快照备份负载隔离等。
- **升级与灾难恢复**：探讨 MDS 升级策略和文件系统布局修改。



#### **行动计划**
- **问题跟踪**：提交 Data Scan Cleanup 卡顿问题至 Tracker，收集 CephFS Fuse vs Kernel 性能数据。
- **功能优化**：研究客户端 Cap 释放策略对 Journal Trimming 的影响，评估快照 MDS 隔离的可行性。
- **文档补充**：完善 MDS Cache/Journal 交互文档。



#### **后续会议推荐**
- **CephFS 运维实战**：Anthony Yetri 分享灾难恢复案例。
- **Per-Subvol Metrics 深度解析**：Egor/Eyore 演讲。



#### **会议总结**
本次会议重点介绍了 CephFS 的最新进展，特别是 CephFS 的 Tentacle 和 Umbrella 版本的新功能。与会者就性能优化、架构设计、升级与灾难恢复等议题展开了深入讨论，并制定了后续行动计划。