---
categories:
- 会议纪要
- 存储技术
date: 2019-09-30
subtitle: 2019-09-24_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
tags:
- Ceph
- 分布式存储
- OSD
- 测试
title: "'2019-09-24 :: Crimson SeaStor OSD Weekly Meeting'"
updated: 2019-10-01
---




会议纪要

**会议时间**： 2019年9月24日

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph分布式存储项目进展及问题讨论

**会议内容**：

**一、项目进展**

1. **Riddick Spear计划和Ackerson计划**：
    - 正在撰写，旨在支持写入操作，定义项目范围和估算时间线。
    - 计划本周完成并提交给利益相关者。

2. **性能测试**：
    - 对Ceph存储性能进行了测试，发现了一些问题，将进行进一步调查和修复。

3. **Riddick pantry writer问题**：
    - 存在返回响应问题，需要进一步调试，尝试使用未修改的Constantine虚拟版本进行调试。

4. **Ceph OSD操作接口**：
    - 正在修改，以支持状态错误和状态迁移，提高代码可读性。

5. **Ceph恢复机制**：
    - 正在重构，以创建更清晰的接口，提高异步操作处理效率。

**二、讨论的主要议题**

1. **Ceph经典OSD与Crimson接口整合**：
    - 讨论如何整合接口，简化代码并提高可读性，决定使用状态机来封装异步操作。

2. **Ceph调度器与Gemini Cook集成**：
    - 讨论如何集成，以更有效地处理异步操作，决定研究集成方案。

3. **Ceph性能测试**：
    - 讨论性能测试的重要性，决定开展更多测试以评估性能。

**三、决定的事项**

1. 完成Riddick Spear和Ackerson计划。
2. 解决Riddick pantry writer问题。
3. 修改Ceph OSD操作接口。
4. 重构Ceph恢复机制。
5. 研究Ceph调度器与Gemini Cook的集成方案。
6. 开展更多Ceph性能测试。

**四、后续行动计划**

1. 项目负责人推进Riddick Spear和Ackerson计划的编写。
2. 技术人员调试Riddick pantry writer问题。
3. 技术人员修改Ceph OSD操作接口和重构Ceph恢复机制。
4. 技术人员研究Ceph调度器与Gemini Cook的集成方案。
5. 技术人员开展更多Ceph性能测试。