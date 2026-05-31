---
categories:
- 视频总结
date: 2022-01-17
subtitle: Ceph_Performance_Meeting_2022-01-13
tags:
- 性能
- 分布式存储
- 测试
title: Ceph Performance Meeting 2022-01-13
updated: 2022-01-18
---




本次会议主要讨论了Ceph分布式存储系统的性能优化和更新，以下为会议的主要内容：

### 主要议题与讨论内容

1. **PR更新与合并情况**
   - **RGW Zipper PR**: 修复了RGW在Age Bidding测试中的性能问题。
   - **TTL Cache Implementation PR**: 已合并，需进一步测试。
   - **Primary Balance PR**: 代码重构，简化了计算PG Up Maps的代码。
   - **Fine Grain Locking PR**: 合并后显示性能优势，但需更多测试验证。
   - **Age Binning PR**: 多年未解决的PR，合并后虽未显示显著性能提升，但提供了更细粒度的缓存控制和更好的缓存项年龄信息。

2. **其他PR更新**
   - **Onode Binning Shardstrimming PR**: 涉及Onode的Binning和Shardstrimming处理，以及Adam关于Onode引用计数器和固定的PR，均因过时被关闭。
   - **Auto Tuning of MDS Cache Memory PR**: 因长时间未更新被关闭，讨论中提到可能使用优先级缓存来解决RSS内存使用的问题。

3. **性能测试计划**
   - 讨论了即将到来的Quincy版本的性能测试计划，包括使用Mako进行大规模集群测试，涉及RBD、RGW、iSCSI、NBD等不同工作负载和设备。
   - 特别提到了恢复测试的改进，由Sridhar提交的新恢复测试方法，创建了两个独立的池和图像，以更好地模拟实际恢复过程。

### 决定事项

- 确认了Quincy版本的性能测试计划。
- 关闭了多个过时的PR。

### 后续行动计划

- 继续进行Quincy版本的性能测试，特别是关注恢复测试的新方法。
- 确保所有关键PR得到适当的审查和测试，以准备Quincy版本的发布。

### 参会人员

- 会议由主持人主持，参会人员包括开发团队成员和其他相关人员。

### 备注

- 会议中提到的具体PR编号和详细技术讨论未在此纪要中列出，具体内容可参考会议录音或相关代码仓库。