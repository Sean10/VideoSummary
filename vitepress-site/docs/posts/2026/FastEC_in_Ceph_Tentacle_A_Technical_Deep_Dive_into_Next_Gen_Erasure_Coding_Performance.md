---
title: "FastEC in Ceph Tentacle A Technical Deep Dive into Next Gen Erasure Coding Performance"
date: 2026-04-20
updated: 2026-04-21
tags:
  - "Ceph"
  - "Erasure Coding"
  - "性能"
  - "BlueStore"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
## 演讲概述

本次演讲由 45Drives 首席架构师 Mitch Hall 主讲，主题为 Ceph Tentacle 版本中的 Fast EC（快速 erasure coding）技术，重点探讨其在 block-based 及低延迟工作负载场景下的可行性与性能表现。

## 背景与动机

在存储架构设计中，"好、快、便宜"三者往只能取其二。2026 年，受 AI 热潮影响，RAM 和 flash 价格大幅上涨，甚至出现同一方案一周内报价翻倍的情况。在此背景下，Fast EC 作为一种新工具，有望在不更换硬件的前提下，通过提升存储效率来降低客户的总拥有成本（TCO）。

传统上，Ceph 的标准冗余策略是三副本（3-replication）。对于从 RAID parity 或镜像方案迁移过来的客户而言，接受三副本的存储开销往是一道心理门槛。而 erasure coding 的 4+2 配置可在不改动任何硬件的情况下将可用存储空间翻倍，2+2 配置则有望在延迟表现上更接近三副本。

## 传统 EC 的核心问题

在 Ceph Squid 及更早版本中，erasure coding 在 block 工作负载上存在以下几个关键瓶颈：

**read-modify-write 问题**：即便只修改一个 stripe 中的单个 chunk，也必须读取整个 stripe、重新计算 parity，再将整个 stripe 写回。对于 4K 随机写，这种放大效应极为严重。

**小 IO 的全 stripe 读取**：在 4+2 配置下读取 4K 数据，实际需要读取 24K 数据，IO 放大明显，延迟偏高。

**小对象 padding**：4K 写入需要对额外的 chunk 进行 padding，导致写入更多 OSD。

**K 值增大加剧 IO 放大**：stripe unit 越大，read-modify-write 带来的 IO 放大越严重。

## Tentacle 版本的优化方案

Ceph Tentacle 通过以下机制显著改善了上述问题：

**Partial reads（部分读取）**：不再强制读取整个 stripe，而是精确响应客户端请求。4K 读取只访问对应的单个 OSD，减少了 round trip 和 IO 放大。

**Partial writes（部分写入）**：小写入不再读取整个 stripe，只读取未被命中的 chunk，重新计算 parity 后写入新 chunk 和新 parity。

**Parity delta writes（parity 增量写入）**：将旧数据与新数据进行 XOR 得到 delta，仅将 delta 应用到 parity shard，无需完整重写 parity。Ceph 会根据效率自动在 partial write 和 parity delta write 之间切换，K 值越大时 parity delta write 越有优势。

**启用方式**：对于已有集群，只需执行 `allow_ec_optimizations = 1` 即可开启上述优化。此外，将 stripe unit 从默认的 4K 提升至 16K 可进一步减少 IO split，但该参数只能在新建 pool 时设置，无法对已有 pool 生效。

## 测试环境

**集群配置**：6 台 45Drives Storinator F16 节点，每节点配备 AMD EPYC 64 核 128 线程处理器、256GB DDR5 内存、16 块 Micron 7450 Pro U.3 NVMe SSD，单节点约 15TB 原始容量，集群总计约 92TB。

**网络**：LACP 100GbE，MTU 9000，L3+L4 哈希负载均衡，使用 Melanox/Nvidia OFED 驱动及 tune工具，启用低延迟 VMA，手动调整网络中断亲和性，禁用 CPU 睡眠状态。

**软件版本**：Ceph Squid 19.2.3 vs Ceph Tentacle 10.2.20，OS 为 Rocky Linux 9.7，内核 5.14，客户端为 Proxmox 最新版，使用 kernel RBD。

**测试工具**：fio 3.35，Ansible playbook 自动化测试，JSON 结果输出，Python 绘图工具，三次取平均值，每个 RBD 500GB 且预填充。

**Pool 配置**：1024 PG，测试三副本、4+2、2+2 三种配置，每次测试前清空集群。

