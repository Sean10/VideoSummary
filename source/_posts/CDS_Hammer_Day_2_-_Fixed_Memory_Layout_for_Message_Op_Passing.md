---
title: "  CDS Hammer (Day 2) - Fixed Memory Layout for Message/Op Passing  "
date: 2014-10-30
updated: 2014-10-31
tags:
- Ceph
- 分布式存储
categories:
- "视频总结"
subtitle: CDS_Hammer_Day_2_-_Fixed_Memory_Layout_for_Message_Op_Passing
---


会议纪要：

**会议主题**： Maya 固定内存布局的消息和输出传递方案讨论

**会议关键细节**：

* 讨论了消息管理，特别是固定内存布局在消息传递中的应用。
* 分析了当前消息传递机制的优缺点，并提出了优化方案。
* 提出了创建一个新的消息类型 `mosd_client_sub-op`，用于简化消息结构并提高效率。

**讨论的主要议题**：

* **消息多样性**： 消息种类繁多，直接优化所有消息结构不切实际。
* **优化目标**： 针对消息处理速度较快的路径进行优化，例如 `mosd up` 和回复消息。
* **优化方法**：
    * 使用固定内存布局，避免解码操作。
    * 减少消息中不必要的数据，例如 `PG stats` 和 `Snapshots`。
    * 创建新的消息类型，只包含必要的字段，例如 `mosd_client_sub-op`。
    * 优化 `mosd sub-op reply` 中的 `OSD Apps` 字段。

**决定的事项**：

* 创建一个新的消息类型 `mosd_client_sub-op`，用于复制客户端操作。
* 优化现有消息结构，去除不必要的数据和字段。
* 优化 `mosd sub-op reply` 中的 `OSD Apps` 字段。

**后续行动计划**：

* 由研发人员根据会议讨论结果，修改代码实现新的消息类型和优化措施。
* 对现有代码进行测试，确保优化措施有效且兼容性良好。

**改进点**：

* 原总结中未提及固定内存布局的讨论，现已补充。
* 原总结中对消息类型 `mosd_client_sub-op` 的描述不够详细，现已补充。
* 原总结中对优化方法的描述较为简略，现已补充具体措施。
* 原总结中未提及后续行动计划，现已补充。