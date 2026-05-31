---
title: Ceph SMB  Opening Windows to the Ceph World
date: 2025-06-24
updated: 2025-06-24
tags:
- CephFS
categories: 
- "视频总结"
subtitle: Ceph_SMB_Opening_Windows_to_the_Ceph_World
---

### 会议纪要：Ceph SMB 集成与管理模块开发讨论

#### 1. 会议基本信息
- **主讲人**：Sachin Prabu（IBM 软件开发者，原 Red Hat SMB/Samba 团队成员）
- **主题**：通过 SMB 协议集成 CephFS（Opening Windows to the Ceph World）
- **背景**：
  - CephFS 通过 Samba 提供 SMB（Server Message Block）协议支持，实现跨平台文件共享。
  - 目标是简化 CephFS 通过 SMB 导出的流程，并解决旧版 VFS 模块的维护问题。

#### 2. 关键讨论内容
##### 2.1 现有架构与改进
- **旧版问题**：手动配置复杂，文档分散，部分 VFS 模块已无人维护。
- **新版改进**：
  - 引入 `vfs_cephfs` 模块，基于 `libcephfs` 底层驱动，替代旧模块。
  - 新增 SMB Manager Module，通过声明式（YAML/JSON）或命令式（CLI）管理集群和共享。

##### 2.2 核心组件
- **Orchestration 流程**：包括 Init Containers 和 Sidecar Containers（如 SMBD、CTDB、Winbind、Prometheus）。
- **Proxy 服务**：解决 Samba 多进程连接导致的内存问题，通过代理集中管理 `libcephfs` 连接。

##### 2.3 功能演示（Demo）
- **场景**：创建两个集群：用户认证集群和 Active Directory 集群。
- **操作命令示例**：`ceph smb cluster create starter --user-auth --placement=label:first` 和 `ceph smb share create starter share1 --fs-volume=cephfs/demos/subvol1`。

##### 2.4 新功能与未来计划
- **已实现功能**：Case Insensitivity、快照支持、多通道传输。
- **未来计划**：QoS 限制、离线域加入、多协议支持（早期阶段）。

#### 3. 决策与行动计划
- **短期行动**：完善 IO 统计并集成到 Dashboard，开发 gRPC 接口提升管理模块扩展性。
- **长期规划**：探索 Multi-protocol Support 的可行性。

#### 4. 问答环节
- **安全问题**：已修复 CLI 中密码明文显示的问题。
- **测试工具**：使用 `smbclient` 进行基础验证，但生产环境需结合 AD 或加密认证。

#### 5. 参会人员反馈
- 演示获得积极反响，团队将持续优化 SMB 与 CephFS 的集成体验。

#### 6. 后续跟进
- Sachin Prabu 将通过邮件提供进一步支持。