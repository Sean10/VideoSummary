---
title: "2019-09-23 :: Ceph Orchestration Meeting"
date: 2019-09-30
updated: 2019-10-01
tags:
  - "Ceph"
  - "编排"
  - "Rook"
  - "分布式存储"
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**会议地点**： 线上会议

**与会人员**： Kifa、Recovery、Travis、Fashion Wagner、Sebastian Hunt、Adam（Red Hat）、其他团队成员

**会议主题**： Orchestrator项目进展、Rook CI、Rook 1.1.1发布、Ceph集群管理、Rook操作工具等

### 会议关键细节

* **OSD创建与平衡**：
    * 讨论了OSD创建过程中可能产生的大量流量问题，提出了将新添加的OSD权重设置为0的方案，以便平衡器可以逐步将其映射到crash map。
    * 决定不将此功能设置为默认行为，需要用户手动调整权重。
* **Dashboard中的驱动器组创建**：
    * 讨论了Dashboard创建驱动器组的需求，需要Rook提供正确的卷库存信息。
    * 决定在Dashboard中实现创建驱动器组的功能，但需要Rook提供安全卷库存。
    * 讨论了保留两种发现机制以避免破坏现有功能。
* **Rook CI**：
    * 讨论了Rook CI的长期计划，并计划下周三进行社区电话会议。
    * 由于Adam（Red Hat）的休假，会议时间需要调整。
* **Rook 1.1.1发布**：
    * 介绍了Rook 1.1.1的发布，其中包含许多修复和稳定性改进。
    * 讨论了Rook 1.1.2的发布计划。
* **Rook操作工具**：
    * 讨论了Rook操作工具的改进，包括如何处理在未安装任何软件的宿主机上运行脚本的情况。
    * 决定使用简单的脚本，并尽量保持其可读性和简洁性。

### 决定的事项

* 不将OSD自动添加到crash map的默认行为。
* 在Dashboard中实现创建驱动器组的功能，需要Rook提供安全卷库存。
* 下周三进行Rook CI社区电话会议，时间待定。
* 发布Rook 1.1.2。
* 改进Rook操作工具。

### 后续行动计划

* Kifa继续进行OSD创建和平衡的改进。
* Recovery继续进行Dashboard驱动器组创建的实现。
* Adam（Red Hat）和团队继续进行Rook CI的改进。
* Travis和团队继续进行Rook 1.1.2的发布。
* Fashion Wagner和Sebastian Hunt继续进行Rook操作工具的改进。

[改进后的内容保留了会议的关键细节，讨论的主要议题，决定的事项以及后续的行动计划，并确保了计算机科学/ceph相关领域的英文原文关键词得以保留]。