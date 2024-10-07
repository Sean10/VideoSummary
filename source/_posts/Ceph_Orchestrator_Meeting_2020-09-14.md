---
title: "Ceph Orchestrator Meeting 2020-09-14"
date: 2020-09-14
updated: 2020-09-15
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **会议主题**: 今日的协调器会议
- **参会人员**: 部分核心成员
- **会议时间**: 今日

#### 主要议题
1. **新拉取请求（Pull Request）讨论**
   - **提出者**: Paul
   - **内容**: 引入adm daemon在所有主机上的持久性，编号为130130。
   - **目的**: 解决从主机获取信息所需时间过长的问题，提升协调器和仪表板的性能。
   - **讨论**: 
     - 该请求目前仅限于收集主机上的硬件信息。
     - 未来可能扩展为更全面的fadm diamond功能。
     - 讨论了设计架构和性能问题，特别是SSH连接的效率和持久性问题。

2. **文档站点问题**
   - **提出者**: Zach
   - **内容**: 当前有两个不同的文档站点，一个在readthedocs.io，另一个在docs.conf。
   - **问题**: 
     - docs.conf的搜索功能有限，只能搜索第一个字符串。
     - readthedocs.io提供了更好的搜索功能，但没有API文档的自动生成。
   - **讨论**: 
     - 需要找到一个解决方案，既能提供良好的搜索功能，又能自动生成API文档。
     - 提出了将API文档源代码提交到源代码树的建议，但存在维护成本问题。

#### 决定事项
- **新拉取请求**: 继续讨论和优化，确保其设计符合当前需求，同时考虑未来的扩展性。
- **文档站点**: 需要进一步讨论和寻找解决方案，以整合搜索功能和API文档生成。

#### 后续行动计划
- **新拉取请求**: 
  - 继续与Paul合作，优化请求内容。
  - 设计高层次的工作流程文档，明确需求和接口。
- **文档站点**: 
  - 在领导团队会议上进一步讨论。
  - 探索更有效的解决方案，以改善文档站点的搜索和API文档生成功能。

#### 其他讨论
- **性能和可扩展性**: 讨论了cephadm和仪表板的性能问题，特别是SSH连接的管理和优化。
- **设计文档**: 强调了设计文档的重要性，以确保项目的长期维护和改进。

#### 会议结束
- **下次会议**: 下次同步会议再见。

---

本次会议重点讨论了新拉取请求的设计和性能问题，以及文档站点的整合问题。会议强调了设计文档的重要性，并提出了后续的行动计划。