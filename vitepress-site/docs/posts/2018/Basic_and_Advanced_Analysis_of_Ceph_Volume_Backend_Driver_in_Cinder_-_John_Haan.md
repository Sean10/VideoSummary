---
title: "Basic and Advanced Analysis of Ceph Volume Backend Driver in Cinder - John Haan"
date: 2018-04-23
updated: 2018-04-24
tags:
  - "Ceph"
  - "分布式存储"
  - "OpenStack"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议主题
Cinder块存储服务在Model公司的应用与实践

#### 参会人员
- Jan Man（Model公司存储团队负责人）
- 其他存储领域相关人员

#### 会议内容

**1. Model公司背景介绍**
- Model公司是一家韩国游戏公司，专注于移动游戏开发和云服务。
- 自2016年起，Model公司采用基于Cinder的分布式存储环境，对游戏服务产生重大影响。

**2. Cinder块存储服务架构**
- Model公司拥有8个Cinder集群，存储约PB级数据。
- 其中，3个集群用于玩家B/D及两个区域，4个集群用于Ingress和Block存储。
- Cinder集群中，一个对象存储池作为主存储，容量利用率达到22%。

**3. Cinder块存储服务特点**
- Cinder提供多种资源管理选项，如RBD（块设备）、Cinder卷等。
- Cinder支持数据生命周期管理，包括快照、克隆等功能。
- Cinder支持快照复制，用于数据备份和灾难恢复。

**4. Cinder快照与克隆**
- Cinder支持快照和克隆功能，便于创建和管理数据副本。
- 快照基于原始数据的静态快照，克隆基于快照或原始数据的动态副本。
- Cinder支持增量快照，减少数据传输量。

**5. Cinder块存储服务的优化**
- Model公司使用不可变镜像功能，提高从镜像创建卷的性能。
- 使用图像缓存卷，减少数据传输量，提高性能。

**6. Cinder块存储服务的应用**
- Model公司在Stack Overflow应用程序中使用了Cinder块存储服务。
- Cinder块存储服务在Model公司的游戏服务和云服务中发挥着重要作用。

#### 决定事项
- 继续优化Cinder块存储服务，提高性能和可靠性。
- 探索Cinder块存储服务的更多应用场景。

#### 后续行动计划
- Model公司将密切关注Cinder块存储服务的最新动态，不断优化和改进服务。
- 与社区合作，共同推动Cinder块存储技术的发展。

#### 关键词
- Cinder块存储
- RBD
- 快照
- 克隆
- 数据生命周期
- 可变镜像
- 图像缓存
- Stack Overflow