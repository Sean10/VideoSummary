---
categories:
- 视频总结
date: 2019-06-13
subtitle: Ceph_Octopus_Roadmap_Planning_series_-_RADOS_GateWay_RGW
tags:
- Ceph
- 分布式存储
- RGW
title: "'Ceph Octopus Roadmap Planning series: RADOS GateWay (RGW)'"
updated: 2019-06-14
---




### 会议纪要

**会议时间**： [请填写会议时间]

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph分布式存储系统开发讨论，重点讨论Octopus版本的功能规划和RADOS Gateway (RGW)。

**会议内容**：

**一、议题讨论**

1. **Nautilus版本功能更新**：
    - 讨论了Nautilus版本的功能更新，包括OPA、Ozzy和AC等特性。
    - 确认了Nautilus版本中的一些功能合并情况，例如Nautilus和Noah的PLC合并。
    - 讨论了Nautilus版本中的同步请求合并，尚未宣布胜利。
    - 认为远程组功能可能不会在Octopus版本中实现。

2. **Octopus版本功能规划**：
    - 讨论了Octopus版本的功能规划，包括S3 Select、复制、动态RBD等。
    - 认为S3 Select和复制功能将在Octopus版本中实现。
    - 讨论了动态RBD的解决方案，认为它需要先完成一些项目。
    - 认为多站点部署的兼容性问题需要考虑向后兼容性。

3. **元数据变更**：
    - 讨论了元数据变更的步骤，包括将区域复制策略从区域组中分离出来。
    - 认为元数据变更可能会影响bucket的复制策略和后端存储。
    - 讨论了后端存储的插件化，认为需要先实现一个最小可行产品（MVP）。

4. **测试**：
    - 讨论了测试计划，包括混合集群测试、升级测试、scrub测试等。
    - 认为需要测试混合集群的兼容性，并支持至少三个版本的向后兼容。
    - 认为scrub测试的重要性，需要确保数据的一致性和完整性。

**二、决策事项**

1. 将Nautilus版本中的功能更新合并到Trello任务板中。
2. 将Octopus版本的功能规划细化，并确定优先级。
3. 制定元数据变更的详细步骤，并确定MVP。
4. 制定测试计划，并确保测试覆盖所有关键场景。

**三、后续行动计划**

1. 各参会人员根据会议讨论内容，完善Trello任务板，并分配任务。
2. 定期召开会议，跟踪项目进度，并解决遇到的问题。
3. 加强团队沟通，确保项目顺利进行。

**四、备注**

1. 会议中涉及的部分计算机科学/ceph相关领域英文原文关键词：
    - Nautilus
    - Octopus
    - S3 Select
    - Replication
    - Dynamic RBD
    - Metadata
    - MVP
    - Testing
    - OPA
    - Ozzy
    - AC
    - PLC
    - STS
    - Keystone
    - RGW
    - Hadoop
    - Scrub
2. 会议中提到的部分项目：
    - OPA
    - Ozzy
    - AC
    - PLC
    - STS
    - Keystone
    - RGW
    - Hadoop
    - Scrub
3. 会议中提到的部分人员：
    - Rebecca
    - Robin
    - Eric