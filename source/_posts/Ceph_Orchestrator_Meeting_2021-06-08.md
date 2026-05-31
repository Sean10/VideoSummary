---
categories:
- 视频总结
date: 2021-06-08
subtitle: Ceph_Orchestrator_Meeting_2021-06-08
tags:
- Ceph
- 编排
title: "Ceph Orchestrator Meeting 2021-06-08"
updated: 2021-06-09
---



### 改进后的会议纪要

#### 会议主题：Rook Manager 模块讨论

#### 会议时间：本周协调会议

#### 参会人员：全体成员

#### 主要议题：

1. **Gherkin 语言实现介绍**
   - Aaron 介绍了 Gherkin 语言，一种测试场景定义语言，使用自然语言定义系统行为，使非技术人员也能参与测试。
   - 使用 Given、When 等关键字运行场景并断言结果，例如登录节点执行命令并验证版本匹配。
   - 讨论了使用 kcli 和虚拟机创建测试环境，以及 Behave 框架和 Gherkin 语言在测试场景中的应用。

2. **测试框架集成**
   - 讨论使用 kcli 和虚拟机快速创建测试环境。
   - 依赖于 Python 的 Behave 框架，使用 Gherkin 语言定义测试场景并通过 Python 实现执行。
   - 讨论了项目文件结构和在社区中实施此项目的方案。

3. **Rook Manager 模块状态与未来方向**
   - 讨论在 Jenkins 中集成测试框架，确保测试自动验证。
   - 讨论Rook在裸机部署中的适用性以及设备管理。
   - 确定需要解决的关键问题，如OSD创建和块数据库设备管理。

#### 决定事项：

- 确定在 Jenkins 中集成测试框架。
- 确认需要新的接口来处理 Kubernetes 环境中的 PV 和动态供应。
- 确定需要与 Rook 和 LSO 相关人员进行进一步讨论，以确定在不同环境中使用 Rook。

#### 后续行动计划：

- Aaron 将继续推进 Gherkin 语言的实现和测试框架的集成。
- 确定与 Rook 和 LSO 相关人员的会议，讨论在不同环境中使用 Rook。
- Joseph 将继续调查 Rook 中的 orange ls 和 rgps 命令问题，并确保这些命令在沙箱环境中正常工作。

#### 其他讨论点：

- 讨论了 Rook 在不同环境中的使用，特别是在 OpenShift 中。
- 确认了需要进一步讨论如何在不同环境中管理设备和 OSD。

#### 会议结束：

- 会议在确认下一步行动计划后结束。

#### 下次会议：

- 下周继续讨论 Rook Manager 模块的进展和其他相关议题。