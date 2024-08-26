---
title: "2020-05-04 :: Ceph Orchestration Meeting"
date: 2020-05-07
updated: 2020-05-08
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **会议主题**: Orchestrator 周会
- **日期**: [具体日期]
- **参会人员**: [参会人员名单]

#### 讨论议题
1. **Orchestrator CLI 简化**:
   - 讨论了关于通过参数（如 `--pool` 或 `--namespace`）和通过 YAML 文件（如 `apply -e`）两种方式创建新服务的问题。
   - 决定简化 CLI，建议只使用 YAML 文件（spec）或参数，避免两者混用，以减少复杂性和潜在的冲突。
   - 计划移除不再使用的特定参数版本，如 `apply -I`。

2. **版本发布计划**:
   - 讨论了即将发布的 Ceph 版本 15.2 的发布时间，预计本周内发布。
   - 决定在版本发布后合并下一个大的代码提交。

3. **测试和集成**:
   - 讨论了将 Orchestrator 测试集成到 Rook CI/CD 的工作进展，Phillip 正在负责此项工作。
   - 提到了使用 Ceph-Demon 模块简化虚拟机设置的方法，计划分享给团队。
   - 讨论了将 Safe ADM 方法用于更广泛的测试，特别是希望将 Dashboard 集成到 Safe ADM 中，以进行更真实的测试。

4. **Safe ADM 和 Tautology 集成**:
   - 讨论了 Safe ADM 与 Tautology 的集成，以及如何通过这种集成提高测试的覆盖率和可靠性。
   - 提到了一个关于 RGW 的 bug，如果 Safe ADM 中有相应的测试，可能会更早发现。

5. **Safe Deploy 的使用**:
   - 讨论了 Safe Deploy 的使用情况，目前并未被广泛支持或使用，建议不再关注。

#### 决定事项
- 简化 Orchestrator CLI，移除不再使用的参数。
- 在 Ceph 15.2 发布后，合并下一个大的代码提交。
- 继续推进 Orchestrator 测试与 Rook CI/CD 的集成工作。
- 探索和实施 Safe ADM 在更广泛测试中的应用，特别是 Dashboard 的集成。

#### 后续行动计划
- 完成 Ceph 15.2 的发布工作。
- 合并并发布下一个大的代码提交。
- 继续推进 Orchestrator 测试与 Rook CI/CD 的集成。
- 探索 Safe ADM 在 Dashboard 和其他组件中的应用。
- 寻找资源解决 RGW 相关的 bug，并增加相应的测试。

#### 其他事项
- 讨论了 Safe ADM 和 Tautology 的集成进展，以及 Safe Deploy 的当前状态。
- 确认了 Safe ADM 作为测试工具的潜力和未来发展方向。

#### 会议结束
- 会议在确认所有议题讨论完毕后结束，下一次会议时间待定。

---

以上是本次 Orchestrator 周会的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。