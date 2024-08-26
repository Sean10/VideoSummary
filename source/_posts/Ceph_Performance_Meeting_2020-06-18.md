---
title: "Ceph Performance Meeting 2020-06-18"
date: 2020-06-19
updated: 2020-06-20
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **UPR** 本周无特别事项。
- **PR关闭情况**：
  - Adams的PR与rocks TV sharding工作相关，防止大型读取日志大小被使用，设置了最大上限。
  - 另一个PR涉及buffer lists编码工作的测试，原计划在测试目录中进行，但建议移至项目外部。
  - 旧PR来自ma Jinping，关于mocking，因无人跟进被关闭，考虑重新开启。
- **更新PR**：
  - 关于blocking traces的PR，Egor自分配但尚未有时间处理。
  - mem pools splitting PR，改进内存池的粒度，更细致地管理内存使用。
  - blue store walking PR，仍在解决QA中发现的问题。
  - MVS中的PR，旨在优化大量读写器和写入器访问单个目录时的性能。

#### 讨论的主要议题
- **IO 500测试**：
  - 初步怀疑MDS中目录的碎片化和导出导致性能下降和停滞。
  - 通过预碎片化和预导出片段进行优化，但在高MDS数量下仍存在低吞吐量和周期性停滞。
  - 使用GB PNP分析发现，大量工作与Southwest journaling相关，特别是e meta blob数据结构的解码过程缓慢。
  - 尝试使用unordered map和vector进行优化，但发现问题可能在于buffer list本身的小分配问题。
  - 讨论了MDS多线程化的必要性，以提高性能。

#### 决定的事项
- 需要进一步优化buffer list的编码过程，可能通过切换到新的编码方案来预留空间，减少内存分配和碎片化。
- 考虑MDS的多线程化，以利用多核优势。

#### 后续行动计划
- 继续优化IO 500测试中的性能问题，特别是buffer list的编码和内存管理。
- 探索MDS的多线程化方案，以提高整体性能。
- 持续跟进和更新相关PR的状态，确保项目进展顺利。

#### 其他事项
- 讨论了内存 footprint 减少和依赖逻辑简化的重要性，希望在下一个版本中实现。
- 会议结束时，鼓励团队成员继续努力，期待下周有新的进展。

### 结束语
会议结束，感谢大家的参与，祝大家下周工作顺利。