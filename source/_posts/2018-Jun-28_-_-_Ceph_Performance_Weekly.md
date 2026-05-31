---
categories:
- 视频总结
date: 2018-06-28
subtitle: 2018-Jun-28_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 性能
- 分布式存储
title: "'2018-Jun-28 :: Ceph Performance Weekly'"
updated: 2018-06-29
---



在本次Ceph性能周会中，研发团队讨论了多个关键议题，包括内存分配器性能、线程行为优化、pull request评估等。

1. **内存分配器**：
    - 讨论了不同内存分配器的性能和碎片化问题，包括stupid allocator、bitmap allocator和libc malloc。
    - 测试结果表明，libc malloc在内存使用上表现不佳，而TC malloc和J malloc在性能和内存使用上更优。
    - 团队决定继续使用TC malloc或J malloc作为Ceph的默认内存分配器，并探讨了优化libc malloc的方法。

2. **KVS线程和finisher线程**：
    - 讨论了KVS线程和finisher线程的行为，以及Majin pang提出的改进方案。
    - Majin pang的改进方案在高并发情况下表现出良好的性能提升。
    - 团队决定进一步研究Majin pang的改进方案，并评估其在生产环境中的效果。

3. **其他议题**：
    - 讨论了静态链接、bitmap分配器碎片化、异步恢复、大页内存等pull request。
    - 讨论了make check性能优化和缓存利用率的提高。
    - 讨论了app tracker优化和分区优化。
    - 讨论了libc malloc的性能测试结果。

4. **决定事项**：
    - 继续使用TC malloc或J malloc作为Ceph的默认内存分配器。
    - 进一步研究Majin pang的KVS线程和finisher线程改进方案。
    - 优化make check性能，提高缓存利用率。
    - 集成p2t wrapper，优化app tracker。
    - 考虑使用libc malloc的优化方法。

5. **后续行动计划**：
    - Majin pang将提供更多关于KVS线程和finisher线程改进方案的信息。
    - 进行libc malloc的优化测试，并评估其效果。
    - 对其他讨论的pull request进行评估和合并。
    - 继续优化Ceph的性能和稳定性。