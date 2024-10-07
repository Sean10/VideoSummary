---
title: "Ceph Crimson 2021-02-23"
date: 2021-02-26
updated: 2021-02-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **参会人员**: 包括Sherhan在内的团队成员。
- **时间**: 最近一周。
- **主要议题**: 讨论了客户端请求序列器（client request sequencer）的优化、单元测试的添加、3D课堂项目的构建问题、以及Ceph存储系统中的并发优化。

#### 讨论的主要议题
1. **客户端请求序列器优化**:
   - Sherhan和团队成员正在优化客户端请求序列器，并尝试添加单元测试。
   - 讨论了在不同构建环境下的性能差异，特别是发布构建（release build）和调试构建（debug build）的性能对比。

2. **3D课堂项目**:
   - 项目在调试构建中工作正常，但在发布构建中出现崩溃。
   - 讨论了硬件性能对构建的影响，特别是SSD和NVMe硬盘的读取速度问题。

3. **Ceph存储系统并发优化**:
   - 讨论了如何在Ceph存储系统中优化并发处理，特别是在crimson osd中的并发请求管道。
   - 强调了客户端请求在底层磁盘上的持久化顺序的重要性，以及如何在Ceph的不同存储实现中保证这一顺序。

#### 决定的事项
- **发布构建崩溃问题**:
   - 决定暂时不深入调试，因为代码仍在频繁变动中。
   - 建议通过添加更多的断言（asserts）或日志输出（logger dot error）来帮助定位问题。

- **并发优化**:
   - 确认了在Ceph存储系统中，客户端请求的持久化顺序必须与它们到达OSD的顺序一致。
   - 讨论了在alien store中如何保证这一顺序，建议通过哈希集合（hash the collection）到线程集合（set of threads）的方式来保证顺序。

#### 后续行动计划
- **发布构建崩溃问题**:
   - 继续监控和收集更多日志信息，以便更好地理解崩溃原因。
   - 在代码稳定后，重新考虑深入调试。

- **并发优化**:
   - 在alien store中实施保证客户端请求顺序的机制。
   - 探索Ceph中是否已有类似的并发处理工具或库，以便更高效地实现并发优化。

#### 其他讨论
- 讨论了硬件性能对软件构建的影响，特别是SSD和NVMe硬盘的读取速度问题。
- 确认了在Ceph存储系统中，多个PG（Placement Groups）的使用是为了实现并行处理，而不是在单个PG内实现并行。

#### 结论
会议强调了在Ceph存储系统中保证客户端请求顺序的重要性，并讨论了如何在不同构建环境和硬件条件下优化性能。后续行动计划包括继续监控和调试发布构建的崩溃问题，以及在alien store中实施并发优化措施。