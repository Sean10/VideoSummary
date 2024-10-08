---
title: "Ceph Performance Meeting 2021-09-11"
date: 2021-09-11
updated: 2021-09-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **会议日期**: 未明确提及
- **参会人员**: 未明确提及
- **会议主持**: 未明确提及

#### 讨论的主要议题
1. **已合并的PR**:
   - **Prometheus VR**: 允许禁用缓存，已合并。
   - **Omap命名方案限制**: Igor提出的PR，用于解决omap列表过大时的内存消耗问题，已合并。
   - **MDS锁切换**: MDS锁切换到公平互斥锁以避免饥饿问题，已合并。

2. **更新中的PR**:
   - **Adam的PR**: 实现写操作的直接I/O和读操作的缓冲I/O。讨论了潜在的一致性问题，需要仔细审查。
   - **BlueStore日志增量更新模式**: 未通过QA测试。
   - **OSD压缩绕过RGW压缩**: 已进入Eric的测试分支。
   - **TTL缓存实现**: 管理模块的TTL缓存实现，正在进行中。
   - **优化PG移除PR**: Igor的优化PG移除PR，已重新审查。
   - **Ceph Messenger头2解码优化**: 已更新，Ilia之前已审查。
   - **MDS从子树映射移除**: 从日志中移除MDS从子树映射，Zhang已更新。

3. **性能回归分析**:
   - **OSD代码分析**: 发现了一些性能回归，主要来源包括mclock QoS更改和BlueStore缓冲I/O的默认启用。
   - **Gabby的PR**: 移除RocksDB中的分配数据，显著提升了4K随机写性能。
   - **Adam的PR**: 讨论了直接写和缓冲读的混合模式，可能引入一致性问题。

4. **IOU Ring的讨论**:
   - **IOU Ring的现状**: 现有代码可能已过时，需要重新评估其在BlueStore中的应用。
   - **潜在的改进**: 考虑使用IOU Ring来改善性能，特别是在缓冲I/O模式下。

#### 决定的事项
- **性能改进**: 确认Gabby的PR显著提升了性能，解决了之前的性能回归问题。
- **IOU Ring的重新评估**: 决定重新评估IOU Ring在Ceph中的应用，特别是在缓冲I/O模式下。

#### 后续行动计划
- **性能审查**: 对Adam的PR进行仔细审查，确保不会引入一致性问题。
- **IOU Ring的评估**: 重新评估和测试IOU Ring的性能和稳定性。
- **讨论论文**: 计划在三周后讨论一篇关于Linux内核低延迟优化的论文。

#### 其他事项
- **会议时间调整**: 由于节假日，下次会议时间调整至30号。

#### 结论
会议讨论了多个PR的进展和性能问题，确认了Gabby的PR对性能的显著提升，并决定重新评估IOU Ring的应用。下次会议将讨论一篇相关论文。