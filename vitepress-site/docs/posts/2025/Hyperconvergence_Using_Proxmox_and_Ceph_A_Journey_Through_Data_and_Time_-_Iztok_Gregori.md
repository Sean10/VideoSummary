---
title: "Hyperconvergence Using Proxmox and Ceph; A Journey Through Data and Time - Iztok Gregori"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
在本次会议中，Linux系统管理员和Proxmox及Ceph用户Iztok Gregori分享了他在使用了Proxmox和Ceph进行超融合存储方面的实践经验。

**主要议题**：

1. **Hyper Convergence介绍**：Hyper Convergence是一种将虚拟化、存储和网络集成在单一节点上的软件定义基础设施，通过多个节点的集群化运行，实现高可用性和易于管理。
2. **Proxmox和Ceph的结合**：Proxmox作为虚拟化平台，支持KVM虚拟机和LXC容器，而Ceph作为存储系统，支持对象存储、块存储和文件系统存储，具备高可用性和扩展性。
3. **Elettra的Ceph集群实践**：Elettra是一个多学科研究中心，位于意大利，使用Proxmox和Ceph构建了超融合集群，用于存储科学数据和企业应用程序。
4. **遇到的问题和解决方案**：在实践过程中，遇到了Zimbra与Ceph不兼容、虚拟机性能问题和网络问题等。通过将Zimbra迁移到RBD存储、升级硬件和优化网络配置等手段解决了这些问题。
5. **未来计划**：计划升级硬件、部署独立的Ceph RGW集群，并继续优化硬件和网络配置。

**关键细节**：

- Elettra的Ceph集群从最初的8节点扩展到16节点，并增加了SSD存储。
- 遇到的网络问题是主要挑战，建议将Proxmox和Ceph网络隔离。
- 为Ceph预留足够的资源，避免过度分配给虚拟化。
- Proxmox的API可以与其他工具集成，但目前没有实现多租户的资源配额管理。

通过本次分享，Iztok Gregori强调了Hyper Convergence的优势，同时也指出了实施过程中可能遇到的挑战和解决方案。