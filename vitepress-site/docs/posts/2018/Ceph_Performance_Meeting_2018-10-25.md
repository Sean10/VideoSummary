---
title: "Ceph Performance Meeting 2018-10-25"
date: 2018-10-25
updated: 2018-10-26
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "RocksDB"
categories:
  - "视频总结"
outline: deep
---
在 2018-10-25 举行的 Ceph 性能会议上，与会人员讨论了多个关键议题，包括 PR 审批、Numa 架构优化、OMAP 性能测试和 RocksDB 数据库优化。以下是对会议内容的详细总结：

**一、PR 审批及后续行动**

* **Radek 的 PR**： 讨论了 Radek 提交的多个 PR，包括缓冲区历史工作、性能测试、数据依赖性分析等。会议决定将大型 PR 分解成更小的部分进行审查，并讨论了简化热点路径的复杂性方案。
* **其他 PR**： 讨论了其他 PR 的进展，包括 gzip 压缩、stack string stream、延迟延迟、OMAP 测试等。
* **遗留问题**： 讨论了遗留问题的处理，包括 attic、slapped allocators、临时内存池计数器等。

**二、Numa 架构优化**

* 讨论了 Numa 架构优化方案，包括 pinning Numa 节点内存、OSD 跨多个 Numa 节点分布等。
* 认识到 Numa 架构优化是一个复杂的问题，需要谨慎处理，并确保不会降低性能。

**三、OMAP 性能测试**

* 讨论了 OMAP 性能测试结果，包括单操作延迟、DB 大小等。
* 认识到 RocksDB 数据库的 DB 大小设置需要优化，以确保性能。
* 讨论了 OMAP 操作批处理的可能性，以提高性能。

**四、RocksDB 数据库优化**

* 讨论了 RocksDB 数据库的优化方案，包括自动调整级别大小、压缩和写放大等。
* 认识到 RocksDB 的级别大小设置需要优化，以确保性能。

**五、其他**

* 讨论了 Rados Bench 的优化，以及是否将重点放在 OMAP 性能测试上。
* 讨论了 RocksDB 的 tombstones 问题。

**行动计划**

* **Radek**：将大型 PR 分解成更小的部分进行审查，并讨论简化热点路径的复杂性方案。
* **Neha 和 Adam**：调查 stack string stream 中的崩溃问题。
* **Sage**：调查 clean PG set 仍然刷新的问题。
* **Nick**：调查 RocksDB 的 DB 大小设置问题，并尝试优化级别大小。
* **Josh 和 Matt**：讨论 OMAP 操作批处理的可能性。
* **Eric**：调查 RocksDB 的 tombstones 问题。

本次会议讨论了 Ceph 项目的多个重要议题，并制定了相应的行动计划。会议强调了 PR 审批、Numa 架构优化、OMAP 性能测试和 RocksDB 数据库优化的重要性。