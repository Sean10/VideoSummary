---
title: "Implementing Ceph at GMUs College of Engineering and Computing"
date: 2026-04-21
updated: 2026-04-21
tags:
  - "Ceph"
  - "分布式存储"
  - "OpenStack"
categories:
  - "视频总结"
outline: deep
---
## 演讲者与机构背景

本次演讲由 Dan O'Brien 主讲，他就职于乔治梅森大学（George Mason University，GMU）工程与计算学院，自 2018 年起负责 Linux 系统管理工作，同时承担 Ceph 存储集群的运维管理职责。

乔治梅森大学位于弗吉尼亚州费尔法克斯，在校学生约 4万人。工程与计算学院是全校最大的学术单位，学生人数超过 1 万。IT 架构上，学校采用分布式 IT 模式：中央 IT 负责网络服务、身份认证及数据中心运营；研究计算办公室运营高性能计算集群；分布式 IT 团队（即演讲者所在团队）主要管理教学用术系统、计算机实验室及教职工桌面支持。

基础设施以 Dell 服务器为主，操作系统以 RHEL/Rocky Linux 为主，服务器机房具备 10Gigabit Ethernet 骨干网络互联。

## 存储挑战：引入 Ceph 的背景

在引入 Ceph 之前，该学院面临多项典型的存储管理痛点：

- **数据分散**：大量数据存放在 VM 的虚拟磁盘上，缺乏统一管理
- **high availability 不足**：并非所有平台都具备高可用保障
- **scalability 差**：现有架构难以横向扩展
- **生命周期管理混乱**：存在大量 EOL 操作系统仍在运行，数据管理生命周期极为临时化
- **用户群体复杂**：兼职教师、在读学生、毕业后返校读研的学生等，用户状态频繁变化，数据归属难以追踪

## 当前 Ceph 集群配置

目前的 Ceph 集群通过 cephadm 容器化部署，规模较小但功能完整：

- **存储节点**：3 个 storage node
- **服务节点**：2 个，运行各类 daemon 和 gateway
- **OSD**：25 个，原始存储容量 128 TB
- **存储介质**：SD 作为缓存层，HDD 作为主存储（当前子集群全为 HDD）
- **网络**：10 Gigabit 骨干，存储节点配置 LACP bonding，实现 20 Gbps 双向带宽；通过 VLAN 隔离 Ceph 后端网络与 iSCSI 网络

## Ceph 的引入历程

最初引入 Ceph 是为了配合 OpenStack 实验。团队原本考虑使用 NFS，但发现配置复杂，转而搭建单节点 Ceph 集群（仅几块 HDD，无 SD），因为 OpenStack 原生支持 Ceph 作为存储后端，集成更为顺畅。目前已有多个 OpenStack 实例共用同一套 Ceph 后端。

Ceph 2024 纽约峰会（Ceph Day 2024 NYC）成为重要转折点，团队在会后正式决定全面投入 Ceph，并在会后补充了 WAL（Write-Ahead Log）和 RocksDB 的 SD 配置。

## cephfs 替代 NFS 的主目录迁移

### 问题起因

原有 3 台 NFS 服务器各自独立，主目录随机分配，依赖复杂的 automount 脚本定位挂载点，缺乏 high availability 保障。

### 数据摸底工具

迁移前，演讲者开发了一套自制库存工具，遍历三台 NFS 服务器，按用户 ID 收集主目录大小、文件数量等统计信息，并整合课程注册信息与在职/在读状态，写入 CSV 后导入 SQLite 数据库，支持精准查询定向迁移目标。

### 迁移触发事件

2025 年 5 月，计算机科学学生大规模采用 VS Code，导致 NFS 服务器在期末作业截止前出现严重 IO 压力：约 200 名学生同时在线，每台 Zeus 系统约 100 个并发用户，超过一半使用 Visual Studio，每秒产生 50KB 至 1MB 的 IO，Dell PERC 卡的 NFS 服务器不堪重负。

### cephfs 配置

- 单一 cephfs 文件系统
- 多个 MDS，配置热备（hot standby）
- 按 subvolume 组织，兼顾管理便利性与数据安全隔离
- 针对不同数据类型创建独立 pool

### 迁移进展

