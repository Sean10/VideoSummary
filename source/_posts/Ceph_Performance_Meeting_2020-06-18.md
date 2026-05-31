---
categories:
- 视频总结
date: 2020-06-19
subtitle: Ceph_Performance_Meeting_2020-06-18
tags:
- Ceph
- 性能优化
- 分布式存储
- MDS
title: Ceph Performance Meeting 2020-06-18
updated: 2020-06-20
---



在 2020 年 6 月 18 日举行的 Ceph 性能会议上，团队讨论了一系列关键议题和更新：

### 关键细节
- UPR 本周没有特别事项。
- PR 关闭情况包括：Adams 的 PR 与 rocks TV sharding 有关，防止读取日志大小过大，设置最大上限；buffer lists 编码测试 PR 建议移至项目外部；ma Jinping 的 mocking PR 因无人跟进被关闭，考虑重新开启。
- 更新 PR 包括：blocking traces PR，Egor 自分配但尚未处理；mem pools splitting PR，改进内存池粒度；blue store walking PR，解决 QA 发现的问题；MVS PR，优化大量读写器访问单个目录时的性能。

### 讨论的主要议题
- IO 500 测试显示，MDS 中目录碎片化和导出可能导致性能下降。
- 优化方案包括预碎片化和预导出片段，但在高 MDS 数量下仍存在低吞吐量和周期性停滞。
- GB PNP 分析指出，Southwest journaling 和 e meta blob 数据结构解码缓慢。
- 讨论了使用 unordered map 和 vector 进行优化，但问题可能在于 buffer list 的小分配。
- 提出MDS多线程化的必要性，以提高性能。

### 决定的事项
- 进一步优化 buffer list 的编码过程，可能通过切换到新的编码方案来预留空间，减少内存分配和碎片化。
- 考虑 MDS 的多线程化，以利用多核优势。

### 后续行动计划
- 继续优化 IO 500 测试中的性能问题，特别是 buffer list 的编码和内存管理。
- 探索 MDS 的多线程化方案，以提高整体性能。
- 持续跟进和更新相关 PR 的状态，确保项目进展顺利。

### 其他事项
- 讨论了内存 footprint 减少和依赖逻辑简化的重要性，希望在下一个版本中实现。
- 鼓励团队成员继续努力，期待下周有新的进展。

### 结束语
会议结束，感谢大家的参与，祝大家下周工作顺利。