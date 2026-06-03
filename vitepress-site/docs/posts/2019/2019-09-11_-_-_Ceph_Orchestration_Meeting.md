---
title: "2019-09-11:: Ceph Orchestration Meeting"
date: 2019-09-20
updated: 2019-09-21
tags:
  - "Ceph"
  - "编排"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： [请填写具体日期和时间]

**参会人员**： [请填写参会人员名单]

**会议主题**：

*   Ceph集群中设备管理及Orchestrator模块的优化
*   完成项（Completion）的实现和改进
*   Dashboard的锁机制
*   Rook模块的性能问题
*   Dashboard的分页功能

**会议内容**：

**一、设备管理**

*   讨论如何通过Orchestrator模块实现设备管理，包括创建新的OSD。
*   确定了从简单设备组开始，逐步过渡到更复杂的设备组的策略。
*   计划实现从单个设备创建OSD的功能，并考虑支持多选设备创建多个OSD。
*   强调了确保设备可用性的重要性。

**二、完成项（Completion）实现**

*   讨论了Ceph中完成项的改进，包括合并读取和写入完成项，使用统一的完成项类。
*   引入了新的完成项结构，其中完成项在获得结果后立即完成，但进度引用（Progress Reference）会保持活跃，直到OSD实际创建完成。
*   讨论了使用进度引用进行锁定的必要性，以避免在Dashboard中同时执行多个OSD创建操作。

**三、Dashboard的锁机制**

*   讨论了在Dashboard中实现锁机制的必要性，以避免同时进行多个系统更改操作。
*   确定了一种基于进度引用的锁定策略，用于在Dashboard中阻止创建新的OSD，直到当前操作完成。
*   讨论了不同Orchestrator模块中锁定机制可能存在的差异，并计划在Orchestrator中实现通用的锁定机制。

**四、Rook模块性能问题**

*   讨论了Rook模块的性能问题，并确认引入事件监听器后性能问题已基本解决。

**五、Dashboard分页功能**

*   讨论了Dashboard中可能需要添加分页功能。

**行动计划**：

*   实现从单个设备创建OSD的功能。
*   优化完成项结构，并实现基于进度引用的锁定机制。
*   在Orchestrator中实现通用的锁定机制。
*   在Dashboard中实现分页功能。
*   查看和修复Rook模块中存在的问题。
*   根据需要添加Dashboard的分页功能。

**备注**：

*   部分内容涉及Ceph相关领域英文原文，如“Completion”、“Progress Reference”、“Orchestrator”等。
*   会议中提到的“Kiva”和“Brooke”可能是项目或模块的名称，具体含义需要根据实际情况进行解释。
*   讨论了环境变量的问题，并决定在Rook模块中修复相关问题。