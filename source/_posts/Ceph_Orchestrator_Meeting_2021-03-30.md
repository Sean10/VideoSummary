---
title: "Ceph Orchestrator Meeting 2021-03-30"
date: 2021-03-30
updated: 2021-03-31
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议主要讨论了Ceph存储系统的几个关键议题，包括网络配置、虚拟IP服务、NFS服务的配置和管理，以及Ceph Dashboard的发展路线图。会议还涉及了Ceph与Rook集成的具体问题，以及如何优化NFS和RGW服务的部署和管理。

#### 主要议题

1. **网络配置与管理**
   - 讨论了如何通过修改网络列表来确保子网配置的正确性，并探讨了`list networks`命令与`gather facts`命令的功能重叠问题。
   - 决定将这两个功能合并，以简化管理和避免重复。

2. **虚拟IP服务（VIP）**
   - 讨论了VIP服务在NFS服务中的应用，特别是在NFS守护进程重启或迁移时的IP地址管理问题。
   - 提出了通过扩展放置规范（placement spec）来简化VIP服务的配置和管理。

3. **NFS服务配置**
   - 讨论了NFS服务的配置问题，特别是RGW块在NFS配置中的必要性和如何与Rook集成。
   - 决定将RGW配置提升到 orchestrator 层，以便于统一管理和避免在Rook和Cephadm中的重复配置。

4. **Ceph Dashboard发展**
   - 讨论了Ceph Dashboard的发展路线图，特别是在即将到来的CDS会议中的讨论安排。
   - 强调了Dashboard与Orchestrator以及其他组件的同步和集成需求。

#### 决定事项

- 合并`list networks`和`gather facts`命令的功能。
- 扩展VIP服务的放置规范，以简化其配置和管理。
- 将RGW配置提升到 orchestrator 层，以统一管理和避免重复。
- 在即将到来的CDS会议中安排关于Ceph Dashboard的讨论。

#### 后续行动计划

- 实施`list networks`和`gather facts`命令的合并。
- 开发和测试VIP服务的扩展放置规范。
- 在 orchestrator 层实现RGW配置的管理。
- 准备在CDS会议中关于Ceph Dashboard的讨论材料。

#### 其他讨论点

- 讨论了NVMF（NVMe over Fabrics）的管理层和子系统与命名空间模型的选择。
- 讨论了Ceph与Rook在NFS服务配置上的差异和集成问题。

本次会议为Ceph存储系统的未来发展方向和具体实施细节提供了明确的指导和决策。