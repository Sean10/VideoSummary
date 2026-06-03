---
title: "2019-06-06 -- Ceph Performance meeting"
date: 2019-06-06
updated: 2019-06-07
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "测试"
categories:
  - "会议总结"
outline: deep
---
本次会议主要讨论了Ceph分布式存储性能方面的进展和计划。以下是会议的主要内容：

**1. 项目进展**

*   **拉取请求（PRs）**：会议审查了多个PR，包括客户端操作触发的恢复操作优先级、异步消息传递、垃圾收集、多站点sink公平性、OST并行清理PG on maps、对象溢出检测优化、RBD性能改进等。
*   **更新**：团队成员分享了各自的工作进展，包括避免Blue Store中重复缓存、IO ring工作更新、用户空间IO get_event的更新、Auto-tuning MVS缓存的工作等。

**2. 讨论议题**

*   **性能测试**：讨论了在PR提交时进行性能测试的计划，包括使用Telemetry进行资源分配和结果查询、使用新节点进行性能测试的硬件配置等。
*   **硬件分配**：讨论了将新节点用于开发、性能测试和回归测试的方案，以及将节点分配给特定开发者的需求。
*   **其他**：讨论了Xerox TV和RocksDB sharding的进展，包括改进写放大和压缩结果。

**3. 决定事项**

*   将部分新节点用于性能测试和回归测试。
*   将部分节点分配给Crimson开发者。
*   将部分节点作为Jenkins从属节点使用。
*   将Telemetry用于PR测试。
*   继续推进Xerox TV和RocksDB sharding的工作。

**4. 行动计划**

*   Mark将跟进Alfredo，以便他加入性能测试项目。
*   Sam将跟进Telemetry的集成。
*   Igor将重新审查垃圾收集PR。
*   Roman将跟进用户空间IO get_event的更新。
*   其他团队成员将跟进各自的项目。

**5. 下次会议**

*   下次会议将在2019年6月7日举行。

**备注**：

*   会议中提到的技术术语包括CBT、CBT gesture notes、RocksDB、RATOS、Telemetry等，这些术语在存储领域和Ceph项目中都很常见。
*   会议中提到的项目包括Crimson、Blue Store、IO ring、MVS缓存等，这些项目都是Ceph的重要组成部分。