---
title: "Ceph Performance Meeting 2021-08-05"
date: 2021-08-21
updated: 2021-08-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **新PR**: 本周有一个新的PR，涉及MDS锁的更改，从非公平互斥锁切换到公平互斥锁，目的是改善等待时间较长的请求的处理，避免资源饥饿。
- **已关闭PR**: Kifu合并了一个关于PG日志的更改，具体是关于回滚信息的修剪。
- **更新PR**: 多个PR正在积极审查和开发中，包括RGW跟踪工作、缓冲区列表的PR以及TTL缓存实现的长期工作。
- **性能问题**: Red Hat内部工作组发现基于Pacific的新存储版本在性能上有所提升，但NVMe基础的DB和WAL分区在OSD中出现了显著的写放大问题，导致SSD驱动器的工作负载比之前版本更重。

#### 讨论的主要议题
- **写放大问题**: 讨论了BlueStore中首选延迟大小与Blob大小的关系，以及这对写操作的影响。特别是，当首选延迟大小等于或大于Blob大小时，会导致大量的延迟I/O流量进入RocksDB的写前日志和MemTable缓冲区，从而引发写放大问题。
- **代码逻辑和行为**: 讨论了BlueStore处理大写操作的逻辑，以及如何通过调整参数（如首选延迟大小）来优化性能和减少写放大。

#### 决定的事项
- **进一步测试和分析**: 决定进行更多测试，特别是简化场景的测试，以更好地理解写放大问题的原因和潜在的解决方案。
- **代码审查和优化**: 需要进一步审查和优化BlueStore的代码，特别是在处理大写操作和延迟写入的逻辑上。

#### 后续行动计划
- **性能测试**: 进行更多性能测试，特别是在不同配置下测试写放大问题。
- **代码审查**: 继续审查和优化BlueStore的代码，特别是与写操作和延迟写入相关的部分。
- **参数调整**: 考虑调整BlueStore的首选延迟大小参数，以减少写放大并优化性能。

#### 结论
会议讨论了Ceph存储系统中的多个开发和性能优化问题，特别是关于MDS锁的改进和BlueStore中的写放大问题。决定进行更多测试和代码审查，以解决这些问题并优化系统性能。感谢所有参与者的贡献和讨论，期待下周继续跟进这些问题。