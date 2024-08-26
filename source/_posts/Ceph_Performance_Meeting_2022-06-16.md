---
title: "Ceph Performance Meeting 2022-06-16"
date: 2022-06-27
updated: 2022-06-28
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要：

1. 概述：
   - 过去一周内，Ceph存储分布式系统的研发工作主要集中在snapmapper性能优化和arbitrary mirror performance研究。
   - 讨论了未决的PR、功能更新和潜在的改进点。
   - 提出了关于snapmapper设计的批评和改进建议。
   - 分享了有关osd（对象存储设备）性能问题的见解。

2. snapmapper相关讨论：
   - snapmapper的性能问题被关注，特别是其全局对象（pg）设计导致的性能开销。
   - 发现snapmapper在处理大量快照时产生大量的删除请求，这些请求可能不会实际删除任何数据但仍占用资源。
   - 提出将snapmapper的改动分享给更广泛的团队以获得反馈。
   - 讨论了pinning行为和简化逻辑的新PR，但需要更多讨论以决定如何进行。

3. arbitrary mirror performance：
   - Gabby分享了有关arbitrary mirror性能的文档，该文档详细分析了rbd mirror在snapmapper中产生的额外开销。
   - 讨论了tombstone生成与rocksdb活动之间的关联以及如何减少影响。

4. OSD性能问题：
   - 当shard queue不能保持满状态时，OSD的性能显著下降。
   - 讨论了使用不同数量的messenger线程、worker线程和shards时的行为差异。
   - 提出了通过循环唤醒单个线程或采用轮询机制来改善性能的潜在方案。

5. 其他讨论：
   - 探讨了避免将pg log更新传递到roxdb的可能性。
   - 讨论了hd starter上pg log读取和条目流的处理。
   - 确定了一些PR的状态，并决定关闭一些过时的PR。

6. 行动计划：
   - 继续调查snapmapper和arbitrary mirror performance的问题。
   - 探索改进OSD性能的方法。
   - 分享更多的发现和文档以促进团队成员间的讨论和协作。

7. 结语：
   - 会议以总结主要讨论点和确定下一步行动计划结束。
   - 鼓励团队成员继续努力，为即将到来的代码提交和功能迭代做准备。