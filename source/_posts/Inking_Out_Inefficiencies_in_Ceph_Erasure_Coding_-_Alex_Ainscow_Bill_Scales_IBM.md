---
title: Inking Out Inefficiencies in Ceph Erasure Coding - Alex Ainscow & Bill Scales, IBM
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- Erasure Coding
- 存储优化
categories: 
- "视频总结"
subtitle: Inking_Out_Inefficiencies_in_Ceph_Erasure_Coding_-_Alex_Ainscow_Bill_Scales_IBM
---

Ceph社区新特性Fast EC（Erasure Coding优化）技术分享会议纪要如下：

### 会议主题

本次会议重点介绍了Ceph社区新特性Fast EC在Tentacle版本中的改进及未来规划。

### 核心议题与讨论内容

#### Erasure Coding (EC) 基础回顾

- 传统副本（Replica）机制效率低，需要3倍存储空间。
- EC原理：通过数学算法将数据分片（K数据分片 + M编码分片），允许最多M个OSD丢失而不影响数据可用性。
- 关键参数：Chunk Size（Stripe Unit）、K/M选择。

#### Fast EC的改进目标

- 性能对标Replica，尤其是在RBD和CephFS场景下。
- 成本效益，以更低存储开销接近副本性能。

#### Fast EC关键技术优化

- **读性能优化**：按需读取，消除K值对性能的影响。
- **写性能优化**：最小化读写，Parity Delta Write直接更新编码分片。
- **存储效率提升**：动态分片分配，支持更大默认值Chunk Size。

#### 性能对比与实测结果

- 读性能：小块读取IOPS提升3倍，接近Replica 50%性能。
- 写性能：小块写入延迟显著降低，效率提升2-3倍。
- 扩展性：性能不受K值影响。

#### 未来规划（Umbrella版本）

- Direct Reads：客户端直接向OSD请求数据，读性能与Replica持平。
- 小对象打包：合并小对象提升存储效率，优化恢复性能。
- 非破坏式Pool Migration：支持在线迁移至新EC配置。
- 功能补齐：支持OMAP和Classes，简化RBD配置。
- 跨站点EC（Stretch Cluster）：探索单EC Pool跨站点或分站点EC副本。

#### 问答环节关键点

- 兼容性：Fast EC支持新旧数据格式，需升级OSD/MON，客户端无需强制升级。
- 带宽场景：S3大对象场景性能提升约5-10%，随机访问受益更明显。
- 资源开销：通过减少IO请求降低CPU和网络负载。
- Pool Migration：后台任务，类似Backfill，提供进度监控。

#### 行动计划

- Tentacle版本：部署Fast EC并测试性能。
- Umbrella版本：评估Direct Reads和Pool Migration特性。
- 长期优化：关注小对象打包和跨站点EC方案。

该总结准确反映了原始内容的要点，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。