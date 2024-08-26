---
title: "Ceph RGW Refactoring Meeting 2023-05-24"
date: 2023-05-24
updated: 2023-05-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间：[具体日期]
#### 参会人员：[参会人员名单]

### 主要议题及讨论内容

1. **Reef版本候选发布通知**
   - 即将发布Reef版本的候选版本，计划下周进行切割。
   - 确保所有已合并到主分支的bug修复都已准备就绪，以便纳入RC版本进行测试。
   - 需要加强多站点（multi-site）的测试，目前缺乏可靠的多站点测试。
   - 计划与Mark安排会议，讨论如何推进多站点测试。

2. **Kafka库的修复**
   - 有两个关于Kafka库的修复，这些修复解决了崩溃问题。
   - 这些修复已经在下游QE中验证，但仍需通过Tautology测试。
   - 需要进行代码审查并可能需要QA标签。

3. **Rook中的DBStore集成**
   - 讨论了在Rook中集成DBStore的可能性，特别是对于需要轻量级解决方案的用户。
   - DBStore目前不支持所有S3操作，因此需要用户进行测试以确定其适用性。
   - 需要进一步讨论和文档化如何在Rook中设置DBStore。

4. **Bucket Notifications和Multi-Site支持**
   - 讨论了如何支持Bucket Notifications的元数据同步。
   - 需要实现所有元数据接口，参考Prisa在STS中对角色的实现。

### 决定事项

- 下周将发布Reef版本的候选版本。
- 需要安排与Mark的会议，讨论多站点测试的推进。
- Kafka库的修复将进行进一步的测试和审查。
- 将在Rook中探索DBStore的集成，并标记为实验性功能。
- 需要进一步讨论和实现Bucket Notifications的元数据同步。

### 后续行动计划

- 确保所有bug修复都已准备就绪，以便纳入Reef RC版本。
- 安排与Mark的会议，讨论多站点测试的具体实施。
- 完成Kafka库修复的测试和审查，并确保其纳入主分支。
- 在Rook中集成DBStore，并提供清晰的设置文档。
- 研究并实现Bucket Notifications的元数据同步功能。

### 其他事项

- 安排了关于Lewis脚本代码走查的演讲，预计在半小时后进行。

### 会议结束

感谢所有参会人员的参与和贡献，会议圆满结束。