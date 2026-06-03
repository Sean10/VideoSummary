---
title: "Ceph User + Dev Monthly Meeting 2024-08-21"
date: 2024-08-21
updated: 2024-08-22
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**会议主题**： Ceph 分布式存储用户开发者会议，重点讨论了用户体验和 Ceph 功能改进。

**参会人员**： Laura、Zach、Joel、Alex 等社区成员。

**会议内容**：

**1. 用户体验（Usability）**

*   **议题**： 如何改进 Ceph 的用户体验，特别是针对非技术用户。
*   **讨论**：
    *   **Joel**： 提出在 Crush Map 中添加网络交换机信息，以帮助管理员更好地了解集群结构，但担心这会导致数据迁移。
    *   **Alex**： 建议使用 PG Remapper 或 upmap remapped 工具来避免数据迁移，并建议创建一个跟踪器来记录问题。
    *   **Zach**： 提出“冰镐倡议”（Ice Pick Initiative），旨在改进 Ceph 命令的帮助输出，使其更易于理解和使用。
    *   **Garv**： 讨论了 Ceph 仪表板的用户体验改进，计划进行社区调查以获取反馈。
*   **决定事项**：
    *   Joel 将创建一个跟踪器，记录添加网络交换机信息的问题，并尝试使用 PG Remapper 或 upmap remapped 工具来解决。
    *   Zach 将开始实施冰镐倡议，并创建一个跟踪器来跟踪所有需要改进的命令。
    *   Garv 将进行社区调查，以获取对 Ceph 仪表板用户体验的反馈。

**2. Ceph 功能改进**

*   **议题**： 讨论 Ceph 功能的改进，特别是与用户体验相关的改进。
*   **讨论**：
    *   **Joel**： 提出使用 upmap 来避免在添加网络交换机信息时进行数据迁移。
    *   **Alex**： 讨论了 upmap 和 upmap balancer 的工作原理，并建议 Joel 尝试使用这些工具来解决他的问题。
    *   **Zach**： 讨论了 Ceph 命令的帮助输出，并提出了改进建议。
    *   **Garv**： 讨论了 Ceph 仪表板的用户体验改进，并计划进行社区调查以获取反馈。
*   **决定事项**： 无

**后续行动计划**：

*   Joel 将创建一个跟踪器，记录添加网络交换机信息的问题，并尝试使用 PG Remapper 或 upmap remapped 工具来解决。
*   Zach 将开始实施冰镐倡议，并创建一个跟踪器来跟踪所有需要改进的命令。
*   Garv 将进行社区调查，以获取对 Ceph 仪表板用户体验的反馈。
*   社区成员将提供反馈，以帮助改进 Ceph 的用户体验。

**关键词**： usability、Crush Map、upmap、upmap balancer、Ice Pick Initiative、Ceph 仪表板、用户体验