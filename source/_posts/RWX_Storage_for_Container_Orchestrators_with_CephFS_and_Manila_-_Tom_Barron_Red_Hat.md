---
categories:
- 视频总结
date: 2019-05-24
subtitle: RWX_Storage_for_Container_Orchestrators_with_CephFS_and_Manila_-_Tom_Barron_Red_Hat
tags:
- CephFS
- Kubernetes
title: "RWX Storage for Container Orchestrators with CephFS and Manila - Tom Barron, Red Hat"
updated: 2019-05-24
---




### 会议纪要

**会议时间**： 2019年5月24日

**会议地点**： [请填写会议地点]

**参会人员**： Tom Barron（红帽下游项目Kim团队负责人）、Robert Vacek（CERN实习生）、James Blair等

**会议主题**： OpenStack Manila与容器编排的集成，特别是针对Ceph文件系统（CephFS）的读写多故事（WX）存储。

**会议内容**：

1. **背景介绍**：
    - Tom Barron介绍了自己的背景和目前的工作，包括作为红帽下游项目Kim团队负责人的角色。
    - 突出了OpenStack Manila在提供可扩展存储基础设施、选择自由和多云租户方面的优势。

2. **OpenStack与容器编排**：
    - 讨论了OpenStack和Kubernetes等容器编排工具之间的差异，以及如何为应用开发者提供更便捷的基础设施服务。
    - 指出应用开发者使用OpenStack时需要具备一定的系统管理员技能。

3. **WX存储**：
    - Tom介绍了Kubernetes中的WX存储概念，即读写多故事存储，允许多个应用程序同时写入同一个文件系统。
    - 强调了CephFS在实现WX存储方面的优势，并讨论了CephFS与Kubernetes CSI接口的集成。

4. **Manila与CephFS**：
    - 介绍了Manila如何支持CephFS，包括通过NFS前端和本地接口。
    - 讨论了即将到来的Manila CSI工作，以及如何将更多功能暴露给容器编排工具。

5. **后续行动计划**：
    - CERN的Robert Vacek正在开发Manila CSI插件，红帽团队将进行集成测试和验证。
    - 计划使用Ansible playbook在OpenStack环境中部署Manila和CephFS。
    - 探索在Kubernetes环境中运行Ceph和Ganesha服务。

**决定事项**：

- 红帽团队将继续推动Manila CSI插件的开发和集成。
- 与CERN合作，进行集成测试和验证。
- 探索在Kubernetes环境中运行Ceph和Ganesha服务。

**后续行动**：

- 红帽团队将发布Ansible playbook，以便用户可以在OpenStack环境中部署Manila和CephFS。
- 与其他感兴趣的开发者合作，共同推动Manila和CephFS的发展。

**备注**：

- 会议中还讨论了CephFS的快照支持、存储扩展和拓扑感知等。
- 会议纪要中保留了计算机科学/CEPH领域英文原文的关键词，以保持原文的专业性。