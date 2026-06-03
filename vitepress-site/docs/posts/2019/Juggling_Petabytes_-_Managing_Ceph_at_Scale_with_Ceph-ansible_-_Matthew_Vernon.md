---
title: "Juggling Petabytes: Managing Ceph at Scale with Ceph-ansible - Matthew Vernon"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
  - "分布式存储"
  - "自动化"
categories:
  - "视频总结"
outline: deep
---
Saenger研究院的Ceph存储集群部署、管理及经验分享会议纪要：

会议介绍了Saenger研究院的概况，包括其在基因测序和基因组分析领域的贡献，以及其高吞吐量计算集群和存储资源。Saenger研究院自2016年开始使用Ceph存储，目前拥有51个节点，18PB的原始容量，并拥有一个测试集群和一个灾备站点。

**会议主要内容包括**：

**一、Ceph存储集群部署**

- 使用Ansible和Ceph Ansible Wall进行集群管理。
- 集群配置包括Supermicro服务器、Mellanox 100G网络和SAS驱动器。
- 使用Collectd收集指标，Nagios进行监控。
- 编写脚本监控OSD状态和硬盘健康状况。

**二、Ceph存储集群升级**

- 从Jewel版本升级到Luminous版本，并计划迁移到Nautilus版本。
- 升级过程相对顺利，但迁移到BlueStore时遇到挑战。

**三、Ceph存储集群使用经验**

- Ceph存储集群易于扩展、高可靠性和高性能。
- 主要用于存储基因测序数据，并通过Rados Gateway提供S3存储服务。

**四、Ceph存储集群的挑战**

- Rados Gateway服务管理复杂。
- 大型OMAP对象处理。
- 无法自动迁移数据到纠删码池。
- 无法自动缩减池大小。
- 部署过程复杂。

**五、行动计划**

- 使用Ceph的新功能，如纠删码和自动缩减池大小。
- 优化Rados Gateway服务管理。
- 简化部署过程。

**六、会议总结**

会议分享了Saenger研究院在Ceph存储集群部署、管理及使用方面的经验，并讨论了遇到的挑战和未来的改进计划。