---
title: "Ceph Crimson/SeaStore 2021-09-29"
date: 2021-10-07
updated: 2021-10-08
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **修复pin crash问题**：上周推送了一个补丁，修复了至少一个pin crash问题，该问题已得到父级处理。
- **处理weight hard limits crash和segment cleaner问题**：即将推送一个PR，解决weight hard limits crash和segment cleaner问题。关键在于在执行out-of-line segment writes之前检查segment cleaner的full status，并允许多个out-of-line segment writes。
- **缓存LRU优化**：计划优化缓存LRU，以实现更有意义的recaching。
- **日志批处理优化**：正在研究日志批处理，已验证可以将写回列表放入队列并合并到更大的缓冲区列表中，然后调用正确的缓冲区。

#### 讨论的主要议题
- **日志批处理策略**：讨论了是否使用定时器或阈值来触发大缓冲区写入磁盘的问题。建议不使用定时器或阈值，而是在没有写入操作时立即写入缓冲区中的数据。
- **日志批处理实现细节**：讨论了如何处理日志批处理中的缓冲区交换和写入操作，以及如何避免在段滚动时写过段末尾的问题。

#### 决定的事项
- **日志批处理策略**：决定不使用定时器或阈值，而是在没有写入操作时立即写入缓冲区中的数据。
- **日志批处理实现**：决定在写入操作完成时，立即将缓冲区中的数据写入磁盘，并在段滚动时确保不写过段末尾。

#### 后续的行动计划
- **推送PR**：即将推送一个PR，解决weight hard limits crash和segment cleaner问题。
- **优化缓存LRU**：继续优化缓存LRU，以实现更有意义的recaching。
- **日志批处理优化**：继续研究日志批处理，确保实现细节符合讨论的策略。
- **实现集群日志**：正在实现集群日志功能，并准备提交一个draft PR。

#### 其他事项
- **代码审查**：承诺尽快完成对其他PR的审查。
- **多设备支持PR修改**：根据建议修改了多设备支持PR，并实现了PC和距离放置策略。

#### 会议结束
- 会议结束时，大家互相道别，祝愿对方有美好的一天或晚上。

### 关键词
- pin crash
- weight hard limits crash
- segment cleaner
- out-of-line segment writes
- cache LRU
- journal batching
- file store journal
- segment roll
- multi-device support PR
- PC and distance placement strategy
- cluster log

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。