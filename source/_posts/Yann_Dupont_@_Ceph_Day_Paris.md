---
categories:
- 视频总结
date: 2014-11-11
subtitle: Yann_Dupont_@_Ceph_Day_Paris
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
- OpenStack
- 网络
title: "Yann Dupont @ Ceph Day Paris"
updated: 2014-11-12
---




在巴黎Ceph Day会议上，Yann Dupont分享了他在法国布列塔尼University City of N的IT服务部门使用Ceph分布式存储的生产环境中的实践经验。

**会议要点**：

- **背景介绍**： University City of N拥有21个学院和约5万名学生员工，IT服务部门负责管理校园网络、电话系统、存储等服务。由于存储系统过于集中，存在数据丢失和系统故障的风险。
- **Ceph存储解决方案的引入**： 经过多次尝试，IRT决定采用Ceph作为存储解决方案。初始部署时，由于缺乏最佳实践和指导，遇到了一些问题，如硬件选择不当、配置错误等。
- **部署架构**： 部署了5个独立的Ceph集群，分别用于不同用途，如实验、生产、备份等。使用LXC容器技术，将OSD部署在物理服务器上，提高了资源利用率。采用10GB网络带宽，并使用特定VLAN进行网络隔离。
- **性能优化**： 调整CRUSH规则，确保数据在不同数据中心之间分布。使用SSD进行日志存储，提高性能。使用Bcache进行数据缓存，减少IO压力。使用OpenStack等工具进行自动化管理。
- **经验教训**： 避免使用硬件RAID，选择可靠的硬件和软件。选择合适的Ceph版本和配置。关注Ceph的社区和邮件列表，及时了解最新动态。定期进行测试和评估，确保系统稳定可靠。
- **未来计划**： 测试Ceph的存储性能和可扩展性。探索Ceph的新功能，如数据迁移、快照等。与Ceph社区合作，共同推动Ceph的发展。

**关键词**：

- Ceph
- 分布式存储
- CRUSH算法
- LXC
- SSD
- Bcache
- OpenStack
- 可扩展性
- 高可靠性
- 硬件选择
- 网络拓扑
- 安全性和稳定性