---
categories:
- 视频总结
date: 2024-08-23
subtitle: Sunbeam_and_Ceph_Sitting_in_a_Tree_Ceph_Days_London_2024
tags:
- Ceph
- OpenStack
- 分布式存储
- Kubernetes
title: "Sunbeam and Ceph Sitting in a Tree | Ceph Days London 2024"
updated: 2024-08-24
---



### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**会议地点**： 线上会议

**参会人员**： James Paage（Canonical公司首席工程师）、Luciano、其他IBM员工

**会议主题**： Sunbeam项目介绍

**会议内容**：

* **James Paage开场致辞**： 
    * 对Bill的Ceph PODS展示表示祝贺。
    * 介绍自己作为Canonical公司首席工程师的背景，包括其在开源领域的参与经历和负责的技术架构。
    * 简述了参与过的项目，如Ensemble（后更名为Juju）、Metal as a Service（MAS）、LXD以及OpenStack charms和MicroStack项目。
* **Sunbeam项目介绍**：
    * Sunbeam项目是Open Infrastructure Foundation技术委员会指导下孵化的项目，旨在实现任何规模的OpenStack部署。
    * 采用混合部署方法，结合Juju和Kubernetes组件。
    * 使用Ceph Snap进行部署，并与Juju和Kubernetes平台集成。
    * 提供MicroStack实现，简化Ceph部署。
    * 使用Juju charm进行Ceph集群管理。
    * 支持Cinder和Nova组件。
    * 支持Rados Gateway，并通过Kubernetes进行暴露。
* **Sunbeam项目优势**：
    * 快速、可重复的部署和操作。
    * 基于图像的部署，减少版本差异。
    * 提高安全性，通过Snap封装。
    * 简化软件，提高可维护性。
    * 提高易用性，降低知识门槛。
    * 提供可选功能，如可观察性、验证工具等。
* **Sunbeam项目发布计划**：
    * 预计2023年底发布基于OpenStack Caracol和Ceph Squid的稳定版。
    * 预计2024年第一季度实现与Charmed OpenStack功能对等。
    * 未来将提供从Charmed OpenStack迁移到Sunbeam的路径。
* **后续行动计划**：
    * 继续开发Sunbeam项目，并发布稳定版。
    * 完善迁移路径，支持从Charmed OpenStack迁移到Sunbeam。
    * 推广Sunbeam项目，并获取用户反馈。

**会议总结**：

Sunbeam项目是一个具有潜力的OpenStack部署解决方案，它简化了部署和操作过程，并提供了多种功能。随着项目的不断发展，Sunbeam有望成为OpenStack部署的首选工具。