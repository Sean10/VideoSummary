---
title: "Ceph Developer Summit Quincy: Orchestrator Follow-up"
date: 2021-04-28
updated: 2021-04-28
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题
跟进EDS（Enterprise Data Services）并制定Quincy的路线图。

#### 参会人员
全体成员

#### 会议内容
1. **路线图制定**
   - 会议开始时，主持人确认目标是制定Quincy的路线图。
   - 主持人已经通过Orchestrated Quincy和其他工具整理了CDS（Ceph Development Sprint）列表中的事项，并浏览了Tracker和Trello，总结出高层次的任务列表。

2. **任务优先级划分**
   - 建议对任务进行高、中、低优先级的划分，以便后续决策。
   - 讨论了多个任务的优先级，包括：
     - **Refractor safe adm into a proper python package**：被认为是开发者体验相关，优先级待定。
     - **Managed client curing**：已在进行中。
     - **Clarify host maintenance mode**：主持人个人关注点，不确定其与调度器的交互是否正确。
     - **NFS-HA**：认为重要，但已有进展。
     - **Postspec crash info**：认为是一个重要的功能缺口。
     - **Agent exporter**：认为非常重要，与NFS-HA同等重要。

3. **后续行动计划**
   - 确认使用Trello来跟踪和管理高层次任务。
   - 讨论了如何改进架构，而不是仅仅提高速度，特别是在处理大规模集群时。
   - 确认了一些任务的当前状态和未来计划，如监控服务的IP绑定、RGW多站点规范的制定等。

4. **其他讨论点**
   - 讨论了如何从集群内部安全地移除集群，建议使用外部工具来执行此操作。
   - 讨论了监控堆栈的定制化需求，建议通过配置选项来统一管理容器镜像。

#### 决定事项
- 使用Trello来管理任务优先级和进度。
- 确认了一些任务的优先级和当前状态。
- 讨论了如何改进架构和处理大规模集群的问题。

#### 后续行动
- 继续在Trello上更新和调整任务优先级。
- 开始实施高优先级任务，如改进架构和处理大规模集群的问题。
- 确认并实施监控堆栈的定制化需求。

#### 会议结束
会议在讨论了所有议题后结束，全体成员对会议结果表示满意，并期待接下来的工作进展。