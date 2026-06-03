---
title: "Why is my SSD Pool so Slow? Decoupling min_size from Write Acknowledgment"
date: 2026-04-20
updated: 2026-04-21
tags:
  - "Ceph"
  - "OSD"
  - "性能优化"
  - "高可用性"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
## 演讲者背景

演讲者是一位来自圣安东尼奥的独立顾问，27岁，从事相关工作近十年。此前在当地一家大型托管服务提供商担任运维职位，主要工作方向之一是帮助企业从公有云迁移回自建基础设施，背景是近年来云计算成本持续攀升。他从2017年前后开始在家庭实验室中使用 Ceph，起因是 Proxmox 宣布集成 Ceph。目前主要支持 Windows VDI 场景，这也是他深入研究 Ceph performance tuning 的直接动力。

## 问题背景：SD 价格上涨与 TCO 压力

过去18个月，企业级 SSD 价格涨幅超过两倍，部分企业级 NVMe SSD 甚至接近三倍涨幅。相比之下，HDD 价格并未出现同等幅度的上涨。这一现实导致在预算会议中，即便应用对 NVMe 级别的低延迟有强烈需求，财务部门也往无法批准全 SD 方案。

这促使演讲者思考：**能否通过混合 CRUSH rule 降低 TCO，同时保持可接受的性能？**

## 混合池方案构想

演讲者提出了一种 hybrid pool 方案：

- 将数据的两份副本存放在 SD OSD 上
- 将第三份副本存放在 HDD（spinning disk）OSD 上
- pool 配置为 `size=3, min_size=2`

理论上，这样可以将存储成本降低约三分之一，同时在正常读写路径上利用 SSD 的低延迟。

## 核心问题：Write Acknowledgment 机制

演讲者深入分析了为何这一方案在 Squid 版本中性能急剧下降。

### 关键代码路径：`submit_transaction`

通过阅读 Ceph 源码（而非文档），可以发现：

- 客户端收到最终写确认（write acknowledgment）的条件是：**`waiting_for_commit` 集合完全清空**
- 该集合并不参考 pool 的`min_size` 配置，而是直接基于 **acting set** 中的所有 OSD
- 如果 acting set 中存在正在 backfill 的 PG，这些 backfill 目标 OSD 同样会被纳入等待集合

这意味着，即便 `min_size=2`，只要 acting set 中有一个 HDD OSD 正在参与，写延迟就会被拉低到 HDD 的水平。

### Squid 版本的重大变化

在 Squid 之前（Quincy、Reef 等版本），系统存在 `waiting_for_apply` 机制，允许利用 replica 侧的 page cache 提前返回确认，变相规避了等待 HDD 物理寻道的延迟。

**Squid 版本彻底移除了 `waiting_for_apply`**，replica 侧缓存不再接受未打标签的回复，page cache 的"作弊"路径被关闭。这使得混合池方案在 Squid 下几乎不可用。

### 全SSD 池同样受影响

即便放弃混合池，构建全 SSD 的 `size=3, min_size=2` pool，在 backfill 期间同样会遭遇性能问题：

- `waiting_for_commit` 包含 `get_acting_recovery_backfill` 返回的所有 shard
- backfill 目标 OSD 可能本身已处于高负载状态
- primary OSD 必须等待该 OSD 的确认，导致写延迟飙升至 backfill 目标的水平

## 为何不能简单解耦 Write Acknowledgment

演讲者指出，不能盲目解耦写确认机制，根本原因在于 **CAP 定理中的一致性（Consistency）保证**。当前架构确保了数据在集群中的强一致性，贸然解耦会引入数据安全风险。

## 潜在解决方向：Raft 协议中的 Non-Voting Learner

演讲者提出了一个借鉴 **Raft 共识算法**的思路：

- Raft 协议引入了 **non-voting learner** 角色
- 这类节点接收数据复制，但不参与 quorum 投票
- 如果将 HDD OSD 设计为 non-voting learner，则：
  - 写确认不需要等待 HDD OSD 的响应
  - 数据仍然会异步复制到 HDD，保证数据安全
  - 写延迟由 SD OSD 决定，不受 HDD 拖累

演讲者认为，这是目前能想到的、既能实现混合池低成本目标、又能保持数据安全性的唯一可行架构方向。

## 文档与源码的不一致问题

演讲者特别指出，当前 Ceph 文档中关于 `min_size` 的描述是针对 Reef 或 Quincy 等旧版本编写的，**尚未更新以反映 Squid 中写确认机制的实际行为**。源码与文档之间存在明显出入，这给运维人员和架构师带来了误导。

## 总结与后续行动

| 议题 | 结论 |
|------|------|
| 混合池在 Squid 下的性能 | 因 `waiting_for_apply` 被移除，性能不可接受 |
| 全 SSD 池 backfill 期间的写延迟 | 同样受 `waiting_for_commit` 机制影响 |
| 根本原因 | write acknowledgment 等待 acting set 全部 OSD，不受 `min_size` 约束 |
| 潜在解决方案 | 引入类 Raft non-voting learner 机制，将 HDD OSD 排除在 quorum 之外 |
| 文档问题 | 需更新 `min_size` 相关文档以反映 Squid 实际行为 |

演讲者希望社区能够将 non-voting learner 方向作为一个正式支持的 feature 进行探讨，从而在未来版本中合法、安全地实现混合池的低 TCO 目标。
