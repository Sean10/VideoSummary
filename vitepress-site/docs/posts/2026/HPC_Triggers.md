---
title: "HPC Triggers"
date: 2026-04-02
updated: 2026-04-03
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
## 演讲背景

本次演讲由来自尼泊尔 SBC（超级计算机/高性能计算集群）的 James 主讲。他所在的大学校园内部署了一套私有云集群，主要通过 RBD 存储为学生提供虚拟机服务，同时也在探索 Ceph 在 HPC（高性能计算）场景下的适用性。

## HPC 工作负载特征

HPC 场景下的计算任务具有以下典型特征：

- **大规模并行计算**：数百乃至数千台计算节点协同处理同一个大型科学问题，任务被拆分后分布在各节点上执行
- **MPI 通信密集**：各计算节点通过 MPI（Message Passing Interface）协议进行通信与协调
- **并发 IO 极高**：MPI ranks 产生高度一致的并发 IO，同时存在小随机读写与顺序读写混合的访问模式
- **元数据密集**：主要使用 cephfs 文件系统存储，元数据操作占比高
- **Checkpointing 需求**：部分任务运行周期超过一年，必须定期做 checkpoint 以防止灾难性失败，而 checkpointing 本身对尾延迟（tail latency）极为敏感

## HPC 对存储的核心期望

SBC 场景对存储系统的要求极为严苛：

- 亚毫秒级（sub-millisecond）读写延迟
- 确定性（deterministic）性能表现
- 高 IOPs 吞吐能力
- 并行文件系统行为
- 低突发写入抖动

## Ceph 在 HPC 场景下的问题分析

### 写入路径的多层延迟

一次典型的 Ceph 写入需要经历以下完整链路：

1. 客户端发起写请求
2. 通过 CRUSH algorithm 选定 primary OSD
3. WAL（Write-Ahead Log）序列化提交，执行 fsync
4. RocksDB 更新元数据（BlueStore 的组成部分）
5. 数据写入 primary OSD
6. 副本复制（replication）并等待网络确认

这六层延迟叠加，在 HPC 高并发场景下会导致尾延迟急剧膨胀，吞吐量在并发压力下崩溃。

### WAL 的序列化瓶颈

WAL 是 Ceph 保障可靠性的核心机制——写入中途发生故障时可回滚并重新写入另一个 primary OSD。然而：

- 每次写入都必须先追加到 WAL 并完成 fsync 才能确认
- 提交操作被串行化排队，形成序列化瓶颈
- 高 fsync 频率下小同步写入性能极差

### RocksDB 的 compaction 问题

RocksDB 作为 BlueStore 的元数据存储引擎，采用 LSM（Log-Structured Merge Tree）架构，写入路径为：memtable → STables → compaction。在 HPC 重负载下，compaction 操作会周期性抢占 CPU 资源，造成明显的性能抖动。

### 副本放大问题

以 3 副本配置为例，即使是一次 4KB 的小写入，实际需要：

- 3 次WAL 写入
- 3 次 RocksDB 元数据更新
- 3 次数据写入
- 3 次网络提交确认

这种写放大在 HPC 场景下代价极高，且 cephfs 的元数据目前不支持 erasure coding，只能依赖 replication，进一步加剧了问题。

### NVMe 无法根本解决问题

即便为 WAL 和 RocksDB 配置高端 NVMe SD，WAL 的串行化提交机制依然存在，网络延迟依然是瓶颈，Ceph 同步写入的本质特性不会改变。

## 现有优化方向（有限改善）

对于确实需要在 HPC 场景使用 Ceph 的团队，以下调优措施可部分缓解问题：

- **合理的 RocksDB DB 大小配置**：建议设置为 OSD 容量的 4%~10%
- **WAL 与 DB 独立部署**：将 WAL 和 RocksDB 分离到高端 NVMe 设备上
- **CPU pining 与 NUMA affinity**：通过绑核和 NUMA 亲和性优化 OSD 的 CPU 利用率

## 结论

Ceph 在 RBD 虚拟机存储等通用场景下表现良好，但对于 HPC/SBC 工作负载，其核心架构存在根本性的不适配：

- 元数据放大（metadata amplification）
- CPU竞争（CPU contention）
- WAL 序列化延迟
- 网络往返开销

目前业界 HPC 场景的主流选择仍是 **Lustre** 和 **BeeGFS** 等专为并行文件系统设计的存储系统。演讲者表示，其所在集群也采用了这两种方案，尚未发现有组织将 Ceph 用于 HPC 核心存储的案例。
