---
categories:
- 视频总结
date: 2018-05-17
subtitle: 2018-May-17_-_Ceph_Performance_Weekly
tags:
- Ceph
- 性能
- BlueStore
- RocksDB
title: "'2018-May-17 :: Ceph Performance Weekly'"
updated: 2018-05-18
---



### 会议纪要

#### 会议时间：
（此处应填写会议具体时间）

#### 参会人员：
（此处应填写参会人员名单）

#### 会议主题：
本周 Pull Requests 汇报及优先级缓存设计讨论

#### 会议内容：

**1. 本周 Pull Requests 汇报**

*   **新提交的 Pull Requests**：
    *   提交了关于 Blue Store 优先级缓存的 Pull Requests，旨在简化用户设置内存使用比例的过程，并允许自动调优。
*   **已合并的 Pull Requests**：
    *   Igor 的 alligator pruning 修复 Pull Requests。
    *   Async messenger Pull Requests，改进了锁定行为。
    *   Overwrite apps 恢复优化 Pull Requests，未合并，作者已关闭。
    *   Igor 的新位图分配器 Pull Requests，Sage 已审查，希望替换旧代码。
    *   lib RBD throttle Pull Requests，更新情况不明。
    *   Radice Slavs 的 crypto SSL Pull Requests，正在测试和修复中。
*   **未合并的 Pull Requests**：
    *   Peter 的 disc right coalescing Pull Requests。
    *   Adam 的哈希相关 Pull Requests，Sage 的版本正在工作。
    *   Peter 的减少 buffer list 重构的 Pull Requests。
    *   Redick 的 huge pages Pull Requests。
    *   Adam 的更多 Pull Requests。
*   **其他**：
    *   讨论了 AES 和加密相关的 Pull Requests。

**2. 优先级缓存设计讨论**

*   **问题**：
    *   用户难以调整缓存设置，且设置比例难以确定。
    *   当 Blue Store 和 RocksDB 的缓存冲突时，性能会下降。
    *   RocksDB 默认会扩展块缓存，可能会超过用户指定的比例，导致索引和过滤器被清除。
*   **解决方案**：
    *   提交的 Pull Requests 旨在简化用户设置内存使用比例的过程，并允许自动调优。
    *   通过优先级方案，可以根据工作负载调整缓存分配。
    *   未来工作包括：
        *   使用基于时间的优先级缓存，根据工作负载动态调整缓存分配。
        *   在 OSD 级别进行缓存管理，考虑更多内存使用情况。
        *   为不同的列族创建多个缓存，或为不同的前缀设置不同的优先级。

#### 决定事项：

*   继续推进优先级缓存设计，并解决相关问题和改进。
*   关注 RocksDB 的行为，并寻找解决方案以避免索引和过滤器被清除。
*   继续进行测试，并评估性能改进。

#### 后续行动计划：

*   与 Sage 商量，确认参会情况。
*   继续开发优先级缓存功能。
*   修复 RocksDB 相关问题。
*   进行更多测试和评估。

#### 会议总结：

本次会议讨论了本周 Pull Requests 和优先级缓存设计，并确定了后续行动计划。会议内容丰富，讨论深入，对 Ceph 的性能优化具有重要意义。