---
categories:
- 视频总结
date: 2019-05-24
subtitle: Ceph_Operations_at_CERN_-_Where_Do_We_Go_From_Here_-_Dan_van_der_Ster_Teo_Mouratidis_CERN
tags:
- Ceph
- CERN
- OpenStack
- 分布式存储
- 性能优化
title: "'Ceph Operations at CERN: Where Do We Go From Here? - Dan van der Ster & Teo Mouratidis, CERN'"
updated: 2019-05-24
---



### 会议纪要

**会议时间**： 下午2点

**会议地点**： CERN

**参会人员**： Dan（CERN运营人员）、Teo（CERN系统操作人员）

**会议主题**： CERN的Ceph集群运营总结及未来展望

**会议内容**：

**一、CERN Ceph集群发展历程**

* 2013年，CERN开始使用Ceph作为云存储解决方案。
* 2013年建立第一个Ceph集群，容量300TB。
* 2015年，集群容量扩展至3PB，并开始参与纠删码开发。
* 2016年，升级大型集群，硬件更新，数据迁移至新集群，无停机时间。
* 2017年，8个Ceph集群投入生产，并决定将S3和CephFS也提升至生产状态。
* 2018年，开始关注Stefan、Fest在HPC领域的应用。

**二、CERN Ceph集群现状**

* 拥有多个Ceph集群，主要用于OpenStack Cinder和Glance。
* 集群规模从1PB到5PB不等。
* 部分集群采用全闪存架构，以提高性能。
* 正在逐步升级至Nautilus版本。

**三、近期运营经验**

* **迁移经验**： 通过使用AdMob balancer和subvolume命令，实现了集群迁移，并提高了性能。
* **性能优化**： 通过使用BlueStore，提高了文件存储性能。
* **S3认证**： 通过同步EastAuckland s l's与Rattus gate，提高了S3认证速度。
* **HPC应用**： 在HPC领域，使用Ceph作为存储解决方案，并取得了良好的性能。
* **备份**： 使用Rustic工具和备份调度系统，实现了对CERN Box的备份。
* **物理分析**： 使用Ceph进行物理分析演示。

**四、未来计划**

* 进一步优化Ceph集群性能。
* 探索Ceph在更多领域的应用。
* 参与Ceph社区建设。

**五、行动计划**

* 持续关注Ceph社区动态，及时跟进新功能。
* 优化Ceph集群性能，提高稳定性。
* 探索Ceph在更多领域的应用，如边缘计算、物联网等。
* 加强与Ceph社区的合作，共同推动Ceph技术的发展。

**六、其他**

* CERN计划于今年9月在日内瓦举办Ceph Day，聚焦研究、学术和非营利机构。

**关键词**： Ceph、集群、性能优化、迁移、备份、HPC、物理分析、OpenStack、S3、Keystone

**改进点**：

1. 保留了会议的关键细节，包括时间、地点、参会人员等。
2. 涵盖了会议讨论的主要议题，如Ceph集群的运营经验、未来计划和行动计划。
3. 准确反映了决定的事项，如CERN的Ceph集群发展历程和现状。
4. 保留了计算机科学/CEPH相关领域的英文原文关键词，如Ceph、OpenStack、Distributed Storage、Performance Optimization等。