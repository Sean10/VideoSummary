---
title: Tracking Data Availability of a Ceph Cluster
date: 2026-04-02
updated: 2026-04-03
tags:
- Ceph
- OSD
categories: 
- 视频总结
subtitle: Tracking_Data_Availability_of_a_Ceph_Cluster
---

## 演讲背景

本次演讲由 Shraddha 主讲，她与 Naveen 同属 Neha 领导下的 RADOS 团队。演讲主题是 Ceph 集群的数据可用性追踪（Data Availability Tracking）功能，涵盖功能背景、实现原理、配置选项及未来规划。

## 为什么需要这个功能

目前，用户想了解集群可用性时，通常执行 `ceph status` 或 `ceph health detail`，但这只能获取集群的**瞬时状态**（point-in-time snapshot），无法反映过去一个月乃至一年内集群的整体表现。

虽然可以将 `ceph status` 输出接入 telemetry，再通过 Prometheus 或 Grafana 可视化，但这需要大量额外工具链，并非内置能力。

更重要的是，集群健康状态与用户真正关心的问题并不完全一致。用户更关心的是：**我的读写请求能否被可靠地处理？** 为此，团队在 Reef 版本发布时进行了一次调查，59 位架构师和开发者参与，多数人表示：**能够以良好性能可靠地提供 IO 服务**，才是他们对集群可用性的定义。

## 功能介绍

该功能引入了一套机制，用于**随时间追踪数据可用性**，区别于传统的集群整体可用性概念。

核心特性：
- 默认以 **1 秒**为采样间隔（cadence）持续追踪
- 从 **Tentacle** 版本起提供，当前为 **Tech Preview** 状态
- 新增命令：`ceph osd pool availability status`

命令输出中，每一行对应一个 pool，包含以下字段：

| 字段 | 含义 |
|------|---|
| uptime | 自追踪开始以来，pool 处于可用状态的累计时长 |
| downtime | pool 处于不可用状态的累计时长 |
| number of failures | 工具捕获到的可用性故障次数 |
| MTBF | 平均故障间隔时间（Mean Time Between Failures） |
| MTTR | 平均恢复时间（Mean Time To Recover） |
| score | 可用性评分（nines 数量） |
| 当前状态 | pool 当前是否可用 |

**示例说明**：若工具运行了 60 分钟，其中 20 分钟为 downtime（无论是一次连续故障还是多次短暂故障），则 uptime 为 40 分钟，downtime 为 20 分钟。

## 实现原理

### 可用性的定义

- **可用（Available）**：pool 中所有 PG 均处于 active 状态
- **不可用（Unavailable）**：只要有一个或多个 PG 处于非 active 或 stale 状态；或者即使所有 PG 均为 active，但存在任意一个 unfound object，该 pool 也被视为不可用，直到 DBA 将这些对象标记为 unfound 或采取类似处理

### 状态转换逻辑

每次采样时，系统对比前一状态（previous state）与当前状态（current state）：

| 前一状态 | 当前状态 | 时间计入 |
|----------|----------|
| 可用 | uptime |
| 不可用 | 可用 | uptime（认为故障刚结束） |
| 可用 | 不可用 | uptime（认为故障刚开始），同时 failures +1 |
| 不可用 | 不可用 | downtime |

### 数据存储与计算

- uptime、downtime、failures 数量及当前可用状态均持久化存储在 MON 中
- MTBF 和 MTTR 在用户查询时实时计算，不持久化存储：
  - MTBF = uptime / number of failures（若 failures 为 0，则 MTBF = 1）
  - MTTR = downtime / number of failures
- **可用性评分（score）** = MTBF / (MTBF + MTTR)
  - score = 0：集群完全不可用，需要资深管理员介入
  - score = 1：从未发生故障，运行良好

## 配置选项

### 1. 启用/禁用功能

由于是 Tech Preview，默认**禁用**。启用命令：

```
ceph config set mon enable_availability_tracking true
```

建议：在预期维护窗口（planned downtime）期间，应先禁用该功能，维护完成后再重新启用，避免计划内停机影响 SLA 统计。该配置支持**运行时修改**，无需重启。

### 2. 调整采样间隔（cadence）

不同集群对采样精度的需求不同，可自定义间隔。默认值为 1 秒，从 Tentacle 首个版本起支持。

注意：由于依赖 Paxos，该值不能小于 Paxos 的 propose interval；且功能关闭时无法修改。

### 3. 清除单个 pool 的可用性统计

若某 pool 发生了预期内的异常（如计划停机 3 小时），可清除该 pool 的历史统计，避免影响整体 SLA 评估：

```
ceph osd pool clear-availability-stats <pool-name>
```

执行后，uptime、downtime 等所有数值归零。功能关闭时不可操作。

### 4. JSON 格式输出

随着时间推移，人类可读格式（如"30 天"）精度不足。可使用 `--format json-pretty` 获取精确数值，从 Tentacle 第一个 point release 起支持。

## 未来规划

### 升级时自动暂停追踪

Ceph 升级（包括滚动升级，逐个更新 daemon）期间会产生预期停机。未来版本将支持：升级开始时**自动禁用**可用性追踪，升级完成后**自动重新启用**。

注意：仅对原本已启用该功能的集群生效，不会主动为用户开启。

### 接入 Telemetry 可视化历史趋势

当前功能可追踪累计可用性，但无法展示评分随时间的变化趋势。未来将把 score 数据上报至 telemetry，用户可据此可视化可用性评分的历史演变。

## 参考资源

- 官方文档：可用于启用功能并进行试用
- Trello 看板及 CDS Reef 会议记录：可了解功能演进历史

## 行动呼吁

- 欢迎在上游社区 Slack 或邮件列表提供反馈
- 团队正在寻求**大规模测试**的合作方，欢迎启用该功能并反馈实际可用性评分数据
