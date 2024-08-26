---
title: "Ceph Crimson/SeaStore 2021-10-27"
date: 2021-11-03
updated: 2021-11-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与讨论内容

1. **Ceph PR审核与合并**
   - 已完成多项PR的审核工作。
   - 成功合并了首个Random Block Manager的PR，感谢所有参与审核的人员。
   - 针对lower bound fix的问题，已实施修复，希望解决了相关问题。

2. **Crimson测试与问题反馈**
   - 正在进行Crimson的测试，并遇到了一些问题，已在上游报告了一个bug。
   - 在配置Crimson时，按照上游文档操作，但在第三步遇到了问题。
   - 问题可能源于文档中的指令错误，Radik正在努力使Crimson与Rook兼容，之后将对此问题进行进一步检查。

3. **OSD Metadata问题**
   - 已修复OSD Metadata相关问题，但仍有其他问题需要调查。
   - 单元测试中存在一些错误，已修复并将更新PR。

4. **Journal Submitter与Metrics问题**
   - 正在调试Journal Submitter，特别是与Metrics Matrix注册失败相关的问题，这影响了LBA测试。
   - 目前正在深入调查，怀疑存在更深层次的问题。

5. **EPM Sprel Sprite LFS Strategy测试**
   - 上周主要处理了相关问题，下周将继续进行测试。

#### 决定事项

- 确认了Crimson配置文档中的指令存在错误，需要进一步修正。
- 将持续跟进OSD Metadata和Journal Submitter的相关问题，并进行深入调查。

#### 后续行动计划

- 更新并修正Crimson配置文档中的错误指令。
- 继续进行Crimson与Rook的兼容性测试。
- 深入调查并解决OSD Metadata和Journal Submitter中的问题。
- 完成EPM Sprel Sprite LFS Strategy的测试工作。

#### 其他事项

- 会议结束时，提醒大家注意沟通问题，确保所有参与者都能听到并参与讨论。

**会议结束语**
- 祝大家本周工作顺利，再见。

---

以上是本次会议的纪要，涵盖了关键细节、讨论的主要议题、决定的事项以及后续的行动计划。