---
title: "It’s Alive! Image Live Migration, Live Import and Instant Restore with Ceph RBD - Danny Harnik, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph分布式存储中的图像实时迁移、导入和即时恢复

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 参会人员：来自IBM研究（Haifa, Israel）的研发团队成员，包括发言人及其同事Effie。

#### 会议内容总结：

1. **图像实时迁移（Image Live Migration）简介**
   - 功能自Nautilus版本开始引入，最初用于同一集群内不同存储池之间的图像迁移。
   - 在Pacific版本中扩展到外部源，支持从外部源实时迁移图像到Ceph集群。

2. **支持的客户端类型**
   - 仅支持Librbd，不支持krbd。适用于OpenStack、KVM虚拟化、NBD RBD及NVMe over Fabrics。

3. **图像实时迁移的工作原理**
   - 采用后复制迁移（post-copy migration）技术，允许在数据迁移过程中立即在目标端开始工作。
   - 写操作直接指向目标端，读操作初始指向目标端，若数据不存在则从源端获取。

4. **主要应用场景**
   - **集群间实时迁移**：适用于拥有多个Ceph集群的部署，支持跨集群的实时数据迁移和负载均衡。
   - **即时导入到Ceph**：允许从外部源（如NAS设备）快速导入图像到Ceph，实现即时使用。
   - **备份与即时恢复**：通过差异备份和即时恢复功能，实现高效的备份和快速的数据恢复。

5. **新功能介绍**
   - **外部NBD源的实时迁移**：新增NBD格式支持，通过chemo NBD服务器连接，实现更灵活的图像导入。
   - **备份与即时恢复的POC**：使用qcow2格式进行差异备份，并通过chemo NBD实现即时恢复。

6. **未来计划与改进方向**
   - 推动现有PR上线的进程。
   - 探索对克隆图像的集群间迁移支持。
   - 改进备份与恢复流程，特别是增加对Ceph原生导出格式的索引支持，以实现更高效的即时恢复。

#### 决定事项：
- 继续推动图像实时迁移功能的开发和优化。
- 完善文档和教程，确保用户能够充分利用新功能。

#### 后续行动计划：
- 完成并上线相关PR。
- 开发和测试对克隆图像的集群间迁移支持。
- 研究和实施对Ceph原生导出格式的索引支持，以优化备份与恢复流程。

#### 会议结束：
- 会议在提问和讨论环节后圆满结束，发言人感谢所有参与者的积极参与和反馈。

---

**备注**：本次会议详细讨论了Ceph分布式存储中的图像实时迁移、导入和即时恢复功能，强调了其在多集群部署和数据备份恢复中的重要性，并提出了未来的改进方向和行动计划。