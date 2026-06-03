---
title: "Panel Discussion"
date: 2026-04-02
updated: 2026-04-03
tags:
  - "分布式存储"
  - "Erasure Coding"
  - "对象存储"
  - "CephFS"
categories:
  - "视频总结"
outline: deep
---
## 概述

本次圆桌讨论由 Vidushi 主持，邀请了 Ceph 社区多位核心专家，涵盖 dashboard、customer engineering、object storage、RADOS、NFS/CephFS、SMB 等方向的负责人，围绕 Ceph 社区当前面临的挑战、路线图规划及用户实际痛点展开了深入交流。

## 各方向路线图概览

### Dashboard

Dashboard 方向目前重点聚焦在 object storage 相关功能的集成，包括：

- 通知管理（notification topic management）
- 存储类生命周期管理（storage class lifecycle management）
- SMB 管理界面
- NVMe 管理支持

上述功能均已在 Tentacle 版本中推进。社区鼓励用户积极试用并反馈 bug，以推动功能完善。

### 性能与 Customer Engineering

该团队重点关注性能 benchmarking 及售前售后支持，主要进展包括：

- **Fast EC（erasure coding）**：Tentacle 版本的核心特性，目标是让 file 和 block 存储也能以 EC 作为默认选项，支持 2+2、4+2、8+3、8+4 等多种 profile，从 TCO 角度替代三副本 replication。
- **BlueStore 压缩**：支持硬件压缩（Intel QAT）和软件压缩（snappy、zlib、std），持续优化压缩性能。
- **自动化故障排查**：包括 core dump 分析、日志分析等自动化工具，计划后续 upstream。

### Object Storage（RGW）

Matt 介绍了 RGW 方向的多项创新：

- **D4N 数据缓存**：基于波士顿大学研究成果的集成式数据缓存，针对分析类工作负载提供加速，持续扩展适用场景。
- **S3 Vectors**：基于 Ceph object 与 LanceDB 融合平台的 S3 向量存储实现，原型阶段接近完成，即将发布。
- **POSIX Driver**：支持将任意文件系统后端通过 S3 接口导出，不局限于 RADOS，正在产品化。
- **S3 over RDMA**：已支持通过 NFS over RDMA 访问完整 S3 命名空间，持续扩展 RDMA 支持。

### RADOS Core

核心存储层的路线图重点：

- **Fast EC增强**：Umbrella 版本将引入 direct reads，大幅提升 EC 读性能，使 EC 对读密集型工作负载更具竞争力。
- **EC 支持 OMAP**：长期以来 EC 不支持 OMAP，该特性上线后将有望实现全 EC 的Ceph 集群。
- **Pool 迁移**：支持现有 pool 迁移到新特性，降低升级门槛。
- **Ceph Manager健壮性**：持续加固各模块，提升可见性和可扩展性。
- **Stretch Cluster 增强**：结合 EC 路线图进一步完善跨站点容灾能力。
- **Crimson**：中期目标，RGW 工作负载的 tech preview 即将落地，EC 支持已在合并中，PG splitting 也将实现。

### NFS / CephFS

CephFS 和 NFS 方向新特性丰富：

- QoS（quality of service）
- TLS 支持
- 增强的 failover 与 high availability
- DBUS 迁移至 gRPC
- Prometheus 监控大幅改进
- Write delegations
- Binary logging与 ring buffer dump
- 异步 snapshot replication（中期）
- Pass file cloning 与 multi-protocol 支持（长期 killer features）

### SMB

SMB 作为相对较新的组件，正在快速追齐 NFS 的功能集：

- BY（加密）支持
- 磁盘加密（on-disk encryption）
- 多租户（multi-tenancy）增强
- QoS 支持
- Persistent file handles（支持特定 Microsoft 应用工作负载）
- SMB over RDMA（规划中，涉及 Linux 内核集成，挑战较大）
- Multi-protocol 支持：同一存储卷可同时通过 CephFS、NFS、SMB 访问

## 用户问题与社区讨论

### Dashboard 使用体验

现场调查显示使用 Ceph dashboard 的用户较少。一位用户反映 Pacific/Octopus 版本中 dashboard 加载 OpenStack volumes 时响应极慢，Nisam 确认新版本已将加载时间优化至 2.5 秒以内。

### PG Rebalancing 问题（NPCI，2.5 PB 集群）

