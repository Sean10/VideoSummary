---
title: "Ceph Orchestrator Meeting 2022-01-11"
date: 2022-01-11
updated: 2022-01-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Orchestrator 会议
#### 日期：[具体日期]
#### 参会人员：[具体人员名单]

#### 主要议题：
1. **Quincy 版本特性冻结**
   - 讨论了 Quincy 版本的特性冻结时间，原计划是本周结束，但具体时间取决于其他组件如 RBG 和 FFS 是否能按时完成。
   - 需要完成的任务包括对 self-adm 二进制文件的重构，这需要在 Quincy 发布前完成。

2. **Quincy 版本的其他待办事项**
   - 讨论了 agent 和特定的 pull request 是否需要合并以满足特性冻结。
   - 强调了文件权限问题和主机缓存大小问题的重要性。

3. **Rook Manager Module 的测试和使用**
   - 讨论了 Rook Manager Module 在 Quincy 版本中的测试情况，目前仅在 CI 中测试。
   - 该模块对于 multi-site 配置非常重要，但不会包含在 Quincy 的初始版本中。

4. **Quincy 版本的后续行动计划**
   - 确认了从兼容性和稳定性角度出发，所有新特性都可以在未来的版本中轻松回溯。
   - 讨论了不同 Rook 版本的兼容性问题，确认 Rook 的接口是向后兼容的。

5. **ISCSI 的回归问题**
   - 讨论了 ISCSI 的回归问题，目前尚未解决，需要进一步调查。

6. **Backporting 问题**
   - 讨论了 backporting 的复杂性，特别是由于 Pacific 和 Quincy 版本之间的差异，导致需要单独处理每个 pull request 的 backporting。
   - 确认了一些具体的 pull request 需要进行 backporting，并讨论了分配任务的可能性。

#### 决定事项：
- 确认了 Quincy 版本的特性冻结时间将取决于其他组件的完成情况。
- 确认了 self-adm 二进制文件的重构需要在 Quincy 发布前完成。
- 确认了 Rook Manager Module 的重要性，但不会包含在 Quincy 的初始版本中。
- 确认了 ISCSI 的回归问题需要进一步调查。
- 确认了 backporting 的复杂性，并讨论了分配任务的可能性。

#### 后续行动计划：
- 继续监控其他组件的进度，以确定 Quincy 版本的特性冻结时间。
- 完成 self-adm 二进制文件的重构工作。
- 继续测试和验证 Rook Manager Module 的功能。
- 调查并解决 ISCSI 的回归问题。
- 分配并完成 backporting 任务。

#### 会议结束：
- 会议在确认无其他议题后结束，感谢所有参会人员，并约定下周再次开会。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。