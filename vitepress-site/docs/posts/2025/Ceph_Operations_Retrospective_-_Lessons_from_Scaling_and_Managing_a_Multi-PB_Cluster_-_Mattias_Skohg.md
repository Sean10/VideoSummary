---
title: "Ceph Operations Retrospective- Lessons from Scaling and Managing a Multi-PB Cluster - Mattias Skohg"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "分布式存储"
  - "高可用性"
categories:
  - "视频总结"
outline: deep
---
### 改进后的中文总结内容

Matias C，Engine Nordic 的 CTO，在斯德哥尔摩分享了他在一个 Ceph 集群项目中的经验，该项目从 4.5 PB 扩展到 8 PB，涵盖了硬件设计、集群设置、遇到的挑战以及扩展过程。

#### 项目背景
- 客户原本计划将硬件用于 vWar 和 IceWarp Gateway，但后来转向使用 CephFS 存储仪器数据、RGW 作为备份和迁移目标，并考虑用于 OpenShift CSI 连接。
- 使用了 10 台服务器，每台配备 28 块 HDD 和 2 块 SSD，没有 NVMe。

#### 集群设置
- 使用了 Ceph Pacific 版本，300 个 OSD，总容量约 4.5 PB。
- 数据和元数据存储在 HDD 上，SSD 用于 RocksDB 的 BlueFS。
- 最初尝试了多 MDS 设置，但由于性能问题，最终回退到单 MDS。
- 使用子卷和子卷组设置文件系统。

#### 遇到的挑战
- 多 MDS 设置导致性能问题，回退到单 MDS。
- 缺乏备份，启用 CephFS 快照作为临时解决方案，但导致了后续的严重问题。
- 文件系统崩溃，需要通过删除损坏的文件和对象来恢复。

#### 集群扩展
- 从 4.5 PB 扩展到 8 PB，添加了新的节点。
- PG 数量不足，导致数据分布不均，逐步增加 PG 数量以解决。
- 扩展过程需要几天到几个月。

#### 经验教训
- 测试集群的重要性。
- PG 数量调整的时机。
- 备份的必要性。
- 扩展计划的提前规划。

#### 未来计划
- 在现有集群中创建 NVMe 元数据池。
- 考虑启动新的集群以避免旧集群的限制。

Matias C 的分享强调了在大型 Ceph 集群中进行操作时需要注意的关键事项，包括硬件选择、集群设置、备份策略和扩展计划。他的经验教训对于其他 Ceph 用户和管理员来说是非常宝贵的。

### 相关标签
- Ceph
- Distributed Storage
- Scale-Out Storage
- Storage Management
- High Availability