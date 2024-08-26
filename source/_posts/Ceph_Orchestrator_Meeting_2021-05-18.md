---
title: "Ceph Orchestrator Meeting 2021-05-18"
date: 2021-05-18
updated: 2021-05-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：本周的 orchestrator 会议

#### 参会人员：全体成员

#### 会议日期：[具体日期]

#### 会议内容总结：

1. **主要议题**：
   - 深入探讨 self-adm agent 的功能和必要性。
   - 讨论 cephadm 中的 reconciliation loop 的扩展性和性能问题。
   - 评估是否需要改进架构以支持更快的故障转移。

2. **讨论细节**：
   - **self-adm agent**：讨论了 self-adm agent 的潜在收益和架构影响。提出了是否需要实施该代理，以及如何实施的问题。
   - **reconciliation loop**：指出了当前 cephadm 中的 reconciliation loop 在扩展性上的限制，特别是在创建 SSH 连接和执行远程命令时的性能问题。
   - **架构改进**：讨论了如何改进架构以支持更快的故障转移，包括考虑使用 push 模型而不是 pull 模型，以及如何处理潜在的竞争条件和失败模式。

3. **决定事项**：
   - 确认改进 reconciliation loop 和引入 self-adm agent 的必要性。
   - 初步决定采用 push 模型，通过 agent 向 manager 推送信息，以提高性能和响应速度。
   - 需要进一步明确 agent 的责任和具体实施细节。

4. **后续行动计划**：
   - 分配任务给特定人员以细化 self-adm agent 的实施细节。
   - 开始设计和实现 agent 的 push 模型，确保其与现有系统的兼容性和安全性。
   - 考虑长期目标，减少对 SSH 的依赖，并探索如何简化 manager 的架构。

5. **其他讨论点**：
   - 讨论了如何处理升级路径和兼容性问题。
   - 探讨了 manager 模块的架构重构可能性，但认为这是一个长期目标。

#### 会议结束：
- 会议在接近预定时间结束，未有其他紧急议题需要讨论。
- 全体成员祝大家有一个愉快的周末。

---

本次会议重点在于优化 ceph 的 orchestration 功能，特别是通过引入新的 self-adm agent 来解决现有的性能瓶颈问题。会议强调了详细的实施计划和考虑潜在的架构影响的重要性。