---
title: "Ceph Day CERN 2019: What’s New In Nautilus & Community News - Mike Perez"
date: 2020-08-25
updated: 2020-08-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
会议由Mike Perez主持，他是Red Hat的开源项目办公室社区经理。会议在CERN举行，感谢Soft Iron和Western Digital的赞助以及CERN提供的场地。会议主要介绍了Ceph社区的最新动态和Nautilus版本的更新。

#### 主要议题
1. **Ceph基金会成立**：
   - 八个月前，Ceph基金会在柏林宣布成立，初始有31个成员，包括13个主要成员、10个一般成员和8个非营利及政府组织。
   - 今年新增了两个一般成员和两个附属成员。
   - 感谢Linux基金会在Ceph基金会成立和大型活动组织方面的支持。

2. **文档改进**：
   - Ceph社区正在改进文档工具和流程，特别是通过DocuBetter项目。
   - 会议每月的第二个和第四个星期三举行，欢迎任何人参与。
   - Ceph基金会正在寻找一名专职的文档改进人员，感兴趣的人可以提交简历。

3. **Ceph简介**：
   - Ceph是一个统一存储系统，提供S3和Swift兼容接口，支持块存储和符合POSIX的文件系统。
   - Ceph使用CRUSH算法来确定数据位置，避免单点故障，支持复制和纠删码，强调数据安全和一致性。

4. **Nautilus版本更新**：
   - Nautilus版本重点改进了易用性和管理功能。
   - 引入了新的仪表盘，整合了多个分散的仪表盘项目，提供监控和管理功能。
   - 推出了Orchestrator API，简化了Ceph的部署和管理，支持多种配置管理工具。
   - 新增了自动管理放置组数量和设备健康指标功能。

5. **Kubernetes和Rook**：
   - Ceph社区关注Kubernetes集成，通过Rook项目简化Ceph在Kubernetes中的部署和管理。
   - Rook是一个强大的Ceph操作器，支持声明式资源定义，简化集群管理。

#### 决定事项
- Ceph基金会将继续支持社区发展，特别是文档和易用性的改进。
- 将继续推动Ceph与Kubernetes的集成，通过Rook等项目简化部署。

#### 后续行动计划
- 继续推进DocuBetter项目，改进Ceph文档和工具。
- 招聘专职的文档改进人员，提升Ceph的文档质量。
- 加强与Kubernetes社区的合作，推动Rook等项目的发展。
- 继续开发和优化Nautilus版本的功能，特别是仪表盘和Orchestrator API。

#### 其他信息
- 会议感谢所有赞助商和组织者的支持。
- 鼓励社区成员参与Ceph Days活动，并提供支持。

#### 会议结束
会议在感谢和掌声中结束，接下来将由Sage继续介绍Octopus版本的最新进展。