---
title: CephFS News
date: 2026-04-02
updated: 2026-04-03
tags:
- CephFS
- 分布式存储
- MDS
- 快照
- Ceph
categories: 
- 视频总结
subtitle: CephFS_News
---

## 概述

本次演讲由 CephFS 团队成员主讲，重点介绍了 Tentacle 版本的主要交付成果、即将发布的 Umbrella 版本的重要特性，以及 Vampire 版本的规划方向。

## Tentacle 版本主要交付

**大小写不敏感目录树（Case-Insensitive Directory Trees）**
为提升与 Samba 的互操作性而引入，主要面向性能优化场景。

**Block Diff RPC**
在用户空间客户端与 MDS 之间新增了一个 RPC 接口，用于推断文件在两个 snapshots 之间的变更块（changed blocks）。该特性与 mirror daemon 深度集成，可利用 block diff RPC 实现向次级集群的快速文件传输。

**操作预计完成时间（ETC）显示**
- MDS log replay 故障转移时，现可显示预计完成时间
- sub volume 删除操作进入队列后，可通过 `ceph status` 查看预计完成时间

## Umbrella 版本主要特性

### Sub Volume Metrics

针对 ODF（OpenShift Data Foundation）工作负载，新增了 per sub volume 的指标采集能力，包括：
- 读写吞吐量（read/write throughput）
- per client 的sub volume 指标

实现基于 cap 协议（capability protocol），客户端周期性地将追踪到的操作数据上报给 MDS，MDS 按 volume 聚合后提供查询接口。初期面向用户空间客户端，后续将扩展至 kernel driver。

### Snapshot 可见性控制

面向 NFS 使用场景，运维人员可动态切换 `.snap` 目录对客户端的可见性。关闭可见性后，客户端访问 snap 目录将收到错误响应，可按需随时开启或关闭。

### Sub Volume 隔离（Quarantine）

作为安全特性引入，主要应对勒索软件（ransomware）攻击场景。通过 manager volumes 提供的 quarantine 接口，可对指定 sub volume 执行隔离操作：
- 已挂载的客户端将被驱逐（evict）
- 新的挂载请求将被拒绝

### CephFS Mirror Daemon 增强

新增多项 mirroring 相关指标：
- 已同步文件数与待同步文件数
- 已同步字节数与待同步字节数
- 读写带宽（read/write bandwidth）

新增 **checkpoint 特性**：可对指定 snapshot 设置检查点，追踪该 snapshot 是否已完成同步。此外，multi-threading 支持已合并至主线，预计带来明显的性能提升。同时，与 dashboard 的集成也在本版本中落地。

### 用户空间加密支持（User Space Encryption）

CephFS 内核客户端自 Linux 6.6 起支持加密（包括目录项名称加密和文件数据加密）。Umbrella 版本将该加密实现移植至用户空间客户端，用可为指定目录配置加密密钥，无密钥者将只能看到无意义的密文数据。

### 灾难恢复工具预计完成时间

针对用户长期反映的痛点，recovery tools 执行时现可显示预计完成时间（ETC），帮助运维人员掌握恢复进度。

### 命令审计日志（Command Audit Logging）

类似 bash history，记录所有对集群状态产生修改的命令（如修改 max MDS 值、执行文件系统恢复操作等）。

**核心价值**：当用户遇到文件系统故障并寻求社区支持时，开发者可直接查询历史操作记录，无需反复与用户确认执行过哪些命令，显著降低问题排查成本。初期从 CephFS 开始，后续计划推广至整个集群。

### MDS Tracing Framework

在 MDS 中构建基础设施，为后续与 OpenTelemetry（如 Jaeger tracing）集成做准备。Umbrella 版本完成基础设施建设，但暂不做完整集成，用户已可查询 trace 数据，完整的 UI 集成将在后续版本实现。

### MDS QoS（Quality of Service）

基于 DM-Clock 算法实现，由韩国开发者贡献，是一个长期悬而未决的 pull request。Umbrella 版本以 Tech Preview 形式发布，计划在 Vampire 版本达到 General Availability（GA）。

## Vampire 版本规划方向

**快速 Snapshot 克隆（Fast Snapshot Cloning）**
当前 snapshot 克隆为全量拷贝，速度慢且随文件数量线性增长。目标是实现增量式快速克隆，逐步向 RBD 的克隆速度靠拢。

**Multi-Protocol 支持**
支持同一数据集通过 NFS 和 Samba 同时访问。目前设计规范正在制定中，NFS 团队与 SMB 团队均有人员参与。团队欢迎有相关应用场景的用户提供需求输入。

## 总结

CephFS 团队在 Tentacle 版本完成了多项基础能力建设，Umbrella 版本将带来大量面向运维和安全的增强特性，Vampire 版本则聚焦于性能突破与多协议互通。如有 multi-protocol 相关需求，欢迎与 NFS 及 SMB 团队直接沟通。