用户反映在维护操作（服务器故障、合规补丁）时频繁触发 PG rebalancing，影响业务 IO。

**社区回应：**
- 服务器故障触发的属于 recovery/backfill，新版本已通过 WPQ 和 mClock 调度器大幅降低对 client IO 的影响。
- 扩容触发的 rebalancing 可使用社区方案（如 CERN/Digital Ocean 开发的 PG premapper，利用 up items 概念控制新 OSD 的 PG 迁移节奏）。
- 计划将相关脚本集成进 Ceph 源码，并加入 teuthology 测试框架，同时长期目标是让 balancer 本身对扩容等主动操作更加智能感知。

### Fast EC 与 Replicated 性能对比（500 TB，12 节点全闪集群）

用户询问 EC 集群何时能在性能上与 replication 竞争，以及 HDD 集群的加速方案。

**社区回应：**
- 当前测试显示，K 值越大（如 8+3、8+4），fast EC 性能越接近甚至持平 replication；2+1 这类小 K 值收益不明显。
- 对于 20-30 节点规模，推荐 8+3 或 8+4 profile（最小节点数要求为 K+M+1）。
- Direct reads 特性（Umbrella 版本）将显著改善 EC 读性能，是 EC 全面竞争 replication 的关键。
- 元数据 pool 仍建议使用 replication，数据 pool 可考虑迁移至大 K 值 EC。
- Cache tiering 已 deprecated，但代码仍保留；BlueStore WAL/DB 建议放在 SD/NVMe 上，DB 空间占比已从 4% 降至 2.5%。
- HDD 集群加速可参考 BlueStore 压缩优化及 D4N 缓存（RGW 场景）。

### Deduplication 支持（Cisco，~2 PB，500-600 OSD）

用户询问 Ceph 在单站点和多站点 object 存储的 deduplication 规划。

**社区回应：**
- Ceph 有来自韩国科学技术院的核心 deduplication 实现，尚未产品化。
- RGW 层有 Benhan 实现的完整 object-level deduplication，支持全对象去重，正在扩展对小对象（head object内嵌数据）的支持。
- Gaby 正在开展更经典的部分文件去重（partial file dedup）工作。
- 上述功能适用于多站点全局命名空间，计划在 Umbrella 版本落地。
- Tentacle 版本已支持 deduplication 效果预估（preview）。

### RGW 多站点复制问题（22 PB，50 亿对象集群）

用户反映多站点 replication 偶发中断，sync status 显示 shard 卡住，目前依赖 Python 脚本通过 bi log/index log/metadata log 手动同步。

**社区回应：**
- Quincy 版本的多站点问题较多，Reef 版本引入了 dynamic resharding 等大量修复，建议升级。
- IBM 内部已针对数亿至十亿级对象规模进行 scale testing，系统已大幅改善。
- 近期将发布针对已知 stuck sync 场景的修复，目标版本为 Ceph main 和 Umbrella。
- Shilpa Jagannath 正在将 bucket index log 从对数时间复杂度迁移至 FIFO 技术（已用于 data log），预计带来超线性的性能提升。
- Dashboard 团队已实现多站点 sync rate 和 ingest rate 的可视化监控。
- Bucket index 架构改进将支持单 bucket 超过 50 亿对象，并解除单对象版本数受单 shard 限制的问题。

### MON 全部丢失的恢复

用户反映小集群（5-6 节点）因补丁操作和节点自动重启导致三个 MON 全部丢失，集群宕机。

**社区回应：**
- 可参考 Ceph 官方文档中的 MON rebuild 流程：从各 OSD 分区提取 OSD map，通过 monmaptool 重建 store.db。
- 生产环境强烈建议将 MON 部署在不同机架，确保 failure domain 隔离，避免单点故障导致 quorum 丢失。

## 总结

本次圆桌讨论覆盖了 Ceph 社区从 dashboard、object storage、erasure coding、CephFS、NFS、SMB 到 RADOS core 的全面路线图，重点方向包括：Fast EC 性能提升与 direct reads、Crimson tech preview、多站点复制稳定性、deduplication 产品化、BlueStore 压缩优化以及 multi-protocol 访问支持。社区对大规模用户的实际痛点（PG rebalancing、多站点 sync、bucket index 扩展性）均有明确的改进计划，Umbrella 版本将是多项关键特性的集中落地版本。
