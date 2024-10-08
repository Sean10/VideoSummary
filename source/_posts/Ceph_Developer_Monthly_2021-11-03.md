---
title: "Ceph Developer Monthly 2021-11-03"
date: 2021-11-04
updated: 2021-11-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是关于Ceph分布式存储系统的月度会议，主要讨论了Crimson更新、Ceph存储技术（Ceph Store）的进展、遥测数据收集以及关键问题的通知机制。会议在假期期间举行，因此参与人数不多。

#### 主要议题

1. **Crimson更新**
   - **稳定性提升**：Radic团队一直在努力解决Crimson中的bug，特别是在Crimson的Toothology套件中。已经进行了大量的稳定性工作，包括对watch notify API的更改和操作顺序逻辑的改进。
   - **部署进展**：Crimson与Rook的集成存在问题，但Chad May对Crimson的Blue Store集成进行了改进，提高了性能。
   - **下一步计划**：将scrub工作转移到Krypson中，正在进行OSD状态机的重构，以便在Crimson中重用大量代码。

2. **Ceph存储技术（Ceph Store）**
   - **性能优化**：Intel团队增加了大量计数器和直方图，用于跟踪事务冲突率和分配信息，有助于解决性能问题。
   - **稳定性改进**：对LBI分配路径进行了重写，解决了逻辑问题，提高了代码的可读性。
   - **新功能开发**：Schwehn的extent placement manager已合并，支持在C-Store内进行分层。Joyhead正在实现基于年龄的竞价方案，这将有助于将extent写入非日志设备。

3. **遥测数据收集**
   - **重新选择流程**：讨论了如何解决用户重新选择的问题，提出了一个新的设计，允许用户重新选择时同步新的数据收集版本。
   - **数据收集策略**：强调了数据收集的透明度和用户隐私，建议对收集的每个字段进行详细说明，并提供一个结构化的JSON描述。

4. **关键问题通知**
   - **健康警告机制**：提出了一个健康警告机制，用于在用户运行存在已知问题的版本时发出警告。讨论了如何通过Redmine标记严重问题，并在集群中生成健康警告。
   - **版本信息管理**：建议使用releases.yaml文件来标记有问题的版本，并在集群中提供这些信息，以便用户在升级时做出明智的决策。

#### 决定事项
- **Crimson稳定性提升**：继续进行Crimson的稳定性改进，特别是与Rook的集成和多核支持。
- **Ceph Store性能优化**：继续优化Ceph Store的性能和稳定性，特别是对LBI分配路径和extent placement manager的改进。
- **遥测数据收集改进**：实施新的重新选择流程，并对收集的数据字段进行详细说明，以提高透明度和用户信任。
- **关键问题通知机制**：开发一个健康警告机制，用于通知用户关于已知的关键问题，并使用releases.yaml文件来管理版本信息。

#### 后续行动计划
- **Crimson开发**：继续进行Crimson的开发和测试，确保与Rook的集成和多核支持的稳定性。
- **Ceph Store改进**：继续优化Ceph Store的性能和稳定性，特别是对LBI分配路径和extent placement manager的改进。
- **遥测数据收集**：实施新的重新选择流程，并对收集的数据字段进行详细说明，以提高透明度和用户信任。
- **关键问题通知机制**：开发一个健康警告机制，用于通知用户关于已知的关键问题，并使用releases.yaml文件来管理版本信息。

#### 结论
本次会议讨论了Ceph分布式存储系统的多个关键领域，包括Crimson的稳定性提升、Ceph Store的性能优化、遥测数据收集的改进以及关键问题的通知机制。会议强调了透明度、用户隐私和性能优化的重要性，并制定了相应的后续行动计划。