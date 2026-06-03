---
title: "Ceph Performance Meeting 2023-01-05"
date: 2023-01-05
updated: 2023-01-07
tags:
  - "Ceph"
  - "测试"
  - "RocksDB"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 参会人员
- 会议主持人：Mark
- 参会人员：Corey

#### 会议主要议题
1. **Pull Requests (PRs) 更新**
   - 由于Ether pad服务中断，会议中未详细审查新的PRs。
   - 讨论了关于m-clock工作的更新PR，意在增加一个高优先级队列。
   - Corey的PR收到评论，需进一步跟进。
   - 两个PR已关闭，包括一个修复race condition的PR。

2. **Corey的工作更新**
   - Corey介绍了在假期前通过取消backfills和手动压缩数据稳定系统的经验。
   - 正在考虑升级和测试新的调整设置，特别是关于删除操作的优化。
   - 正在测试RocksDB版本7.8.3，特别是range delete的新特性。

3. **RocksDB更新**
   - 讨论了RocksDB 7.8.3的新特性，特别是range delete的迭代优化。
   - 计划尽快将新版本的RocksDB纳入测试。

4. **数据库性能问题**
   - 讨论了数据库溢出到硬盘的问题，导致compaction过程耗时过长。
   - 计划继续研究短期解决方案。

5. **其他议题**
   - 讨论了Adam正在进行的优化RBD mirroring的共享blob管理的工作。

#### 决定事项
- 尽快测试RocksDB 7.8.3的新特性，并评估其应用效果。
- 继续研究数据库溢出到硬盘的问题，并寻找短期解决方案。

#### 后续行动计划
- Corey将继续测试RocksDB 7.8.3，并评估其对memtable和SSD文件的影响。
- 一旦实验室的VPN恢复，将尽快进行RocksDB的升级测试。
- 继续跟进Adam的工作进展，特别是关于优化blob管理的改进。

#### 会议结束
- 会议在感谢和告别中结束，计划下周再次会议。



**备注**：会议中提到的技术术语和产品名称如“m-clock”、“RocksDB”、“PR”等，保留原文以确保专业性和准确性。