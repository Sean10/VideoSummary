---
title: "Ceph Performance Meeting 2021-03-11"
date: 2021-03-18
updated: 2021-03-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题
1. **OMAP性能基准测试**
   - 会议开始时，讨论了两个新的Pull Request (PR)。第一个PR是由会议主持人提出的，旨在为对象存储测试套件实现一个快速且简单的OMAP基准测试。该测试基于现有的简单OMAP测试，增加了写入多个对象和大量键的能力，并进行时间测试。
   - 第二个PR来自Gabby，目的是从RocksDB中移除分配。Josh和Igor已经进行了审查，并提出了一些改进建议。

2. **其他PR更新**
   - 讨论了其他几个PR，包括Shuhan提交的PR，该PR涉及将Alien存储线程分散到不同的CPU核心，以及Adam的PR，用于区分BlueFS中的Buffered和Direct IO。
   - 还讨论了Seth的PR，该PR涉及并发检索设备数据，目前仍在讨论和改进中。

3. **BlueStore性能问题**
   - 会议中详细讨论了BlueStore的性能问题，特别是在OMAP迭代和RocksDB代码路径方面。讨论了可能的性能瓶颈，如块缓存争用和RocksDB的迭代性能。
   - 提出了一些理论，如内存使用情况可能影响性能，特别是BlueStore和FileStore之间的差异。

4. **后续行动计划**
   - 会议主持人计划继续深入研究BlueStore的性能问题，特别是理解RocksDB代码和块缓存的使用情况。
   - 鼓励团队成员查看基准测试代码，并提供反馈和改进建议。

#### 决定事项
- 确认了继续深入研究BlueStore性能问题的必要性，特别是OMAP性能和RocksDB的使用。
- 确定了需要进一步讨论和改进的PR，包括Gabby和Shuhan的PR。

#### 后续行动
- 会议主持人将继续工作于OMAP性能基准测试，并分享进展。
- 团队成员被鼓励查看和评论相关的PR，以帮助改进和优化。

#### 其他讨论
- 讨论了FileStore和BlueStore在内存使用和性能方面的差异，以及可能的解释和解决方案。
- 提到了RocksDB的块缓存和迭代性能，以及可能的改进方向。

#### 结论
会议结束时，主持人感谢大家的参与，并提醒大家下周再见。会议强调了持续关注和改进Ceph存储系统的性能问题的重要性。