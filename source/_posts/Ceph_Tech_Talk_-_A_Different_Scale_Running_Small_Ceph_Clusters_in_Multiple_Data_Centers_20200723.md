---
title: "Ceph Tech Talk: A Different Scale, Running Small Ceph Clusters in Multiple Data Centers 20200723"
date: 2020-07-28
updated: 2020-07-29
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：
讨论小型子集群（small subclusters）在多数据中心中的应用

#### 主讲人：
Yuval（系统工程师，拥有17年系统工作经验，目前在柏林工作，自2017年起开始使用Ceph）

#### 会议内容总结：

1. **个人背景介绍**：
   - Yuval拥有17年系统工作经验，涉及多种存储系统。
   - 目前在柏林工作，担任系统工程师，工作范围广泛。
   - 自2017年起开始使用Ceph，首次接触的生产版本是Jewel。

2. **讨论小型子集群的原因**：
   - 小型集群不仅实用，而且具有隐藏的优势。
   - 小型集群易于扩展和管理，可以根据需要增加磁盘或节点。

3. **使用案例介绍**：
   - 当前在不同地点运行多个小型子集群。
   - 计划在未来几个月内升级到Octopus版本。
   - 集群配置为四节点，三路复制，每个集群有三台监控器和三台管理器。
   - 使用Ceph作为后端存储，直接连接到虚拟磁盘。

4. **关于小型集群的常见问题**：
   - 是否需要四节点？是否浪费资源？
   - 小型集群的优势包括避免脑裂问题、可调整的复制级别、易于扩展和维护。

5. **小型集群与大型集群的比较**：
   - 小型集群更易于手动管理，自动化需求较低。
   - 手动升级和维护时间较短，例如从Mimic升级到Nautilus仅需40分钟。

6. **生产环境中的真实故事**：
   - 从HDD迁移到SSD的不同策略。
   - 节点更换和命名一致性的重要性。
   - 减少PG数量以适应新的OSD配置。
   - 集群间服务迁移的策略，使用Zstandard压缩算法进行数据迁移。

7. **问答环节**：
   - 讨论了PG数量和内存使用的相关问题。
   - 分享了关于PG比例和内存使用的实际经验。

#### 决定事项：
- 小型集群在多数据中心中的应用具有实际优势，特别是在避免脑裂问题、易于管理和扩展方面。
- 小型集群的维护和升级相对简单，适合手动管理。

#### 后续行动计划：
- 继续监控和优化小型集群的性能和资源使用。
- 考虑在未来的升级中采用更高效的数据迁移策略。

#### 会议结束：
- 感谢参与者的提问和分享，鼓励进一步的技术交流和合作。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。