## 测试结果

### 块大小延迟扫描（单 VM，单队列深度）

从 4K 到 128K 的延迟扫描中，Tentacle 相比 Squid 整体有所下降。值得注意的是，在 16K 块大小处出现了延迟略微上升的情况，推测与 16K stripe unit 设置有关，后续需要针对性测试。读延迟整体低于写延迟，符合预期。

### 响应曲线测试（4K 随机读写，1~16 并发 VM）

这是本次测试的核心场景。

**Squid 表现**：三副本延迟极为稳定，平均延迟远低于 1ms，P99 也保持在 2ms 以内。4+2 在 16并发 VM 时平均延迟约 1.6ms，但 P99 已超过 2ms 并快速攀升。

**Tentacle 表现**：差距显著缩小。2+2 配置在 16 并发 VM 之前延迟保持在 1ms 以内，4+2 也有明显改善。P99 延迟增长趋势较 Squid 平缓得多。另外观察到一个有趣现象：单线程无其他 IO 时延迟反而偏高，随负载增加延迟有所下降，Fast EC 团队也观察到类似现象，可能与 BlueStore 行为有关。

### 饱和测试（高队列深度，高并发）

**Squid**：三副本在约 4ms 附近保持稳定；4+2 在超过 50,000 IOPS 后延迟急剧上升，100,000 IOPS 时超过 60ms，基本不可用；2+2 稍好，但 100,000 IOPS 时也达到约 10ms。

**Tentacle**：在 100,000 IOPS 时，4+2 和 2+2 的延迟均低于 3.5ms，相比 Squid 的约 16ms 降低了近 4倍，表现极为亮眼。读延迟两版本差异不大。

### 顺序吞吐量测试（1MB 块大小）

Squid 中 2+2 表现最佳，达到约 11.7 GB/s。Tentacle 中三副本吞吐量有所提升，甚至超过了 EC 配置，但 EC pool仍维持约 11.7 GB/s。读吞吐量各配置差异不大。

## 实际应用场景分析

基于上述测试结果，Fast EC 为以下工作负载开辟了新的可能性：

**开发/测试 VM 集群**：无 SLA 要求，对毫秒级延迟不敏感，从三副本切换到 EC 可大幅降低存储成本。

**CI/CD DevOps 流水线**：构建任务通常耗时数分钟，轻微的延迟增加不影响整体效率。

**VDI 环境**：用户对 5~10ms 以内的延迟通常无感知，中等规模 VDI 环境迁移到 EC 具有可行性，待进一步验证。

**数据库读副本**：高性能写密集型数据库主库不适合 EC，但 MySQL 从库、Elasticsearch 数据节点等读密集型副本迁移到 EC 是现实可行的选项。

**Kubernetes persistent volumes**：适合对延迟要求不极端的持久化存储场景。

**温备份（Warm Backup）**：EC 在冷备份场景已被广泛使用多年，Fast EC 有望将其延伸至温备份场景，满足更快的 RTO 需求。

**RGW 混合工作负载**：应用资源、缩略图、机器学习训练数据等随机访问模式，在 Fast EC 加持下比以往更适合运行在 EC pool 上。

**更高 K 值的 erasure coding profile**：partial reads 和 partial writes 消除了增大 K 值带来的 IO 放大惩罚，使更高效的 EC 配置在更多场景下具备实用价值。

## TCO 影响

同等硬件下存储容量翻倍，是最直接的成本收益。此外，更少的 OSD 意味着更少的 NVMe 和 RAM 需求，而当前 RAM 价格高企，这一节省尤为显著。在大规模部署中，还可带来可观的电力和机架空间节省。

## 结论与后续计划

Fast EC 与 Tentacle 代表了 Ceph erasure coding 性能迄今最重要的一次飞跃，不仅限于 block 工作负载，对所有使用场景均有提升。本次测试为 EC 的延迟表现提供了量化数据，初步验证了多类工作负载迁移到 EC 的可行性。

45 Drives 计划在未来为虚拟化客户提供 EC 支持的 block storage，以改善其 TCO。所有测试方法、Ansible playbook 和 Python 绘图工具均将公开发布，供社区复现和验证。后续将继续开展真实业务负载（而非纯 benchmark）测试，包括 VDI、数据库副本、温备份等场景的深入验证。
