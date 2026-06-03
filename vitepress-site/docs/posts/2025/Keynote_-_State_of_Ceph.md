---
title: "Keynote - State of Ceph"
date: 2025-06-24
updated: 2025-06-24
tags:
  - "Ceph"
  - "分布式存储"
  - "社区动态"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
Ceph社区会议纪要中，Neha Ojha（IBM工程经理、Ceph执行委员会成员）主持了会议，主题为Ceph社区现状及即将发布的Tentacle版本更新。以下是会议的主要内容：

### 会议基本信息
- **主持人**: Neha Ojha
- **会议主题**: Ceph社区现状及Tentacle版本更新
- **地点**: 伦敦（Ceph Days活动）
- **赞助方**: IBM和Coronicle

### 社区现状与统计
- **贡献者规模**: 约1400名GitHub贡献者
- **代码规模**: 70万+行代码，15万次提交
- **版本支持策略**: 支持 N-2 版本（当前支持Squid和Reef，未来支持Tentacle）

### 项目里程碑与社区活动
- **SAFLCAN 2023**: 去年活动成功举办，T恤设计获好评
- **存储规模**: Ceph集群总容量达1.8艾字节
- **社区参与渠道**: Slack频道、Meetup小组、Ceph用户委员会
- **学术合作**: 与多所大学合作开发新功能
- **性能里程碑**: Squid版本中实现1 TB/s的吞吐量

### Ceph基金会更新
- **新成员**: Digital Ocean加入为银牌会员，现有钻石会员包括Bluebug、IBM和45 Drives
- **新职位**: Anthony Middleton担任社区经理
- **活动计划**: 全球Ceph Days，SAFLCAN 2025将于10月在加拿大温哥华举办

### Tentacle版本技术亮点
- **核心改进**: Erasure Coding性能优化，目录列表性能改进，可用性评分，Stretch Cluster支持，网络分裂警报
- **Bluestore优化**: 压缩可调性，分配器性能改进
- **Crimson（下一代OSD）**: 用户体验改进，功能开发，Seastore后端
- **对象存储（RGW）**: S3 API扩展，性能优化，新功能
- **块存储（RBD）**: 灾难恢复，在线迁移，内核支持
- **文件存储（CephFS）**: 稳定性改进，新特性
- **Dashboard与管理工具**: 多集群管理，Cephadm改进
- **LUKS加密**: 迁移支持
- **遥测与文档**: 遥测数据价值，文档改进
- **开发者体验与性能基准**: CI/CD优化，CBT（Ceph Benchmarking Tool）

### 后续行动
- 参与社区调查，关注性能与易用性
- 试用Tentacle的Tech Preview功能
- 关注即将举办的Ceph Days和SAFLCAN 2025

会议强调了Ceph社区的活跃发展和Tentacle版本的技术亮点，包括性能优化、功能增强和社区参与的增加。