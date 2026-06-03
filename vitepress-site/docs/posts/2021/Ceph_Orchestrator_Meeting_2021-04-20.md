---
title: "Ceph Orchestrator Meeting 2021-04-20"
date: 2021-04-20
updated: 2021-04-21
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议概述
本次Ceph Orchestrator会议主要围绕Ceph分布式存储系统的部署、管理和优化展开，讨论了多个关键议题，包括Ganesha NFS服务配置、NVMe over Fabrics的实现、密钥管理以及客户端配置管理等。

#### 主要议题

1. **Ceph部署与Ganesha NFS服务配置**
   - 讨论了如何优化Ganesha NFS服务的部署，特别是在Ceph环境中。
   - 决定使用Ceph的调度机制来管理Ganesha服务的重启和故障转移。
   - 提出了通过Ingress服务和HAProxy来管理NFS服务的IP地址和负载均衡。

2. **NVMe over Fabrics的实现**
   - 讨论了在SPDK中实现NVMe over Fabrics的命名空间掩码功能。
   - 展示了如何在SPDK中通过RPC调用来动态附加和分离控制器到命名空间。
   - 提出了将SPDK的命名空间掩码功能与Ceph的访问控制机制集成。

3. **Ceph部署中的密钥管理**
   - 讨论了在Ceph部署中如何管理密钥环。
   - 决定在短期内继续使用现有的密钥环部署方式，但未来将修改Ganesha以支持在配置中明确指定密钥。

4. **Ceph客户端配置管理**
   - 讨论了如何管理Ceph客户端的配置文件（ceph.conf）。
   - 提出了通过Ceph的管理工具来动态更新客户端节点的配置文件。

#### 决定事项

- 使用Ceph的调度机制来管理Ganesha NFS服务的重启和故障转移。
- 通过Ingress服务和HAProxy来管理NFS服务的IP地址和负载均衡。
- 在短期内继续使用现有的密钥环部署方式，未来将修改Ganesha以支持在配置中明确指定密钥。
- 通过Ceph的管理工具动态更新客户端节点的配置文件。

#### 后续行动计划

- 继续优化Ganesha NFS服务的部署和管理。
- 在SPDK中实现并测试NVMe over Fabrics的命名空间掩码功能。
- 修改Ganesha以支持在配置中明确指定密钥。
- 开发Ceph管理工具，动态更新客户端节点的配置文件。

#### 其他事项

- 需要进一步讨论和测试HAProxy的配置。
- 需要与Ganesha开发团队讨论，确保Ganesha服务的配置和管理符合Ceph的最佳实践。

#### 结论
本次会议针对Ceph分布式存储系统的多个关键议题进行了深入的讨论，并制定了具体的行动计划，旨在优化Ceph的部署、管理和性能。