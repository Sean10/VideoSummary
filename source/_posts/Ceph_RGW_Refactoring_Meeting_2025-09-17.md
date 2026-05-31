---
title: Ceph RGW Refactoring Meeting 2025-09-17
date: 2025-09-18
updated: 2025-09-19
tags:
- Ceph
- RGW
categories: 
- "视频总结"
subtitle: Ceph_RGW_Refactoring_Meeting_2025-09-17
---

### 会议纪要 - Ceph RGW 重构会议 2025-09-17

本次会议主要讨论了以下几个关键议题：

1. **KMIP 后端支持 SSE-S3 的设计讨论**：
   - 设计目标：参考 Vault Transit 后端模式，实现 KMIP 后端对 SSE-S3 的支持，采用 KEK 和 DEK 分离模型。
   - 代码贡献策略：优先在 Ceph 的 `libkmip` fork 中开发，并推动上游合并。
   - 测试计划：转向 Go 实现的 KMIP 服务测试，替代 `pykmip`，并恢复 CI 测试覆盖。

2. **RGW 生命周期处理问题分析及解决方案**：
   - 问题现象：Bucket 处理被错误跳过，因 `already_run_today` 逻辑缺陷。
   - 根因分析：Shard 锁复用问题和 `is_expired` 检查误用。
   - 解决方案：优化时间判断逻辑，处理锁竞争，分离 shard 锁与 bucket 状态更新锁。

3. **DBStore 后端未来规划**：
   - 现状：新测试用例普遍不支持 DBStore，开发重心转向 POSIX 后端。
   - 共识：DBStore 已达成概念验证目标，若无特殊需求可逐步弃用。

### 其他事项

- **KMIP 性能优化**：计划引入 Per-Bucket Key 减少密钥操作开销。
- **测试改进**：增强生命周期处理的并发测试覆盖。

### 下一步行动计划

| 任务                          | 负责人       | 时间节点   |
|-|-||
| 提交 KMIP Encrypt/Decrypt PR  | 提案人       | 两周内     |
| 修复 LC `is_expired` 逻辑     | Kunal       | 本周       |
| 优化 `already_run_today` 逻辑 | Casey       | 下周       |
| 评估 Go KMIP 测试方案         | 全体相关成员 | 持续跟进  |

本次会议针对 RGW 的重构进行了深入讨论，明确了后续的开发方向和行动计划。