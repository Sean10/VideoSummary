---
title: "Ceph Orchestrator Meeting 2023-02-21"
date: 2023-02-21
updated: 2023-02-22
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph 主机维护模式增强功能讨论

#### 与会人员：Ceph 研发团队成员

#### 会议时间：[具体日期]

#### 会议地点：视频会议

#### 主要议题：
1. **主机维护模式（Host Maintenance Mode）的强制执行问题**
   - 当前主机维护模式的强制标志（force flag）仅能强制停止其下的功能，但在某些情况下，即使使用强制标志，主机仍无法进入维护模式。
   - 提出了增加一个新的标志，以便在必要时能够强制进入维护模式，即使存在可能导致PG（Placement Groups）降级的条件。

#### 讨论细节：
- **当前问题描述**：
  - 强制标志（force flag）在主机维护模式中仅能强制停止其下的功能，但在某些情况下，即使使用强制标志，主机仍无法进入维护模式。
  - 存在一些情况，例如PG降级，导致无法将主机置于维护模式。

- **提出的解决方案**：
  - 建议增加一个新的标志，例如“紧急”（emergency）或“我确实真的需要这个”（yes I really really mean it），以允许在必要时强制进入维护模式。
  - 该标志将允许用户在即使存在可能导致PG降级的条件下，也能强制停止所有守护进程（demons），以便进行必要的维护工作。

- **标志命名讨论**：
  - 讨论了多个标志名称，包括“紧急”（emergency）和“我确实真的需要这个”（yes I really really mean it）。
  - 最终倾向于使用“我确实真的需要这个”（yes I really really mean it），因为它在Ceph社区中更为常见，且能更好地传达操作的危险性。

- **操作细节**：
  - 该标志将允许用户在不考虑安全检查的情况下，强制停止所有守护进程，以便进行维护。
  - 该操作不会移除任何东西，只是停止守护进程，使其暂时不参与集群活动。

#### 决定事项：
- 增加一个新的标志，用于在必要时强制进入主机维护模式，即使存在可能导致PG降级的条件。
- 标志名称倾向于使用“我确实真的需要这个”（yes I really really mean it）。

#### 后续行动计划：
- 实现新的标志功能，并在代码中添加相应的警告和提示信息。
- 更新文档，明确新标志的使用场景和潜在风险。

#### 其他讨论：
- 讨论了其他可能的标志名称和使用场景，但最终决定采用“我确实真的需要这个”（yes I really really mean it）。

#### 会议结束：
- 会议在讨论完所有议题后结束，没有其他待讨论的新议题。

#### 下次会议预告：
- 下次会议将根据项目进度和新的开发需求进行安排。

---

**会议记录人：[记录人姓名]**

**审核人：[审核人姓名]**

**日期：[具体日期]**