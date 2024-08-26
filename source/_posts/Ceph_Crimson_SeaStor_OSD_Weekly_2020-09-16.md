---
title: "Ceph Crimson/SeaStor OSD Weekly 2020-09-16"
date: 2020-09-16
updated: 2020-09-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **Thresha Totology Basis Threat Test**: 上周仍在进行相关工作，最新问题涉及BlueStore中的一个段错误。
- **DIO Errors PR**: David Zaffman已审核并批准，但仍有需要解决的关注点。
- **Snapshots in CStore**: 讨论了在CStore中支持快照的可能性，需要进一步学习和讨论。
- **Test Case for Tree and Debug**: 正在编写测试用例，并考虑使用reader's bench重现问题。
- **Scrubbing**: 完成了昨天的scrubbing工作，有一个测试案例需要修复。
- **GC Stuff Debugging**: 正在调试GC相关问题，预计几天内完成，之后将打包成PR。
- **Transaction Manager Layer**: 正在进行性能测试，预计会有很多改进空间。
- **HSE Implementation**: 阅读了HSE的实现，计划在详细测试后评估其CPU开销。
- **Piafano 3**: 已经发送了初始版本，正在确保架构和设计决策的正确性。

#### 讨论的主要议题
- **BlueStore中的段错误**: 讨论了如何处理和重现该问题。
- **CStore中的快照支持**: 讨论了是否可以采用不同的方法来支持快照。
- **Transaction Manager Layer的性能**: 讨论了当前实现的性能问题和未来的改进方向。
- **HSE的实现和设计**: 讨论了HSE的两个组件和其API的设计。

#### 决定的事项
- **BlueStore段错误**: 建议查看崩溃时的日志信息，而不是尝试重现。
- **CStore快照支持**: 需要进一步学习和讨论，以决定是否采用不同的方法。
- **Transaction Manager Layer**: 确认可以开始性能测试，尽管性能可能不佳。

#### 后续的行动计划
- **BlueStore段错误**: 查看日志信息，并考虑使用新引入的功能在笔记本上运行测试。
- **CStore快照支持**: 深入研究并准备后续讨论。
- **Transaction Manager Layer**: 进行性能测试并准备改进。
- **HSE实现**: 继续阅读并准备性能测试。
- **Piafano 3**: 继续完善并确保设计正确性。

#### 其他事项
- 一位成员将从周四开始暂时离线，专注于数据库系统考试的复习。

### 会议结束
会议参与者确认无其他事项，会议结束。