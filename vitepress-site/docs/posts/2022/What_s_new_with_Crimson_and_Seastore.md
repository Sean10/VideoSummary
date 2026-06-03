---
title: "What's new with Crimson and Seastore?"
date: 2022-11-10
updated: 2022-11-11
tags:
  - "Ceph"
  - "Crimson"
  - "分布式存储"
  - "可扩展性"
categories:
  - "视频总结"
outline: deep
---
Ceph项目中的Crimson和Seastore是两个重要的研发方向，旨在提升Ceph存储系统的性能和可伸缩性。以下是会议内容的改进总结：

### 会议纪要

#### 会议主题：Crimson项目介绍及近期开发工作

#### 主讲人：Sam

#### 会议内容总结：

1. **Crimson项目概述**：
   - Crimson项目旨在减少每I/O的CPU开销，特别是针对新兴存储技术如NVMe。
   - 项目重点在于优化CPU使用，提升每核心的IOPs，而非原始IOPs。

2. **Crimson架构设计**：
   - 通过预分配每个核心的单个线程和分区数据结构，避免核心切换，减少锁的使用。
   - 使用C-star用户空间调度库，利用异步I/O结果，减少回调的使用。

3. **C-store组件**：
   - C-store是针对Crimson的线程模型设计的对象存储实现，旨在避免CPU密集型元数据设计。
   - 利用Zone Namespace Storage（ZNS）减少写放大和尾延迟。

4. **近期开发工作**：
   - 稳定化Blue Store RBD RADOS测试，实现多核心数据结构分区和消息路由架构。
   - 快照支持：基本I/O路径组件已实现，修剪和恢复组件正在进行中。
   - 用户保护措施：添加实验性功能标志，防止用户意外创建Crimson OSDs。

5. **下一步计划**：
   - 扩展测试覆盖范围，实现scrub功能，提升正确性验证。
   - 多核心支持的进一步改进，包括多反应器支持和性能测试。
   - C-store的稳定性提升，包括多核心反应器支持和快照功能的实现。

6. **问答环节**：
   - 建议使用vstart命令和Crimson标志进行部署。
   - Crimson未来将支持EC（Erasure Coding），但具体时间取决于后续工作进展。

#### 后续行动计划：
- 继续推进Crimson和Seastore的开发，特别是在多核心支持和性能优化方面。
- 完善文档和测试，确保Crimson和Seastore能够安全地用于特定生产环境中。
- 定期发布性能测试数据，以便社区了解Crimson和Seastore的进展和性能表现。