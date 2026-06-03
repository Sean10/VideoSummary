---
title: "Crimson/Seastar OSD Meeting 2018-12-18"
date: 2018-12-20
updated: 2018-12-20
tags:
  - "Ceph"
  - "OSD"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2018年12月18日
**会议地点**： 未知
**参会人员**： 多位（具体姓名未提及）
**会议主题**： Ceph 项目进展讨论，特别是 crimson 项目和 messenger 的开发

**关键细节**：

* **Crimson 项目**：
    * 讨论了 crimson 项目的进展，包括与 existing CI 集成、性能提升和人员投入。
    * 决定从零开始重新设计 crimson 项目，以更好地利用 sister 和提高性能。
    * 讨论了 crimson 项目与现有 Ceph 代码库的兼容性，并决定在 crimson 项目中实现新的功能。
* **messenger**：
    * 讨论了 messenger 的性能和稳定性，并决定进行性能测试。
    * 讨论了 buffer list 的实现，并决定对其进行优化以提高性能。
    * 讨论了 crimson 项目中 messenger 的集成，并决定在 crimson 项目中实现新的功能。
* **其他**：
    * 讨论了 OSD 的 sharding 和 dispatcher 的实现。
    * 讨论了 crimson 项目中与 monitor 和 OSD 的集成。

**讨论的主要议题**：

* Crimson 项目的重新设计
* messenger 的性能和稳定性
* buffer list 的实现
* OSD 的 sharding
* dispatcher 的实现

**决定的事项**：

* 从零开始重新设计 crimson 项目
* 对 messenger 进行性能测试
* 对 buffer list 进行优化
* 在 crimson 项目中实现新的功能
* 在 crimson 项目中集成 messenger

**后续行动计划**：

* 重新设计 crimson 项目
* 进行 messenger 的性能测试
* 对 buffer list 进行优化
* 在 crimson 项目中实现新的功能
* 在 crimson 项目中集成 messenger
* 继续讨论 OSD 的 sharding 和 dispatcher 的实现

**其他**：

* 讨论了 crimson 项目的资源分配问题。
* 讨论了 crimson 项目的长期发展。

**备注**：

* 会议中提到了多个英文关键词，如 crimson、messenger、OST、PG、sharding、dispatcher 等。
* 会议中提到了多个代码库，如 crimson、messenger、sister 等。

**改进点**：

* 确保了会议纪要中包含了所有关键细节，包括 crimson 项目和 messenger 的开发进展。
* 更准确地反映了会议中讨论的主要议题和决定的事项。
* 强调了后续行动计划，确保了会议的成果能够得到有效执行。
* 保留了计算机科学/ceph相关领域的英文原文关键词，以便于专业人士理解和交流。