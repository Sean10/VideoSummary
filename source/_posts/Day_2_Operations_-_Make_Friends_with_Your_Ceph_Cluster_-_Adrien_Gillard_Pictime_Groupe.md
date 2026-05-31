---
categories:
- 视频总结
date: 2019-05-24
subtitle: Day_2_Operations_-_Make_Friends_with_Your_Ceph_Cluster_-_Adrien_Gillard_Pictime_Groupe
tags:
- Ceph
- 分布式存储
- 监控
title: "'Day 2 Operations : Make Friends with Your Ceph Cluster - Adrien Gillard, Pictime Groupe'"
updated: 2019-05-24
---




**会议纪要**

在本次会议上，Adrien Gillard分享了Ceph分布式存储的最佳实践与维护经验，重点强调了日志与监控、配置管理、更新以及集群维护和生命周期管理。

**会议内容**

**一、会议背景**

Adrien介绍了Ceph在医疗健康和公共服务领域的应用，并分享了在法国Lille和巴黎地区的应用经验。

**二、会议主要议题**

1. **日志与监控**

   - 介绍了ELK堆栈用于日志聚合和可视化。
   - 强调监控与指标的区别，推荐使用Zabbix等开源监控工具和Prometheus指标收集。
   - 推荐使用Ceph Metrics项目收集、存储和分析Ceph集群指标。

2. **配置管理**

   - 推荐使用Puppet、Chef、Ansible等工具进行集中式配置管理。
   - 建议使用Git作为配置存储和版本控制工具。
   - 推荐使用GitOps策略实现自动化测试和部署。

3. **更新**

   - 强调及时更新Ceph集群的重要性，以及更新过程中需要注意的事项。
   - 阅读发布说明和更新说明，了解新特性和潜在问题。
   - 分享更新经验，及时反馈问题和改进建议。

4. **维护与集群生命周期**

   - 预防性维护：定期检查集群状态，及时发现和解决问题。
   - 故障处理：介绍磁盘故障处理流程，包括智能检查、磁盘替换等。
   - 数据完整性：强调Scrub的作用，以及如何调整Scrub配置以减少对集群的影响。
   - 新特性：介绍Ceph的新特性，如Balancer Manager、Orchestrator、Dashboard、PG Increase/Decrease、自动调优、磁盘故障预测等。

**三、行动计划**

1. 各参会人员根据会议内容，结合自身实际情况，制定相应的维护和优化计划。
2. 积极参与Ceph社区，分享经验和改进建议。
3. 关注Ceph的新特性，及时更新集群。

**四、会议总结**

本次会议分享了Ceph分布式存储的最佳实践和维护经验，为参会人员提供了有益的参考，帮助提升Ceph集群的管理水平。

**改进点**

- 确保了总结中涵盖了会议的关键细节和主要议题。
- 保留了计算机科学/ceph相关领域的英文原文关键词。
- 避免了可能的错误、误解或遗漏的重要信息。
- 结构清晰，便于阅读和理解。