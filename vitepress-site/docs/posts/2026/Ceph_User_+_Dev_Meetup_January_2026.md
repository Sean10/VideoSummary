---
title: "Ceph User + Dev Meetup January 2026"
date: 2026-01-28
updated: 2026-01-29
tags:
  - "Ceph"
  - "BlueStore"
  - "OSD"
  - "RBD"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph User + Dev Meetup 于 2026 年 1 月举行，主要围绕两个核心议题展开讨论：一是 bluestore elastic shared blobs 数据损坏 bug 的告警机制问题，二是 RBD namespace 级别 quota 支持的可行性分析。

## 议题一：BlueStore Elastic Shared Blobs Bug 的告警机制

### 背景

该 bug 与 bluestore 的 elastic shared blobs 特性相关。当该特性开启时，会触发 OSD 元数据损坏问题。具体表现为：

- 执行 `fsck` 检查时不会报错，集群看似正常
- 但在写入对象时会触发断言失败（assert）导致 OSD 崩溃
- 损坏的对象甚至无法被删除，因为删除操作同样会访问并尝试修改损坏的元数据
- **唯一的修复方式是重新部署受影响的 OSD**

### 修复状态

- **Tentacle** 版本：已修复并发布
- **Squid** 版本：修复已合并，但尚未正式发布

需要特别注意的是，代码层面的修复仅防止新的损坏发生，**无法修复已经损坏的元数据**。因此，即使升级到修复版本，历史上已损坏的 OSD 仍可能在未来某个时刻崩溃。

### 核心争议：是否应添加 health warning

讨论中各方观点如下：

**支持添加 health warning 的观点（Stefan、Frederick 等）：**
- health warning 是确保运维人员注意到问题的最可靠渠道，大多数运维人员会定期检查集群状态
- 该 bug 可能导致数据丢失，属于关键级别问题
- 运维人员不应被要求回溯阅读所有历史版本的 release notes，尤其是在人员交接后新接手的管理员
- 即使升级到新版本，历史损坏的 OSD 仍存在风险，这是一个持续性的运维问题

**反对直接添加 health warning 的观点（Adam、Laura 等）：**
- 历史上 health warning 主要用于反映集群当前运行状态（如 MON 磁盘空间不足），而非针对特定 bug
- 如果有 500 个 OSD 受影响，升级时日志中会出现 500 条告警，噪音过大
- 针对特定 bug 的处理方式历来是通过 release notes 和文档中的故障排查章节
- 告警触发条件的界定本身也存在复杂性

**Adam 提出的折中方案：**
- 在 OSD 层面写入 cluster error log，而非引入新的 health warning 基础设施
- 利用现有监控工具（如 Loki）解析日志，在 dashboard 中展示相关信息
- 可考虑将 health warning 体系扩展为分级告警（alert / warning / info），将此类 bug 归入 alert 类别

### 更广泛的讨论：如何有效通知运维人员

Joel 指出，Pacific 版本的 release notes 中曾有过 "DANGER: DO NOT UPGRADE" 的醒目警告（针对 OMAP 格式转换 bug），这是开发者主动在 release notes 中标注关键 bug 的先例。

与会者普遍认同存在一个信息传递的缺口：
- 部分运维人员不跟踪邮件列表和更新动态
- release notes 只覆盖部分信息，无法替代运维社区的实践经验
- 需要一个更主动的机制，让运维人员能够及时获知影响数据完整性的关键问题

**最终共识：** 各方同意确实需要一个易于运维人员发现的通知渠道，但具体实现方式（health warning、cluster error log、还是其他机制）需要在邮件列表或后续会议中进行更广泛的讨论，并征求更多长期参与项目的开发者意见。

## 议题二：RBD Namespace 级别 Quota 支持

### 需求背景（Stefan 提出）

RBD namespace 支持为多租户场景提供了隔离能力，但目前缺少 quota 支持，导致：
- 单个租户可能占满整个 pool，成为"noisy neighbor"
- 现有的 pool quota 会影响所有租户，无法实现细粒度控制
- 在 Proxmox/QEMU 等虚拟化场景中，namespace 级别的 quota 可以减少 pool 数量，提升 PG 利用效率

该需求在 Cephalocon dev summit 期间也获得了广泛认可。

### 技术分析（Ilia 详细解析）

**RBD namespace 的底层实现：**

RBD namespace 本质上是 RADOS namespace，其物理实现仅是对象名称中的一个特殊前缀。RADOS 层面的 namespace 是**隐式创建、隐式销毁**的，OSD 中没有任何与 namespace 关联的数据结构。RBD 在此基础上增加了 `namespace create/list/remove` 命令，主要用于提供更好的错误提示。

**物理级别 quota（按实际使用空间）：**
- 需要在 RADOS/OSD 层实现，RBD 层无法独立完成
- 需要引入全新的数据结构来追踪 namespace
- 需要复杂的同步机制来强制执行 quota
- 实现难度：**困难到非常困难**
- 结论：需将此 tracker 移至 RADOS 项目

**逻辑级别 quota（按预分配空间）：**
- 可在 RBD 层实现，因为 RBD 维护了 namespace 的管理层
- 但存在严重的实用性问题：
  - thin provisioning 场景下，逻辑空间几乎是"免费"的，限制意义不大
  - snapshot 的计算方式存在两难困境：若计入 quota，每次快照都需按镜像全量大小计算（100GB 镜像拍一次快照即占用 200GB quota），极不实用；若不计入，则恶意用户可通过反复创建快照耗尽集群空间
- 结论：逻辑级别 quota 要么过于严苛导致不可用，要么形同虚设

**Proxmox 的立场：**
- 前 Proxmox 开发者在聊天中指出，quota 会导致 VM 的 IO 被阻塞，因此 Proxmox 建议不对 RBD 使用 quota

**关于阻塞行为的补充讨论：**

Ilia 提出可以为 RBD 实现一个可选 flag，使 quota 超限时立即返回错误（而非阻塞 IO）。这样 VM 的根文件系统会进入只读模式，虽然 VM 仍需重启，但至少不会无限期挂起。默认行为可保持阻塞模式以兼容历史行为。

### 结论

- 物理级别 namespace quota 需移至 RADOS 层实现，技术复杂度高
- 逻辑级别 quota 实用价值有限，更适合由上层编排工具或自定义脚本实现
- Laura 将更新 tracker，明确 quota 类型并调整归属项目

## 后续行动计划

1. **BlueStore bug 告警机制**：Laura 将联系更多长期开发者，在邮件列表或下次会议中继续讨论；同时检查并完善 Tentacle/Squid 相关 release notes 中的操作指引
2. **RBD namespace quota**：更新 tracker 注释，明确物理级别 quota 需在 RADOS 层实现，并将 ticket 移至对应项目
3. 本次未能覆盖的其他 tracker tickets 将在后续会议中逐一跟进
