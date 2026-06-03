---
title: "Ceph Performance Meeting 2022-06-16"
date: 2022-06-16
updated: 2022-06-28
tags:
  - "Ceph"
  - "性能优化"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

1. **会议概述**：
   - 本次会议重点讨论了Ceph存储系统性能优化相关议题，包括snapmapper性能和arbitrary mirror性能。
   - 团队成员对未决的Pull Requests (PR)、功能更新及潜在改进点进行了讨论。
   - 对snapmapper的设计提出了批评和建议，并分享了关于OSD性能问题的见解。

2. **snapmapper相关讨论**：
   - 重点关注snapmapper的性能问题，特别是其全局对象（PG）设计导致的性能开销。
   - 发现snapmapper在处理大量快照时产生大量删除请求，可能占用资源而不实际删除数据。
   - 讨论了简化逻辑的新PR，但需进一步讨论确定实施方案。

3. **arbitrary mirror performance**：
   - 分析了rbd mirror在snapmapper中产生的额外开销。
   - 讨论了tombstone生成与rocksdb活动之间的关联，以及如何减少影响。

4. **OSD性能问题**：
   - 当shard queue不能保持满状态时，OSD的性能显著下降。
   - 讨论了使用不同数量的messenger线程、worker线程和shards时的行为差异。
   - 提出了通过循环唤醒单个线程或采用轮询机制来改善性能的潜在方案。

5. **其他讨论**：
   - 探讨了避免将pg log更新传递到roxdb的可能性。
   - 讨论了hd starter上pg log读取和条目流的处理。
   - 确定了一些PR的状态，并决定关闭一些过时的PR。

6. **行动计划**：
   - 继续调查snapmapper和arbitrary mirror performance的问题。
   - 探索改进OSD性能的方法。
   - 分享更多的发现和文档以促进团队成员间的讨论和协作。

7. **结语**：
   - 会议总结主要讨论点和确定下一步行动计划。
   - 鼓励团队成员继续努力，为即将到来的代码提交和功能迭代做准备。