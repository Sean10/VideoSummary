---
categories:
- 视频总结
date: 2019-02-22
subtitle: 2019-02-11_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 分布式存储
- 自动化
- 云计算
title: "'2019-02-11 :: Ceph Orchestration Meeting'"
updated: 2019-02-23
---



本次会议主要讨论了Ceph项目的多个重要议题，包括会议纪要损坏、设备清单刷新、Cats实现、库存过滤器标签、添加/删除主机、Rook问题和OpenShift安装器。

**会议纪要损坏问题**： 上次会议的会议纪要由于多人同时编辑而损坏，现已恢复。

**设备清单刷新**： 讨论了在Rook和DeepSea等 orchestrator 中触发设备清单刷新的问题，决定提供一个刷新标志，但不会在Rook或DeepSea中实现缓存。

**Cats实现**： 讨论了为所有 orchestrator 实现Cats（缓存）的可行性，决定将Cats作为一个服务实现。

**库存过滤器标签**： 讨论了是否应该在库存过滤器中使用标签，决定将标签保留在orchestrator中，但不会在通用接口中使用。

**添加/删除主机**： 讨论了是否应该在orchestrator接口中保留添加/删除主机的功能，决定保留该功能。

**Rook问题**： 讨论了Rook在创建OSD时出现的问题，Sebastian Han正在调查这个问题。

**OpenShift安装器**： 讨论了使用OpenShift安装器部署Ceph的问题，决定调查使用Ansible Runner Service的Ansible实现。

会议还制定了相应的行动计划，包括调查Rook创建OSD时的问题、探索使用Ansible Runner Service的Ansible实现，以及确定下次面对面会议的时间和地点。