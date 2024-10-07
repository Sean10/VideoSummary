---
title: "Enabling Near-Data Processing in Ceph - Rixin Luo, Huawei"
date: 2023-05-18
updated: 2023-05-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：启用近数据处理（Near Data Processing）

#### 主讲人：Russian Law

#### 会议内容总结：

1. **近数据处理简介**：
   - 近数据处理是一种新的计算范式，允许将计算移动到数据所在的位置，或将数据放置在计算附近，以减少数据移动。
   - Ceph定义了计算存储（Computational Storage），可以在设备上添加计算功能，将主机处理卸载到设备上。

2. **挑战与现有解决方案**：
   - 近数据处理面临的主要挑战是数据放置问题。Ceph的数据流模型和擦除码（Erasure Code）会导致数据对象被分割，从而丢失部分信息。
   - Ceph当前的分布式存储系统设计侧重于高性能和高可靠性，而非近数据处理。

3. **Ceph的存储池类型**：
   - Ceph有两种存储池：副本池（Replica Pool）和擦除码池（Erasure Code Pool）。
   - 副本池提供高性能但空间利用率低，而擦除码池提供高空间利用率但性能较低。

4. **解决方案：启用近数据处理**：
   - 关键在于保持对象的完整性，不分割存储对象。通过添加聚合模块（Aggregate Module），将相同ID的对象合并为新的聚合对象。
   - 聚合规则包括：聚合对象大小等于擦除码条带大小，不进行分割。

5. **支持元数据**：
   - 元数据用于将对象ID映射到聚合对象ID，作为omap项存储。

6. **近数据处理操作**：
   - 通过在OST（Object Storage Target）中添加新的数据处理请求和模块，执行数据库查询、正则表达式匹配等操作。
   - 这些操作可以扩展第三方库，通过加载第三方库来执行近数据处理操作。

7. **测试结果**：
   - 测试使用6个OST和4+2擦除码数据条带，比较了基本擦除码和聚合擦除码的性能。
   - 结果显示，聚合擦除码在读取中间2MB数据时，减少了集群间的流量，从而减少了数据移动。

8. **后续行动计划**：
   - 继续开发和优化近数据处理功能，支持更多数据处理操作。
   - 考虑将计算功能卸载到计算存储设备上，以提高性能。

#### 讨论与问题：
- 与会者提问关于对象类（Object Classes）和Skyhook项目，主讲人表示这些方案与近数据处理的实现方式不同，但值得进一步研究和考虑。

#### 会议结束：
- 主讲人感谢大家的参与，并邀请进一步的问题和讨论。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。