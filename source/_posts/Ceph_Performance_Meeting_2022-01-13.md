---
title: "Ceph Performance Meeting 2022-01-13"
date: 2022-01-17
updated: 2022-01-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题与讨论内容

1. **PR更新与合并情况**
   - **RGW Zipper PR**: 这是一个Bug修复PR，解决了在某些Age Bidding测试中RGW和Master运行非常慢的问题。原因是由于一个较旧的PR，虽然主要是外观上的改变，但影响了RGW中每个桶加载时的统计数据加载，导致性能下降。修复后，性能恢复到之前的水平。
   - **TTL Cache Implementation PR**: 该PR已合并，未见进一步讨论，主要需要通过一些测试。
   - **Primary Balance PR**: 由Josh Solomon提交，主要包含代码重构，简化了计算PG Up Maps的代码。原PR中的文档部分被移至另一个PR，将在Quincy分支后合并。
   - **Fine Grain Locking PR**: 由Adam提交，经过长时间讨论和测试后终于合并。初步测试显示有性能优势，但需要更多详细的Quincy测试来验证。
   - **Age Binning PR**: 这是一个多年未解决的PR，最终合并。虽然初步测试未显示显著性能提升，但在某些测试中显示了小幅改进，主要好处是提供了更细粒度的缓存控制和更好的缓存项年龄信息。

2. **其他PR更新**
   - **Onode Binning Shardstrimming PR**: 由Igor提交，涉及Onode的Binning和Shardstrimming处理，以及Adam关于Onode引用计数器和固定的PR，这两个PR因过时被关闭。
   - **Auto Tuning of MDS Cache Memory PR**: 基于RSS使用的自动调整MDS缓存内存的PR，因长时间未更新被关闭。讨论中提到可能使用优先级缓存来解决RSS内存使用的问题。

3. **性能测试计划**
   - 讨论了即将到来的Quincy版本的性能测试计划，包括使用Mako进行大规模集群测试，涉及RBD、RGW、iSCSI、NBD等不同工作负载和设备。
   - 特别提到了恢复测试的改进，由Sridhar提交的新恢复测试方法，创建了两个独立的池和图像，以更好地模拟实际恢复过程。

#### 决定事项

- 确认了Quincy版本的性能测试计划，包括使用Mako进行大规模集群测试，涉及多种工作负载和设备。
- 关闭了多个过时的PR，确保项目向前推进。

#### 后续行动计划

- 继续进行Quincy版本的性能测试，特别是关注恢复测试的新方法。
- 确保所有关键PR得到适当的审查和测试，以准备Quincy版本的发布。

#### 参会人员

- 会议由主持人主持，参会人员包括开发团队成员和其他相关人员。

#### 备注

- 会议中提到的具体PR编号和详细技术讨论未在此纪要中列出，具体内容可参考会议录音或相关代码仓库。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。