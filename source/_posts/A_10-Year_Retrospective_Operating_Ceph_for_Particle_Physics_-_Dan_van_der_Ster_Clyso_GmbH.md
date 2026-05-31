---
categories:
- 视频总结
date: 2023-05-05
subtitle: A_10-Year_Retrospective_Operating_Ceph_for_Particle_Physics_-_Dan_van_der_Ster_Clyso_GmbH
tags:
- Ceph
- 分布式存储
- CERN
- OpenStack
title: "A 10-Year Retrospective Operating Ceph for Particle Physics - Dan van der Ster, Clyso GmbH"
updated: 2023-05-05
---




该视频回顾了CERN使用Ceph分布式存储系统的十年经验。以下是对会议内容的关键点的总结：

**个人背景介绍：**
- Dan van der Ster，加拿大籍荷兰人，在CERN担任了多年的工程和技术管理人员，目前任职于Clyso GmbH。

**CERN简介：**
- CERN是世界上最大的粒子物理实验室，位于瑞士日内瓦。

**Ceph在CERN的应用：**
- CERN自2013年开始使用Ceph，从最初的概念验证迅速扩展到3PB的生产环境。
- Ceph支持了CERN的实验室基础设施，包括配置管理、操作系统、数据库、监控和分析平台等。
- 目前，CERN拥有17个Ceph集群，约100PB的原始磁盘容量。

**Ceph在CERN的重要性：**
- Ceph的有机增长能力和性价比使其成为CERN的理想选择，避免了硬件供应商锁定。
- Ceph支持了CERN的多个业务连续性和灾难恢复用例。

**Ceph架构和挑战：**
- CERN面临的挑战包括硬件选择、数据副本策略、SSD使用和网络架构等。
- CERN采用的服务器架构使用四合一机箱，配备SSD和双路Xeon或AMD处理器。

**性能和可扩展性：**
- Ceph的性能通常被认为是“它就是那样”，强调了Ceph在处理复杂问题时的透明性。
- Ceph的性能改进包括使用SSD缓存层、BlueStore的延迟优化等。

**操作经验和教训：**
- 操作Ceph集群需要谨慎应用更改，避免触发可能导致长时间恢复的条件。
- Ceph需要更好的工具来预览和验证配置更改。
- 数据放置的均匀性是一个挑战，但UpMap平衡器和PG重映射工具提供了帮助。

**成功案例和社区贡献：**
- Ceph成功集成到OpenStack、Kubernetes等平台，保护数据可靠性。
- CERN积极参与Ceph社区，并计划今年举办六次确认的面对面活动。

**后续行动计划：**
- 继续参与Ceph社区活动。
- 探索和实施Ceph的新功能和改进。

**结论：**
- Ceph在CERN的十年操作经验证明了其作为分布式存储解决方案的可靠性和灵活性。通过持续的改进和社区支持，Ceph将继续在CERN及其他机构中发挥重要作用。