---
title: "Ceph RGW Refactoring Meeting 2023-02-15"
date: 2023-02-16
updated: 2023-02-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题
1. **S3代理过滤器和Zipper的讨论**：会议开始时，讨论了如何实现S3代理过滤器和Zipper的问题，这是为了在d4n之下进行集成。昨天的d4n会议中对此有大量讨论，但未解决，因此希望在今天的会议中继续讨论。
2. **Reef项目的进展**：询问了Reef项目的现状，包括需要完成的功能和未合并的重要修复。
3. **Ragweed问题的修复**：提到了Ragweed问题的修复进展，已经解决了Ragweed的失败问题。

#### 讨论细节
- **S3代理过滤器的问题**：讨论了S3代理过滤器在Zipper API中的不适用性，因为Zipper API将S3操作分解为许多小API调用。理想的S3处理方式是在操作层进行代理，但这与Zipper的设计冲突。
- **权限验证问题**：讨论了如何在无法访问桶元数据和策略的情况下进行权限验证。
- **新的抽象层提议**：提出了为d4n和其他可能的应用构建一个新的抽象层，这个层更面向应用，更容易进行代理。

#### 决定事项
- **重新安排讨论**：由于关键成员Matt不在场，决定重新安排关于S3代理过滤器的讨论。
- **Reef项目的关注点**：确认了Reef项目的进展和需要关注的功能和修复。

#### 后续行动计划
- **继续讨论S3代理过滤器**：待所有关键成员到齐后，继续讨论S3代理过滤器的实现细节。
- **Reef项目的跟进**：继续关注Reef项目的进展，确保所有重要功能和修复得到及时合并。
- **新抽象层的开发**：开始规划和设计一个新的抽象层，以更好地支持d4n和其他应用的需求。

#### 其他讨论点
- **缓存层的设计**：讨论了缓存层的设计，特别是如何处理元数据和数据的问题。
- **权限验证的实现**：讨论了在不同存储后端中如何实现权限验证的问题。

#### 会议总结
会议持续了近一个小时，讨论了多个关键的技术问题，并提出了一些解决方案和后续行动计划。感谢所有参与者的积极参与和贡献。