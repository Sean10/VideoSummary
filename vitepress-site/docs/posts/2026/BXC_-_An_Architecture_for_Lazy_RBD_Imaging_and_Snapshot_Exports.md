---
title: "BXC - An Architecture for Lazy RBD Imaging and Snapshot Exports"
date: 2026-04-20
updated: 2026-04-21
tags:
  - "RBD"
  - "块存储"
  - "快照"
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
## 演讲背景

本次演讲由 Digital Ocean 的工程经理 Kam Saleem 与高级存储工程师 Alicia Casey 联合呈现。Digital Ocean 是全球最大的 Ceph 部署方之一，拥有分布在 16 个区域的约 40 个集群，涵盖 RBD block storage 和 RGW object storage 两类业务。

随着越来越多的 VM 用户希望将本地 NVMe 资源留给高性能业务，而将 OS 启动盘迁移到 RBD volumes 上，Digital Ocean 面临了大规模 RBD 镜像写入与 snapshot 备份的工程挑战，并为此设计了名为 **Block Exchange（BXC）** 的架构。


## 核心问题：RBD 镜像写入的三种传统方案及其缺陷

### 方案一：Clone +保留 golden image

将所有 VM 启动盘设为同一个 golden RBD image 的 clone。问题在于：

- 所有 VM 都依赖同一个 snapshot，一旦该 snapshot 损坏，整棵依赖树全部受影响。
- Ceph 支持无限长的 snapshot chain，导致 golden image 无法删除，管理极为困难。

### 方案二：Clone + Flatten

Clone 后立即 flatten，彻底解除依赖。问题在于：

- Digital Ocean 采用 3x replication，大规模 VM 批量创建时，flatten 操作会产生巨量写流量。
- 以 50 GB镜像批量创建 1000 台 VM 为例，会产生约 15 TB 的 RBD 写流量，严重竞争运行时 IO。

### 方案三：实时从 image server拉取并 import

每次创建 VM 时直接从 image server 拉取并执行 `rbd import`。问题在于：

- 没有 deduplication，大量重复数据反复在网络上传输，带宽浪费严重。


## BXC 架构设计：Lazy RBD Imaging

### 核心思路

利用 Ceph 的 **RBD import-only live migration** 特性，将 RBD volume 的 parent设置为一个 HTTP server，从而实现按需（on-demand）拉取 block 数据，同时在后台异步完成完整镜像写入。

### 镜像存储层

Digital Ocean 的 image store 构建在 S3 之上，每个镜像不以原始文件或 ISO 存储，而是切分为若干 1 MB 的 snappy 压缩 block，支持层级（layer）元数据，类似 OCI image registry的分层结构。

### 前端 HTTP Server（Block Image Daemon）

在 image store 前部署一个 HTTP server，负责：

- 接收来自 librbd 的 HTTP range request（由 RBD live migration 机制触发）。
- 对请求的 extent 进行解压缩（snappy decompression）。
- 对已请求过的 extent 进行 edge cache，实现 deduplication。
- 将数据回写到 RBD volume。

### 启动流程

1. 用户请求创建启动盘，指定目标镜像。
2. BXC 调用 `migration prepare import`，将 RBD volume 的 parent 配置为指向该镜像的 HTTP server 地址。
3. VM 立即可以启动，OS 按需请求 block，librbd 将请求转换为 HTTP range request，由 HTTP server 实时响应。
4. 后台同时触发 `migration execute`，异步完成完整镜像的 lazy imaging。
5. 迁移完成后，通过 status polling 确认状态，执行 commit。

### 技术收益

- **即时启动（instant boot）**：OS 只需请求启动所需的少量 block，无需等待完整镜像写入。
- **Deduplication**：已缓存的 extent 不重复传输。
- **后台 lazy imaging**：完整数据在后台异步写入，不阻塞用户。

### Go-Ceph 集成

Digital Ocean 是 Go 技术栈，整个流程通过 go-ceph 绑定实现：

```
RADOS connection → open RBD image → migration_prepare_import（指定 HTTP source spec）→ migration_execute → status polling → migration_commit
```


## BXC 架构设计：差量 RBD Snapshot 备份

### 传统 Ceph snapshot 的问题

- Ceph snapshot 与数据存储在同一 pool 和 cluster，集群故障时 snapshot 与数据同时丢失，不构成真正意义上的备份。
- 全量 export浪费存储与带宽。
- 依赖 QEMU change tracking 或 NBD metadata 等外部变更追踪机制，增加系统复杂度和故障点。

### 差量备份实现流程

1. 列出上一次成功备份的 snapshot。
2. 对当前数据创建新 snapshot。
3. 调用 `diff_iterate`，对比父 snapshot 获取变更的 extent 列表（dirty blocks）。
4. 调用 `read_at` 读取这些 extent 的数据。
5. 通过固定数量的 worker 并发写入目标 image store，形成新的差量 layer。
6. Commit 新 layer，删除旧的父 snapshot。

目标 image store 支持 OCI 风格的层级结构，能够理解 block offset 和 layer 之间的父子关系，与 RBD snapshot chain 的语义保持一致。

### Snapshot Chain 管理

为避免无限增长的 snapshot chain，Digital Ocean 采用以下策略：

- 用户按照配置的备份周期（cadence）保留 snapshot，过期后自动清理。
- 后台持续运行 layer 合并（collapse/converge）进程，在过期窗口到期后，判断哪些 block 可以释放，并将其合并到需要保留的 layer 中，而非简单删除旧 block。

### 灾难恢复边界

- **用户侧灾难恢复**：用户误操作导致运行时数据损坏，可通过差量备份恢复。
- **基础设施侧灾难恢复**：依赖存储设备自身的 deduplication 能力，或 Ceph 的 3x replication，failure domain 在数据传输链路的另一端。


## BXC 整体架构与编排

### 架构命名

Block Exchange（BXC）：在 RBD block system 与 image store block system 之间双向交换 block 数据。

### 编排层：Temporal

使用 **Temporal** 作为工作流编排引擎，管理两个方向的数据流：

- **前端**：gRPC 接口，接收 source URI 和 target URI。
- **Worker**：BXC worker 根据 source/target URI 判断数据流方向，触发对应的 Temporal workflow。
  - **备份方向**（RBD → image store）：执行 snapshot、diff_iterate、dirty block export、layer commit流程。
  - **镜像写入方向**（image store → RBD）：初始化 HTTP server（Block Image Daemon），触发 RBD import-only live migration，并负责 status polling 与 commit。


## Q&A 摘要

**Q：差量 snapshot chain 在灾难恢复时的 reconciliation 复杂度如何？**

A：Digital Ocean 通过持续运行的 layer 合并进程来避免无限长的 chain。过期窗口到期后，系统自动判断可释放的 block 并合并到保留 layer，而非依赖手动清理。对于基础设施级别的灾难恢复，依赖存储设备或 Ceph 3x replication 保障，差量系统主要面向用户侧的数据恢复场景。

**Q（演讲者反问）：是否有其他团队在做 RBD volumes 的差量备份？**

现场反应热烈，表明该方案具有较强的参考价值。
