---
title: "Ceph Performance Meeting 2022-10-20"
date: 2022-10-20
updated: 2022-10-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议主要讨论了Ceph项目的两个新的Pull Request（PR），以及一些关于性能优化和数据恢复的讨论。

#### 主要议题
1. **PR讨论**
   - **PR1**: 来自Canonical的贡献者发现了一个与Unknown Cash相关的竞态条件（race condition），由Igor提交。这个修复看似简单，但可能存在一些潜在的问题。已将Igor添加为审阅者。
   - **PR2**: Adam提交的关于改进Deferred决策的PR。会议中讨论了可能的改进方向，包括完全移除Deferred路径的可能性。

2. **性能问题**
   - 讨论了使用Secure Mode时客户端性能显著下降的问题，可能与Adam Emerson的SEO优化有关。这是一个需要进一步调查的假设。

3. **数据恢复**
   - 讨论了一个新的数据恢复方法，该方法涉及使用RocksDB的快照进行数据恢复。虽然这种方法可能有助于快速恢复，但也存在数据不一致的风险。需要进一步讨论和测试。

4. **Deferred Writes优化**
   - 讨论了完全移除Deferred Writes的可能性，并探讨了如何通过改进内核设备和块设备接口来优化写入过程。

5. **RocksDB的碎片化和Tombstones问题**
   - 讨论了RocksDB在处理大量删除操作时的性能问题，特别是与SST文件和Memtable中的Tombstones相关的问题。提出了一些可能的解决方案，包括改进RocksDB的设置和自定义删除跟踪。

#### 决定事项
- 需要对PR1和PR2进行进一步的审查和测试。
- 对于Secure Mode性能下降的问题，需要进行详细的性能分析。
- 数据恢复方法需要更多的讨论和测试，以确保其安全性和有效性。
- 对于Deferred Writes的优化，需要进一步的研究和实验。
- RocksDB的碎片化和Tombstones问题需要更多的诊断工具和可能的改进措施。

#### 后续行动计划
- 对PR1和PR2进行代码审查和测试。
- 对Secure Mode的性能进行详细分析。
- 进一步讨论和测试数据恢复方法。
- 研究和实验Deferred Writes的优化方案。
- 开发和测试RocksDB的碎片化和Tombstones问题的解决方案。

#### 会议结束
会议在讨论了所有议题后结束，感谢所有参与者的贡献，并祝愿大家有一个愉快的一周。