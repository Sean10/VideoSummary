---
title: " 2019-06-27 :: Ceph Performance Meeting "
date: 2019-06-28
updated: 2019-06-28
tags:
- Ceph
- 分布式存储
- 性能优化
- 测试
- BlueStore
- RADOS
- OpenStack
categories:
- "视频总结"
subtitle: 2019-06-27_-_-_Ceph_Performance_Meeting
---

本次会议主要讨论了Ceph分布式存储项目的性能优化和测试进展。以下为会议的关键细节：

**关键细节**：

* **调试级别调整**： 讨论将trim和boost的调试级别提高到20以上，并决定将trim整块代码放入单独的调试模块中。
* **性能优化**：
    * 讨论禁用apptracker可能带来的20%到30%的性能提升。
    * 分析删除操作优化，发现OST在删除PG时花费大量时间，并讨论优化扫描、预取和预加载到缓存中的策略。
    * 讨论steno SD或SDHC卡的恢复最大活跃数，并决定增加并发回填以提升性能。
    * 讨论max backfills和max active之间的关系，并决定进行实验以确定是否需要增加max backfills。
    * 讨论优化BlueStore缓存，包括避免重复缓存和缓存旋转等。
* **性能测试**：
    * 讨论在硅谷进行性能测试，并计划设置持续性能基准测试。
    * 讨论Jenkins和GitHub的集成，以及使用GitHub API进行结果发布。
    * 讨论性能测试标签和回归检测，以及如何确定回归的阈值。
* **硬件测试**：
    * 讨论Intel提供的新Officalis集群，包括TLC和QLC驱动器的配置。
    * 讨论将节点迁移到Jenkins以进行性能回归测试。
    * 讨论将高效能节点用于PR测试。

**决定事项**：

* 将trim和boost的调试级别提高到20以上。
* 将trim整块代码放入单独的调试模块中。
* 禁用apptracker进行性能测试。
* 优化删除操作，包括扫描、预取和预加载。
* 增加并发回填以提升性能。
* 进行实验以确定是否需要增加max backfills。
* 优化BlueStore缓存，包括避免重复缓存和缓存旋转。
* 在硅谷进行性能测试，并设置持续性能基准测试。
* 使用Jenkins和GitHub进行集成，并发布测试结果。
* 使用GitHub API进行结果发布。
* 确定性能测试标签和回归检测的阈值。
* 使用Intel提供的新Officalis集群进行测试。
* 将节点迁移到Jenkins以进行性能回归测试。
* 将高效能节点用于PR测试。

**后续行动计划**：

* 进行trim和boost调试级别调整的测试。
* 进行禁用apptracker和优化删除操作的测试。
* 进行steno SD或SDHC卡的恢复最大活跃数和max backfills的实验。
* 优化BlueStore缓存。
* 设置持续性能基准测试。
* 完成 Jenkins 和 GitHub 的集成。
* 进行性能测试标签和回归检测的测试。
* 准备Intel提供的新Officalis集群。
* 将节点迁移到 Jenkins。
* 将高效能节点用于 PR 测试。

[改进后的中文总结内容结束]