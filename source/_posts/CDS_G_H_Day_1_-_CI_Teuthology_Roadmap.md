---
categories:
- 视频总结
date: 2014-06-24
subtitle: CDS_G_H_Day_1_-_CI_Teuthology_Roadmap
tags:
- Teuthology
- 测试
- 分布式存储
title: "CDS G/H (Day 1) - CI & Teuthology Roadmap"
updated: 2014-06-25
---




会议主题为Ceph CI和Teuthology路线图的讨论。与会人员包括Sage, Zach, Alfredo, L, Greg, Luis等。

**主要议题和讨论内容**：

1. **Toothology路线图**：
   - Zach介绍了Toothology的最新进展，包括任务从框架工作中分离、队列和锁定机制迁移到Paddles服务、作业调度方式改进等。
   - 讨论了Toothology测试套件对裸金属机器的依赖性，以及如何使用虚拟机进行测试。
   - 讨论了如何使Toothology更具通用性，以便测试其他分布式系统。

2. **CI流程改进**：
   - 讨论了如何改进Ceph的CI流程，确保所有代码更改在合并到主分支之前都经过充分测试。
   - 提出了使用类似Linux Next的方法建立每晚构建的临时分支，并在此分支上运行完整测试套件。
   - 讨论了使用Jenkins或Travis CI等工具实现这一目标，并确保测试结果能够及时反馈给开发者。
   - 讨论了如何处理失败的构建，以及如何将测试结果注释到相关的Pull Request中。

3. **其他讨论**：
   - 讨论了如何命名集成分支，以及如何管理历史构建。
   - 讨论了是否使用Jenkins或Travis CI作为CI工具，并考虑了各自的优缺点。
   - 讨论了如何改进Jenkins配置，以提高其效率和可维护性。

**行动计划**：

- Zach继续推进Toothology的开发工作。
- 讨论组将制定详细的CI流程改进计划，并选择合适的工具和策略。
- 相关人员将负责实现CI流程改进计划，并进行测试和验证。

**可能的错误、误解或遗漏**：

- 原始字幕内容可能存在部分错误，例如“tutoy”可能误写成“tutorials”。
- 会议中提到的具体实现细节，如分支命名、测试结果反馈等，未在总结中详细说明。

**改进后的总结**：

会议重点讨论了Ceph CI和Teuthology的改进计划。Toothology的开发工作将重点关注任务分离、队列和锁定机制迁移等。CI流程的改进将采取类似Linux Next的方法，并考虑使用Jenkins或Travis CI等工具。讨论了如何命名集成分支、管理历史构建，以及选择CI工具等问题。会议确定了后续行动计划，包括Toothology的开发、CI流程改进计划的制定和实施。