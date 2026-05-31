---
title: Detect, Decide, Fence Resolving Netsplits in 3 AZ Stretch Cluster
date: 2026-04-20
updated: 2026-04-21
tags:
- Ceph
- 高可用性
- 分布式存储
categories: 
- 视频总结
subtitle: Detect_Decide_Fence_Resolving_Netsplits_in_3_AZ_Stretch_Cluster
---

## 概述

本次演讲聚焦于 Ceph 从 2AZ（双可用区）stretch 模式扩展到 3 AZ（三可用区）部署时遇到的 split-brain 问题，以及对应的检测、决策与 fencing 解决方案。

## 背景：从 2 AZ 到 3 AZ

**2 AZ stretch 模式**将集群跨两个数据中心部署，将 failure domain 从 host/OSD 级别提升至 zone/数据中心级别。由于跨数据中心通信走 WAN 而非 LAN，网络分区（network partition）成为需要处理的核心问题。

2 AZ 模式通过引入 **tiebreaker monitor** 解决网络分区问题——tiebreaker 会自动选择连通性更好的一侧，隐式完成 net split 的解决。

随着业务对更高 availability 的需求，需要扩展到 **3 AZ**。目标同样是：在单个 zone 故障或网络分区时保持集群可用。然而，3 AZ 架构无法沿用 tiebreaker monitor 的设计，因此需要将同等能力内嵌到 MON 自身逻辑中。

## 问题：3 AZ 下的 Split-Brain

以 DC1、DC2、DC3 三个数据中心为例，当 DC1 与 DC2 之间发生网络分区时：

1. DC2 的 OSD（如 OSD 3、OSD 4）向 leader monitor 上报无法连接 DC1 的 OSD。
2. Leader monitor 将DC1 的 OSD 标记为 down。
3. 但 DC1 的 OSD 0 仍能连接到 leader monitor，并请求将自己标记回 up。
4. Leader monitor 反复在 down/up 之间切换，导致 PG 持续 re-pering，最终读写不可用。

根本原因是 monitor 在两侧都能收到消息时做出了矛盾决策，需要明确选出"胜出方"继续服务 IO。

## 解决方案：Detect → Decide → Fence

### 第一步：检测 Net Split

Ceph MON 持续追踪各 peer 之间的连通性评分。该功能已在 **Squid** 版本合并，可以：

- 在 `ceph -s` 的 health warning 中显示 monitor 级别的连通性问题（如"monitor A 无法连接 monitor D"）。
- 当 failure domain 配置为 zone/数据中心时，能够判断出 DC1 与 DC2 之间发生了完整的 net split。

### 第二步：决定胜出分区（Decide）

检测到 net split 后，需要从可能的分区组合中选出胜出方。以 DC1-DC2-DC3 为例，候选组合为 {DC1, DC3} 和 {DC2, DC3}。

**算法：Bron-Kerbosch（BK）最大团搜索**

将各 zone 建模为图的顶点，连通性为边，使用 BK 算法寻找**最大团（maximal clique）**——即每个顶点都与组内其他顶点直接相连的最大子集。由于 zone 数量在实际部署中极少，算法的指数级时间复杂度不构成问题。

在上述例子中，算法会找到两个等大的最大团：{DC1, DC3} 和 {DC2, DC3}，需要进一步决策。

**决策方式一：用户配置 net split zone preference**

用户在部署 3 AZ 前预先配置各 zone 的优先级（如 DC1 > DC2 > DC3），系统据此计算胜出分区。

**决策方式二：自动启发式（Heuristics）**

若用户不配置偏好，Ceph 按以下优先级依次比较，首个分出胜负的指标即决定胜出方：

1. **Total effective OSD weight**：OSD CRUSH weight × OSD map weight（容量），权重更高的分区胜出。
2. **Monitor 数量**：MON 更多意味着 quorum 更强，集群更稳定。
3. **Monitor 连接评分总和**：连通性更好的分区胜出。
4. **字典序比较**：若以上全部相同，则按字典序决定，确保确定性。

### 第三步：Fencing 落败分区

确定胜出分区后，需要对落败分区执行 fencing，防止其继续操作：

**Fencing 前的准备：**
- 将需要 fence 的 OSD 信息持久化到 OSD map。
- 全局设置 `no recovery`、`no backfill`，避免 fencing 过程中发生数据迁移。

**Fencing 的具体行为：**
- MON 忽略来自被 fence OSD 的所有上报和消息，从根本上消除 split-brain 的触发条件。
- 被 fence 的 OSD 不再作为 PG acting set 的候选，PG 不会选择落败分区的 OSD 参与服务。
- Fencing 期间禁止修改 net split zone preference，避免竞态条件。

**Fencing 完成后：**
- 解除全局 `no recovery`、`no backfill` 限制。
- PG 自动进入 active 状态（处于 undersized + degraded，但集群保持可用，继续服务 IO）。

## Fence 解除（Lift Fencing）

为防止 fence flapping（因瞬时网络抖动导致反复 fence/unfence），引入 **90 秒阈值**：MON 连续 90 秒未检测到网络分区，才会解除 fence。

Fence 解除后，PG 重新进入 pering 流程，最终恢复为 active+clean 状态，集群完全恢复正常。

## 边界情况处理

**场景三（不切换胜出方）：** 当 fencing 已在进行中，启发式计算发现落败分区的连通性评分反而更高时，系统**不会**切换胜出方。原因是切换代价远大于收益——切换会中断当前正在进行的操作，引入不确定性。因此保持当前选择，以次优状态继续服务 IO。

## 总结

| 阶段 | 机制 | 版本 |
|------|------|------|
| 检测 net split | MON 连通性评分 + BK 算法 | Squid（已合并） |
| 决定胜出分区 | 用户偏好 或 四级启发式 | 开发中 |
| Fencing 落败分区 | OSD map 持久化 + MON 忽略消息 | 开发中 |
| 解除 Fence | 90 秒无分区阈值 | 开发中 |

该方案将 2 AZ tiebreaker monitor 的核心思想内嵌到 MON 自身，使 3 AZ stretch cluster 在无外部仲裁节点的情况下，也能自动检测、决策并隔离网络分区，保障集群持续提供 IO 服务。
