---
title: " 2018-NOV-07 :: Ceph Developer Monthly "
date: 2018-11-14
updated: 2018-11-15
tags:
- Ceph
- 分布式存储
- 编排
- RBD
categories:
- "视频总结"
subtitle: 2018-NOV-07_-_-_Ceph_Developer_Monthly
---

在本次 Ceph 开发者月度会议上，讨论了多个关键议题，包括 orchestrator、Anible、RBD 缓存、持久性缓存和 Orchestrator/Messenger 的进展。

**主要讨论内容**：

* **深海 orchestrator 模块和 Anible**：讨论了两者相似的方法和轨迹，以及如何使用 libstorage management 控制闪烁灯，以及设备状态跟踪和健康警报。
* **Ceph OSD 删除器代码**：Mina 更新了代码进展，包括单元测试和文档，并建议进行性能测试。
* **RBD 共享缓存**：Yen 更新了缓存架构、工作流程和性能测试结果，讨论了缓存容量配置、缓存空间管理策略和与集群配置的集成。
* **RBD 持久性缓存**：Jason 更新了代码架构、性能目标和挑战，讨论了一致性、性能和可扩展性，以及如何与 SSD 集成。
* **Orchestrator 和 Messenger**：讨论了协议 V2 的实现、地址端点管理和加密，以及如何与现有 Ceph 版本兼容。

**行动计划**：

* 完成深海 orchestrator 模块和 Anible 的开发。
* 对 Ceph OSD 删除器代码进行性能测试。
* 完成 RBD 共享缓存和 RBD 持久性缓存的开发。
* 加快 Orchestrator 和 Messenger 的开发。
* 完成协议 V2 的实现和加密功能。

**其他事项**：

* 讨论了集群连接性监控和 RDMA 连接问题。
* 讨论了 Ceph 代码的可维护性和可扩展性。

本次会议反映了 Ceph 社区在分布式存储技术方面的不断进步和创新能力。