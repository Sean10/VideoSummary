---
title: "Ceph Orchestrator Meeting 2020-10-05"
date: 2020-10-06
updated: 2020-10-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Rook Manager Module 的状态和未来

#### 参会人员：未明确列出，但提到了Patrick、Travis、Joshua等人。

#### 会议时间：未明确列出，但提到了几天前发送的邮件。

#### 会议地点：未明确列出，通过视频会议进行。

#### 主要议题：
1. **Rook Manager Module 的现状和需求**
   - 该模块两年前创建，但未得到充分维护和使用。
   - 讨论了该模块的优先级和是否仍需保留。
   - 确认了Dashboard对Rook Manager Module的兴趣。

2. **Rook Manager Module 的启用状态和社区反馈**
   - 该模块未默认启用，上游社区未注意到或询问为何不默认启用。
   - 发现了该模块的多个bug，但缺乏测试。

3. **资源和优先级问题**
   - 讨论了资源有限，当前主要优先级是FDM（Federated Deployment Manager）。
   - Red Hat和SUSE的资源分配问题，特别是Red Hat目前主要集中在FDM上。

4. **Rook Manager Module 的功能和测试需求**
   - 需要确定Rook Manager Module的具体使用场景和功能需求。
   - 强调了测试的重要性，特别是与Rook和Cephadm的集成测试。

5. **Rook Manager Module 的未来方向**
   - 讨论了是否应该继续支持Rook Manager Module，以及如何分配资源。
   - 提出了可能的解决方案，如使用外部资源或调整资源分配。

#### 决定事项：
- 需要进一步明确Rook Manager Module的使用场景和功能需求。
- 需要加强测试，特别是与Rook和Cephadm的集成测试。
- 需要讨论资源分配问题，特别是如何平衡FDM和Rook Manager Module的开发资源。

#### 后续行动计划：
- 继续讨论Rook Manager Module的未来方向和资源分配。
- 加强测试，特别是与Rook和Cephadm的集成测试。
- 需要明确Dashboard对Rook Manager Module的需求和使用场景。

#### 其他讨论：
- 讨论了SSH和HTTPS在获取主机信息方面的性能和安全性问题。
- 需要进一步在真实硬件上测试SSH的性能，以决定是否继续使用或切换到HTTPS。

#### 会议总结：
会议主要讨论了Rook Manager Module的现状、需求、资源分配和未来方向。强调了测试的重要性，并提出了需要进一步明确的使用场景和功能需求。同时，讨论了SSH和HTTPS在获取主机信息方面的性能和安全性问题，并提出了需要在真实硬件上进行进一步测试的建议。

---

以上是根据会议内容总结的会议纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。