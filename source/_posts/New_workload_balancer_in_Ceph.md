---
categories:
- 视频总结
date: 2022-11-15
subtitle: New_workload_balancer_in_Ceph
tags:
- Ceph
- Distributed Storage
- CRUSH Algorithm
- Workload Balancer
- Performance Optimization
title: "New workload balancer in Ceph"
updated: 2022-11-16
---




### 会议纪要

#### 会议参与者
- Joe Solomon：前架构师，现为Red Hat的CTO办公室新兴技术团队成员。
- Laura Flores：Red Hat的RADOS核心团队成员，专注于上游测试。

#### 会议主题
- 介绍Reef版本中即将引入的新工作负载平衡器。

#### 讨论内容
1. **动机与背景**
   - 当前Ceph在高负载下性能受限于最弱环节。
   - 现有容量平衡器保证OSD间容量均匀分布，但未解决读取平衡问题。
   - CRUSH算法在大型集群中平衡读取，但在小型集群中表现不佳。

2. **现有问题与改进**
   - 对多种系统OSD Mark文件进行测试。
   - 重构现有平衡器代码，提高可读性和可修改性。
   - 创建新的工作负载平衡器，考虑读取操作。

3. **新rebalancer设计**
   - 新rebalancer主要针对小型集群，设计基于池的读取平衡。
   - 考虑读写工作负载差异，未来版本将考虑设备大小和性能波动。

4. **功能与实现**
   - 引入新命令改变PG的主OSD，不涉及数据移动。
   - 实现两个主要函数：`calc desired primary distribution`和`balanced primaries`。

5. **演示与测试**
   - 展示了新rebalancer在不同场景下改善读取平衡。
   - 强调未来将进行更多上游测试和性能测试。

#### 决定事项
- 新rebalancer将在Reef版本中作为离线工具提供，未来计划集成到自动平衡模块中。
- 未来版本将考虑设备大小和动态性能调整。

#### 后续行动计划
- 继续进行上游测试和性能测试。
- 考虑将新rebalancer集成到自动平衡模块中。
- 探索更复杂的平衡策略，如基于设备大小和动态性能调整。

#### 其他讨论点
- 讨论了primary affinity的潜在改进和客户端读取策略的复杂性。
- 强调了未来版本中可能考虑的更高级平衡策略。

#### 会议结束
- 感谢所有参与者的提问和讨论。
- 分享了相关GitHub仓库链接，以便进一步交流和反馈。



本次会议纪要准确反映了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划，并保留了Ceph相关领域的英文原文关键词。