---
categories:
- 视频总结
date: 2017-01-11
subtitle: 2016-SEP-28_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 分布式存储
- 性能优化
- BlueStore
- RocksDB
- OSD
- MDS
- PG
title: "'2016-SEP-28 :: Ceph Performance Weekly'"
updated: 2017-01-12
---




### 会议纪要

**会议时间**：  [未提供具体时间]

**参会人员**：  [未提供具体人员姓名]

**会议主题**：  Ceph分布式存储项目进展、内存管理讨论、性能优化议题

**会议内容**：

**一、Ceph项目进展**

*   **代码提交与Pull Requests**：
    *   本周提交了大量Pull Requests，包括bug修复、性能提升等。
    *   重点关注优化重叠blob垃圾收集、Sages ER减少更新量、RocksDB迭代器改进、BlueStore性能提升等。
*   **测试与回归**：
    *   发现最近Pull Request中存在aged random reads或aged system随机读写性能下降问题，需要进一步调查和修复。

**二、内存管理讨论**

*   **Ice Age项目**：
    *   讨论了Ice Age项目的内存管理需求，包括内存预算分配和资源管理。
    *   提出使用Ceph可配置参数定义RocksDB内存使用量，并根据总缓存大小进行动态调整。
    *   重点关注OSD中PG日志和MDS的内存管理问题。
*   **内存分配器**：
    *   讨论了自定义内存分配器的必要性，以及如何进行内存统计和资源管理。
    *   提出使用现有内存分配器，并添加会计功能跟踪内存使用情况。

**三、性能优化**

*   **Fast Info**：
    *   Fast Info功能准备进行测试，预计将显著减少元数据负载。
*   **Aged Random Read Regression**：
    *   需要调查最近版本Pull Request中aged random read或aged system随机读写性能下降问题。
*   **异步消息传递**：
    *   讨论了异步消息传递的性能问题，并提出了可能的优化方案。

**四、后续行动计划**

*   继续讨论Ice Age项目的内存管理方案。
*   调查aged random read regression问题。
*   优化异步消息传递的性能。
*   继续进行性能测试和代码审查。

**五、其他事项**

*   讨论了添加会计功能优化内存管理。
*   讨论了使用原子操作和线程本地存储提高内存分配和释放的效率。