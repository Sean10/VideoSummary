---
title: Volume Shadow Copies with CephFS- A Samba-Centric Approach - Shwetha Acharya, IBM
date: 2025-01-23
updated: 2025-01-24
tags:
- CephFS
categories: 
  - "视频总结"
subtitle: Volume_Shadow_Copies_with_CephFS_-_A_Samba-Centric_Approach_-_Shwetha_Acharya_IBM
---

### 会议纪要

**会议主题**: Ceph与Samba集成中的Volume Shadow Copy Service (VSSS)

**主讲人**: Sha Aaria (IBM Ceph工程团队)

**会议内容总结**:

1. **背景介绍**:
   - **SMB与Samba**: SMB是Windows系统中用于文件共享的协议，而Linux系统通常使用NFS。Samba是一个开源项目，允许Linux系统与Windows环境集成，使Windows客户端能够访问Linux服务器上的文件。
   - **Volume Shadow Copy Service (VSSS)**: VSSS是Windows系统中的一个服务，用于创建数据的快照，以便在不影响正在进行的操作的情况下进行快速恢复和回滚。Ceph提供了类似的功能，但VSSS提供了更高效的解决方案，确保数据一致性并协调所有相关组件的交互。

2. **Ceph与VSSS的集成**:
   - **组件**: VSSS服务、VSSS请求者、VSSS写入者、VSSS提供者。Ceph在集成中扮演VSSS写入者和提供者的角色，确保数据一致性并创建快照。
   - **FSRVP协议**: VSSS使用FSRVP（File Server Remote VSS Protocol）协议在不同组件之间进行通信，支持快照的创建、删除和枚举。

3. **Samba配置**:
   - **VFS模块**: Samba中的VFS模块用于访问Ceph快照，需在Samba配置文件中启用相关模块（如VFS Ceph snapshots）。
   - **配置示例**: 提供了两种配置方式，一种是使用libcephfs库访问文件，另一种是使用内核挂载。

4. **演示**:
   - 展示了一个三节点Ceph集群的设置，如何在Linux服务器上创建快照，并通过Windows客户端访问和恢复这些快照。

5. **未来计划**:
   - 计划将VSSS功能默认支持在共享文件夹中。
   - 增加对管理模块的支持，包括NFS Ganesha和Samba的快照管理。
   - 进行更多测试和Bug修复。

6. **Q&A**:
   - 讨论了内核挂载与libcephfs的使用区别。
   - 确认当前版本的Samba已经支持VSSS功能，但尚未完全测试，不建议在生产环境中使用。

**后续行动计划**:
- 社区成员可以测试该功能并报告Bug，帮助改进VSSS与Ceph的集成。
- 未来版本将默认支持VSSS功能，并增加管理模块的支持。

**参考链接**:
- Ceph相关问题报告链接: [tracker.ceph.com](https://tracker.ceph.com)
- Bug报告链接: [bugs.samba.org](https://bugs.samba.org)

**会议结束**