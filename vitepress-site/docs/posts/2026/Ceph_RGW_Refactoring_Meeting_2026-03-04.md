---
title: "Ceph RGW Refactoring Meeting 2026-03-04"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "Erasure Coding"
  - "对象存储"
  - "RADOS"
  - "OSD"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次会议围绕 Ceph 小对象存储效率问题展开深入讨论，核心议题是 Gaby 提出的一种针对 erasure coding 场景下小对象低效问题的分层缓存架构方案，并就该方案与 Alex 正在推进的 object packing 方案之间的关系进行了探讨。

## 主要议题

### 一、erasure coding 小对象存储的现有问题

Gabby 首先阐述了当前 erasure coding 实现在处理小对象时存在的多项效率问题：

**空间浪费与碎片化**

以 4+2 erasure coding 配置为例，一个 4 KB 的对象会被拆分为 6 个 chunk（4 个数据块 + 2 个校验块），每个 chunk 约 1 KB。由于 bluestore 的最小分配单元为 4 KB，每个 chunk 都需要 padding 补齐，导致严重的空间浪费。对象删除后遗留的碎片化空间也难以被有效复用。

**元数据冗余**

在 erasure coding 模式下，RGW 的对象属性（manifest、用户自定义属性等）会在每个 erasure coding 成员上各保存一份，造成元数据的多倍冗余存储。

**写放大问题**

某客户场景中，平均对象大小仅 16 KB（范围 4 KB 至 32 KB），写入量达数十亿级别。每个小对象都需要触发完整的 erasure coding 写流程，代价极高。

**现有缓解方案的局限性**

目前有一种通过双 storage class 将head（仅含元数据）与 tail（数据）分离的方式，可将元数据冗余从 6 份降至 3 份（replica 层），但该方案在客户中并不普及，且无法解决写放大和碎片化问题。

### 二、Gabby 提出的两层架构方案

Gabby 提出了一种"前端缓存层 + 后端数据层"的两层存储架构：

**前端层（Front/Cache Tier）**

-以标准 RADOS OSD 实现，采用 replication 模式（3 副本）
- 接收小对象写入，在 OSD 内部维护一个循环写缓冲区（建议使用 SD，理想情况下使用 NVRAM）
- 对象的 extent info扩展新模式：除原有指向 bluestore 地址的模式外，新增"remote 模式"，允许 extent 指向外部存储层的偏移地址
- 写入的对象数据先追加写入本地 log device，同时在内存中保留副本以提升读性能
- 当缓冲区积累到一定大小（如 4 MB或 16 MB）后，批量顺序刷写至后端数据层

**后端层（Data Tier）**

- 可以是 erasure coding pool、replica pool，甚至外部存储系统（NFS、flash 阵列等）
- 对上层透明，只需支持大块顺序写入即可获得最佳性能
- 收到后端确认后，前端层更新 extent info 指向后端地址，释放本地缓冲区（采用双缓冲设计，确保刷写期间仍可接受新写入）

### 三、架构定位讨论

Matt 就该方案的架构归属提出了关键问题：

**RADOS 层 vs. RGW 层**

Matt 认为，该方案虽以 RGW 场景为出发点，但其核心机制（两个 pool 之间的 tiering、数据路径变更）本质上属于 RADOS 内部架构，应归属于 OSD 层以下，而非 RGW 层。Gabby 也认同该设计应对 RGW 透明，具备通用性。

**与 Alex 的 object packing 方案的关系**

Alex 正在设计/实现一套完全在 RADOS 层内部进行 object packing 的方案，已在 Cephalocon 开发者会议上有所介绍。两个方案存在一定重叠：
- Alex 的方案侧重于在 erasure coding 层内部合并小对象，解决元数据冗余和空间效率问题
- Gabby 的方案额外引入了 IO 顺序化（sequentialization）和跨 PG 边界的对象聚合能力，这是 Alex 方案目前尚未覆盖的部分

与会者普遍认为两个方案存在互补性，建议在 RADOS 层统一协调，避免在 RGW 层引入复杂的多 pool 操作逻辑。

**对 CephFS 的适用性**

讨论中指出，该方案对 POSIX 文件系统（CephFS）的适用性有限，因为文件系统本身已有处理小文件的机制，额外的 packing 层可能反而增加开销。该方案的主要收益集中在 RADOS object storage 场景。

**性能收益预期**

与会者认为性能提升远不止 10-20%，在小对象密集写入场景下收益显著，尤其是考虑到当前 4 KB 对象在 erasure coding 下的高额开销。

**PG 一致性与恢复的挑战**

有与会者指出，PG log 是RADOS 一致性和 recovery 的重要机制，在引入缓存层后如何保证一致性是需要认真对待的工程挑战。Matt 也坦承，RADOS 当前的一致性约束对性能存在较大制约，Ceph 若要在高 IOPS 场景下保持竞争力，需要探索在保持一致性的同时提升并行度和扩展性的新方法。

### 四、后续行动

- 建议将该议题提交至 **Ceph Developer Monthly** 会议，邀请更多相关团队（RGW、RADOS、CephFS）的 stakeholder 共同讨论
- Gabby 将继续完善设计方案，并与 Alex 就两个方案的协同与边界进行沟通
- 建议整理 Alex 的 object packing 上游设计文档，供团队参考对比

## 其他议题

**OIDC thumbprint 可选化**

上周会议中 Krainal 提出的 OIDC thumbprint 强制校验问题已有进展：Preetham 回复确认可将其改为可选。Krainal 已准备好相关 PR，将在 tracker 中完成自我分配并关联 PR。

## 总结

本次会议深入探讨了 Ceph 在小对象 erasure coding 场景下的性能瓶颈，Gabby 提出的两层缓存架构方案具有较大潜力，但需要在 RADOS 层统一规划，并与 Alex 的 object packing 方案协调推进。下一步将在更广泛的开发者论坛中继续讨论架构方向。
