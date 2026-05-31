---
title: Ceph NVMe-of Road Map - Orit Wasserman & Aviv Caro, IBM
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 高可用性
- 分布式存储
categories: 
- "视频总结"
subtitle: Ceph_NVMe-of_Road_Map_-_Orit_Wasserman_Aviv_Caro_IBM
---

本次会议主要讨论了Ceph NVMe over TCP Gateway的路线图，包括架构、高可用性、当前状态和未来功能。以下是对会议内容的详细总结：

**会议要点**：

1. **NVMe over TCP Gateway的概念与术语**：
   - Namespace：类似于Ceph中的RBD镜像。
   - NVMe Subsystem：主机连接的实体，包含多个Namespace和控制器，通过NQN标识。
   - NVMe IO Controller：主机连接时创建的控制器，每个主机连接对应一个控制器。

2. **Gateway架构与高可用性**：
   - 多Gateway支持：支持在同一个Ceph集群中部署多个Gateway，实现负载均衡和高可用性。
   - Gateway Group：一组共享相同配置的Gateway，主机连接到所有Gateway实现多路径和故障切换。
   - 高可用性实现：使用NVMe-oF ANAGRP协议，每个Gateway负责一个ANAGRP，故障时自动切换。

3. **当前状态与技术预览**：
   - Ceph Riff和Squid：技术预览阶段。
   - Ceph Tentacle：生产就绪，代码已合并到Ceph主分支。

4. **路线图与未来功能**：
   - 高可用性：至少需要两个Gateway部署在同一集群中，使用Ceph Mon监控Gateway状态。
   - 负载均衡与自动重平衡：计划在Tentacle版本中实现自动重平衡。
   - CLI集成：将CLI集成到Ceph CLI中，简化操作。
   - Dashboard支持：在Tentacle版本中，用户可以通过Ceph Dashboard管理Gateway。

5. **性能与扩展性**：
   - 性能测试：使用SPDK实现了较高的IOPS，但需要优化资源分配。
   - 扩展性：当前支持4个Gateway Group，未来计划扩展到8个；支持128个子系统，未来计划扩展到256个。

6. **安全性**：
   - 加密与认证：支持NVMe-oF的TLS加密和CHAP认证，未来将增加Namespace级别的访问控制。
   - MTLS：管理API使用MTLS加密通信。

7. **VMware支持**：
   - VMware vSphere：支持基本的vSphere API，未来将扩展支持更多的VMware存储管理API。

8. **性能优化与未来方向**：
   - SPDK优化：减少线程和内存使用，优化Ceph context分配。
   - 硬件加速：计划使用Intel DSA等硬件加速器来提升性能。

**决定事项与后续行动计划**：

1. 高可用性与负载均衡：在Tentacle版本中实现自动重平衡，并优化Gateway的资源分配。
2. CLI与Dashboard集成：将NVMe over TCP Gateway的CLI集成到Ceph CLI中，并在Dashboard中增加相关功能。
3. 性能优化：继续优化SPDK和Ceph的资源使用，减少CPU占用，提升整体性能。
4. 安全性增强：在Tentacle版本中增加Namespace级别的访问控制，并优化加密与认证机制。

本次会议详细讨论了NVMe over TCP Gateway的架构、高可用性实现、当前状态以及未来的路线图。重点介绍了高可用性、负载均衡、性能优化和安全性等方面的进展与计划。未来工作将集中在性能优化、自动化管理以及安全性增强上。