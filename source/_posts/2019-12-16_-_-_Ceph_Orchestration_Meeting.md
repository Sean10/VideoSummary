---
title: "2019-12-16 :: Ceph Orchestration Meeting"
date: 2020-01-10
updated: 2020-01-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间与参与人员
- **时间：** 会议开始于预定时间，但有几分钟延迟。
- **参与人员：** 会议由主持人主持，Brooke等团队成员参与。

#### 主要议题与讨论内容
1. **Ceph 1.2 版本发布计划**
   - Brooke 计划在未来几天内完成1.2版本的发布，目前正在进行最后的修复工作。
   - 讨论了关于自动删除OSD的代码变更，决定不再自动删除OSD，以避免数据丢失，改为用户手动操作。

2. **设计文档与未来规划**
   - 讨论了OSD移除的设计文档，目前正在等待进一步的反馈和时间来重新审视。
   - 提及了多站点RGW的设计进展，由Radia负责，可能对未来的对象存储CR有影响。

3. **Ceph Orchestrator 与 Dashboard 集成**
   - 讨论了将新的CR添加到对象存储CR中，以支持跨集群配置。
   - 计划在本周内由Elly开放设计PR，以便团队成员可以更积极地参与讨论和反馈。

4. **Ceph Manager 模块的测试与集成**
   - 讨论了Ceph Manager模块的测试问题，目前缺乏有效的QA和CI集成。
   - 提出了在Rook CI中集成Ceph Manager模块的建议，以便进行更有效的测试。

5. **其他技术细节与问题**
   - 讨论了Ceph Orchestrator的并行化问题，以及如何在多节点环境中进行有效的部署和管理。
   - 提及了Ganesha的集成问题，计划在未来进行更深入的探讨和实施。

#### 决定事项
- 不再自动删除OSD，改为用户手动操作。
- 计划在本周内由Elly开放设计PR，以便团队成员可以更积极地参与讨论和反馈。
- 提出了在Rook CI中集成Ceph Manager模块的建议，以便进行更有效的测试。

#### 后续行动计划
- 完成Ceph 1.2版本的发布工作。
- Elly将在本周内开放设计PR。
- 进一步探讨和实施Ceph Manager模块的测试和集成方案。
- 对Ganesha的集成问题进行更深入的探讨和实施。

#### 其他备注
- 会议中还讨论了一些技术细节和问题，但未形成具体的决定或行动计划。
- 会议结束时，主持人感谢大家的参与，并宣布会议结束。

### 会议结束
- **时间：** 会议在讨论完所有议题后结束。
- **参与人员：** 所有参与人员确认会议结束。