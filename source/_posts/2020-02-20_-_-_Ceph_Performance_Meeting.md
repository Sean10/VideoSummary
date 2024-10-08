---
title: "2020-02-20 :: Ceph Performance Meeting"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间
- 日期：[具体日期]
- 时间：上午

#### 参会人员
- Josh
- Mike
- Igor
- 其他核心团队成员

#### 主要议题
1. **PRC（Pull Request Community）更新**
   - Igor提交了几个新的PR，包括使用延迟写入避免小块碎片化的优化，以及基于AVL和位图的混合分配器。
   - 讨论了其他PR的进展，包括SPD cape性能改进、nvme设备代码优化、upper list和nvme设备分割等。

2. **性能优化讨论**
   - Igor分享了关于使用AVL和位图混合分配器的性能数据，讨论了内存使用和性能优化的权衡。
   - 讨论了4k最小分配单元对性能的影响，特别是在读写操作中的表现。

3. **IO 500基准测试**
   - 讨论了在Ceph上运行IO 500基准测试的进展和挑战，包括性能瓶颈和MDS（Metadata Server）的负载均衡问题。
   - 提到了使用新的officinalis节点进行测试，以及尝试使用FUSE客户端时遇到的问题。

#### 决定事项
- 继续优化和测试Igor的PR，特别是混合分配器和延迟写入策略。
- 继续进行IO 500基准测试，重点关注MDS的负载均衡和客户端性能。

#### 后续行动计划
- Igor将继续优化混合分配器和延迟写入策略，并分享更多性能数据。
- 继续进行IO 500基准测试，尝试解决性能瓶颈和MDS负载均衡问题。
- 使用Patrick的脚本进行更深入的性能分析和调试。

#### 其他讨论
- 讨论了Ceph在生产环境中的内存使用问题，以及如何通过优化分配器来解决。
- 提到了Ceph在IO 500基准测试中的排名，目标是提高性能并进入前13名。

#### 会议结束
- 会议在感谢所有参会人员的参与后结束，并约定下周再次开会。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。