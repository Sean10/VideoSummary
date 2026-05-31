---
categories:
- 视频总结
date: 2019-04-25
subtitle: 2019-04-25_-_-_Ceph_Performance_meeting
tags:
- Ceph
- 分布式存储
- 性能优化
- RocksDB
title: "'2019-04-25 :: Ceph Performance meeting'"
updated: 2019-04-26
---




### 会议纪要

**会议时间**： 2019年4月25日

**参会人员**： Igor, Adam, Radek, Ma Jinping, Sam, Daehan, Abhishek, Nick等

**会议主题**： Ceph分布式存储项目进展及性能讨论

**关键细节与议题**：

* **Pull Requests (PRs) 讨论**：
    * 本周有许多PR被关闭，部分原因是旧的BOTS自动关闭了这些PR。
    * Igor的PR涉及RocksDB的预取和缓冲读取模式，正在调查直接IO模式。
    * Ma Jinping的PR进行了一些性能优化，但具体影响尚不明确。
    * Radek的PR引入了Crimson OSD的执行阶段，目前还在讨论中。
    * Sam的PR关于增强指令缓存局部性，目前还在讨论中。
    * Adam的PR关于优化Booster缓存和Roxy D块缓存，已合并。
    * Beige的PR关于UTF-8优化，已合并。
    * Jason的PR关于RBE和右回退哈希，目前还在讨论中。
    * Daehan的PR关于测试RocksDB分配器，希望将其转换为单元测试。
    * Sage希望保留Adam关于Blue Store分配器的测试工作。
* **其他讨论**：
    * Adam正在研究TeaDB，并发现其写放大率较低。
    * Nick询问了关于RocksDB的问题，希望将其集成到Ceph中。
    * Abhishek和Nick讨论了使用S3的App性能问题，发现PR276997会影响性能。
* **后续行动计划**：
    * 继续对现有的PR进行审查和合并。
    * 探索将TeaDB集成到Ceph中的可能性。
    * 优化S3相关的性能问题。

**总结**：

本周Ceph项目的进展顺利，多个PR已合并，但仍有一些PR需要进一步讨论和优化。团队成员将继续努力，确保Ceph项目的稳定性和性能。