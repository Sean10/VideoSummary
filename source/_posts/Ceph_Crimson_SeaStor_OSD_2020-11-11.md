---
title: "Ceph Crimson/SeaStor OSD 2020-11-11"
date: 2020-11-24
updated: 2020-11-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **日期**: 不详
- **参与者**: 不详
- **主要议题**: 讨论了Ceph项目的多个方面，包括代码重构、性能优化、并发处理、文档更新等。

#### 讨论的主要议题
1. **代码重构与优化**
   - 重构对象上下文锁定（object context locking），使用GridLock，并提供了一个草稿PR供初步审查。
   - 对omap3的补丁进行了更新，并计划进一步优化。
   - 完成了对经典scrubbing的评论回复，并创建了一个squashed分支准备合并。
   - 对crimson的interruptable库进行了审查，并发布了审查意见。

2. **性能与并发处理**
   - 讨论了如何通过改进并发处理来提高性能，特别是在处理多个并发I/O请求时。
   - 引入了基于UUID的nonce来改进journal的段管理，以确保在重用段时的正确性。
   - 实施了journal中的校验和（checksum）以增强原子性，并优化了段滚动机制以减少校验和计算的开销。

3. **文档与计划**
   - 更新了关于多层设备系统的文档，重点关注原子保证和架构变化。
   - 讨论了事务管理器的计划，该管理器将支持持久内存和基于块的opt-in。

#### 决定的事项
- 确认了多个PR的合并计划，并对代码进行了初步审查。
- 确定了改进并发处理和性能优化的具体步骤。
- 确认了文档更新的计划，并指定了相关人员进行后续工作。

#### 后续行动计划
- 继续进行代码重构和优化工作，特别是关于并发处理和性能提升的部分。
- 完成并合并相关的PR，确保代码的质量和稳定性。
- 继续更新和完善文档，确保所有变更和优化都有详细的记录和说明。

#### 备注
- 会议中提到了多个技术细节和具体实现，如GridLock、UUID nonce、checksumming、transaction manager等，这些关键词体现了会议的专业性和技术深度。
- 会议参与者对各自负责的部分进行了详细的汇报和讨论，确保了项目的顺利进行和团队成员之间的有效沟通。

### 结束语
会议在确认了各项任务的进展和后续计划后结束，确保了项目的持续推进和团队成员之间的协作。感谢所有参与者的努力和贡献。