---
categories:
- 视频总结
date: 2018-04-23
subtitle: Ceph_for_Big_Science_-_Dan_van_der_Ster
tags:
- Ceph
- 分布式存储
- CERN
title: "Ceph for Big Science - Dan van der Ster"
updated: 2018-04-23
---




CERN使用Ceph进行大规模科学存储的会议中，Dan van der Ster分享了CERN在Ceph方面的应用经验和改进建议。

**会议要点**：

* **CERN背景介绍**：CERN是世界上最大的粒子加速器，拥有庞大的存储和计算资源，是全球LHC计算网格的一部分。
* **Ceph在CERN的应用**：
    * CERN使用Ceph存储大量科学数据，包括实验数据、虚拟文件系统等。
    * CERN的存储集群已扩展至8个生产集群，存储量接近6PB。
    * Ceph用于OpenStack Cinder、Glance、CephFS、物理数据存储和S3对象存储。
    * Ceph文件系统（CephFS）用于替代虚拟NFS文件系统，提供高可用性和可扩展性。
    * Ceph块设备（RBD）用于存储Glance镜像和Cinder卷。
* **Ceph改进建议**：
    * 开发RBD性能监控工具，提高性能和可靠性。
    * 改善SEF文件系统的并行I/O性能，提高HPC存储性能。
    * 支持池级别对象备份，例如从副本复制到快照。
    * 解决大型集群的配置和升级问题。
* **未来展望**：
    * CERN预计在2020年代将产生数百PB的数据，需要更强大的存储系统。
    * CERN正在与Ceph社区合作，进行大规模测试，验证Ceph的扩展性。
    * CERN希望将Ceph用于更多存储场景，包括全球数据湖。

**行动计划**：

* CERN将继续与Ceph社区合作，推动Ceph的改进。
* CERN将进行更多测试，验证Ceph在大型集群中的性能和可靠性。
* CERN将探索将Ceph用于更多存储场景的可能性。

**关键词**： CERN、Ceph、OpenStack、Cinder、Glance、S3、RBD、CephFS、HPC、数据湖