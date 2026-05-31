---
categories:
- 视频总结
date: 2019-05-24
subtitle: Hands_On_with_Rook_-_Ceph_Kubernetes_-_Maxime_Guyot_Root_Pi_John_Studarus_Packet_Host
tags:
- Ceph
- Kubernetes
- Rook
- 分布式存储
- 云计算
title: "Hands On with Rook- Ceph & Kubernetes - Maxime Guyot, Root Pi & John Studarus, Packet Host"
updated: 2019-05-24
---


本次研讨会主要介绍如何使用 Rook 在裸金属上部署和运行 Ceph 分布式存储系统。会议内容覆盖了以下几个方面：

**一、环境搭建**

* 参会者使用两台物理服务器进行实验，一台为 T1 小型服务器，另一台为 C2 中型服务器。
* T1 服务器仅包含文件系统，C2 服务器包含文件系统和多个 NVMe SSD 驱动器。
* 参会者可通过 SSH 访问实验环境。

**二、Rook 部署**

* 使用 Rook 部署 Ceph 集群，包括 Ceph Mon、Manager 和 OSD。
* 验证 Kubernetes 集群是否正常运行。

**三、Ceph 集群配置**

* 创建 Ceph 块存储池和文件系统。
* 创建 Ceph 对象存储网关（RGW）。
* 使用 Ceph 对象存储上传和下载文件。

**四、监控**

* 使用 Prometheus 和 Grafana 监控 Ceph 集群的健康状况、性能和容量。
* 创建自定义仪表板以可视化监控数据。

**五、升级**

* 使用 Rook 升级 Ceph 集群到最新版本。

**六、实验与模拟**

* 参会者通过实际操作加深了对 Ceph 和 Rook 的理解，并掌握了相关操作技能。
* 模拟了 Ceph 集群的故障，以展示 Rook 的容错能力。
* 创建了 WordPress 应用，展示了 Ceph 与 Kubernetes 的集成。

**七、后续行动计划**

* 参会者完成实验任务并提交实验报告。
* 主持人整理实验结果并撰写实验总结。
* 主持人收集参会者反馈，改进实验指南。

本次研讨会为参会者提供了深入了解 Ceph 和 Rook 的机会，并通过实际操作加深了对分布式存储技术的理解。