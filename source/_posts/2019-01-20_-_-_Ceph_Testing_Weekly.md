---
categories:
- 视频总结
date: 2019-02-03
subtitle: 2019-01-20_-_-_Ceph_Testing_Weekly
tags:
- Ceph
- 测试
- 分布式存储
title: "'2019-01-20 :: Ceph Testing Weekly'"
updated: 2019-02-03
---




### 会议纪要

**会议时间**： 2019年1月20日

**会议地点**： [未提供]

**参会人员**： Sebastian, Richard, Jessica, Tim, Dan等

**会议主题**： Ceph存储系统开发、测试和部署相关讨论

**关键细节**：

* **Ceph存储系统开发**：
    * 讨论了Ceph存储系统接口开发的进度，由于一些意外情况，进度有所延迟。
    * 讨论了使用“calc option”和“dry run”等选项简化测试流程的方法。
    * 讨论了在Ceph集群中运行多个make test命令的可能性，以及如何确保它们在相同的环境中产生相同的输出。
* **Ceph测试**：
    * 讨论了验证Ceph Orchestrator功能的方法，以确保其正常运行。
    * 讨论了为Orchestrator编写测试用例，以及如何与其他组件进行集成。
    * 讨论了解决Orchestrator与Rook之间集成问题。
* **Ceph部署**：
    * 讨论了使用Rook将Ceph集群部署到Kubernetes或OpenShift等平台。
    * 讨论了使用Ansible或其他工具进行Ceph集群的部署和配置。

**主要议题**：

* Ceph存储系统接口开发进度
* Ceph测试用例编写和验证
* Ceph集群部署和配置

**决定的事项**：

* 继续推进Ceph存储系统接口开发。
* 编写和验证Ceph测试用例。
* 探索使用Rook将Ceph集群部署到Kubernetes或OpenShift等平台。

**后续行动计划**：

* Sebastian将继续推进Ceph存储系统接口开发。
* Richard将负责编写和验证Ceph测试用例。
* Tim将探索使用Rook将Ceph集群部署到Kubernetes或OpenShift等平台。

**其他事项**：

* 讨论了OVH云服务的一些变化，以及它们对Ceph集群部署的影响。
* 讨论了Ceph社区的一些活动，以及如何吸引更多开发者参与。
* 讨论了Ceph Orchestrator与Rook集成的问题，以及如何进行测试和验证。
* 讨论了Ceph集群在OVH云服务上的部署问题，包括虚拟化限制和网络配置。
* 讨论了Ceph与其他存储平台的集成，如Kubernetes和OpenShift。