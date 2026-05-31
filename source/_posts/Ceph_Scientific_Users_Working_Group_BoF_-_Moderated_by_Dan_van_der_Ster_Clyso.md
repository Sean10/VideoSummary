---
title: Ceph Scientific Users Working Group BoF - Moderated by Dan van der Ster, Clyso
date: 2025-11-19
updated: 2025-11-20
tags:
- 分布式存储
- 存储优化
- 云计算
categories: 
- "视频总结"
subtitle: Ceph_Scientific_Users_Working_Group_BoF_-_Moderated_by_Dan_van_der_Ster_Clyso
---

### Ceph 科学用户工作组 BoF 会议纪要

#### 会议基本信息

- **会议名称**: Ceph 科学用户组（鸟群聚会）
- **时间**: 2023年10月（具体日期未明确）
- **地点**: 温哥华（线下）
- **主持人**: Kevin
- **核心组织者**: Kevin、Mataya（ETH Zurich）、Tom（SDFC）、Enrico（CERN）
- **会议形式**: 非正式讨论（鸟群聚会）

#### 会议关键讨论内容

#### 1. 参会者自我介绍

- **Kevin**: Ceph社区科学用户组的发起人，组织每两个月一次的虚拟会议。
- **Mataya**: ETH Zurich，专注于私有云场景下的Ceph部署，支持HPC和Batch系统。
- **Tom**: 英国科研机构SDFC，管理大规模Ceph集群，支持通用存储用例。
- **Enrico**: CERN，管理Ceph集群支持OpenStack和容器存储，未用于物理实验数据。
- **其他参与者**: Jeff Albert（University Victoria）、Gregori（Elettra同步辐射实验室）、Torson（University of Bremen）等。

#### 2. 主要议题

##### (1) 旧硬件的再利用与生命周期管理

- **挑战**: 硬件保修到期后可靠性下降，容量规划困难。
- **解决方案**: 将过保硬件用于非关键负载、逐步淘汰老旧服务器、保留过保硬件作为备件。

##### (2) Ceph在科学场景中的扩展挑战

- **未充分覆盖的用例**: 企业级虚拟化存储、HPC高性能存储、教育与推广。
- **潜在方向**: 通过试点验证CephFS性能、推动开源存储替代商业方案。

##### (3) Ceph与磁带库的集成

- **现状**: CERN使用自有磁带库，IBM方案通过RGW将数据推送至磁带。
- **讨论共识**: 磁带是长期归档的最佳选择，Ceph可作为热存储层。

##### (4) 社区贡献与Ceph基金会合作

- **当前贡献形式**: 技术预览反馈、文档补充、构建包维护。
- **未来建议**: 更多机构加入Ceph基金会、组织地区性活动。

#### 行动计划与决议

1. **旧硬件管理**: 探索将过保硬件用于独立故障域、制定硬件淘汰标准。
2. **性能优化**: 推动CephFS在HPC场景的基准测试。
3. **归档集成**: 评估IBM RGW到磁带的方案。
4. **社区协作**: 下次虚拟会议将于11月25日举行，议题征集通过邮件列表通知。

#### 关键词保留

- **Ceph组件**: OSD、MON、MDS、PG、RADOS、RGW、CephFS、RBD、librados.
- **技术概念**: CRUSH算法、高可用性（HA）、副本（Replication）、纠删码（Erasure Coding）、BlueStore、性能调优（Performance Tuning）.
- **生态集成**: Kubernetes、OpenStack、AWS S3、磁带归档（Tape Library）.