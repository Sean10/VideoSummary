---
title: "Getting Started as a Rook-Ceph Developer - Blaine Gardner, SUSE"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
  - "Rook"
  - "Kubernetes"
  - "存储"
categories:
  - "视频总结"
outline: deep
---
本次会议记录了SUSE企业存储部门的Blaine Gardner关于如何成为一名Rook-Ceph开发者的入门指导。以下是会议的主要内容和讨论要点：

**Rook 简介**：
Rook是一个用于在Kubernetes上创建、部署和管理存储集群的框架。它通过使用Kubernetes API和自定义资源定义（CRD）来实现其功能，旨在简化Ceph存储系统与Kubernetes的集成。

**Rook 架构**：
Rook采用Operator模式，其中Operator是一个运行在Kubernetes上的应用程序，用于管理Ceph集群。其主要组件包括Rook Operator（管理Ceph集群的生命周期）、CRD（定义Ceph集群的配置和数据）、Pod（运行Ceph服务的容器）、Config Map和Secret（存储配置信息和敏感信息）以及DaemonSet（在Kubernetes节点上运行特定的服务）。

**Rook 开发**：
开发Rook需要熟悉Kubernetes、容器化和Ceph。开发者可以使用MiniCube或其他Kubernetes集成测试环境来测试Rook。Rook提供了单元测试和集成测试，以确保代码质量。开发者可以通过GitHub和Slack等平台与其他开发者进行交流。

**社区参与**：
Ceph社区日历提供了上游协调和社区活动的信息。Rook社区活跃，开发者可以通过GitHub、Slack等平台与其他开发者进行交流。

**讨论的主要议题**：
* Rook的架构和功能
* Rook开发的流程
* 社区参与的方式

**决定的事项**：
* 鼓励开发者参与Rook社区
* 提供Rook开发资源和支持

**后续行动计划**：
* Sebastian Vogner将介绍Rook Orchestrator的开发环境
* Travis Neilson将介绍Rook的测试环境
* Blaine Gardner将回答关于Rook的问题

会议中，Blaine Gardner详细介绍了Rook的架构，包括Ceph集群的部署、Monitor、OSD、MDS以及Gateway等组件的创建和配置。他还分享了Rook的代码结构和测试环境，以及如何使用Rook进行开发。最后，他强调了社区参与的重要性，并鼓励开发者积极参与Rook社区。