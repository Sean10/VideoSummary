---
title: "Ceph Performance Meeting 2021-09-23"
date: 2021-10-07
updated: 2021-10-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与更新

1. **RocksDB LRU缓存更新**
   - 问题：自定义的RocksDB LRU缓存实现与新版本的RocksDB不兼容。
   - 解决：Kifu修复了接口问题，并已合并到主分支。
   - 讨论：对于维护者使用最新版本的RocksDB进行编译表示担忧，建议避免用户使用未经测试的版本。

2. **RGW OSD压缩绕过**
   - 状态：Casey上周审查通过，已重新基于最新版本，接近合并状态。

3. **BlueStore Fighting Green Locking**
   - 更新：Adam更新并由Sage审查，主要是小改动。
   - 讨论：需要进一步审查，特别是与Gabby相关的问题。

4. **BlueStore增量更新模式**
   - 状态：正在进行测试，已更新以修复错误。

5. **TTL缓存实现**
   - 请求：请求对管理模块的TTL缓存实现进行审查。
   - 状态：已修复make check问题，可能需要再次审查。

6. **PG移除优化**
   - 更新：Igor的PR有额外审查和测试，讨论了是否需要为硬盘优化。
   - 状态：测试失败，需要进一步审查。

7. **其他更新**
   - MDS相关的新PR需要重新基于最新版本。
   - RGW团队的共享对象缓存PR正在等待进一步处理。
   - MemStore清理PR目前不紧急。

#### 行动计划

1. **RocksDB版本使用**
   - 确认Fedora和其他前沿发行版是否使用最新版本的RocksDB，并建议避免使用未经测试的版本。

2. **PR审查与合并**
   - 继续审查和测试RGW OSD压缩绕过、BlueStore Fighting Green Locking、BlueStore增量更新模式等PR。
   - 确保Igor的PG移除优化PR通过测试并进行必要的审查。

3. **论文讨论准备**
   - 下周将讨论Josh推荐的关于重构Linux存储栈的论文。
   - 建议与会者提前阅读论文，并准备三个关键的讨论点。

#### 后续会议

- 下周会议将重点讨论关于Linux存储栈重构的论文，建议与会者提前准备并分享三个关键的讨论点。

#### 其他事项

- 会议中提到的其他PR和项目将继续跟踪和处理，确保及时更新和审查。

### 会议结束

感谢所有参与者的贡献，期待下周的会议讨论。祝大家一周愉快！

---

以上是本次会议的纪要，涵盖了关键的讨论点、决定的事项以及后续的行动计划。