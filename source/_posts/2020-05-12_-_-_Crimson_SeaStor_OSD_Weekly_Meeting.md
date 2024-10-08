---
title: "2020-05-12 :: Crimson SeaStor OSD Weekly Meeting"
date: 2020-05-13
updated: 2020-05-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph分布式存储系统的开发与优化

#### 参会人员：Ceph研发团队成员

#### 会议日期：[具体日期]

#### 会议地点：视频会议

#### 主要议题及讨论内容：

1. **单元测试与代码重构**
   - **发言人：[姓名]**
   - **内容摘要：** 正在增加更多的单元测试，并计划基于现有能力重写变异和复制逻辑。计划采用基于树的实现方式来处理分配和释放操作。同时，讨论了PR 334492的相关内容，将在会议后进行详细审查。

2. **代码更新与功能实现**
   - **发言人：[姓名]**
   - **内容摘要：** 更新了exact map tree的实现，正在尝试理解管理器接口并进行树形编码。关于树形实现的讨论，提到了与现有代码的相似性和可能的借用。

3. **系统状态与功能清理**
   - **发言人：[姓名]**
   - **内容摘要：** 成功实现了对象到两个副本的切换，并清理了分支，实现了一些缺失的功能。正在将分支合并到主分支，但由于基于较旧的恢复分支版本，需要追赶许多更新。

4. **代码审查与项目进展**
   - **发言人：[姓名]**
   - **内容摘要：** 审查了一个PR，认为虽然改动不大，但方向正确。讨论了内存泄漏问题，预计本周解决。

5. **服务理解与状态机代码迁移**
   - **发言人：[姓名]**
   - **内容摘要：** 主要通过阅读代码来理解服务，以便实际迁移状态机代码。计划通过提问来进一步理解服务和基础设施。

6. **单元测试与逻辑实现**
   - **发言人：[姓名]**
   - **内容摘要：** 成功实现了笔记分割的单元测试，正在处理增量图逻辑，涉及移除纸质映射。讨论了基于树形结构的实现细节。

7. **树形结构的实现与优化**
   - **发言人：[姓名]**
   - **内容摘要：** 实现了块布局和索引查找，计划基于当前工作实现插入和分割。讨论了如何最小化字符串比较的努力。

8. **优雅关机策略讨论**
   - **发言人：[姓名]**
   - **内容摘要：** 讨论了如何实现优雅关机，提出了通过设置停止标志或从信使中注销调度器来防止进一步事件处理。讨论了如何跟踪事件消费并让每个组件自行处理。

#### 决定事项：
- 继续推进单元测试和代码重构工作。
- 解决内存泄漏问题，并确保代码合并到主分支的顺利进行。
- 深入理解服务和基础设施，以便更好地迁移状态机代码。
- 实现树形结构的插入和分割功能，优化字符串比较。
- 确定优雅关机的具体实现策略，包括如何处理事件消费和组件关机。

#### 后续行动计划：
- 完成PR 334492的详细审查。
- 解决内存泄漏问题，并确保所有功能按预期工作。
- 继续阅读代码，理解服务和基础设施。
- 实现树形结构的插入和分割功能，并进行优化。
- 确定优雅关机的具体实现细节，并进行实施。

#### 会议结束语：
感谢大家的参与和贡献，期待下次会议能看到更多的进展和成果。

---

**备注：** 会议中提到的具体姓名和日期等信息已省略，以保护隐私和安全。