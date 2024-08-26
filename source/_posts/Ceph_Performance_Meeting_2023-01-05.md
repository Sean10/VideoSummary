---
title: "Ceph Performance Meeting 2023-01-05"
date: 2023-01-06
updated: 2023-01-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- 会议主持人：Mark
- 参会人员：Corey

#### 会议主要议题
1. **Pull Requests (PRs) 更新**
   - 由于Ether pad暂时无法使用，会议中没有详细审查新的PRs。
   - 提到了一个关于m-clock工作的更新PR，旨在增加一个高优先级队列用于操作。
   - Corey的PR收到了一些评论，需要进一步跟进。
   - 有两个PR已经关闭，包括一个修复race condition的PR。

2. **Corey的工作更新**
   - Corey报告了他们在假期前通过取消所有backfills和手动压缩数据来稳定系统的经验。
   - 目前正在考虑升级和测试一些新的调整设置，特别是关于删除操作的优化。
   - 正在测试RocksDB版本7.8.3，特别是关于range delete的新特性，这可能对性能有显著提升。

3. **RocksDB更新**
   - 讨论了RocksDB 7.8.3的新特性，特别是range delete的迭代优化，这可能对Ceph的性能有重大影响。
   - 计划尽快将新版本的RocksDB纳入测试。

4. **数据库性能问题**
   - 讨论了数据库溢出到硬盘的问题，这导致compaction过程耗时过长。
   - 计划继续研究短期解决方案，同时关注RocksDB升级的长远影响。

5. **其他议题**
   - 讨论了Adam正在进行的工作，包括优化RBD mirroring的共享blob管理。

#### 决定事项
- 尽快测试RocksDB 7.8.3的新特性，并评估其在Ceph中的应用效果。
- 继续研究数据库溢出到硬盘的问题，并寻找短期解决方案。

#### 后续行动计划
- Corey将继续测试RocksDB 7.8.3，并评估其对memtable和SSD文件的影响。
- 一旦实验室的VPN恢复，将尽快进行RocksDB的升级测试。
- 继续跟进Adam的工作进展，特别是关于优化blob管理的改进。

#### 会议结束
- 会议在感谢和告别中结束，计划下周再次会议。

---

**备注**：会议中提到的技术术语和产品名称如“m-clock”、“RocksDB”、“PR”等，保留原文以确保专业性和准确性。