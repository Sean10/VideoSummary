---
title: "Ceph Performance Meeting 2020-07-16"
date: 2020-07-16
updated: 2020-07-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期与时间**: 具体日期未提供，会议在早晨开始。
- **参会人员**: 会议参与者包括但不限于Josh、Matt、Igor、Radik等。

#### 讨论的主要议题
1. **PR合并情况**:
   - 讨论了多个PR的合并情况，包括性能测试、Jenkins失败原因、以及一些具体的技术实现细节。
   - 提到了PR在Octopus版本的回溯问题。

2. **性能优化**:
   - 讨论了MD的日志记录性能问题，特别是活跃的MDS配置下的日志记录代码开销。
   - 探讨了使用Denk编码框架的可能性及其潜在问题。

3. **RocksDB性能问题**:
   - Igor分享了RocksDB在大量删除操作后的性能问题，特别是在高负载下的表现。
   - 讨论了手动压缩作为临时解决方案的有效性，以及自动压缩的潜在需求。

#### 决定的事项
- 需要进一步研究和实验以确定Denk编码框架的可行性和性能提升。
- 对于RocksDB的性能问题，需要一个可靠的复现案例来进行深入分析和解决方案的开发。

#### 后续行动计划
- 继续研究和实验Denk编码框架，特别是Radik将探索使用循环缓冲区来优化内存分配。
- 寻找和建立RocksDB性能问题的可靠复现案例，以便进行针对性的优化。
- 考虑实施自动压缩机制，以减轻手动压缩的负担。

#### 其他备注
- 会议中提到了多个具体的PR和代码变更，这些细节对于后续的技术实现和问题解决具有重要参考价值。
- 强调了团队合作和持续改进的重要性，特别是在面对复杂的技术挑战时。

#### 结论
会议对当前的技术挑战进行了深入的讨论，并制定了具体的后续行动计划。团队将继续致力于性能优化和问题解决，以提升Ceph存储系统的稳定性和效率。