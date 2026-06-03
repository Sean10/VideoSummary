---
title: "Ceph User + Dev Monthly - April 2026"
date: 2026-04-15
updated: 2026-04-16
tags:
  - "Ceph"
  - "RGW"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph 用户与开发者月度会议（2026年4月）涵盖三个主要议题：PG autoscaler 的均匀分配改进、RGW auto tiering 的实践经验与讨论，以及 BlueStore 相关 bug 的排查与 RGW admin 删除对象功能的需求说明。


## 议题一：PG Autoscaler 均匀分配问题改进

### 背景介绍

演讲者 Eric是 RADOS 团队的 co-op 开发者，入职约两个月。本次分享了他在 PG autoscaler 上所做的改进工作。

### 问题描述

PG autoscaler 的核心功能是根据各 pool 的数据量自动调整 PG 数量。用户可通过 `target_sizeratio`（目标容量占比）或 `target_size_bytes`（目标字节数）进行配置。

**已知 Bug**：当多个 pool 设置了相同的 `target_size_ratio` 时，autoscaler 并不会为它们分配相同数量的 PG。

**根本原因**：当前实现采用"先到先得"的顺序迭代方式。每处理完一个 pool，就从总 PG 预算中扣除已分配的数量，导致后续 pool 的计算基数不断缩小。

**示例**：假设总预算为 6,000 PGs，三个 pool 各设 `target_size_ratio = 0.33`：
- Pool 1：1/3 × 6,000 = 2,000，除以 3 副本 ≈ 667，向下取整到 512，实际分配 1,536 PGs
- Pool 2：1/3 × 4,464（剩余预算）≈ 512，仍可分配 1,536 PGs
- Pool 3：1/3 × 2,928（剩余预算）≈ 256，实际分配 768 PGs

结果三个 pool 分配不均，最后一个 pool 被"饿死"。

### 解决方案

Eric 将此问题建模为类似**背包问题（Knapsack Problem）**的动态规划优化：

1. **Pool 分组**：将具有相同配置（PG target、replication size、biasbulk、autoscale enabled）的 pool 归为一组，确保同组内所有 pool 向同一方向取整（全部向上或全部向下），保证公平性。

2. **全局优化**：初始状态假设所有 pool 均向下取整到最近的 2 的幂次，然后逐组迭代，判断是否可以向上取整（不超出预算），选择总代价（与目标值偏差之和）最小的方案。

3. **时间复杂度**：O(n log m)，其中 n 为 pool 数量，m 为总 PG 预算。

该改进已提交 Pull Request，无需用户手动配置，升级后自动生效。

### 讨论要点

**关于 erasure coding pool 的支持**：与会者 Anscar 询问此方案是否适用于 erasure coded pool。Eric 确认同样适用，因为 pool 大小计算方式一致，只需将副本数替换为 k+m 即可。

**关于 PG 大小 vs PG 数量**：Anscar 提出随着硬盘容量不断增大（如 245TB 的驱动器即将上市），autoscaler 是否应更关注单个 PG 的大小而非每 OSD 的 PG 数量。

Anthony 补充说明：
- CRUSH algorithm 会保证各 OSD 的 PG 数量与其权重（容量）成比例，大容量 OSD 自然会获得更多 PG。
- J balancer 已经考虑了 PG 大小因素，autoscaler 与 balancer 是相关但不同的组件，不应混淆。
- 建议将 `mon_target_pg_per_osd` 从默认值 100 提升至 200，以给 balancer 更大的工作空间。
- 将 balancer 的 `max_deviation` 从 5 调整为 1，可显著改善混合 OSD 大小集群的均衡效果。

**文档问题**：与会者指出，`mon_target_pg_per_osd` 的文档不够清晰——在混合 OSD 大小的集群中，该参数究竟是针对哪种 OSD 的平均值？建议补充文档说明。Anthony 请其提交 tracker issue 并tag 他跟进。


## 议题二：RGW Auto Tiering 实践与讨论

### Hetzner 的实践经验

来自 Hetzner 的工程师分享了他们在 RGW 中实现 auto tiering 的经验：

**背景**：Hetzner 发现约 13% 的 S3 对象小于 4 KB，这类小对象放在 erasure coded pool 中效率极低。

**分层策略**：
- 小于 4 KB 的对象→ NVMe replicated pool
- 小于 erasure coding 写放大阈值的对象 → HDD replicated pool
- 其余对象 → erasure coded pool

