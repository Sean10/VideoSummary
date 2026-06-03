---
title: "Ceph RGW Refactoring Meeting 2025-08-27"
date: 2025-08-27
updated: 2025-09-08
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
### 会议主题

本次会议主要讨论了Ceph RGW的重构问题，包括Usage Log Trimming问题、RGW测试套件稳定性问题以及RGW主要版本稳定性策略。

### 1. Usage Log Trimming问题讨论

**问题描述**：当前Ceph RGW的Usage Log管理方式存在两种key格式，但实际操作中出现key格式混合存储的情况，导致trim操作无法正确清理过期logs，影响性能。

**解决方案提案**：提出两种解决方案：
- **方案1**：修改key格式，确保与time-based key严格分离。
- **方案2**：调整迭代逻辑，兼容混合key场景。

**讨论要点**：
- 方案1需通过config option控制过渡逻辑，未来可关闭以消除性能开销。
- 仅影响cls_rgw.cc，对用户透明。

**后续行动**：
- 提交PR供团队审核。
- 完善Release Notes，说明配置选项的调整步骤。

### 2. RGW测试套件稳定性问题

**主要问题**：
1. DBStore测试失败，需标记已知失败的测试用例。
2. Valgrind内存泄漏，影响`notifications`和`multisite`测试。
3. CLS测试超时，部分测试因非EC集群配置失败。

**后续计划**：
- 定期检查Toothology测试结果，更新Bug Tracker。
- 每周四召开Bug Scrub会议，协调问题修复优先级。

### 3. RGW主要版本稳定性策略

**核心讨论**：如何定义和确保上游main分支的稳定性？

**当前实践**：
- main分支为“不稳定”分支，允许合并新特性。
- 发布稳定分支后，仅接受bugfix。
- 依赖RGW测试套件和下游规模化测试。

**改进建议**：
1. 自动化规模化测试。
2. 性能基线比对。
3. 资源协调。

**后续行动**：
- 在CSE会议中讨论测试流程优化。
- 联系Mark Nelson征询性能测试意见。

### 其他事项

- Adam的Datalog PR，剩余两个PR将优先拆分提交。

### 行动计划总结

| 事项 | 负责人 | 时间节点 |
||--|-|
| 提交Usage Log Trimming PR | Matthew H | 本周内 |
| 标记DBStore测试失败用例 | Adam/Ali | 下周 |
| Valgrind问题定位 | 待分配 | 两周内 |
| 规模化测试方案讨论 | Casey/Yuri | 下次CSE会议 |

**备注**：保留关键词（如CRUSH, OSD, RADOS, Erasure Coding等）以符合技术上下文。