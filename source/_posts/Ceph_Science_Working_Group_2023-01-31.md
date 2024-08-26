---
title: "Ceph Science Working Group 2023-01-31"
date: 2023-02-01
updated: 2023-02-01
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是本年度的首次会议，旨在为来自不同背景的存储领域专业人士提供一个交流平台，讨论包括Ceph在内的分布式存储系统的各种议题，如升级、问题解决等。会议由一名组织者主持，参与者包括来自大学、研究机构和企业的人员。

#### 主要议题与讨论
1. **Ceph集群介绍与经验分享**
   - **Garen Atterbury**（University of Nebraska Lincoln）分享了他们在Ceph集群上的经验，包括从HDFS迁移到Ceph，以及管理多个Ceph集群的情况。
   - **Jeremy**（South African Radio Astronomy Observatory）介绍了他们使用Ceph作为Meerkat射电望远镜数据产品的对象存储的案例。
   - **Pieter**（CSC）讨论了他们在Ceph集群上实施的S3认证和密钥管理策略，以及遇到的挑战和解决方案。

2. **Ceph集群升级经验**
   - **Bruno Cannings**（Sanger Institute）分享了他们从Ubuntu 18.04升级到20.04的经验，以及在升级过程中遇到的挑战和解决方案。
   - **组织者**和**Jeremy**讨论了从CentOS 7和8升级到Rocky 8的经验，以及如何进行In-Place转换。

3. **Ceph集群管理和优化**
   - **讨论了Ceph集群的平衡器使用情况**，包括内置算法和其他第三方平衡器的比较。
   - **Pieter**提到了他们在大型Ceph集群中遇到的管理和扩展性问题，特别是在使用Ceph Orchestrator时。

4. **Ceph集群的硬件和操作系统选择**
   - **讨论了在不同操作系统版本上运行Ceph的情况**，包括CentOS、Rocky Linux和Ubuntu。
   - **Pieter**提到了他们在使用NVMe存储设备时遇到的写放大问题。

#### 决定事项
- 会议决定不举行下一次虚拟会议，而是计划在即将到来的Cephalocon 2023会议上举行面对面的Birds of a Feather session。

#### 后续行动计划
- 组织者将考虑在Cephalocon 2023上组织一个Birds of a Feather session，以便参与者可以更深入地讨论Ceph相关的话题。
- 参与者将继续关注Ceph的开发和社区动态，以便及时了解和应用新的功能和改进。

#### 其他备注
- 会议中提到了一些具体的Ceph版本和配置问题，如Ceph 16、Ceph 17、Erasure Coding等，这些信息对于理解和解决特定问题非常有帮助。
- 会议强调了社区交流的重要性，鼓励参与者在Cephalocon等活动中进行更多的面对面交流。

本次会议为Ceph社区成员提供了一个宝贵的交流机会，促进了知识和经验的共享，有助于提升Ceph集群的管理和性能优化。