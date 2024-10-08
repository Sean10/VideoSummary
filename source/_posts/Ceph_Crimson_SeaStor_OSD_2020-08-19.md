---
title: "Ceph Crimson/SeaStor OSD 2020-08-19"
date: 2020-08-19
updated: 2020-08-19
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与讨论内容

1. **技术问题与解决方案**
   - **Ceph存储系统中的问题**：
     - 上周主要工作集中在技术基础的测试上，遇到了一些与后台字段恢复相关的问题，这些问题是由于缺少某些操作导致的。
     - 增加了对这些操作的支持，并发现对象不一定总是包含映射，这导致了一些运行时的错误。
     - 计划增强新添加操作的错误处理支持，以减少错误消息的意外性。

2. **EIO处理案例**
   - 正在研究在代码中的哪个位置应该进行EIO处理，特别是在CRC不匹配和对象存储返回EIO的情况下。
   - 传统上，这些处理在经典OSD中是通过rep_repair_primary函数完成的，而在Crimson中则需要在pg_backend中进行相应的处理。

3. **CRUSH算法的扩展**
   - 讨论了在FAST 2020会议上提出的一篇关于CRUSH算法扩展的论文，该论文解决了在非平凡集群扩展时数据迁移的问题。
   - 计划继续讨论该论文，并将其链接分享给团队成员以供进一步研究。

4. **代码实现与测试**
   - 完成了字符串键布局操作，并正在处理树节点实现。
   - 正在解决单元测试中发现的一个bug，并考虑如何改进基于PG日志的恢复。
   - 强调了测试的重要性，特别是对于Crimson的稳定性和功能验证。

5. **后续行动计划**
   - 需要对Crimson中的问题进行分类，并创建相应的bug报告。
   - 强调了在病理运行中发现问题时，应及时创建bug报告的重要性。
   - 计划继续优化代码，特别是错误处理和垃圾收集机制。

#### 决定事项

- 继续推进对Crimson的测试和错误修复工作。
- 对发现的问题进行分类，并创建详细的bug报告。
- 继续研究和讨论CRUSH算法的扩展，以及其在Ceph中的应用。

#### 后续行动计划

- 继续完善和增强Crimson的错误处理机制。
- 对Crimson中的问题进行分类，并创建详细的bug报告。
- 继续研究和讨论CRUSH算法的扩展，以及其在Ceph中的应用。
- 继续优化代码，特别是错误处理和垃圾收集机制。

#### 会议结束

- 会议结束时，团队成员被鼓励继续关注和参与Crimson的开发和测试工作，并保持沟通和协作。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。