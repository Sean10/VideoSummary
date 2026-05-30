---
categories:
- 视频总结
date: 2021-04-16
subtitle: Ceph_Crimson_SeaStore_2021-04-14
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可伸缩性
title: "Ceph Crimson/SeaStore 2021-04-14"
updated: 2021-04-17
---
本次会议主要讨论了Ceph存储系统中的watch和notify功能，以及如何优化这些机制以支持端到端映射。主要议题包括：

- **PR审查进展**：上周提交了多个PR，主要涉及watch和notify功能的实现，包括分离watch的超时处理和一些小的修复。
- **经典OSD与Crimson的watch和notify实现差异**：讨论了经典OSD中watch与session紧密耦合的问题，以及在Crimson中如何实现更独立的watch机制。
- **包管理优化**：建议创建一个单独的包来区分Crimson和经典OSD，以避免混淆和提高用户识别度。
- **调试信息输出**：讨论了如何改进调试信息的输出格式，以便更方便地进行调试，特别是改进backtrace的输出。
- **C-store性能优化**：讨论了c-store的性能优化问题，包括改进缓存数据结构和事务处理的内部机制，以及增加性能计数器。

会议决定的事项包括：

- 继续审查和合并与watch和notify功能相关的PR。
- 决定是否可以移除经典OSD中watch和session的耦合，以简化实现并提高效率。
- 优化Crimson的包管理，创建一个单独的包来区分Crimson和经典OSD。
- 改进调试信息的输出格式，特别是backtrace的输出。
- 探索C-store的性能优化，包括改进缓存数据结构和事务处理的内部机制，以及增加性能计数器。

后续行动计划包括：

- 完成PR的审查和合并工作。
- 探索并实施移除经典OSD中watch和session耦合的方案。
- 优化Crimson的包管理，创建单独的包。
- 改进调试信息的输出格式，特别是backtrace的输出。
- 探索C-store的性能优化，包括改进缓存数据结构和事务处理的内部机制，以及增加性能计数器。

## 相关标签
- [Ceph]
- [分布式存储]
- [CRUSH算法]
- [高可用性]
- [可伸缩性]