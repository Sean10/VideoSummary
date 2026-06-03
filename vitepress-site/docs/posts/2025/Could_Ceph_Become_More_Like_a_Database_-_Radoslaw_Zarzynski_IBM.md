---
title: "Could Ceph Become More Like a Database? - Radoslaw Zarzynski, IBM"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
  - "RADOS"
  - "BlueStore"
  - "RocksDB"
categories:
  - "视频总结"
outline: deep
---
### Ceph会议纪要：RADOS原生索引概念探讨

**会议基本信息**
- **主讲人**：Radjinski（长期Ceph开发者，RADOS团队成员）
- **会议主题**：RADOS原生索引（Native Indexing）概念探讨
- **性质**：概念性讨论，非正式提案

**核心讨论内容**

会议主要探讨了Ceph的RADOS原生索引概念，旨在提高存储系统的效率和可用性。

#### 历史背景与问题分析
- Ceph的OMAP（Object Map）从使用`std::map`序列化直接存储，到引入CLS T-map，再到基于LevelDB/RocksDB的现代OMAP，其演进历史展示了存储系统的不断优化。
- 当前OMAP的限制包括原子性缺失、客户端复杂性高以及BlueStore层OMAP隔离的人为设计限制。

#### RADOS Native Indexing提案
- 利用BlueStore底层统一的RocksDB keyspace，通过key前缀区分不同索引，保持数据与索引的共置。
- 新增原生索引创建/删除操作，扩展object write操作支持索引标记，支持单次原子操作替代现有3阶段协议。

#### 潜在应用场景
- 改进RGW，简化bucket index维护流程。
- 优化CephFS，减少目录遍历开销。
- 长期可能性包括类数据库查询能力和丰富的二级索引支持。

#### 关键技术挑战
- 与ordered bucket index的协调，可能影响现有的数据/元数据分离设计。
- 性能考量，Resharding开销增加，OSD热点风险增加。
- 兼容性，保持现有POOL和OBJECT作为核心抽象，不引入分布式锁等破坏现有设计原则的机制。

#### 权衡分析
- 优势包括简化客户端逻辑、原子性保证和性能提升潜力。
- 挑战包括修改多层架构、与EC pools的兼容性、Resharding成本增加、统一索引管理和可能违反现有设计哲学。

#### 后续行动计划
- 概念验证，在BlueStore层验证统一keyspace可行性，测量索引操作对RocksDB性能影响。
- RGW集成研究，评估与ordered bucket index的协同方案，分析实际工作负载下的对象大小分布。
- 设计细化，制定索引生命周期管理方案，确定故障恢复机制。
- 社区讨论，收集更多使用场景需求，评估优先级。

**备注**：本提案处于早期概念阶段，实际实现可能需要分阶段进行并优先解决RGW等关键用例的需求。