---
categories:
- 视频总结
date: 2022-06-01
subtitle: Ceph_User_+_Dev_Monthly_2022-06-01
tags:
- Ceph
- 分布式存储
- 算法
- PG Remapper
- Ceph Dashboard
title: "Ceph User + Dev Monthly 2022-06-01"
updated: 2022-06-01
---




本次Ceph用户及开发者月度会议主要围绕Ceph分布式存储系统的优化与管理展开，由Joshua Bergen和Pedro两位专家分享了他们的研究成果和实践经验。

**主要内容包括**：

1. **Joshua Bergen的演讲：PG Remapper工具介绍**
   - Joshua Bergen介绍了他们开发的PG Remapper工具，该工具旨在解决Ceph集群中回填（backfill）相关的问题，如回填并发、源过载、等待恢复和降级回填等。
   - PG Remapper通过控制upmap异常表来管理回填，提供了诸如drain、cancel backfill、undo upmaps等命令，以优化回填过程，避免降级状态。
   - 提出了改进Ceph代码库的建议，如改进回填并发管理、增加回填源的预订机制等。

2. **Pedro的演讲：Ceph Dashboard的新功能**
   - Pedro展示了Ceph Dashboard中新增的文件系统、卷组和子卷管理功能，包括创建、编辑和删除操作。
   - 详细演示了如何在Dashboard中进行文件系统、子卷和子卷组的管理，以及如何处理快照。
   - 计划增加快照的创建、编辑和删除功能，以及改进快照的列表显示，同时考虑实现镜像管理功能。

**讨论与反馈**：

- 讨论了PG Remapper与Ceph内部平衡器的集成问题，以及如何避免在回填过程中出现OSD过载的情况。
- 提到了Ceph的版本更新计划，包括即将发布的17.2.7版本和后续的18.2.1及16.2.15版本，并呼吁社区成员对Pacific版本的PR进行关注和测试。

**后续行动计划**：

- 鼓励社区成员在Ceph的Upstream Slack频道和用户邮件列表中提供反馈和讨论。
- 建议社区成员关注并参与即将发布的Ceph版本的测试和PR审核。

本次会议通过两位专家的详细介绍和演示，展示了Ceph在存储管理和优化方面的新工具和新功能，同时也强调了社区参与和版本更新的重要性。