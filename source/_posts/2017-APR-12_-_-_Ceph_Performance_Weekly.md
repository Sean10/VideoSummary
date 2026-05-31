---
categories:
- 视频总结
date: 2017-05-16
subtitle: 2017-APR-12_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 分布式存储
- 性能优化
title: "'2017-APR-12 :: Ceph Performance Weekly'"
updated: 2017-05-17
---



本次Ceph性能会议于2023年X月X日举行，主要讨论了Ceph系统的性能优化和Pull Request的相关议题。以下是会议的主要内容：

**一、Ceph Pull Requests讨论**

1. **Igor的工作**：
   - 成功合并了修复小文件性能问题的pull request，提高了系统的鲁棒性。
   - 提交了参数调整和添加硬盘SSD变体的pull request，需要进一步审查。
   - 发现蓝存储在NVMe上的性能下降，需进一步分析。
   - 提交了将blob转换为blob的pull request，需单独测试。

2. **Brightest Law的工作**：
   - 合并了速度表优化和限流模型优化的pull request，用户现在在蓝存储中只有一个限流指标。
   - 下一个pull request将测试自动调整限流，基于目标延迟进行调整。

3. **其他pull requests**：
   - 一些pull requests正在审查中，包括文件顺序调整和回调合并等。

**二、蓝存储性能问题**

1. **蓝存储缓存测试失败**：
   - 需要重新运行测试，检查是否有问题。

2. **分离PVC线程**：
   - 将线程分为两部分可能有助于提高性能。

3. **蓝存储文件系统优化**：
   - 将蓝存储文件系统放置在硬盘中间可以减少臂运动，提高性能。

4. **文件系统检查内存使用**：
   - 需要进一步分析内存使用情况，确保没有未计数的内存使用。

**三、其他议题**

1. **墙钟分析**：
   - 讨论了墙钟分析工具的选择，包括gdb、py-cpu-profiler等。

2. **libunwind问题**：
   - 讨论了libunwind在信号处理中的问题。

**四、行动计划**

1. **Igor**：
   - 审查和合并参数调整和硬盘SSD变体的pull request。
   - 分析蓝存储在NVMe上的性能下降问题。

2. **Brightest Law**：
   - 测试自动调整限流的pull request。

3. **Mark**：
   - 重新运行蓝存储缓存测试，检查是否有问题。

4. **Nick**：
   - 分析文件系统检查内存使用情况。

5. **所有人员**：
   - 关注墙钟分析工具的选择和libunwind问题。

本次会议重点关注了Ceph系统中蓝存储的性能优化，以及相关Pull Request的审查和合并。会议还讨论了墙钟分析工具和libunwind问题，并制定了相应的行动计划。