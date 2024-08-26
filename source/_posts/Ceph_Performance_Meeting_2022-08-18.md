---
title: "Ceph Performance Meeting 2022-08-18"
date: 2022-10-20
updated: 2022-10-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### PRS (Pull Requests) 更新
- **新提交与关闭的PR**：
  - 在Crimson的c-store日志代码中，通过将缓冲区列表移动来减少内存复制的新PR，由Shoihan提交并已立即合并。
  - 在rgw中，关于deos后端blue代码的PR，作者已关闭，可能会有使用更优库或新版本库的新PR提交。
- **更新中的PR**：
  - 由Josh Solomon添加的主要平衡评分到平衡器的PR，正在审查中。
  - 关于boost Valgrind的cmake更改，讨论较多，但已基本准备就绪。
  - Igor的PR，关于在每个事务中移除状态更新，已添加到whipTheory测试中，有望很快合并。

#### 讨论议题
- **RocksDB Tombstone 移除项目**：
  - Adam建议尝试修改RocksDB本身，在迭代过程中看到一定数量的tombstones时发出memtable刷新。
  - 经过代码审查，发现实现这一功能可能不简单，且现有代码主要针对elite tombstones而非elite range tombstones。
  - 建议在KV层自行跟踪删除和删除范围，手动触发压缩或刷新，这样代码会更简单易处理。

#### 后续行动计划
- 继续关注和审查现有PR的进展。
- 与Adam进一步讨论RocksDB Tombstone移除项目的实施方案。

#### 其他事项
- 会议中未提及其他重要事项，会议简短结束。

#### 会议结束
- 感谢所有参与者的出席，并祝大家本周愉快。

**会议主持人**：[未提及]  
**记录人**：[未提及]  
**日期**：[未提及]  
**参会人员**：[未提及]