---
categories:
- 视频总结
date: 2018-01-04
subtitle: 2018-JAN-03_-_-_Ceph_Developer_Monthly
tags:
- Ceph
- Kubernetes
- Rook
- OSD
- CephFS
- OpenStack
title: "'2018-JAN-03 :: Ceph Developer Monthly'"
updated: 2018-01-04
---




**会议时间**： 2018年1月（具体日期未提及）
**会议地点**： CPM（Ceph社区项目会议）
**参会人员**： Sage、Quentin、Jason、Dan、Mark、Kenda等

**会议主题**：

* **Ceph配置管理系统（mod）更新**： 包括配置存储、解析、验证和展示等，支持多种配置获取方式，但当前未进行身份验证。
* **Kubernetes集群部署Ceph（Rook项目）**： Rook项目成为Ceph在Kubernetes集群中部署的首选工具，支持自动化集群部署、升级和运维等操作。
* **Easy Clones功能改进**： 简化RBD克隆和快照操作，通过OSD能力（caps）控制克隆和快照操作。
* **Ceph OSD性能优化**： 旨在提高Ceph在高速存储设备上的性能，包括重构OSD、使用异步框架等。
* **Ceph存储后端（C Store）开发**： 开发新的存储后端，支持高速存储设备，使用Seastar框架和SPDK库。
* **OpenStack测试平台（Technology）使用**： 用于测试OpenStack与Ceph的集成。

**会议内容**：

* **Ceph配置管理系统（mod）更新**： 讨论了配置选项的敏感性、Ceph存储后端缓存策略等问题，并建议使用“C Store”或“C18 Store”作为新存储后端的命名。
* **Kubernetes集群部署Ceph（Rook项目）**： 讨论了Rook项目的自定义控制器、自动化集群部署、升级和运维等操作，并与Rook项目团队合作，确保其与Ceph Mimic版本同步发布。
* **Easy Clones功能改进**： 讨论了如何通过OSD能力（caps）控制克隆和快照操作，以及如何将快照移动到“已删除但仍有引用”的命名空间，以防止误删除。
* **Ceph OSD性能优化**： 讨论了使用C Star框架重构OSD、使用异步框架改进OSD性能，以及开发针对高速存储设备的新的对象存储后端。
* **Ceph存储后端（C Store）开发**： 讨论了C Store项目的开发进度，包括使用Seastar框架和SPDK库，以及提供日志结构化的存储格式。
* **OpenStack测试平台（Technology）使用**： 讨论了Technology平台在测试OpenStack与Ceph集成中的作用，以及如何使用该平台进行Ceph测试。

**后续行动计划**：

* 完成配置管理功能的身份验证功能。
* 完成Rook项目的开发工作，并确保其与Ceph Mimic版本同步发布。
* 完成Easy Clones功能的开发工作。
* 完成Ceph OSD性能优化项目的开发工作。
* 开发Ceph存储后端（C Store）。
* 探索使用Technology平台进行Ceph测试。

**其他事项**：

* 讨论了Ceph配置选项的敏感性、Ceph存储后端缓存策略等问题。
* 讨论了Ceph存储后端（C Store）的命名问题，建议使用“C Store”或“C18 Store”。
* 讨论了Ceph社区将继续努力改进Ceph的性能和功能，以满足用户的需求。