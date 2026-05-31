---
title: Ceph User + Dev Monthly Meetup - May 2026
date: 2026-05-27
updated: 2026-05-27
tags:
- Ceph
- BlueStore
- OSD
categories: 
- 视频总结
subtitle: Ceph_User_+_Dev_Monthly_Meetup_-_May_2026
---

## 会议概述

本次 Ceph 用户与开发者月度例会于 2026 年 5 月举行，涵盖 dashboard 新功能展示、VMware vSphere 与 NVMe TCP 集成问题讨论、Crimson 项目进展询问，以及异构磁盘集群使用经验分享等多个议题。

## 一、Dashboard 概览页面展示

### 初始集群视图

演讲者 Afne 展示了 Ceph dashboard 的全新 onboarding 页面。当集群通过 `cephadm` 完成 bootstrap 后，页面会显示欢迎信息并提示最低配置要求，引导用户决定是否跳过存储配置流程直接进入集群概览页。

初始集群状态展示要点：

- **数据弹性（Data Resiliency）**：所有 PG 均处于 active clean 状态，465 个 placement groups 全部健康，数据完全复制可用
- **系统状态（Systems Tab）**：MON 正常运行，但仅有一个 active manager，无 standby manager，dashboard 对此发出警告
- **OSD 状态**：所有 OSD 均处于 in/up 状态，所有节点可用，无活跃告警
- **性能数据**：初始状态下 IOPS、延迟和吞吐量数据为空

### 成熟集群视图

演讲者切换至一个创建于 5 月 21 日的成熟集群进行对比展示：

- **消费趋势卡片（Consumption Trend）**：仅在有足够用户数据时显示，提供存储填满时间的粗略估算（约 7 小时），以及每日平均消费量（约 70 GB/天）
- **性能图表**：支持按时间跨度（最近几天/30 天）查看，可独立切换读/写 IOPS 及读/写吞吐量的显示
- **存储分解视图**：展示 raw capacity 的详细分布，包含 block pools和 object storage buckets 的占用情况
- **告警系统**：展示了多个严重告警，包括 module crash需要排查

### 故障模拟演示

演讲者通过以下操作模拟集群异常状态：

- 手动将一个 OSD 标记为 down，触发 PG 状态变化
- 调低 near full ratio阈值，触发高存储使用率告警
- 展示 data resiliency 指标的实时响应：active clean PG 百分比降至 0，超过半数 PG 进入 degraded 状态，部分 PG 处于 undersized 状态
- 一个节点离线，一个 MON 退出 quorum，6 个 OSD 中仅 4 个处于 in/up 状态

dashboard 能够实时捕捉集群状态变化，响应速度较快。

## 二、VMware vSphere 7/8 与 NVMe TCP 集成问题

### 背景

社区新成员 Zoha 正在对 VMware vSphere 环境下 Ceph 的 NVMe over TCP（block storage）进行 benchmarking，整体性能结果良好，但存在稳定性问题。

### 问题一：NTP 时间同步

**现象**：在超融合平台上，NTP 同步不稳定时会导致 NVMe TCP gateway 频繁崩溃。

**具体经历**：
- 使用 chrony 进行时间同步效果不佳
- 切换为 Ubuntu 原生 NTP 服务后有所改善，但节点重启后仍出现 NTP 同步问题
- 存在明显的时间漂移（time drift）

**社区建议**：
- 社区成员 Philip 分享了一种可行方案：指定一台服务器与外部 NTP 服务器同步，其余 Ceph 节点统一指向该服务器，即使其他节点离线也能保持稳定
- Philip 表示愿意分享其 chrony 配置文件，双方约定后续通过 Google Meet 进一步交流

### 问题二：VMware vSphere Full Clone 性能

**现象**：在 VMware 环境中对连接至 Ceph block storage 的虚拟机执行 full clone 操作时，耗时数小时，原因是 clone 操作未被下放（offload）至存储层执行。

**开发进展**：Ceph NVMe 核心开发者 Aviv 在会议中确认：
- vSphere full clone 功能目前正在开发中
- 当前实现方式为从一个 datastore 读取并写入另一个 datastore
- 预计在未来几个月内完成支持，属于 work in progress

**后续行动**：
- Zoha 将在 Ceph tracker 的 NVMe 项目下创建 issue，并附上相关日志
- Aviv 将跟进该 issue

### 社区资源推荐

- 订阅 **ceph-users 邮件列表**并重新发送问题（首次可能未获足够关注）
- 加入 **Ceph Slack** 相关频道
- 查阅 **Ceph GitHub** 仓库中 NVMe fabric 相关 commits
- 观看 **Ceph Days** 的 YouTube 录像（Mike 和 Aviv 的相关演讲）
- 参加每周举行的 NVMe 专项会议

## 三、Crimson 项目进展询问

社区成员询问 Crimson（针对 NVMe 优化的新一代 Ceph OSD 实现）的开发进展。

**回应**：Crimson 项目仍在积极开发中，有专属团队负责推进，最新进展可在 Ceph 官网的 Crimson 项目页面查阅。

## 四、NVMe over TCP 成熟度

社区成员询问 NVMe over TCP 及 NVMe over RoCE（NVMe-oF）的成熟度。

- Ceph 官方文档中有相关说明
- Zoha 分享了 IBM 提供的 NVMe TCP 配置文档链接（已附于会议 etherpad）
- 整体而言，NVMe over TCP 已可用于生产环境，但在特定配置（如 VMware 集成）下仍存在稳定性挑战

## 五、异构磁盘集群使用经验

Gregory 提问：在使用不同容量磁盘的异构集群时是否存在明显坑点？

**社区经验分享**：

- 异构磁盘集群可以正常运行，但需要关注 **PG 分布不均衡**问题
- 容量较小的磁盘可能因 PG 分配比例相同而导致使用率过高
- **解决方案**：通过调整 CRUSH weight 进行手动 rebalancing，例如对 1TB 磁盘相对于 4TB 磁盘适当降低权重（`ceph osd crush reweight`）
- 操作并不复杂，整体可控

## 后续行动计划

| 负责人 | 行动项 |
|--------|--------|
| Zoha | 在 Ceph tracker NVMe 项目下创建 issue，附上 NVMe TCP gateway崩溃日志 |
| Zoha & Philip | 通过 Google Meet 交流 chrony NTP 配置方案 |
| Anthony | 本周内通过邮件列表和 Slack 发送会议时间调查问卷 |
| 会议组织者 | 将 NVMe tracker 项目链接和 IBM 文档链接更新至 etherpad |

## 下次会议

下次月度例会将于 2026 年 6 月举行，欢迎持续关注 ceph-users 邮件列表及 Slack 频道获取会议通知。
