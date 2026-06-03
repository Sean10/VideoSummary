---
title: "Rook Ceph Disaster Recovery"
date: 2026-04-02
updated: 2026-04-03
tags:
  - "Ceph"
  - "Kubernetes"
  - "Rook"
  - "OSD"
categories:
  - "视频总结"
outline: deep
---
## 概述

本文整理自 Dinakaran（NPCA 公司 MLOps 工程师）的技术分享，主题为在 Kubernetes 集群中运行 Rook Ceph 时的灾难恢复策略。演讲涵盖了生产环境中常见的四类故障场景，并通过实操演示展示了如何在完全销毁集群后实现无数据丢失的恢复。


## 场景一：MON 仲裁恢复（Recovering MON Quorum）

MON 仲裁丢失是 Ceph 集群中最常见的故障之一，通常由节点突然重启导致。

**恢复步骤：**

1. 使用 `kubectl get pods` 检查 MON Pod 状态，确认哪些 MON 处于 `CrashLoopBackOff` 状态。
2. 删除异常的 MON Pod，Rook operator 会自动重新调度。
3. 若 MON 无法自动恢复，可通过手动命令强制添加 MON，使集群重新达到 quorum。

**关键点：** 只要有一个健康的 MON（如 mon-B），集群就具备恢复基础，通过重启或手动添加 mon-A、mon-C 即可恢复仲裁。


## 场景二：OSD 故障处理（OSD Failure）

OSD 故障通常由硬盘损坏或其他硬件问题引起。

**恢复步骤：**

1. 执行 `ceph status` 确认哪些 OSD 处于 down 状态。
2. 将故障 OSD 标记为 out：`ceph osd out <osd-id>`。
3. 将对应 Deployment 的副本数缩减为 0，停止该 OSD 进程。
4. 进入 toolbox Pod，执行 `ceph osd safe-to-destroy <osd-id>` 确认可以安全销毁。
5. 执行 `ceph osd purge <osd-id>` 从集群中彻底移除该 OSD。
6. **关键步骤（不可遗漏）：** 执行 `ceph osd tree` 确认该 OSD 已从 CRUSH map 中移除，否则后续添加新 OSD 时会遇到冲突问题。
7. 删除对应的 Deployment，完成清理。
8. 若磁盘可复用（非损坏/丢失），需执行磁盘清理操作后方可重新加入集群。


## 场景三：节点故障与替换（Node Failure / Replacement）

以 10 节点集群为例，当某个节点完全宕机时的处理流程：

**恢复步骤：**

1. 查找该节点上所有 OSD 的 ID。
2. 按照场景二的流程，逐一对每个 OSD 执行 mark out → purge → 从 CRUSH map 移除的操作。
3. 所有 OSD 清理完毕后，对该节点执行 `kubectl drain` 驱逐工作负载。
4. 执行 `kubectl delete node` 将节点从集群中移除。
5. 新节点加入集群后，Rook 会自动发现并纳管新磁盘，重新加入 OSD。


## 场景四：PG 不一致修复（PG Inconsistent）

由于网络抖动或其他异常，PG 可能出现 degraded 或 inconsistent 状态。

**恢复步骤：**

1. 执行 `ceph status` 发现 PG 异常提示。
2. 执行 `ceph health detail` 获取具体受影响的 PG ID。
3. 针对该 PG 执行修复命令：`ceph pg repair <pg-id>`，确保各副本数据一致。
4. 执行 `ceph pg deep-scrub <pg-id>` 进行深度扫描，检测并修复数据损坏。


## 实操演示：完整集群销毁与恢复（Full Cluster Restore Demo）

演讲者通过现场演示，展示了在 Kubernetes 上完全删除 Rook Ceph 集群后，如何实现无数据丢失的恢复。

### 演示环境准备

- 部署 Rook Ceph 集群，确认所有组件（OSD、MON、CSI、operator）正常运行。
- 部署一个测试应用，该应用通过 RBD 存储数据库，每秒写入一条递增数字记录。
- 应用获取外部 IP 后开始持续写入，最后写入数字为 **18**。

### 集群销毁过程

1. 直接 `kubectl delete namespace rook-ceph` 无法完全删除，因为 Rook 使用 finalizers 保护关键资源。
2. **关键操作：** 在删除前，必须备份以下资源：
   - MON 的 ConfigMap（包含 MON endpoints、集群 FSID 等元数据）
   - MON 的 Secret（包含认证密钥）
3. 手动移除各资源的 finalizers，依次处理：ConfigMap、Secret、CephBlockPool、CSI 相关 Profile 等。
4. 强制删除 namespace，确认 `rook-ceph` namespace 完全消失。

### 集群恢复过程

1. 重新应用 CRD（Custom Resource Definition），已存在的 CRD 会跳过，缺失的会重新创建。
2. 重新部署 Rook operator。
3. **核心步骤：** 将之前备份的 ConfigMap 和 Secret 重新应用到集群中。Rook operator 会读取旧的 MON IP 和元数据，从而识别并重建原有集群，而非创建新集群。
4. 重新应用 cluster.yaml，重启 operator。
5. 观察集群状态，operator 会自动拉起所有 MON 和 OSD，恢复原有集群状态。

### 恢复验证

- 集群恢复后，测试应用自动重新连接并继续写入，数字从 **27** 开始（18 之后因集群重建耗时约 9 秒）。
- 进入 toolbox Pod 执行 `ceph status`，对比恢复前后的 **FSID（Cluster ID）** 完全一致，证明恢复的是原有集群，数据完整无损。


## 关键结论

- Rook Ceph 的 finalizers 机制是保护集群元数据的重要手段，灾难恢复的核心在于**提前备份 MON ConfigMap 和 Secret**。
- 只要 MON 的元数据（endpoints、FSID、认证信息）完整保留，即使集群被完全删除，也可以实现无数据丢失的完整恢复。
- OSD 故障处理中，从 CRUSH map 移除是容易被遗漏但至关重要的步骤。
- PG inconsistent 问题通过 `repair` 和 `deep-scrub` 组合命令可有效解决。
