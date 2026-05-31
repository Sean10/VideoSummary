---
categories:
- 视频总结
date: 2018-06-01
subtitle: 2018-May-31_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 分布式存储
- 性能优化
title: "'2018-May-31 :: Ceph Performance Weekly'"
updated: 2018-06-02
---




本次会议主要讨论了Ceph项目的多个进展，包括Beast项目、Rocky CB1 Mark、内存使用优化、锁优化等方面。

**Beast项目**： Adam Emerson正在将兼容I/O接口集成到Beast中，会议强调需要关注接口兼容性问题，确保与解放应用程序的兼容性。

**Rocky CB1 Mark**： 会议讨论了该PR的视频功能，认为其对性能提升有限，但不会造成负面影响。

**内存使用优化**： 会议讨论了OS memory usage的问题，希望实现内存使用量的动态调整，并根据优先级分配内存。同时探讨了如何获取内存分配的统计数据，并考虑使用malloc_usable_size等接口。

**锁优化**： 会议讨论了scrubbing期间锁的竞争问题，并分析了可能的锁冲突原因。建议使用GDB wall clock profiler或Adams wall clock profiler进行分析，并尝试调整scrubbing步长大小以改善性能。

**后续行动计划**：

* Adam Emerson继续推进Beast项目，并提交相关PR。
* 会议参与者积极审查Adam提交的PR。
* 会议参与者继续关注内存使用优化工作，并尝试获取相关统计数据。
* 会议参与者尝试使用GDB wall clock profiler或Adams wall clock profiler分析scrubbing期间锁的竞争问题。
* 会议参与者尝试调整scrubbing步长大小以改善性能。

**其他事项**：

* 会议讨论了rocksdb buffer size动态调整的可能性。
* 会议鼓励大家积极分享经验和反馈。

本次会议讨论了Ceph项目的多个进展，并制定了后续行动计划。会议氛围积极，参与者积极参与讨论，为Ceph项目的持续发展贡献力量。