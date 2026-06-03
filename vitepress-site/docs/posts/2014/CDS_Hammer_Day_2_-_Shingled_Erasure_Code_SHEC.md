---
title: "CDS Hammer (Day 2) - Shingled Erasure Code (SHEC)"
date: 2014-10-30
updated: 2014-10-31
tags:
  - "Ceph"
  - "分布式存储"
  - "Erasure Coding"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议主题**： Shingled Erasure Code (Shake) 介绍及讨论

**与会人员**： 来自富士通的 Takeshi Miyamai 博士，以及其他 Ceph 开发者和测试人员

**会议内容**：

1. **Shake 介绍**：
   - Takeshi Miyamai 博士介绍了他们开发的名为 "Shangri-La" 的 Shingled Erasure Code (Shake)，这是一种高效的擦除码，能够在磁盘发生故障时快速恢复数据。
   - Shake 在 I/O Workshop 上展示了其初步成果，并寻求社区反馈以改进未来工作。
   - 与现有的擦除码（如 DSA）相比，Shake 在多种磁盘故障情况下展现出更高的恢复效率。
   - Shake 的设计允许用户根据需要调整恢复效率，以平衡存储空间和恢复效率。

2. **Shake 的特性**：
   - 采用类似于 Check 1065 的布局，包含 10 个数据块和 6 个校验块。
   - 校验块具有局部性，每个校验块只覆盖相邻的数据块。
   - 在恢复数据时，只需读取少量校验块，从而减少了读取操作的数量。

3. **Shake 的优势**：
   - 在处理多磁盘故障时，Shake 具有更高的恢复效率，只需读取少量校验块即可恢复数据。
   - Shake 具有更高的调整性，用户可以根据需要调整恢复效率。
   - 与现有的 Firefly 磁盘兼容。

4. **Shake 的未来工作**：
   - 扩展 Shake 的功能，使其能够支持更多的存储系统和错误检测机制。
   - 在 Ceph 中集成 Shake，并与其他擦除码进行比较和测试。

5. **后续行动计划**：
   - Takeshi Miyamai 博士将提供 Shake 的源代码，并与其他 Ceph 开发者合作，将其集成到 Ceph 中。
   - 开发者将编写文档和单元测试，以确保 Shake 的正确性和稳定性。
   - 社区成员将对 Shake 进行测试和反馈，以改进其功能。

**关键术语**：

- Shingled Erasure Code (Shake)
- 擦除码
- 恢复效率
- 数据块
- 校验块
- 局部性
- Firefly
- Ceph