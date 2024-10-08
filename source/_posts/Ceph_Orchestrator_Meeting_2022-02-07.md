---
title: "Ceph Orchestrator Meeting 2022-02-07"
date: 2022-02-12
updated: 2022-02-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph 升级相关问题讨论

#### 参会人员：Ceph 研发团队成员

#### 主要议题：
1. **升级过程中的OSD依赖问题**
2. **升级过程的粒度控制**

#### 讨论内容：

##### 1. OSD依赖问题
- **问题描述**：在升级过程中，OSD依赖于CRUSH map，导致在升级监控器后所有OSD需要重新配置，这在大型集群中（如3900个OSD）会显著减慢升级速度，并影响用户体验。
- **解决方案**：考虑延迟OSD的重新配置直到升级完成，以减少不必要的重新配置时间。
- **潜在风险**：需要评估延迟重新配置可能带来的风险，并确保在升级过程中不会对集群稳定性造成影响。

##### 2. 升级过程的粒度控制
- **问题描述**：大型集群的用户可能希望更细粒度地控制升级过程，例如按主机或按守护进程类型进行升级，以便更好地管理升级过程和减少潜在的风险。
- **解决方案**：考虑实现按主机或按守护进程类型的升级选项，同时确保升级顺序的正确性，特别是管理器和监控器必须在其他守护进程之前升级。
- **用户界面**：改进升级状态显示，提供更详细的升级进度信息，包括预计升级的守护进程数量和类型。

#### 决定事项：
- **OSD依赖问题**：将探索延迟OSD重新配置的可行性，并评估其潜在风险。
- **升级粒度控制**：将实现按主机和按守护进程类型的升级选项，并确保升级顺序的正确性。

#### 后续行动计划：
- **技术调研**：进一步研究延迟OSD重新配置的技术细节和潜在风险。
- **功能开发**：开发按主机和按守护进程类型的升级选项，并确保升级顺序的正确性。
- **用户界面改进**：改进升级状态显示，提供更详细的升级进度信息。

#### 其他讨论点：
- **升级过程中的离线主机处理**：讨论了在升级过程中如何处理离线主机的问题。
- **升级状态显示**：讨论了如何改进升级状态显示，以便用户更好地了解升级进度。

#### 会议结束：
- 确认了下一步的行动计划，并安排了下次会议的时间。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。