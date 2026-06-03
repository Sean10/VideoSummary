---
title: "2019-07-25 :: Ceph Performance Meeting"
date: 2019-07-25
updated: 2019-07-26
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "RocksDB"
  - "会议纪要"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议主题**： Ceph分布式存储项目性能讨论

**会议时间**： 2019年7月25日

**参会人员**： Eric、Bret、Josh、Casey等

**会议内容**：

**1. RGW数据副本删除请求**
- 讨论了Rados Gateway（RGW）中删除数据副本的功能。
- 该功能将基于当前正在合并的代码实现，并可能回溯到Nautilus版本。

**2. 双缓存机制**
- 讨论了双缓存机制的优化，基于Eric正在合并的代码实现。
- 讨论了将该功能回溯到Nautilus版本的可能性。

**3. 格式变更**
- 由于格式变更，用户可能需要重新安装OSDS（Object Storage Device Server）。
- 讨论了回溯该变更到Nautilus版本的可能性。

**4. Pull Requests**
- 讨论了当前待处理的Pull Requests，包括缓存、trim行为、双重缓存避免等。

**5. RocksDB优化**
- 讨论了RocksDB的优化，包括读取前优化、ARM范围优化、自动调整读取前优化等。

**6. RocksDB版本选择**
- 讨论了选择RocksDB版本的问题，包括Luminous版本5.9、Nautilus版本5.17.2等。

**7. RocksDB回溯**
- 讨论了将RocksDB优化回溯到Luminous版本的可能性。

**8. RocksDB性能优化**
- 讨论了RocksDB的性能优化，包括连接线程、读取前优化、ARM范围优化等。

**9. 其他议题**
- 讨论了其他议题，包括快速垃圾回收、BlueFS碎片化问题等。

**后续行动计划**：

- 进一步讨论双缓存机制回溯到Nautilus版本的可能性。
- 审查并合并待处理的Pull Requests。
- 选择合适的RocksDB版本，并进行回溯和优化。
- 评估其他议题的解决方案。

**备注**：

- 会议中提到了一些关键的技术术语，如RGW、OSDS、RocksDB、ARM范围、读取前优化等。
- 会议讨论了多个技术细节，需要进一步研究和验证。