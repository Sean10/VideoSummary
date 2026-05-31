---
title: Ceph-CSI- The Engine Behind Persistent Storage in Kubernetes - Niels de Vos & Madhu Rajanna
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- Kubernetes
- 存储
- 云计算
categories: 
- "视频总结"
subtitle: Ceph-CSI_-_The_Engine_Behind_Persistent_Storage_in_Kubernetes_-_Niels_de_Vos_Madhu_Rajanna
---

Ceph-CSI项目是Kubernetes持久存储的重要驱动力量，本次会议由IBM的Niels de Vos和Madhu Rajanna主持，深入探讨了Ceph CSI及其生态系统组件的技术。

### 会议核心内容

#### 1. Ceph CSI基础架构
- **CSI规范**：定义了容器存储接口标准，提供基础存储操作，如volume创建/删除和snapshotting等。
- **Kubernetes集成**：通过PV与CSI volume的映射，用户通过PVC申请存储资源。

#### 2. Ceph CSI支持的后端存储
- **CephFS**：多节点共享文件系统，支持读写多（RWX）。
- **RBD**：块存储，支持虚拟机live migration，支持读写一次（RWO）。
- **NFS**：网络文件系统，兼容传统NFS场景。

#### 3. 关键功能特性
- **标准CSI功能**：volume创建/删除、容量扩展、快照管理、volume group snapshot、RBD Changed Block Tracking。
- **非标准扩展功能**：topology-based provisioning、静态数据加密、CSI add-ons的实验性功能。

#### 4. Ceph CSI Operator
- **设计目标**：统一部署方式，减少维护负担，保持配置简洁性。
- **CRD设计**：OperatorConfig、Driver、CephConnection、ClientProfile。

#### 5. CSI Add-ons项目
- **设计理念**：扩展CSI规范外的存储功能，提供通用框架供其他存储供应商使用。
- **核心功能**：密钥轮换、网络隔离、空间回收、卷复制、卷状态报告。

#### 未来路线图
- NVMe-oF支持
- Operator增强
- 存储功能扩展

#### 行动项
- 用户迁移
- 功能推广
- 社区协作

#### Q&A重点
- 网络隔离在跨集群场景的应用价值
- 密钥轮换的安全实践
- Volume Group复制的一致性保障
- 与Kubernetes原生功能的集成深度

本次会议全面展示了Ceph CSI生态系统的最新进展，特别是在操作简化和功能扩展方面的创新，为Kubernetes上的Ceph存储管理提供了企业级解决方案。