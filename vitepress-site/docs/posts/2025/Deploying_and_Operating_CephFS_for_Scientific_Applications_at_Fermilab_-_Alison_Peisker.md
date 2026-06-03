---
title: "Deploying and Operating CephFS for Scientific Applications at Fermilab - Alison Peisker"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
### **Fermilab CephFS 部署与运维实践总结**

#### **1. 会议概述**
- **演讲者**: Alison Peisker（Fermilab 软件开发工程师）
- **主题**: Fermilab 如何为科学应用部署和运维 CephFS
- **背景**: Fermilab 是美国高能物理和加速器科学的领先实验室，需要处理海量实验数据。

#### **2. Fermilab 数据存储架构**
- **主要组件**: dcache（原始数据存储），磁带系统（长期存储），CephFS（交互式数据分析）
- **数据流**: 实验数据 → 数据采集系统 → dcache/磁带 → CephFS（用户分析）

#### **3. CephFS 集群选型与设计**
- **选择原因**: 开源、活跃社区、POSIX 兼容、支持快照、硬件灵活性、扩展性
- **集群规模**: Head Nodes 5个，Storage Nodes 25个，Over 500 OSDs
- **Pool 配置**: 元数据池（4副本，NVMe），数据池（3副本，NVMe；EC 4+2 HDD；EC 8+3 HDD）

#### **4. 部署与运维经验**
- **部署工具**: cephadm
- **挑战与解决方案**: 硬件故障（自动恢复），软件问题（社区修复），安全合规（自动化脚本）
- **性能调优**: 默认配置为主，调整 MDS 缓存内存限制、客户端自动驱逐

#### **5. 自动化与监控**
- **内核更新工具**: 逐节点重启，检查集群健康状态
- **配额管理**: 自定义脚本 + 配置文件，自动同步配额至监控页面
- **监控看板**: 展示各实验目录的存储使用量和配额占比

#### **6. 未来计划**
- **对象存储**: 用于科学数据
- **块存储**: 替换 dcache 的硬件 RAID 6
- **数据流扩展**: 通过 Globus/XD 工具实现跨实验室数据迁移

#### **7. 总结**
CephFS 在 Fermilab 成功替代传统 NAS，满足科学计算的扩展性和灵活性需求。通过 cephadm 简化部署，结合自动化工具降低运维成本，未来将持续探索 Ceph 的多模态存储（对象/块）在科研场景中的应用。

**关键词保留**: CephFS, POSIX, OSD, MON, MDS, EC (Erasure Coding), RADOS, PG, cephadm, kernel client, capability recall.