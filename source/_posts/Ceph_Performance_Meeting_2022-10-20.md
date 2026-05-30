---
categories:
- 视频总结
date: 2022-10-20
subtitle: Ceph_Performance_Meeting_2022-10-20
tags:
- Ceph
- 分布式存储
- 性能优化
- 数据恢复
- RocksDB
title: Ceph Performance Meeting 2022-10-20
updated: 2022-10-21
---


本次Ceph性能会议主要讨论了以下议题：

1. **Pull Request (PR) 讨论**:
   - **PR1**: 来自Canonical的贡献者发现了一个与Unknown Cash相关的竞争条件，由Igor提交。这个修复看似简单，但可能存在潜在问题。
   - **PR2**: Adam提交了关于改进Deferred决策的PR，讨论了可能的改进方向，包括完全移除Deferred路径的可能性。

2. **性能问题**:
   - 讨论了使用Secure Mode时客户端性能显著下降的问题，可能与SEO优化有关。

3. **数据恢复**:
   - 讨论了一个新的数据恢复方法，使用RocksDB快照进行数据恢复，但存在数据不一致的风险。

4. **Deferred Writes优化**:
   - 讨论了完全移除Deferred Writes的可能性，以及如何优化写入过程。

5. **RocksDB的碎片化和Tombstones问题**:
   - 讨论了RocksDB在处理大量删除操作时的性能问题，并提出了可能的解决方案。

会议决定：
- 对PR1和PR2进行进一步的审查和测试。
- 详细分析Secure Mode的性能问题。
- 进一步讨论和测试数据恢复方法。
- 研究和实验Deferred Writes的优化方案。
- 开发和测试RocksDB的碎片化和Tombstones问题的解决方案。

后续行动计划：
- 对PR1和PR2进行代码审查和测试。
- 对Secure Mode的性能进行详细分析。
- 进一步讨论和测试数据恢复方法。
- 研究和实验Deferred Writes的优化方案。
- 开发和测试RocksDB的碎片化和Tombstones问题的解决方案。