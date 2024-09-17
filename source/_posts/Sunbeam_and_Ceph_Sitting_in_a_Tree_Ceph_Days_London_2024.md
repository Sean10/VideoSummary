---
title: "Sunbeam and Ceph Sitting in a Tree | Ceph Days London 2024"
date: 2024-08-23
updated: 2024-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**会议地点**： 线上会议

**参会人员**： James Paage（Canonical公司首席工程师）、Luciano、其他IBM员工

**会议主题**： Sunbeam项目介绍

**会议内容**：

* **James Paage开场致辞**： 
    * 对Bill的Ceph PODS展示表示祝贺。
    * 介绍自己，作为Canonical公司首席工程师，负责OpenStack Ceph和OVN团队的技术架构师。
    * 简述了自2010年加入Canonical以来在开源领域的参与经历，包括参与Eucalyptus和OpenStack项目。
    * 介绍了Ensemble项目（后更名为Juju），用于部署和操作分布式系统。
    * 介绍了Metal as a Service（MAS）和LXD项目，用于容器化OpenStack组件。
    * 介绍了OpenStack charms项目，用于部署和配置OpenStack。
    * 介绍了MicroStack项目，用于简化OpenStack部署。
    * 介绍了Ceph Snap，用于简化Ceph部署。
* **Sunbeam项目介绍**：
    * Sunbeam项目是一个在Open Infrastructure Foundation技术委员会指导下孵化的项目，旨在实现任何规模（从个人电脑到多数据中心）的OpenStack部署。
    * Sunbeam项目采用混合部署方法，结合了Juju和Kubernetes组件。
    * Sunbeam项目使用Ceph Snap进行部署，并与Juju和Kubernetes平台集成。
    * Sunbeam项目提供了MicroStack实现，用于简化Ceph部署。
    * Sunbeam项目使用Juju charm进行Ceph集群管理。
    * Sunbeam项目支持Cinder和Nova组件。
    * Sunbeam项目支持Rados Gateway，并通过Kubernetes进行暴露。
* **Sunbeam项目优势**：
    * 快速、可重复的部署和操作。
    * 基于图像的部署，减少版本差异。
    * 提高安全性，通过Snap封装。
    * 简化软件，提高可维护性。
    * 提高易用性，降低知识门槛。
    * 提高可观察性和透明度。
    * 提供可选功能，如可观察性、验证工具等。
* **Sunbeam项目发布计划**：
    * 预计2023年底发布基于OpenStack Caracol和Ceph Squid的稳定版。
    * 预计2024年第一季度实现与Charmed OpenStack功能对等。
    * 未来将提供从Charmed OpenStack迁移到Sunbeam的路径。

**后续行动计划**：

* 继续开发Sunbeam项目，并发布稳定版。
* 完善迁移路径，支持从Charmed OpenStack迁移到Sunbeam。
* 推广Sunbeam项目，并获取用户反馈。

**会议总结**：

Sunbeam项目是一个具有潜力的OpenStack部署解决方案，它简化了部署和操作过程，并提供了多种功能。随着项目的不断发展，Sunbeam有望成为OpenStack部署的首选工具。