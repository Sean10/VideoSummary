---
title: "  2016-NOV-16 :: Ceph Performance Weekly  "
date: 2017-01-11
updated: 2017-01-12
tags:
- Ceph
- 分布式存储
- RocksDB
- 性能优化
- BlueStore
categories:
- "视频总结"
subtitle: 2016-NOV-16_-_-_Ceph_Performance_Weekly
---



### 会议纪要

**会议时间**： 2023年某月某日

**会议主题**： Ceph分布式存储项目进展及讨论

**参会人员**： （此处列出参会人员名单）

**会议内容**：

**一、本周进展**

1. **Polar请求**：
    - 优化搜索计算的请求，通过获取零缓冲区（0 1）来提升性能。
    - 40副本缓冲列表的请求正在审查中，期待进行微基准测试以验证效果。
    - 改进Booster Cache中元数据的使用，可能有助于提升性能。

2. **Blue Store改进**：
    - 将更多内容引入MemCaches，以更好地跟踪和提升用户体验。
    - 其他改进工作，包括回调功能、移除Crush Lock请求等。

3. **RocksDB相关**：
    - 使用RocksDB TVL families，已基本实现，但存在一些bug，如Cupid分配器问题。
    - 通过RocksDB TVL families进行压缩统计，发现约三分之一的压缩流量来自Omap，约三分之二来自元数据操作。
    - 在启用column families时，RocksDB TVL的性能表现较好，特别是随机小写操作。

**二、讨论议题**

1. **RocksDB TVL families的bug**：
    - Cupid分配器问题导致数据错误地进入B树。
    - Commit start断言错误，原因不明。
    - 需要进一步调查这两个问题是否相关。

2. **RocksDB TVL families的性能**：
    - 在启用column families时，RocksDB TVL的性能表现较好，特别是随机小写操作。
    - 需要进一步测试和优化。

**三、决定事项**

1. 继续调查RocksDB TVL families的bug，并修复相关问题。
2. 进一步测试和优化RocksDB TVL families的性能。

**四、后续行动计划**

1. Kiku和Matt将继续审查40副本缓冲列表的请求，并进行微基准测试。
2. 团队将继续关注RocksDB TVL families的bug，并修复相关问题。
3. 团队将进行更多测试，以验证RocksDB TVL families的性能，并进一步优化。

**五、其他事项**

1. 下周会议将讨论RCU（Read-Copy-Update）相关议题。
2. 如有其他议题需要讨论，请提前提交至会议议程。