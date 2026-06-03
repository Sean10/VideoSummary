---
title: "2017-JUN-08 :: Ceph Performance Weekly"
date: 2017-06-21
updated: 2017-06-22
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "BlueStore"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议时间**： 2023年11月（具体日期未提及）

**会议主题**： Ceph分布式存储项目讨论

**参会人员**： Sage, Greg, Josh, James, Peter, Mohammad 等

**会议内容**：

* **CDM会议回顾**： 讨论了多个可用性操作问题，包括缓存、日志、扩展器重硬等。已合并的请求包括：scrub作业优先级调整、日志条目、扩展器重硬避免重叠、动态重硬、空批次事务提交、统计信息、unshare blob等。性能方面，luminous版本表现良好，parpc fast zero功能有潜力，但需进一步优化。
* **监控器日志**： 新增监控器命令，显示集群日志中最新的日志条目，并防止重复条目。
* **元数据缓存**： 讨论了元数据缓存配置，建议根据硬件配置进行调整，并考虑了Blue Store Cache和RocksDB Cache的配置。
* **PG日志**： 讨论了PG日志长度对性能和恢复时间的影响，建议将PG日志长度配置为内存占用量。
* **Blue Store和RocksDB缓存**： 调查了Blue Store和RocksDB缓存之间的交互，并考虑了压缩和未压缩缓存的影响。
* **白名单回退设置**： 讨论了白名单回退设置对性能的影响，并考虑了硬盘和SSD的设置。
* **其他**： 讨论了lmdb和buffer list的优化，以及使用SDVector替换SDList的可能性。

**行动计划**：

* Sage将测试不同缓存配置对性能的影响。
* Josh将调查从PG日志中借用内存给Blue Store的可能性。
* Peter将审查parpc fast zero功能。
* James将调查白名单回退设置对性能的影响。
* Mohammad将进行buffer list的基准测试。

**后续会议**：

* 将在下周进行后续会议，继续讨论以上议题。