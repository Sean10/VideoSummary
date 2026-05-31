---
categories:
- 视频总结
date: 2020-08-25
subtitle: Ceph_Day_CERN_2019_-_Ceph_in_Compute_Canada_-_Mike_Cave
tags:
- Ceph
- 分布式存储
- 高可用性
- 可扩展性
title: "'Ceph Day CERN 2019: Ceph in Compute Canada - Mike Cave'"
updated: 2020-08-26
---



会议纪要

会议主题：Compute Canada 中 Ceph 的使用情况介绍

主讲人：Mike Cave
- **职位**：Senior Unix Administrator
- **单位**：University of Victoria, Research Computing Support

Compute Canada 概述
- **性质**：加拿大国家数字计算研究平台，提供研究人员HPC资源、云资源、存储、备份等服务。
- **资金模型**：联合资助模式，由四个联盟共同运作：West Grid, Compute Ontario, Calcul Quebec, ACENET。
- **服务站点**：全国五个主要站点，支持超过70个机构。
- **网络**：100 Gigabit 全国网络。

Ceph 在 Compute Canada 的应用
- **Ceph部署**：所有云站点均使用Ceph，存储规模从4.5 PB到100 TB不等。
- **Arbutus云**：Compute Canada最大云部署，提供10,000物理核心，虚拟化后提供近20,000核心，4.5 PB可用存储。
- **Ceph部署历史**：从初始的500 TB三重复制存储，手动部署，到现在的32个OSD节点，640个OSD，5.3 PB原始存储，使用BlueStore和Erasure Coded Profile。

监控与管理
- **监控系统**：使用UV Stats、Prometheus、Grafana进行系统监控。
- **日志管理**：通过Flare系统集中管理日志，实现基于事件的智能报警。

后续行动计划
- **数据迁移**：用户自行迁移数据到新集群。
- **硬件更新**：逐步淘汰旧硬件，引入新硬件。
- **持续监控**：继续优化监控系统，确保集群稳定运行。

结论
Mike Cave 介绍了Compute Canada在Ceph存储解决方案的应用和发展历程，强调了联合资助模式在资源共享和硬件更新方面的重要性，并展示了如何通过先进的监控和管理工具确保系统的高可用性和性能。此外，他还详细介绍了Ceph部署的演进过程，包括从手动部署到自动化部署，以及使用BlueStore和Erasure Coded Profile等新技术。