---
categories:
- 视频总结
date: 2023-05-05
subtitle: 优化Ceph文件系统：结合MDS QoS调度和静态-动态子树分区
tags:
- CephFS
- MDS QoS Scheduling
- Static
- Dynamic Subtree Partitioning
- Ceph Optimization
- Ceph Performance
title: "Optimizing CephFS with Combining MDS QoS Scheduling and Static-Dynamic Subtree Partitioning"
updated: 2023-05-05
---




### 会议纪要

#### 会议概述
本次会议由Young主持，来自Lion公司的专业人员分享了他们在Ceph分布式存储系统上的优化工作。主要讨论了Ceph文件系统（CephFS）的性能优化，包括MDS QoS调度和静态-动态子树分区策略。

#### 主要议题
1. **公司背景与Ceph应用介绍**
   - Lion公司是一家提供消息和通信服务的公司，拥有超过1.5亿日活跃用户。
   - 公司采用OpenStack和Kubernetes作为私有云基础设施，并使用Azure软件定义存储策略。
   - 自2020年起，公司使用CephFS处理大量数据，并面临性能优化挑战。

2. **CephFS的应用与挑战**
   - 介绍了CephFS与OpenStack Manila的集成，用于处理OpenStack项目的共享卷。
   - 面临的主要挑战包括处理AI和ML工程师存储的大量数据，以及优化性能。

3. **集群管理与性能优化**
   - 描述了两个主要集群的配置，每个集群包含超过30个活动实例。
   - 讨论了从裸金属服务器到虚拟机的转变，以及如何通过小规模虚拟机优化MDS。

4. **静态-动态子树分区策略**
   - 动态子树分区：根据客户工作负载动态调整元数据分布，但可能导致迁移开销和性能波动。
   - 静态子树分区：通过预分配特定链接来减少元数据迁移，但可能导致工作负载分布不均。

5. **结合静态-动态分区的新策略**
   - 提出了一种结合动态和静态分区策略的新方法，以优化性能和减少迁移开销。

6. **MDS QoS调度器**
   - 介绍了基于M Clock算法的QoS调度器，用于控制MDS的请求处理速度，确保稳定性和性能。

#### 决定事项
- 确定了结合静态-动态分区策略的新架构，以优化CFS的性能和稳定性。
- 实施了MDS QoS调度器，以更好地管理MDS的请求处理和资源分配。

#### 后续行动计划
- 继续测试和优化新的分区策略，确保其在多种工作负载下的有效性。
- 进一步开发和部署MDS QoS调度器，以应对复杂的应用场景和增加的需求。
- 持续与社区合作，分享经验并获取反馈，以不断改进Ceph的性能和功能。

#### 结论
Lion公司通过结合静态-动态分区策略和实施MDS QoS调度器，有效地优化了Ceph文件系统的性能和稳定性。未来将继续探索更多优化措施，并积极参与社区贡献。