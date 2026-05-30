---
categories:
- 视频总结
date: 2023-05-05
subtitle: Ceph_QoS_Refinements_for_Background_Operations_Using_MClock
tags:
- Ceph
- QoS Optimization
- MClock Algorithm
- Distributed Storage
- Ceph Storage
title: "Ceph QoS Refinements for Background Operations Using MClock"
updated: 2023-05-05
---




### 会议纪要

#### 会议主题：Ceph中M clock算法的QoS优化

#### 参会人员：Ceph研发团队成员

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 会议内容概述：
本次会议深入讨论了Ceph中使用M clock算法对后台操作进行QoS（服务质量）优化的方法。M clock算法是一种用于IO资源分配的算法，在Ceph的SEF模块中被使用。会议详细介绍了M clock的工作原理、与之前使用的WPQ（加权优先队列）的对比、以及M clock的优化和测试结果。

#### 主要议题：
1. **M clock算法介绍**：
   - M clock是一种用于IO资源分配的算法，主要用于Ceph中的SEF模块。
   - 通过三个参数（reservation、limit、weight）控制IO资源的分配。

2. **与WPQ的对比**：
   - WPQ是之前Ceph OSDs使用的调度器，每个操作都有一个优先级和成本。
   - WPQ缺乏资源分配能力、无法区分不同类型的操作，且需要大量配置选项来控制后台操作。

3. **M clock的优化**：
   - 调整了M clock的成本模型，使其更加动态，能够反映操作的实际IO大小。
   - 优化了M clock的内置配置文件，使其更加用户友好。

4. **测试结果**：
   - 在内部实验室环境中进行的测试显示，M clock在恢复操作和客户端操作方面表现优于WPQ。
   - 在恢复操作方面，M clock的性能提升显著，且客户端操作的延迟更低。

#### 决定事项：
- 继续优化M clock的成本模型和配置文件。
- 计划在更大规模的环境中进行测试，以验证M clock的性能。

#### 后续行动计划：
- 在更大规模的环境中测试M clock的性能。
- 继续优化M clock的配置文件，使其更加用户友好。
- 准备将M clock的相关优化合并到Ceph的下一次版本更新中。

#### 会议总结：
本次会议详细讨论了Ceph中M clock算法的QoS优化，通过与WPQ的对比，展示了M clock在性能和用户友好性方面的优势。团队将继续进行测试和优化，以确保M clock能够在实际生产环境中稳定高效地运行。