---
title: Ceph RGW Refactoring Meeting 2026-01-14
date: 2026-01-25
updated: 2026-01-26
tags: 
- RGW
- OSD
- RADOS
- 性能优化
- 存储优化
categories: 
- 视频总结
subtitle: Ceph_RGW_Refactoring_Meeting_2026-01-14
---

## 会议概述

本次会议由 Gaby 和 Nuval 主导，核心议题是 RGW 中 bucket ID 和对象前缀（prefix）字符串过长的问题，以及如何通过缩短这些标识符来降低存储开销和提升系统效率。

## 主要议题

### 问题背景：bucket ID 和prefix 过长

当前 RGW 中，bucket ID 由完整的 zone UUID（约 40+ 字节）加上递增计数器组成，prefix 则是 34 字节的随机生成数据。这些长字符串存在于系统中的每一个 RADOS 对象名称里，包括：

- head object名称
- tail object 名称
- manifest 中的 prefix 字段
- bucket index shard 的 RADOS 对象名称
- tail tag / ref tag

由于对象名称存储在 OSD 的 OMAP 中，对于小对象（如 16KB 对象），对名称本身往占据 object node 元数据的最大比例，造成不必要的空间浪费。在大规模部署场景下，这一问题尤为显著。

### 方案讨论：缩短 bucket ID

**核心思路**：用更短的 zone 标识替换 bucket ID 中冗长的 zone UUID。

**方案一：CLS 递增计数器**

通过 CLS（Class Library）维护一个全局递增计数器，每次创建 bucket 时调用 CLS 获取下一个编号作为 bucket ID。优点是保证唯一性，缺点是每次 bucket 创建需要额外的 round trip。

**方案二：使用已有的 zone short ID**

RGW 中已存在 zone short ID 的概念，是一个 32-bit 整数，通过对 zone UUID 取hash 生成，并在 period map 中检查碰撞。转换为 hex string 后仅需 8 字节，相比当前 40+ 字节的 UUID 大幅缩短。

与会者基本认同这是最简单可行的方案，因为：
- 代码已实现，只是未用于 bucket instance ID命名
- zone short ID 存储在 period config 中，可同步到所有 zone
- 实际部署中 zone 数量极少（AWS 全球约 50 个），碰撞概率极低

**遗留问题**：若某个 zone 被删除后重建，新 zone 可能生成相同的 short ID 而无法被检测到。建议参考 ref tag 的做法，维护一份已退役 zone 的列表，以便检测历史碰撞。

**方案三：全局递增 zone 编号**

在 zone 创建时由 master zone 分配一个递增的 32-bit 编号，彻底避免碰撞。但与会者指出 zone 在不同集群中创建，难以维护单一 RADOS 对象来追踪编号，且现有 zone short ID 方案已足够满足需求，不值得引入新机制。

### 方案讨论：缩短 prefix

prefix 的唯一性要求仅限于同一 bucket 内（因为 RADOS 对象名称已包含 bucket ID 作为前缀保证全局唯一性）。

**CLS 范围分配方案**：

- 每次调用 CLS 不获取单个计数器，而是获取一段连续范围（如 64K 个值）
- RGW 实例在本地消耗这段范围，无需频繁请求
- 范围耗尽前异步预取下一段，实现近乎零延迟的分配
- 即使实例崩溃，丢失的范围在 64-bit 空间中微不足道

**随机字符串方案的局限性**：

讨论了直接缩短随机 prefix 的可行性。根据生日悖论，若 bucket中存在数十亿甚至万亿级别的对象，需要约 80-128 bit 的随机空间才能将碰撞概率控制在可接受范围（如 2^-64），对应 16-32 字节，与现有 34 字节相差不大，节省空间有限。

**结论**：prefix 优化的收益相对较小，且实现复杂度更高。会议决定**优先推进 bucket ID 的缩短**，待该方案验证可行后再评估是否处理 prefix。

### tail tag 的影响

一旦 bucket ID 缩短，tail tag 中包含的 bucket ID 部分也会自动变短，无需额外修改。

### bucket index 的影响

bucket index shard 的 RADOS 对象名称中包含 bucket marker，同样会受益于 bucket ID 的缩短。manifest 中也存储了 marker、prefix 和 bucket ID，理论上 marker 可以不含 bucket ID 而在运行时动态生成，但目前实现中是包含的。

## 决定事项

1. **优先缩短 bucket ID**：使用 zone short ID（32-bit）替换 bucket ID 中的完整 zone UUID，这是最低成本、最高收益的改动。
2. **提交 PR验证可行性**：将方案落地为具体代码，通过 PR 评审来确认实现复杂度和正确性，而非停留在理论讨论层面。
3. **暂缓 prefix 优化**：待bucket ID 方案成功落地后，再评估 prefix 缩短的必要性。
4. **审计 zone short ID 的碰撞处理**：检查 period map 中已移除的 zone 是否持久化保留，以便检测重建 zone 时的 short ID 碰撞。

## 后续行动计划

- **Gaby / Nuval**：起草 bucket ID 缩短方案的 PR，验证使用 zone short ID 替换 UUID 的实现复杂度
- **相关开发者**：审计 `RGWPeriodMap` 中 zone short ID 的碰撞检测逻辑，确认已退役 zone 的处理方式
- **后续评估**：根据 bucket ID PR 的进展，决定是否启动 prefix 缩短的工作
