---
title: "Ceph RGW Refactoring Meeting 2026-05-13"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次会议主要围绕 RGW cloud transition（云分层迁移）相关 PR 的技术细节展开讨论，重点涉及 null version 对象在 cloud restore（云恢复）场景下的 OLH epoch 处理问题，以及一位 Google Summer of Code 新成员的自我介绍。

## 主要议题

### Cloud Transition PR：null version 的OLH epoch 问题

提交者介绍了一个关于 cloud transition 的 PR，该 PR 允许在对象迁移到云端后，以 cloud tier stub 的形式保留对象的版本实例，而非原先的 delete marker 方式（此为可选的 operator opt-in 行为）。

**核心问题：**

当 null version 对象被迁移到 cloud tier 时，其 OLH epoch 被标记为 0。在执行 cloud restore 时，系统会以 epoch 0 写回该对象，导致该版本被错误地提升为 latest version，覆盖了原本应为最新版本的对象。这一行为在语义上不正确——restore 的是一个旧版本，不应改变当前 latest 的指向。

**提出的解决方案：**

提交者提出的临时 workaround 是：在 restore null version 时，将 OLH epoch 设置为 1 而非 0。理由如下：
- epoch 1 在历史上被保留用于"从 plain entries 转换而来"的场景，不会与常规版本上传冲突。
- OLH allocator 的 bootstrap 起始值为 2，因此使用 1 作为特殊标记相对安全。
- 此方案避免了直接修改 CLS 层代码，改动范围较小。

**讨论中的替代方案：**

与会者（疑似 Casey）提出另一种思路：在 restore null version 时完全跳过 `set_olh` 调用，避免触发 OLH 相关的 index 更新。

提交者解释了此方案的问题：若使用 cloud tier stub 而非 delete marker，写入对象时 stub 本身是 zero-byte 对象，若不更新 OLH，bucket index 中该实例的大小将显示为 0 字节，导致 listing 信息不准确。

进一步讨论中提到，bucket index 事务分为两个阶段：prepare（写入 head object）和 complete，以及独立的 `set_olh` / link OLH / replace OLH log等步骤。与会者建议可以在两个阶段之间插入逻辑，或通过增加参数来控制是否跳过 `set_olh`，但提交者担心此类改动影响范围超出 cloud tier，可能波及其他调用方，因此倾向于保持改动的局部性。

### null version 的其他 Bug 修复

该 PR 还包含另一个修复：当请求未携带 version ID 时，代码错误地拉取了 null version，而非按照 AWS 语义拉取 is-latest 对象。提交者确认这是一个独立的 bug，在引入 cloud tier stub 后被更明显地暴露出来，但本身与 cloud tier 无关。

### 版本状态变更引发的 race condition

提交者提到，当 bucket经历"unversioned → versioned → suspended"的状态变迁时，cloud restore 和 cloud transition 存在多种 race condition。当前 PR 修复了其中部分场景，后续还将有更多 PR 处理边缘情况。根本原因在于原始代码假设 bucket 的 mutable state 不会发生变化，这一假设在实际使用中并不成立。

### Restore 时间戳更新的潜在问题

另一位与会者（疑似 Yuval）提醒：此前曾讨论过在 restore 时更新对象时间戳，以便 sync 机制能够感知到该对象并将其视为新上传处理。他建议关注此行为是否与当前 versioning 问题存在交叉影响。

## 后续行动

- 提交者将继续完善该 PR，并等待 Samya 本周或下周进行 review。
- 后续将有独立 PR 处理 cloud delete synchronization 功能（规模较大）。
- 继续跟进 cloud transition/restore 在 bucket 状态变更场景下的 race condition 修复。

## 新成员介绍

会议末尾，Google Summer of Code 学生 **Gautam Shapiro** 进行了自我介绍。其项目目标为：
1. 改善 RGW 的 CLI 接口用户体验。
2. 实现文档的自动化生成。

导师为 **Yuval** 和 **Jack**，Gautam 表示将在下周三的例会上再次与大家交流。
