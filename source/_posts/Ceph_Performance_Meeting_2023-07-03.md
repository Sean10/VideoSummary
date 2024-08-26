---
title: "Ceph Performance Meeting 2023-07-03"
date: 2023-07-03
updated: 2023-07-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间
- 日期：具体未提供
- 参与者：Igor, Casey, Adam, Corey Snyder, Paul, 以及其他相关人员

#### 主要议题
1. **GCC 13 修复与 RocksDB 更新**
   - 讨论了关于 GCC 13 的修复问题，特别是针对 RocksDB 的 FTBFS（无法构建从源）问题。
   - 决定将修复合并到 Reef 分支，并确保未来更新 Main 分支时能同步这些更改。
   - 讨论了 RocksDB 的版本管理和更新策略，建议定期跟进 RocksDB 的主要版本更新。

2. **Snappy 库的问题与替代方案**
   - 讨论了 Snappy 库在新的操作系统发行版中导致的编译问题，特别是与 RTTI 支持的缺失有关。
   - 提出了几种解决方案，包括使用自定义的 Snappy 分支、禁用系统 Snappy 库等。
   - 讨论了 Snappy 的性能和替代方案，建议考虑弃用 Snappy，特别是在 RGW 中的使用。

3. **Elastic Shared Blobs PR 的讨论**
   - 讨论了关于 Elastic Shared Blobs 的 PR，特别是关于如何处理部分代码的 ifdefs 问题。
   - 决定暂不合并 PR，而是先进行必要的修改以适应新的运行时条件。

4. **RBD 性能测试结果分析**
   - 讨论了 RBD 在 Reef 和 Quincy 版本中的性能测试结果，特别是关于 CPU 使用率和 I/O 效率的问题。
   - 提出了一些假设和测试方向，包括调整内存目标大小、不同 I/O 大小的测试等。

#### 决定事项
- 确认了 RocksDB 的更新策略，建议定期跟进主要版本更新。
- 对于 Snappy 库的问题，决定先观察其他发行版的处理方式，再决定具体实施方案。
- Elastic Shared Blobs PR 将进行必要的修改后再考虑合并。

#### 后续行动计划
- 继续监控和分析 RBD 性能测试结果，特别是关于 RocksDB 和 I/O 效率的问题。
- 跟进 Snappy 库的问题，特别是与其他发行版的协调和处理方式。
- 修改并重新审查 Elastic Shared Blobs PR，确保其符合新的运行时条件后进行合并。

#### 其他讨论
- 讨论了 Debian 和 Fedora 对于 Snappy 库的处理方式，建议在主问题跟踪器中记录相关问题。
- 讨论了 RBD 性能测试中的具体细节和可能的优化方向。

#### 会议结束
- 会议在讨论完所有议题后结束，感谢所有参与者的贡献，并祝愿大家有一个愉快的一周。