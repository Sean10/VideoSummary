---
title: "Ceph Orchestrator Meeting 2021-04-20"
date: 2021-04-20
updated: 2021-04-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了与Ceph分布式存储系统相关的多个议题，包括Ceph部署、Ganesha NFS服务配置、以及NVMe over Fabrics的实现细节。会议还涉及了后续行动计划和一些技术决策。

#### 主要议题

1. **Ceph部署与Ganesha NFS服务配置**
   - 讨论了如何优化Ganesha NFS服务的部署，特别是在Ceph环境中。
   - 决定使用Ceph的调度机制来管理Ganesha服务的重启和故障转移，而不是依赖于Peoplesoft ID。
   - 提出了通过Ingress服务和HAProxy来管理NFS服务的IP地址和负载均衡，以确保服务的高可用性和性能。

2. **NVMe over Fabrics的实现**
   - 讨论了如何在SPDK（Storage Performance Development Kit）中实现NVMe over Fabrics的命名空间掩码功能。
   - 展示了如何在SPDK中通过RPC调用来动态附加和分离控制器到命名空间，以及如何处理活动和非活动命名空间ID。
   - 提出了将SPDK的命名空间掩码功能与Ceph的访问控制机制集成，以便更好地管理权限和安全性。

3. **Ceph部署中的密钥管理**
   - 讨论了在Ceph部署中如何管理密钥环，特别是在Ganesha配置中。
   - 决定在短期内继续使用现有的密钥环部署方式，但未来将修改Ganesha以支持在配置中明确指定密钥，从而避免物理部署密钥环文件。

4. **Ceph客户端配置管理**
   - 讨论了如何管理Ceph客户端的配置文件（ceph.conf），特别是在集群中的客户端节点上。
   - 提出了通过Ceph的管理工具来动态更新客户端节点的配置文件，以确保客户端能够正确访问Ceph集群。

#### 决定事项

- 使用Ceph的调度机制来管理Ganesha NFS服务的重启和故障转移。
- 通过Ingress服务和HAProxy来管理NFS服务的IP地址和负载均衡。
- 在短期内继续使用现有的密钥环部署方式，未来将修改Ganesha以支持在配置中明确指定密钥。
- 通过Ceph的管理工具动态更新客户端节点的配置文件。

#### 后续行动计划

- 继续优化Ganesha NFS服务的部署和管理，确保服务的高可用性和性能。
- 在SPDK中实现并测试NVMe over Fabrics的命名空间掩码功能，并考虑与Ceph的访问控制机制集成。
- 修改Ganesha以支持在配置中明确指定密钥，避免物理部署密钥环文件。
- 开发Ceph管理工具，动态更新客户端节点的配置文件，确保客户端能够正确访问Ceph集群。

#### 其他事项

- 需要进一步讨论和测试HAProxy的配置，确保在服务故障转移时客户端不会被重定向到错误的节点。
- 需要与Ganesha开发团队讨论，确保Ganesha服务的配置和管理符合Ceph的最佳实践。

#### 结论

本次会议涵盖了多个与Ceph分布式存储系统相关的重要议题，并制定了具体的行动计划。团队将继续优化Ceph和Ganesha的集成，确保系统的高可用性、性能和安全性。