- 按主目录数量：已完成约 95%（约 16,000 个在 cephfs，约 800 个仍在 NFS）
- 按数据量：仅完成约 50%（剩余均为"硬骨头"——大体积目录）
- 迁移脚本核心为 rsync，跳过 Visual Studio 缓存目录（`.cache`、JetBrains 缓存等）
- 实测效果显著：部分主目录迁移后体积缩减 90%（100MB → 10MB）；迁移超过 3TB 数据后，cephfs 中实际仅占用约 1.2TB，推测 NFS 的 4K block与 cephfs 的 512B block 差异也贡献了可观的空间节省
- 当前 cephfs 中约有 2400 万个文件

### 迁移效果

自 CS 学生主目录迁移至 cephfs 后，期末考试和期中考试期间**零宕机**，CS 教职工对此高度满意。

## Quota 管理

为防止 cephfs 重蹈 NFS 混乱局面，团队基于库存数据制定了 quota 策略：

- **学生**：10 GB / 用户（原计划 5 GB，经上级建议调整）
- **教职工**：250 GB + 50 万文件数上限
- 主目录创建或迁移时自动设置 quota
- 提供自助临时提额脚本，用户无需开工单即可申请短期扩容
- 登录时展示当前使用率：75% 显示黄色警告，90% 及以上显示红色警告

## 其他 Ceph 功能应用

### NFS Gateway

部分老旧系统（如仍运行 RHEL 6 的节点）无法直接挂载 cephfs，通过 NFS gateway 转接访问。此外，部分 VM 所在的旧 oVirt 集群因网络架构限制无法直接访问存储网络，同样依赖 NFS gateway。

### Block Storage（RBD）

oVirt 集群使用 Ceph RBD 作为 block storage 后端。正在评估新 oVirt 集群（RHEL 9 节点）直接使用 Ceph managed block storage，但尚未完全调通。

### Object Storage（RGW）

已搭建 RGW（RADOS Gateway），主要探索与 OpenStack Swift 的集成。文档中未明确说明 Ceph RGW 可直接替代 Swift，导致初期配置走了弯路。目前已部署但使用有限，计划用于主目录数据的归档存储。

### Web内容存储

计划将分散在各 VM 上的 Web 内容统一迁移至 cephfs subvolume，配合反向代理架构，实现内容存储与交付解耦，提升安全性（Web 服务器不再暴露于公网子网）、简化备份与容量扩展。

## 未来规划

1. **完成 NFS 迁移**：剩余约 800 个主目录需与教职工高接触沟通确认数据去留
2. **扩展 Ceph 集群**：退役 oVirt 和 NFS 的硬件资源将并入 Ceph 集群
3. **升级至 Tentacle**：关注 iSCSI gateway 在 Squid/Tentacle 版本中的演进，以及 Samba 与 Windows Active Directory 集成能力
4. **专用 SD tier**：计划建立独立 SSD tiering 层（受预算制约）
5. **存储节点与服务节点分离**：gateway 等服务节点与 OSD 节点完全分离
6. **erasure coding**：节点数达到 5 个后启用 erasure coding，降低存储开销
7. **MDS 基础设施强化**：主要使用场景已从 OpenStack block storage 转变为约 1万名学生的主目录服务，需相应加强 MDS 配置
8. **scheduled snapshots**：应对期末高峰期"误删文件"的求助工单，提供比"恢复到昨天备份"更细粒度的恢复能力
9. **异地复制**：计划搭建第二套 Ceph 集群实现数据复制
10. **Storage as a Service**：为教职工提供托管存储服务，替代不受管控的 NAS 设备，解决安全隐患

## Q&A 要点

**Q：是否计划提供 S3 兼容的对象存储服务？**

A：完全在计划之中。原本引入 OpenStack 的目的之一就是为学生提供内部云资源（含虚拟机和对象存储）。演讲者同时分享了一个 AWS 成本失控的案例：一名学生因 RDS 性能不佳不断升配，另一团队使用 16xlarge GPU 实例运行 7 天才触发预算告警，累计损失约 2 万美元。这充分说明建设内部基础设施、为不熟悉云计费模型的学生提供可控环境的必要性。

**Q：高峰期并发写入规模？**

A：约 200 名学生同时活跃登录并进行编码操作，全部主目录均在 cephfs 上。

**Q：主目录总量？**

A：初始约 3 万个，经归档清理后降至约 1.5 万个。
