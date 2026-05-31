---
title: Ceph RGW Refactoring Meeting 2025-11-05
date: 2025-12-03
updated: 2025-12-04
tags:
- Ceph
- RGW
- 分布式存储
- OpenStack
categories: 
- "视频总结"
subtitle: Ceph_RGW_Refactoring_Meeting_2025-11-05
---

### Ceph RGW 重构会议纪要

**日期**：2025年11月5日  
**参会人员**：Phillip, Shelpa 等核心开发成员



### 1. 议题讨论与关键细节

#### (1) RGW Valgrind 问题修复
- **问题描述**：近期 RGW 测试中出现了大量 Valgrind 报错，原因是构建流程中遗漏了 `boost valgrind` 定义。
- **解决方案**：已经修复了这一问题，并将在 Slack 上同步测试结果，后续集中处理剩余问题。
- **行动计划**：
  - 合并修复补丁后建立干净的测试基线。
  - 团队协作修复剩余的 Valgrind 报错。

#### (2) Keystone 审计功能开发（Phillip）
- **需求背景**：客户需要审计 Keystone 对 RGW 的访问日志，目前缺乏数据收集能力。
- **实现方案**：
  - 将 Keystone 的 scope 数据转发到 Ops Log。
  - 提供三个开关选项，包括合规性相关的用户身份信息过滤。
- **讨论要点**：
  - 代码审查由常规 Reviewer 负责，但需要 OpenStack 专家（如 Keystone 相关开发者）确认设计合理性。
  - Phillip 已提交详细设计文档，团队认为当前实现逻辑清晰。
- **后续行动**：
  - 在 PR 中标记相关 OpenStack 专家进行评审。
  - Phillip 根据反馈调整代码。

#### (3) BI Log 重构与 FIFO 后端设计（Shelpa）
- **目标**：分离 BI Log（Bucket Index Log）与 Bucket Index 数据以提升扩展性。
- **关键变更**：
  - **CLS 层**：分离 BI Log 和 Bucket Index 的操作逻辑。
  - **后端选择**：基于 `bucket index log layout type` 动态路由，默认目标为 FIFO 后端。
  - **FIFO 设计**：
    - 单 FIFO 对象/桶（未分片，避免与 Bucket Index 分片耦合）。
    - 支持同步/异步接口（当前仅测试同步）。
    - 异步批处理功能预留（暂不启用）。
- **开放问题**：
  - **分片必要性**：Bucket Sync 依赖多分片并行处理，需评估是否引入默认分片。
  - **数据迁移**：从 OMAP 迁移到 FIFO 时需处理旧日志读取，计划采用 generation-based 方案。
- **后续计划**：
  - 完善设计文档与草案 PR。
  - 优先验证同步逻辑，后续逐步启用异步和批处理优化。



### 2. 决议事项
1. 合并 Valgrind 定义修复后推进问题闭环。
2. 代码通过常规评审后，由 OpenStack 专家确认 Keystone 集成部分。
3. 初步采用单 FIFO 设计，后续讨论分片策略。
4. 同步接口优先，稳定后逐步启用异步优化。



### 3. 后续行动计划
| 任务 | 负责人 | 时间节点 |
||--|-|
| RGW Valgrind 修复合并 | 发起人 | 近期 |
| Keystone 审计 PR 评审 | Phillip + OpenStack 专家 | 本周内 |
| BI Log 分片方案讨论 | Shelpa + Adam | 下阶段会议 |
| FIFO 异步接口测试 | Shelpa | 功能稳定后 |



**备注**：
- 关键词保留：RGW, BI Log, FIFO, CLS, OMAP, Keystone, Valgrind, async/sync.
- 下次会议将重点跟进 BI Log 分片设计与迁移逻辑。

**会议结束**：全体成员确认无其他议题后散会。