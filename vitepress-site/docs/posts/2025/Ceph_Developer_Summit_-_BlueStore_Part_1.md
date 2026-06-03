---
title: "Ceph Developer Summit - BlueStore Part 1"
date: 2025-09-12
updated: 2025-09-12
tags:
  - "Ceph"
  - "BlueStore"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph Bluestore 开发会议纪要

**会议主题**: Bluestore 在 Umbrella 版本中的规划与改进
**主持人**: （未提及姓名）
**参会人员**: Bluestore 扩展团队成员、Igor Fedotov（Bluestore 负责人）、Gary Danovich、Ja Prakesh Madaka 等



#### **会议背景**
本次会议主要讨论 Bluestore 在 Umbrella 版本中的技术规划，内容基于 Bluestore 团队的每周二例会（Bluestore Upkeep and Evolution Meeting）的讨论成果。目前多数改进已有初步 PR，但由于 Bluestore 对代码稳定性要求极高，从 PR 到最终合并通常耗时较长。



#### **主要议题与讨论**
##### **(1) RoxDB 缓存优化**
- **问题**: 现有缓存分片机制存在缺陷，导致超大缓存元素插入时引发持续缓存驱逐。
- **解决方案**: 已提交 PR 修复，计划向后兼容（backport）到旧版本。
- **重要性**: 关键修复，改善 OMAP 性能。

##### **(2) FIE Map 与零值支持**
- **需求**: 区分“未映射的零值”和“客户端显式写入的零值”，对 RBD 和纠删码至关重要。
- **挑战**: 纠删码需额外存储零值映射信息，当前处于研究阶段。

##### **(3) PowerPC 大页（64KB）支持**
- **问题**: Bluestore 默认假设系统页大小为 4KB，在 PowerPC 上引发直接 I/O 与缓冲 I/O 冲突。
- **潜在解决方案**: 改用 direct IO，并开发 Bluestore 专用缓存。

##### **(4) 快速 Onode 恢复（Fast Onode Recovery）**
- **问题**: 传统单线程恢复方式耗时过长，导致 OSD 被误判为下线。
- **改进**: 多线程恢复显著缩短时间。

##### **(5) Scrub 期间对象优化**
- **功能**: 在 Scrub 读取对象时，同步执行重压缩和碎片整理。
- **扩展讨论**: 未来可进一步优化对象元数据处理。

##### **(6) 分配映射持久化改进（Alloc Map Persistency）**
- **问题**: 现有分配映射存储方式在磁盘高度碎片化时效率极低。
- **改进**: PR 优化了碎片化场景下的恢复速度。

##### **(7) 性能分析工具（CPU Trace）**
- **用途**: 精确测量代码优化效果，支持小规模渐进式性能提升。

##### **(8) 内存优化（White Overhaul）**
- **目标**: 减少元数据内存占用，提高缓存利用率。
- **状态**: 尚未确定具体方案。



#### **后续行动计划**
1. **优先级任务**: 合并关键修复 PR，推进 Scrub 优化框架设计。
2. **研究性工作**: 研究 FIE Map 零值支持的跨模块兼容性，评估 PowerPC 大页支持的长期方案。
3. **工具与测试**: 推广 CPU Trace 工具，开展内存优化基准测试。



#### **开放讨论**
鼓励社区成员提出未被覆盖的改进方向，或参与每周二的 Bluestore Upkeep and Evolution Meeting。