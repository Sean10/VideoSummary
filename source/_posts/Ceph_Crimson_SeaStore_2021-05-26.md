---
title: "Ceph Crimson/SeaStore 2021-05-26"
date: 2021-05-26
updated: 2021-05-27
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
1. **代码链接问题**：
   - Kifu发现有三段代码如果注释掉，可以解决链接问题，但目前尚不清楚原因。Kifu正在调查这个问题，并承认是他引入了这个回归问题。
   - 这三段代码来自x out of change，Kifu已经通过电子邮件发送了回滚这些更改的提交。

2. **mclock移植**：
   - 讨论了将mclock移植到Ceph存储系统的不同组件中，特别是PG和OSD（crimson和systole）。
   - 目前的工作包括将mclock实现移植到OSD调度器，但存在一些争议和复杂性。
   - 讨论了mclock是否应该与线程模型解耦，以及如何处理内部使用的pthread锁。

3. **性能计数器与指标**：
   - 讨论了在crimson OSD中使用性能计数器（perf counter）和指标（metrics）的问题。
   - 决定在crimson中使用seastar metrics来暴露perf counter的状态，同时保持与经典OSD的兼容性。

4. **其他更新**：
   - 讨论了extent placement manager的工作进展，包括实现parallel for each函数。
   - 提到了ono tree的API已经合并，并测试了重启功能。
   - 讨论了tc malloc属性的复制问题，以及如何区分测试套件中的OSD变体。

#### 决定事项
1. **代码链接问题**：
   - 暂时注释掉导致链接问题的三段代码，Kifu将继续调查原因。

2. **mclock移植**：
   - 初步决定将mclock移植到crimson和systole中，但需要进一步讨论和调整以避免线程模型的依赖。

3. **性能计数器与指标**：
   - 在crimson中使用seastar metrics来暴露perf counter的状态，保持与经典OSD的兼容性。

#### 后续行动计划
1. **代码链接问题**：
   - Kifu将继续调查三段代码导致链接问题的原因，并寻找更长期的解决方案。

2. **mclock移植**：
   - 开始讨论和实施mclock的移植工作，特别是如何处理线程模型和pthread锁的问题。

3. **性能计数器与指标**：
   - 在crimson中实现seastar metrics的包装器，以便暴露perf counter的状态。

4. **其他更新**：
   - 继续推进extent placement manager和ono tree的工作，确保功能的稳定性和性能。

5. **tc malloc属性的复制**：
   - 讨论并实施区分测试套件中OSD变体的解决方案，确保测试的准确性和覆盖率。

### 会议总结
本次会议主要讨论了Ceph存储系统中的多个技术问题，包括代码链接问题、mclock移植、性能计数器与指标的使用等。通过详细的讨论和决策，确定了后续的行动计划，以确保系统的稳定性和性能优化。