---
title: "Ceph Developer Monthly 2021-11-03"
date: 2021-11-03
updated: 2021-11-05
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
本次Ceph开发者月度会议主要讨论了Crimson更新、Ceph存储技术（Ceph Store）的进展、遥测数据收集以及关键问题通知机制。

**Crimson更新**：
- Radic团队致力于解决Crimson中的bug，特别是Toothology套件中的问题，包括watch notify API的更改和操作顺序逻辑的改进。
- Crimson与Rook的集成存在问题，但Chad May对Blue Store集成进行了改进，提高了性能。
- 下一步计划包括将scrub工作转移到Krypson中，重构OSD状态机以提高Crimson的重用代码量。

**Ceph Store**：
- Intel团队增加了大量计数器和直方图，用于跟踪事务冲突率和分配信息，有助于解决性能问题。
- 对LBI分配路径进行了重写，解决了逻辑问题，提高了代码的可读性。
- Schwehn的extent placement manager已合并，支持在C-Store内进行分层。
- Joyhead正在实现基于年龄的竞价方案，这将有助于将extent写入非日志设备。

**遥测数据收集**：
- 讨论了如何解决用户重新选择的问题，提出了一个新的设计，允许用户重新选择时同步新的数据收集版本。
- 强调了数据收集的透明度和用户隐私，建议对收集的每个字段进行详细说明，并提供一个结构化的JSON描述。

**关键问题通知**：
- 提出了一个健康警告机制，用于在用户运行存在已知问题的版本时发出警告。
- 建议使用releases.yaml文件来标记有问题的版本，并在集群中提供这些信息，以便用户在升级时做出明智的决策。

会议决定继续进行Crimson的稳定性改进、Ceph Store的性能优化、遥测数据收集的改进以及关键问题通知机制的开发。后续行动计划包括继续开发Crimson、优化Ceph Store、实施遥测数据收集改进以及开发健康警告机制。