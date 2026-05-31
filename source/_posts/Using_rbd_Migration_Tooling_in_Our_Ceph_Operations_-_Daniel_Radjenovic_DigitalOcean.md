---
title: Using rbd Migration Tooling in Our Ceph Operations - Daniel Radjenovic, DigitalOcean
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 分布式存储
categories: 
- "视频总结"
subtitle: Using_rbd_Migration_Tooling_in_Our_Ceph_Operations_-_Daniel_Radjenovic_DigitalOcean
---

### **Ceph RBD迁移工具链实践分享**

#### **会议主题**
DigitalOcean存储系统团队（Daniel、Matt、Tyler、Shawn）分享了他们在Ceph集群间进行RBD镜像迁移的实用工具链，包括Gantry、Elvos和Seale的设计背景、功能以及未来优化方向。



#### **1. 背景与原因**
团队选择部署多个小型Ceph集群而非单一大型集群，原因如下：
1. **故障域控制**：维护或升级时，仅影响部分客户，快速升级。
2. **成本与扩展性**：新区域成本低，填充后直接新增集群而非扩容。
3. **文件描述符限制**：多集群减少hypervisor的文件描述符压力。
4. **风险缓解**：新集群可从干净状态启动，逐步淘汰旧集群。



#### **2. 迁移工具介绍**
#### (1) Gantry
- **功能**：基于RBD mirroring，实现非在线RBD镜像迁移。
- **流程**：设置集群间replication peers，同步数据至目标集群，Promote/Demote操作后禁用mirroring。
- **优点**：快速、支持snapshots同步。
- **局限**：迁移需关闭VM，影响客户体验。

#### (2) Elvos
- **功能**：支持在线迁移（VM无需停机）。
- **技术**：基于QEMU block jobs，实时同步数据至目标集群。
- **流程**：创建目标集群的RBD镜像，发起QEMU block job，检测convergence后切换VM至目标镜像。
- **挑战**：引入额外latency，需进一步优化。

#### (3) Seale
- **功能**：自动化迁移决策工具。
- **场景**：检测集群fill level，提议批量迁移，一键清空旧集群。
- **优势**：替代手动管理TXT文件，通过Slack交互式审批流程。



#### **3. 工具链对比**
| 工具    | 适用场景               | 核心技术          | 关键优势                  |  
|||-||  
| Gantry  | 非在线 **RBD** 迁移    | RBD mirroring     | 快速、支持快照            |  
| Elvos   | 在线 **VM-attached** 迁移 | QEMU block jobs   | 无需停机                  |  
| Seale   | 自动化迁移决策         | 集群监控+调度     | 简化批量操作              |  



#### **4. 后续行动计划**
1. **优化Elvos**：降低迁移对客户latency的影响。
2. **分层存储支持**：开发工具支持客户数据在不同storage tier间迁移。
3. **持续自动化**：增强Seale的智能调度能力。



### **总结**
DigitalOcean团队通过Gantry、Elvos和Seale的迭代，实现了从手动到自动化、离线和在线迁移的全覆盖，显著提升了Ceph集群管理的灵活性与效率。未来将聚焦性能优化和分层存储支持，进一步强化分布式存储的运维能力。