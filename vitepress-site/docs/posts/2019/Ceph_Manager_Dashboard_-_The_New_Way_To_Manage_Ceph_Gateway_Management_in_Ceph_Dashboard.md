---
title: "Ceph Manager Dashboard - The New Way To Manage Ceph & Gateway Management in Ceph Dashboard"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议主题
本次会议主要介绍了Ceph存储系统的仪表盘（原名为“Safe Dashboard”）的最新功能和改进，并进行了现场演示。

#### 关键细节
- **仪表盘发展历程**：从Luminous版本引入的初始版本，经历了多个版本的发展，包括用户管理、角色配置、SSL支持、审计日志等功能。
- **新功能**：
  - 支持用户注册和角色配置，实现不同权限的用户管理。
  - SSL支持，增强仪表盘的安全性。
  - 审计日志，记录操作记录。
  - 多语言支持，目前支持6-7种语言。
  - 完善的API文档，方便开发者使用。
  - 配置管理器，在UI中修改配置。
  - 存储池管理，包括创建、删除、修改等功能。
  - RBD镜像管理，包括快照、克隆、移动到回收站等功能。
  - RGW镜像管理，配置远程节点和复制策略。
- **外部服务管理**：
  - 支持管理RGW、NFS Ganesha和iSCSI网关。
  - 通过REST API与网关进行交互，实现用户管理、存储池管理等功能。

#### 讨论的主要议题
- 仪表盘的功能和改进。
- 如何使用仪表盘管理外部服务。
- 用户反馈和改进建议。

#### 决定的事项
- 将仪表盘的功能和改进进行总结和记录。
- 邀请用户测试仪表盘，并提供反馈和建议。
- 继续完善仪表盘的功能和性能。

#### 后续行动计划
- 继续开发仪表盘的新功能。
- 优化仪表盘的用户体验。
- 加强社区合作，收集用户反馈和建议。

#### 计算机科学/CEPH相关领域英文原文关键词
- Ceph Dashboard
- Safe Dashboard
- REST API
- Angular
- RBG Mirroring
- OSD Management
- Crush Map
- Monitor Manager Modules
- Pool Manager
- RBD Mirroring
- RGW Management
- NFS Ganesha
- iSCSI
- Gateway Management