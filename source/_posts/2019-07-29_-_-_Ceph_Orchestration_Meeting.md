---
categories:
- 视频总结
date: 2019-07-30
subtitle: 2019-07-29_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 分布式存储
- 编排
- CRUSH算法
title: "'2019-07-29 :: Ceph Orchestration Meeting'"
updated: 2019-07-31
---



**会议纪要**

**会议时间**： 2019年7月29日

**参会人员**： [请填写参会人员名单]

**会议主题**：

本次会议主要讨论了Ceph集群的运维、管理和优化问题，包括客户端库更新、Orchestrator队列管理、Rook模块的启用配置、CRD验证等多个议题。

**会议内容**：

1. **客户端库更新**：
   - 指出Sentra 7芯片上的Cumulative Client Python库版本过旧，无法满足Ceph客户端的最低要求。
   - 讨论了将Python库打包成RPM包并在CentOS 7上安装的方案，以解决依赖问题。
   - 期望CentOS团队能够将更新回滚到CentOS 7，以便用户能够使用最新版本的客户端。

2. **Orchestrator队列管理**：
   - 讨论了Orchestrator队列中任务挂起的问题，如果任务因任何原因挂起，目前没有其他方法清除队列，除非重启Manager。
   - 提出了添加一个安全Orchestrator文本层的想法，以便在需要时安全地清除队列。

3. **Rook模块的启用配置**：
   - 讨论了Rook中Manager模块的启用配置问题，目前Rook只能自动启用某些模块，没有提供用户自定义模块的选项。
   - 提出了在Rook CR中添加一个通用设置，以指示是否启用特定模块的方案。
   - 讨论了是否应该自动启用PG自动缩放器，以及是否应该将此功能设置为默认启用。

4. **CRD验证**：
   - 讨论了CRD验证的更新，包括对集群、存储池和文件系统的验证。
   - 讨论了将两个PR合并的建议，因为它们之间存在冲突。

5. **其他议题**：
   - 讨论了基于PVC的OSD创建、LVM配置和Rook的其他功能。

**后续行动计划**：

- 完成Python库的RPM包打包和安装。
- 实现Orchestrator队列的安全清除功能。
- 更新Rook模块的启用配置。
- 完成CRD验证的更新。
- 继续推进Rook的其他功能开发。

**备注**：

- 会议中提到了SSH Orchestrator，但被推迟到下周讨论。

**总结**：

本次会议讨论了Ceph集群的多个关键议题，并制定了后续的行动计划。会议内容涵盖了客户端库更新、Orchestrator队列管理、Rook模块的启用配置、CRD验证等多个方面，对于Ceph集群的运维和管理具有重要意义。