---
title: "2019-04-15:: Ceph Orchestration Meeting"
date: 2019-04-15
updated: 2019-04-16
tags:
  - "Ceph"
  - "编排"
  - "Rook"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Travis, Blaine, Alec, Jeff, 以及其他相关人员

**会议主题**： Ceph 项目进展、Rook 升级测试、Barcelona 会议安排等

**关键细节与讨论议题**：

**1. Orchestrator 与 Rook**：
* Travis 分享了一个 Orchestrator 的视频，展示了如何通过命令创建 OSD、更新集群自定义资源，并由 Operator 执行操作。目前，大部分功能已实现，但仍需进一步测试。
* 讨论了 Rook 的 CI 问题，目前 CI 构建完全受阻，需要优先修复。
* 讨论了 Rook 升级过程中的问题，例如从 Mimic 升级到 Nautilus 后，需要运行特定命令才能启用 Messenger，否则 Operator 无法与 Mon 进行通信。
* Blaine 提到正在进行的 Rook 升级测试，并计划进行文档更新。

**2. Nautilus 版本**：
* 讨论了将 Nautilus 作为默认版本的计划，以便新用户默认使用 Nautilus。
* Travis 指出，下一个 Nautilus 版本已被标记，并正在进行 URI 测试，预计将与 Nautilus 的发布点一起合并。

**3. Barcelona 会议**：
* 讨论了在 Barcelona 举行会议的可能性，并计划在 Red Hat 巴塞罗那办公室进行面对面的讨论。
* 计划于周六下午 3:30 后举行会议，持续约 2 小时。

**4. 其他议题**：
* 讨论了 Manager Pod 故障的问题，并考虑在 Rook 中运行多个 Manager Pod。
* 讨论了文档更新，特别是针对 1.0 版本的升级测试和文档。

**决定事项**：
* 修复 Rook 的 CI 问题。
* 继续进行 Rook 的升级测试，并更新文档。
* 确定 Barcelona 会议的具体时间和地点。
* 调查 Manager Pod 故障问题。

**后续行动计划**：
* Travis 将继续修复 Rook 的 CI 问题。
* Blaine 将继续进行 Rook 的升级测试，并更新文档。
* 相关人员将确定 Barcelona 会议的具体时间和地点。
* 相关人员将调查 Manager Pod 故障问题。

**备注**：
* 会议中提到的部分计算机科学/ceph相关领域英文原文的关键词包括：Orchestrator, Operator, OSD, Mon, Messenger, Rook, CI, Nautilus, Barcelona, Manager Pod 等。



[相关标签]
- Ceph
- Orchestrator
- Rook
- Nautilus
- Barcelona 会议