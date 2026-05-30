---
categories:
- 视频总结
date: 2024-08-23
subtitle: Unlocking_Ceph_s_Potential_with_NVMe_oF_Integration_Ceph_Days_London_2024
tags:
- Ceph
- NVMe
- oF
- 存储优化
- 分布式存储
- 云计算
title: "Unlocking Ceph's Potential with NVMe oF Integration | Ceph Days London 2024"
updated: 2024-08-24
---




### 改进后的会议纪要

**会议主题**： Ceph与NVMe-oF集成潜力探讨

**参会人员**： NVMe-oF项目成员、Ceph研发人员等

**会议内容**：

**一、NVMe-oF 介绍**

* NVMe-oF是一种基于网络协议的存储访问方式，允许通过网络访问本地NVMe设备，具有高性能、低延迟和可扩展性等优点。
* NVMe-oF支持多种网络协议（如TCP、iSCSI、RoCE）和NVMe设备（如NVMe SSD、NVMe-oF Target），并提供多种访问控制方式（如ACL、RBAC）。

**二、NVMe-oF的进展**

* NVMe-oF已取得显著进展，包括支持多种网络协议、NVMe设备和访问控制方式。
* NVMe-oF在网络传输中可以充分利用高速网络带宽，提高访问速度，并降低延迟。

**三、NVMe-oF的优势**

* 相比传统NVMe，NVMe-oF提供更高性能、更低延迟和更好可扩展性。
* NVMe-oF易于使用硬件加速器进行卸载，减轻CPU负担。

**四、NVMe-oF的应用场景**

* NVMe-oF适用于数据中心存储、分布式存储和云计算领域。

**五、Ceph与NVMe-oF的集成**

* Ceph已集成NVMe-oF，支持NVMe连接、命名空间管理、访问控制和数据传输。
* Ceph使用SPDK框架实现NVMe-oF，并支持NVMe连接和断开连接等功能。
* Ceph支持NVMe-oF的发现服务，允许自动连接到所有目标。

**六、高可用性**

* Ceph使用网关组实现高可用性，支持至少两个网关部署，并支持故障转移和故障恢复。
* 网关组中的所有网关读取相同的配置文件，并自动负载均衡命名空间。

**七、后续行动计划**

* 集成NVMe-oF CLI到Ceph主CLI中。
* 支持NVMe-oF In-Band消息通知。
* 支持子系统级别的访问控制。
* 支持名称空间屏蔽功能。
* 支持更广泛的网络协议和设备。
* 提高性能和可扩展性。

**八、讨论要点**

* NVMe-oF的网络协议支持和设备支持。
* NVMe-oF的访问控制方式。
* NVMe-oF的性能优化方法。

**九、会议总结**

NVMe-oF项目取得了显著进展，Ceph与NVMe-oF的集成为用户提供更好的存储服务。未来将继续优化NVMe-oF的性能和可扩展性，并支持更广泛的网络协议和设备。