**实现方式**：基于社区 Lua 脚本方案，在上传时根据对象大小自动设置 storage class。

**遇到的问题**：

1. **Storage class 泄露**：客户在 list bucket 时会看到内部使用的 storage class 名称。Hetzner 已开发内部补丁，将对客户展示的 storage class 与内部实际使用的隔离，计划贡献至上游。

2. **生命周期策略干扰**：若客户知晓内部 storage class，可自行编写 lifecycle policy 将数据从 HDD 迁移至 NVMe，绕过服务商的管控。目前考虑在 RGW 层面拦截包含受限 storage class 的 lifecycle policy 请求。

3. **存量数据迁移**：为解决已有数据的迁移问题，Hetzner 开发了 `radosgw-admin object rewrite` 命令扩展，支持指定目标 storage class，可根据对象大小批量迁移存量数据。

### 社区讨论

**Philip（另一家服务商）**：也在使用类似方案，主要痛点是按 storage class 统计对象数量和用量，目前通过对象计数方式处理，但不够理想。Casey 补充说上游已有相关 PR，将支持按 storage class 分别统计 bucket 用量并配置配额。

**Frederick 的分析**：Hetzner 的核心需求是：
1. 对客户隐藏内部 storage class，始终展示标准 storage class
2. 作为服务商能够设置"管理员级别"的 lifecycle policy，优先级高于客户自定义策略，且客户不可见

**Casey 的回应**：
- 全局 lifecycle policy 的主要挑战是扩展性——当前 lifecycle 处理只遍历有策略的 bucket，全局策略需要遍历所有 bucket。
- Storage class 是S3 的用户可控特性，建议区分"用户可见 storage class"与"内部 storage class"，可能需要设计一个新的独立特性，而非在现有 storage class 上打补丁。
- Lua 脚本方案虽然灵活，但局限性明显，不应作为长期解决方案。
- 建议将此需求纳入后续用户调查，评估社区对 intelligent tiering 功能的需求程度。

**结论**：该功能对大型 S3 服务商有明确价值，值得设计一个完整的上游特性方案，而非依赖 Lua 脚本的临时方案。


## 议题三：BlueStore 崩溃 Bug 排查

来自 Hetzner 的 Savan 报告了 Samsung BM7 系列 NVMe 驱动器出现疑似 BlueStore 数据损坏的问题，多块驱动器进入 crash loop。

**排查结论**：
- 该问题与 BlueStore elastic shared blobs bug 相关
- 19.3.2（dot2）版本中 Proxmox 通过修改默认配置添加了 workaround，但并未包含完整修复
- 完整修复在 19.3.4（dot4）版本中才正式合入
- 重要提示：该 flag 修复仅对**新创建的 OSD** 生效，已有 OSD 需要重新部署才能受益

**行动项**：建议提交 tracker issue，注明版本信息及复现细节，以便社区跟进。


## 议题四：RGW Admin 删除 Bucket 内所有对象功能需求

### 背景

在 Ceph multisite 场景下，Hetzner 仅同步 metadata（用户、bucket 元数据），不同步 bucket 数据。当某集群空间不足时，需要将 bucket 数据从源集群迁移至目标集群，迁移完成后需要清空源集群上该 bucket 的数据，但不能删除 bucket 本身（否则会影响 multisite 元数据同步）。

### 现有问题

`radosgw-admin bucket rm` 命令会删除整个 bucket，在 multisite 场景下不可用。

### 需求

开发 `radosgw-admin bucket rm --objects-only`（或类似命令），支持删除 bucket 内所有对象而不删除 bucket 本身。Hetzner 的开发者 Sarahan 已开始相关代码工作，希望将其贡献至上游，避免长期维护私有补丁。


## 后续行动计划

| 负责人 | 行动项 |
|--------|--------|
| 与会者（Anscar） | 提交 tracker issue，说明 `mon_target_pg_per_osd` 文档需补充"适用于哪种 OSD"的说明，并 tag Anthony |
| Hetzner 团队 | 将 storage class 隔离补丁贡献至上游 |
| Hetzner 团队 | 推进 `radosgw-admin object rewrite` 存储类指定功能的上游合入 |
| Hetzner 团队（Sarahan） | 推进 bucket 内容删除命令的上游合入 |
| Savan | 提交 BlueStore elastic shared blobs crash相关 tracker issue |
| Casey | 评估 RGW 按 storage class 统计用量 PR 的进展 |
| 社区 | 在下次用户调查中加入 intelligent tiering / admin lifecycle policy 需求调研 |
