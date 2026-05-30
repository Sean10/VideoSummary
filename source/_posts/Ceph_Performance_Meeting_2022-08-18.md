---
categories:
- 视频总结
date: 2022-10-20
subtitle: Ceph_Performance_Meeting_2022-08-18
tags:
- Ceph
- RocksDB
- PRS
- Performance
- Distributed Storage
title: "Ceph Performance Meeting 2022-08-18"
updated: 2022-10-21
---



### 会议纪要

#### PRS (Pull Requests) 更新
- **新提交与关闭的PR**：
  - Shoihan提交的Crimson c-store日志代码优化PR已合并，减少了内存复制。
  - rgw中关于deos后端blue代码的PR已关闭，作者可能将提交使用新库的PR。
- **更新中的PR**：
  - Josh Solomon添加的主要平衡评分到平衡器的PR正在审查中。
  - 关于boost Valgrind的cmake更改PR已准备就绪，等待进一步讨论。
  - Igor的PR，关于在每个事务中移除状态更新，已添加到whipTheory测试中，预计将很快合并。

#### 讨论议题
- **RocksDB Tombstone 移除项目**：
  - Adam提出修改RocksDB以在迭代过程中看到一定数量的tombstones时发出memtable刷新的建议。
  - 代码审查显示实现这一功能可能不简单，且现有代码主要针对elite tombstones而非elite range tombstones。
  - 建议在KV层自行跟踪删除和删除范围，手动触发压缩或刷新，以简化代码。

#### 后续行动计划
- 继续关注和审查现有PR的进展。
- 与Adam进一步讨论RocksDB Tombstone移除项目的实施方案。

#### 其他事项
- 会议简短结束，无其他重要事项提及。

#### 会议结束
- 感谢所有参与者的出席，并祝大家本周愉快。

**会议主持人**：[未提及]  
**记录人**：[未提及]  
**日期**：[未提及]  
**参会人员**：[未提及]