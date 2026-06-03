---
title: "Ceph RGW Refactoring Meeting 2025-06-11"
date: 2025-06-11
updated: 2025-06-23
tags:
  - "Ceph"
  - "RGW"
  - "分布式存储"
  - "加密"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
### Ceph RGW 重构会议纪要 2025-06-11

**日期**：2025-06-11
**参会人员**：Cena、Marcus、Casey、Shelpa（未出席但涉及议题）等



#### 主要议题与讨论

1. **跨区域组复制（Cross-Zone Group Replication）设计规划**
   - Cena 已提交初步设计草案，但存在未解决的开放性问题，需团队共识后拆分任务并排期。
   - 决定通过 RGW Devel 频道异步讨论，并需编写详细设计文档（Design Doc）。

2. **加密对象复制（Copy Encrypted Objects）的PR选择**
   - Marcus 和 Cena 的 PR 对比分析，包括代码结构、测试覆盖等方面。
   - 决策：优先合并 Marcus PR（因已有下游验证），后续由 Cena 在其基础上优化代码结构。

3. **多站点复制（Multi-Site Replication）的未决问题**
   - 多部分对象复制后的加密一致性测试。
   - 需补充以下场景的自动化测试：跨集群复制、同集群多区域复制、多部分对象复制。

4. **Tentacle 发布计划**
   - 首个RC版本已启动测试，但部分关键功能未合并。
   - 决策：Marcus 将推进CI构建，Casey 协助补充多站点测试用例。



#### 行动计划与责任人

| 任务 | 责任人 | 时间节点 |
||--|-|
| 提交跨区域复制设计文档 | Cena & Shelpa | 下周 |
| 修复 Marcus PR 的CI构建问题 | Marcus | 本周 |
| 扩展多站点复制测试用例（集成Vault） | Casey & Cena | RC测试阶段 |
| 评审并合并 Somia的`restore object` PR | Casey | 本周 |
| 补充多部分对象复制的S3测试 | Cena | 本周 |



#### 遗留问题

- 多站点复制密钥管理。
- `copy object` 路径中是否需避免不必要的解压/压缩。

**下次会议重点**：Review CI测试结果与多站点复制测试进展。



会议全程英文进行，部分技术术语保留原词（如PR、SSE-S3、Vault等）以确保准确性。