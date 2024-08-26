---
title: "Ceph Performance Meeting 2022-07-14"
date: 2022-07-19
updated: 2022-07-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题

1. **Blue Store Zero Block Detection PR 性能问题**
   - **讨论内容**：会议讨论了关于Blue Store Zero Block Detection PR在Quincy版本中的性能问题。该功能在17.2.1版本中被默认关闭，导致性能相对于之前的版本有所下降。
   - **决定事项**：需要进一步分析和理解性能下降的原因。
   - **后续行动**：Laura将与DFG存储团队合作，深入研究17.2.0和17.2.1版本之间的性能差异，特别是Blue Store Zero Block Detection功能的启用和禁用对性能的影响。

2. **内存使用问题与PG Log中的Dupe Ops跟踪**
   - **讨论内容**：会议讨论了在PG Log中跟踪Dupe Ops时遇到的内存使用问题。当存在损坏的Dupe条目时，会导致停止修剪，从而允许Dupe条目积累。
   - **决定事项**：目前提出的解决方案是在OSD重启时，逐步修剪条目（每次10,000条），以恢复稳定状态。
   - **后续行动**：将继续进行测试和验证，确保该解决方案的有效性，并考虑在HDDs上进行验证。

3. **Snap Map性能影响**
   - **讨论内容**：Gabri讨论了Snap Map对性能的影响，特别是在Snapdragon和Clone Object Creation方面的性能问题。
   - **决定事项**：需要设计针对性的测试来验证Snap Map的性能影响。
   - **后续行动**：Gabri将与团队合作，设计并执行相关测试，以验证Snap Map的性能影响，并分析CPU使用率和写入放大问题。

4. **Smithy节点替换计划**
   - **讨论内容**：会议讨论了可能的资金支持用于替换Smithy节点，并提出了一个基于高能效的硬件配置方案。
   - **决定事项**：需要尽快确定硬件配置，并在短时间内提交报价。
   - **后续行动**：David Galloway将与团队合作，尽快确定硬件配置，并提交报价。

#### 后续行动计划

- Laura和DFG存储团队将继续研究Blue Store Zero Block Detection PR的性能问题，并寻找解决方案。
- 团队将继续测试和验证PG Log中Dupe Ops跟踪的内存使用问题解决方案。
- Gabri将与团队合作，设计并执行针对Snap Map性能影响的测试。
- David Galloway将与团队合作，尽快确定Smithy节点替换的硬件配置，并提交报价。

#### 其他事项

- 会议中还讨论了其他潜在的性能优化和硬件升级问题，但未形成具体决定或行动计划。

#### 结论

会议涵盖了多个关键议题，包括性能优化、内存管理、硬件升级等，并制定了相应的后续行动计划。团队将继续合作，确保各项议题得到有效解决。