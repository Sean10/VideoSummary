---
title: "Ceph Performance Meeting 2021-09-23"
date: 2021-09-23
updated: 2021-10-07
tags:
  - "Ceph"
  - "分布式存储"
  - "RocksDB"
  - "BlueStore"
  - "RGW"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
本次Ceph性能会议主要讨论了以下议题：

1. **RocksDB LRU缓存更新**：由于与RocksDB新版本不兼容，Kifu修复了接口问题，并已合并到主分支。会议讨论了维护者使用最新版本RocksDB编译的问题，建议避免使用未经测试的版本。

2. **RGW OSD压缩绕过**：Casey上周审查通过，已重新基于最新版本，接近合并状态。

3. **BlueStore Fighting Green Locking**：Adam更新并由Sage审查，主要是小改动。会议讨论了需要进一步审查，特别是与Gabby相关的问题。

4. **BlueStore增量更新模式**：正在进行测试，已更新以修复错误。

5. **TTL缓存实现**：请求对管理模块的TTL缓存实现进行审查。已修复make check问题，可能需要再次审查。

6. **PG移除优化**：Igor的PR有额外审查和测试，讨论了是否需要为硬盘优化。测试失败，需要进一步审查。

7. **其他更新**：MDS相关的新PR需要重新基于最新版本，RGW团队的共享对象缓存PR正在等待进一步处理，MemStore清理PR目前不紧急。

会议确定了以下行动计划：

1. 确认Fedora和其他前沿发行版是否使用最新版本的RocksDB，并建议避免使用未经测试的版本。

2. 继续审查和测试RGW OSD压缩绕过、BlueStore Fighting Green Locking、BlueStore增量更新模式等PR。

3. 确保Igor的PG移除优化PR通过测试并进行必要的审查。

4. 下周将讨论Josh推荐的关于重构Linux存储栈的论文，建议与会者提前阅读并准备三个关键的讨论点。

会议还提醒大家，下周会议将重点讨论Linux存储栈重构的论文，并建议与会者提前准备并分享三个关键的讨论点。

本次会议纪要涵盖了关键的讨论点、决定的事项以及后续的行动计划，对于Ceph社区的成员来说具有重要的参考价值。