---
title: Ceph User + Dev Monthly - September 2025
date: 2025-09-17
updated: 2025-09-18
tags:
- Ceph
categories: 
- "视频总结"
subtitle: Ceph_User_+_Dev_Monthly_-_September_2025
---

本次Ceph用户和开发者月度会议主要讨论了Balancer模块的功能增强，特别是针对PG remapping问题的解决方案。以下是会议的主要内容：

## 会议基本信息
- **会议主题**：Balancer模块功能增强讨论（针对PG remapping问题）
- **主持人**：Laura
- **参会人员**：Laura, Dan Vanderster, Alexander, Frederick, Enrico等社区成员

## 主要讨论内容
- **当前问题背景**：讨论了两个非官方脚本：`upmap_remapper`（Python实现）和`pg_remapper`（Go实现），它们用于解决PG卡在`remapped`和`backfilling`状态的问题。
- **核心用例分析**：包括容量变更（添加/移除主机或机架、更改CRUSH规则或可调参数、排空主机）、恢复优先级问题和OSD map修剪问题。
- **现有解决方案比较**：比较了`upmap_remapper`、`pg_remapper`和`JJ balancer`的主要功能和额外功能。
- **提案讨论**：
  - **短期方案（Umbrella版本）**：添加新的`ceph pg remap undo`命令，提供官方支持，而不修改balancer模块的现有行为。
  - **长期方案**：修改balancer模块的行为，当misplaced比例超过阈值时自动执行部分remapping，并考虑工作时间窗口。
- **技术细节讨论**：包括`undo`命令功能和与balancer的交互。

## 决策事项
1. **优先实现方案**：首先实现`ceph pg remap undo`命令，保持与现有脚本相同的核心功能。
2. **后续开发计划**：添加基础命令及测试用例，增强balancer模块的智能行为，采用分阶段验证策略。
3. **测试场景**：包括大规模容量增减、CRUSH规则变更和OSD权重调整。

## 行动计划
1. **Laura**：深入研究现有脚本实现，评估添加新命令的技术方案，设计测试用例。
2. **社区成员**：提供具体的使用场景和命令行示例，创建关于CRUSH reweight dry run功能的feature tracker。
3. **跟踪机制**：通过现有feature ticket继续讨论，后续userdev会议跟进进展。

## 其他建议
- 考虑添加CRUSH操作预测功能（dry run）。
- 加强文档说明新命令的使用场景和注意事项。
- 在实现中考虑添加警告机制（当需要关闭balancer时）。

本次会议对Balancer模块的功能增强进行了深入讨论，并制定了详细的开发计划，旨在提高Ceph集群的稳定性和性能。