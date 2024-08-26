---
title: "2020-01-30 :: Ceph Performance Meeting"
date: 2020-03-31
updated: 2020-04-01
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **新PR介绍**: 会议开始时，提到了多个新的Pull Requests (PRs)，包括来自Casey和Braddock的优化buffer lists的PRs。
- **Igor的PR**: Igor提交了一个简化Onoda pin和unpin逻辑的PR，该PR解决了之前尝试修复时引入的复杂性和潜在的竞态条件问题。
- **Zone Commodity配置**: 讨论了允许zone commodity配置index charts的PR，该PR还包括增加bucket shards数量的简单更改。
- **PG autoscaler更新**: 一个增加默认PG数量到32的PR已经合并，旨在提高OSD对更多PG的响应性。
- **Bufferless和Buffer List优化**: Radek和Corel讨论了优化buffer list大小的旧努力，包括使用迭代器和减少内存占用。

#### 讨论的主要议题
- **性能优化**: 重点讨论了如何通过优化buffer lists和调整PG数量来提高性能。
- **简化逻辑**: 强调了简化代码逻辑的重要性，如Igor的PR所示。
- **CI和测试**: 讨论了CI系统的改进，包括增加对master分支的CI支持和对不同基准测试的性能比较。

#### 决定的事项
- **合并PR**: 多个PR被合并或准备合并，包括优化PG数量和bufferless使用的PR。
- **CI改进**: 决定继续改进CI系统，增加对更多基准测试的支持。

#### 后续行动计划
- **继续优化**: 继续关注和优化buffer lists和PG autoscaler。
- **CI系统升级**: 继续升级CI系统，确保所有测试环境的一致性和最新性。
- **性能测试**: 进行更多的性能测试，特别是在不同硬件和配置下的测试。

#### 其他讨论点
- **SSD性能问题**: 讨论了SSD性能问题，特别是关于队列大小和服务时间的优化。
- **环境升级**: 讨论了测试环境的升级，包括从CentOS 7升级到更高版本。

会议最后，主持人宣布将休息两周，期间可能不会有会议。整体上，会议聚焦于性能优化和CI系统的改进，同时讨论了具体的PR和未来的工作方向。