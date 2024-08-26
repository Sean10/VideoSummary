---
title: "Ceph CSI Driver: Bridging Containers and Ceph - Rakshith R & Yati Padia, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题
讨论关于Ceph CSI（Container Storage Interface）的集成和使用，以及其在容器编排中的应用。

#### 与会人员
- **Rakshita**：IBM工程师，有两年半的Ceph CSI、Rook和Ceph开发经验。
- **Yati**：Ceph CSI团队成员，曾任职于Red Hat，现为IBM员工。

#### 会议议程
1. **简介**
2. **容器和容器编排**
3. **容器存储驱动（CSI）介绍**
4. **Ceph CSI及其主要功能**
5. **CSI附加功能**
6. **Ceph CSI的未来路线图**
7. **问答环节**

#### 主要讨论内容

##### 容器和容器编排
- **容器**：标准化的软件单元，包含所有依赖和所需资源，可在任何Linux机器上运行，具有便携性、轻量级和安全性。
- **容器编排**：管理容器的部署、扩展、内存调度等，常见平台包括Kubernetes、Docker Swarm、Apache Mesos等。

##### 容器存储接口（CSI）
- **CSI**：解决原生存储驱动的问题，提供gRPC协议，定义API供编排器管理存储资源，支持动态配置、挂载、卸载等操作。
- **Ceph CSI**：专门为Ceph存储系统设计的CSI驱动，作为CSI编排器和Ceph集群之间的桥梁。

##### Ceph CSI驱动
- **RBD驱动**：高性能块设备，支持快照、复制和强一致性。
- **CephFS驱动**：POSIX兼容文件系统，支持多客户端同时访问。
- **NFS驱动**：基于CephFS的NFS导出，支持外部客户端访问。

##### CSI附加功能
- **空间回收**：执行RBD擦除和文件系统空间释放命令。
- **网络隔离**：在节点丢失或灾难恢复场景中，阻止特定IP范围访问存储资源。
- **卷复制**：支持卷的复制和状态切换，适用于区域灾难恢复。

##### 未来路线图
- **密钥轮换**：支持加密卷的密钥轮换。
- **浅层NFS卷**：实现NFS卷的浅层克隆。
- **Kerberos认证**：为NFS卷提供Kerberos认证。
- **卷组快照**：同时对多个卷进行快照。
- **卷组复制**：支持卷组的复制。
- **存储容量跟踪**：让Kubernetes了解Ceph集群的存储容量。

#### 决定事项
- **Ceph CSI**将继续开发和优化，以支持更多的存储操作和提高性能。
- **CSI附加功能**将进一步扩展，以满足更复杂的存储管理需求。

#### 后续行动计划
- 继续开发和测试Ceph CSI的新功能。
- 与Kubernetes社区合作，确保CSI驱动的兼容性和稳定性。
- 定期更新文档和用户指南，以便用户更好地理解和使用Ceph CSI。

#### 问答环节
- **RBD卷的挂载和卸载**：在文件系统模式下，RBD驱动使用`makefs`创建文件系统并挂载到工作负载。
- **外部依赖**：Ceph CSI直接与Kubernetes交互，不依赖OpenStack层或类似的中间层。
- **CSI附加功能的声明性**：CSI附加功能通过CRD（Custom Resource Definitions）实现声明性管理。

#### 参考资料
- 会议中提到的相关链接和文档将在后续提供。

#### 结束语
感谢所有与会者的参与和讨论，期待Ceph CSI的进一步发展和应用。

[掌声]