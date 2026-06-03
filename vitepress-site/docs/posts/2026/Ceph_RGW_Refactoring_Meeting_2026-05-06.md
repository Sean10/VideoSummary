---
title: "Ceph RGW Refactoring Meeting 2026-05-06"
date: 2026-05-06
updated: 2026-05-14
tags:
  - "RGW"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概要

本次 RGW Refactoring Meeting 主要围绕两个议题展开：cloud transition 的异步删除支持，以及 lifecycle 处理的多线程优化方案。

## 议题一：Cloud Transition 异步删除支持（Matthew）

Matthew 介绍了一个正在审查中的 PR，目标是为 cloud transition 功能添加对云端对象的异步删除调用支持。

**主要特性：**

- 引入 FIFO Queue 机制，支持退避（back-off）策略
- 提供对应的 CLI 输出
- 该功能为 opt-in，默认不开启，保持 cloud tier 作为归档系统的基本定位

**背景说明：**

部分运营商已将 cloud transition 的使用场景扩展到其原始设计范围之外，需要将 RGW 的删除操作同步到 cloud tier 端点。此 PR 在一定程度上补全了 cloud transition 的功能闭环。

由于 Samia 本周不在，Matthew 希望先收集社区的初步反馈。据悉 Samia 此前对该方案持开放态度。

## 议题二：Lifecycle 多线程处理方案（Matthew）

Matthew 的团队针对 lifecycle 处理性能问题提出了两种竞争方案，核心目标是提升大桶（large bucket）的 lifecycle 处理速度。

### 方案一：Intra-RGW 多线程（单 Daemon 内部并行）

- 保持现有 on-disk 格式不变
- 新增约 200 行代码，配合部分重构
- 引入内存队列（in-memory queue），对大桶创建 fan-out 队列
- 空闲的 LC worker 完成自身调度桶后，进入 fan-out 队列协助处理长时运行的 lifecycle 任务
- 初步 PoC 结果：对长时运行的桶，处理速度提升 2~3 倍，且对 OSD 负载影响较小
- 实现相对简单，但仅限单 Daemon 范围内的并行

### 方案二：Cross-RGW 多线程（跨 Daemon 协同）

- 修改 on-disk 格式，使不同 RGW daemon 可独立处理同一个桶
- 利用 OMAP 在多个 RGW daemon 之间进行调度协调
- 可将集群中所有空闲 worker 纳入参与，潜力更大
- 实现复杂度高，存在调度竞态（race condition）风险，RADOS 写入开销也更大

### 社区讨论

与会者就当前瓶颈进行了讨论：

- 当前 lifecycle 处理瓶颈更多在于对象操作 throttle，而非 CPU
- 建议考虑部署专用 RGW daemon 处理 lifecycle，配置更大的 throttle 上限
- 对于极端大桶场景（单桶 100~200 亿对象），跨 worker 拆分处理可能是必要的

**实际用户场景：**

Matthew 分享了一个典型客户案例：某视频处理公司受法律合规约束，需在规定时间内删除特定视频，若 lifecycle 处理不及时将构成 SLA 违约。该客户预计单桶对象数将达到 150~200 亿，且每晚需批量过期大量对象。

目前团队正与该客户协商将数据分散到多个桶或多个区域端点，但客户应用改造存在一定阻力，因此短期内仍需从 RGW 侧提升 lifecycle 处理能力。

**结论：**

Casey 表示希望尽量避免拆分单桶处理逻辑，但承认在极端场景下可能确有必要，后续将与 Matt 团队进一步讨论最佳设计方案。

## 公告

Ceph 版本 Reef（Umbrella）的 feature freeze 将于本月底到来，有意合入新功能的开发者需在本月内完成相关工作。
