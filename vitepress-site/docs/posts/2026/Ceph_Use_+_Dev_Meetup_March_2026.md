---
title: "Ceph Use + Dev Meetup March 2026"
date: 2026-03-20
updated: 2026-03-21
tags:
  - "Ceph"
  - "OSD"
  - "RBD"
  - "HDD"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph Use + Dev Meetup 于 2026 年 3 月举行，采用开放讨论形式，与会者就社区活动、已知 bug 及性能调优等议题展开交流。

## 议题一：Ceph Day London 征稿通知

社区组织者 Lee Sanders宣布 Ceph Day London 的 Call for Papers（CFP）正式开放。活动将于 **6 月 17 日**在伦敦举办，征稿截止日期为 **4 月 24 日**。

征稿方向包括：
- 用户实际使用案例（use cases）与用户故事
- performance 测试与优化经验
- 新功能开发进展
- 任何与 Ceph 上游社区相关的内容

有意投稿者可发送邮件至 **londonsef.io** 咨询。

此外，主持人还提醒与会者，**Ceph Days Raleigh** 将于下周举行，尚未注册的用户仍可报名参加。

## 议题二：RBD clone 展平后读取返回零的 Bug

用户 Laura 汇报了一个与 RBD clone flattening 相关的 bug（已创建 tracker）。

**问题描述：**
当客户端正在访问一个 clone snapshot 时，若该 clone 被并发执行 flatten 操作，后续的读取请求将全部返回零值，直到客户端将该 clone snapshot 执行 unmap/unmount 并重新 remap/remount 后才恢复正常。

**影响范围：**
- 初步判断影响 Squid（tentacle）等近期版本，可能在更早版本及 main 分支上同样存在
- 该问题已由 Nikola 完成初步调查，但尚无 PR 提交，需要进一步 code review

**后续行动：**
- 请求在 tracker 中补充复现所用的具体版本信息，以便提高 reproducibility
- 主持人将把该 issue 转发给 RBD 团队（Ilia 等）进行评估
- 感谢 MLA 在 ticket 中补充了复现步骤

## 议题三：大容量 HDD 上的 deep scrub 性能问题

用户 Alexandra 提出了在大容量 HDD（如 26 TB）上执行 deep scrub 时遭遇的性能瓶颈问题。

**问题背景：**
- 用户正在使用带有独立 DB volume 的大容量 HDD（26 TB）部署 Ceph（BlueStore 配置）
- deep scrub 对 HDD 而言本质上是随机读（random read）操作
- 在实际负载下（如 CephFS 存储用户数据），HDD 的随机读性能仅约 **10~20 MB/s**
- Ceph 默认的 `osd_deep_scrub_interval` 为 **1 周**，在如此大容量的 HDD 上根本无法在一周内完成一次完整的 deep scrub

**讨论要点：**

Anthony 指出：
- 在此场景下，将 `osd_deep_scrub_interval` 调大（如改为 1 个月）是常见的应对方式，但会降低 deep scrub 的保护效果，属于 tradeoff
- 使用 replication 而非 erasure coding 的集群可以承受更高频率的 scrub
- 当 **MCLOCK** 调度器正确配置并生效时，该问题会有所缓解；而使用 **WPQ** 调度器时，问题会更为突出
- scrub 速度受限的另一个原因是 **PG 粒度的 reservation 机制**：scrub 需要对该 PG 所涉及的所有 OSD 申请 reservation，容易产生"gridlock"，导致实际吞吐远低于 HDD 的顺序读上限（70~100 MB/s）

**PG 数量调优建议：**
- 若使用 PG autoscaler 默认参数，每个 OSD 的 PG 数可能仅约 60，导致单个 PG 体积过大，加剧 scrub 耗时
- 建议将每 OSD 的 PG 数调整至 **150~200**
- 可通过调整 `mon_max_pg_per_osd` 和 `mon_target_pg_per_osd` 参数实现
- Alexandra 确认该集群已禁用 autoscaler，当前每 OSD 约有 100 个 PG

**行业趋势补充：**
- Seagate 已有最高 **44 TB** 的 HDD 即将上市，HDD 容量持续增大将使该问题愈发突出
- 有观点认为默认值应随 HDD 容量动态调整，或为 HDD 与 SSD 设置不同的默认值，但修改默认值较为复杂，需谨慎评估

**后续行动：**
- Alexandra 将与 Anthony 线下沟通（Ceph Slack 或邮件），进一步排查该集群的具体配置并寻求调优方案

## 会议总结与展望

本次会议为开放讨论形式，议题较为轻松。主持人表示，未来的 userdev meetup 计划恢复针对 Ceph 核心支柱（如用户体验、performance 优化等）的专项议题讨论，并将通过 Slack 频道或用户邮件列表进一步征集议题和参与者。
