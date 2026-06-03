---
title: "Fragmentation in Ceph- Why It Happens and How We Fix It - Mark Nelson, Clyso"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
  - "BlueStore"
  - "RocksDB"
categories:
  - "视频总结"
outline: deep
---
### Ceph 分布式存储中碎片化问题的分析与解决 - Mark Nelson, Clyso

#### 会议概述
本次会议深入探讨了 Ceph 分布式存储系统中的碎片化问题及其对性能的影响。主讲人 Mark Nelson 详细分析了 FileStore 和 BlueStore 的设计差异，并探讨了优化策略，涉及对象数据、元数据、空闲空间和内存等多个方面。

#### 核心议题与讨论要点

1. **FileStore 时代的碎片化问题**
   - FileStore 采用嵌套目录结构存储对象，导致元数据分散，引发性能瓶颈。
   - XFS 的 inode 限制和Btrfs 的写时复制（CoW）机制导致性能问题。

2. **BlueStore 的改进与遗留挑战**
   - RocksDB 作为 BlueStore 的核心，优化了元数据存储和写入性能。
   - BlueStore 的 CoW 机制和 SST 文件碎片化需要进一步优化。

3. **碎片化优化实践**
   - Elastic Shared Blobs 和 Defragment-on-Clone 方法用于优化 RBD 镜像克隆场景。
   - Deep Scrub 整合碎片整理，结合压缩和去重优化存储效率。

4. **未来方向与未解问题**
   - 通过 BlueStore 的 Denk 框架批量分配内存，减少小对象开销。
   - Seastore 新设计预期改变碎片处理逻辑。
   - 工具链完善，加强碎片检测与分析工具的开发。

#### 关键决策与行动计划
- 推广 Elastic Shared Blobs 作为 RBD 镜像克隆的长期解决方案。
- 推进 Deep Scrub 整合优化，完善碎片整理与压缩的联合实现。
- 开发工具，增强 `ceph-osd` 碎片评分文档，探索基于 `blktrace` 和 `iowatcher` 的碎片可视化方案。

#### 问答环节摘要
- 推荐使用 `ceph-osd` 内置评分、`iowatcher` 及 RocksDB 调试日志进行碎片分析。
- 讨论了不同分配单元大小对碎片化影响，以及物理 vs 逻辑碎片的问题。

#### 后续重点
- 加速 Deep Scrub 优化相关 PR 的合并。
- 邀请用户反馈碎片整理与压缩的实际场景需求。

#### 会议结论
碎片化是 Ceph 性能优化的关键战场，需要结合架构改进与运行时策略持续攻坚。



[以上内容包含了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划，同时保留了计算机科学/Ceph相关领域的英文原文关键词，并按照 Markdown 格式进行了排版。]