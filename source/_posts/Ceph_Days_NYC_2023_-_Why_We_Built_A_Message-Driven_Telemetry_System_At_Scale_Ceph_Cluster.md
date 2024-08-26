---
title: "Ceph Days NYC 2023: Why We Built A “Message-Driven Telemetry System At Scale” Ceph Cluster"
date: 2023-05-17
updated: 2023-05-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
会议由Nathan Howard主持，他是Bloomberg的高级软件工程师，隶属于分布式存储团队。Nathan在Bloomberg工作已有七年，主要负责软件定义存储，特别是对象级存储，即S3 API，内部称为Bloomberg Cloud Storage (BCS)，该存储系统基于Ceph构建。

#### 会议议程
1. **公司介绍**：Bloomberg是一家成立于1981年的金融科技公司，以其旗舰产品Bloomberg终端闻名，为全球超过35万订阅者提供数据服务、新闻分析等。
2. **存储工程团队介绍**：负责设计和维护所有存储系统，包括文件、块和对象存储，以及数据保护和存储工作流程自动化。
3. **集群信息**：介绍了LCF集群的详细信息，包括数据中心分布、租户数量、存储容量和OSD数量。
4. **Ceph默认Telemetry系统的问题**：讨论了Ceph默认集成的Prometheus系统的局限性，特别是在大规模集群中的性能问题和缺乏用户级指标。
5. **解决方案要求**：提出了实时性、可扩展性、集成Grafana和易于扩展等要求。
6. **解决方案概述**：介绍了基于发布-订阅模型的解决方案，使用RabbitMQ作为消息代理，Celery作为任务调度器，Python编写，易于扩展和维护。
7. **技术栈细节**：详细介绍了RabbitMQ和Celery的使用，以及如何通过这些技术实现高可扩展性和容错性。
8. **代码示例**：展示了如何使用Celery进行任务调度和消息传递。
9. **结果和未来计划**：讨论了解决方案的实际效果，包括快速响应、良好资源利用和易于扩展，并提出了未来可能的改进方向，如扩展到RBD和收集元数据指标。

#### 决定事项
- 确定了解决Ceph Telemetry系统问题的技术方案，使用RabbitMQ和Celery构建分布式任务调度系统。
- 确认了集成Grafana进行数据可视化和监控。

#### 后续行动计划
- 继续优化和扩展当前的Telemetry系统，以支持更多的存储类型和更细粒度的指标。
- 考虑将解决方案贡献给开源社区，以帮助其他Ceph用户。
- 招聘更多人才，以支持公司内部Ceph和其他技术的开发和维护。

#### 会议结束
Nathan Howard在会议结束时表示，Bloomberg正在招聘，并欢迎对Ceph或其他技术感兴趣的人士与他联系。会议在掌声中结束。