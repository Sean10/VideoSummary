---
categories:
- 视频总结
date: 2024-10-03
subtitle: Ceph_Days_Asia_-_Ceph_with_Arrow_-_How_object_gateway_can_accelerate_querying_data
tags:
- Ceph
- 对象存储
- 分布式存储
title: "Ceph Days Asia- Ceph with Arrow- How object gateway can accelerate querying data"
updated: 2024-10-04
---


### 会议纪要

#### 会议概述
主讲人首先为迟到道歉，并介绍了自己所在的Kore gr团体，这是一个对技术有兴趣的团体，欢迎所有对存储技术或新商业有兴趣的人参与。

#### 主要议题
1. **Ceph简介**：
   - Ceph是一个开源分布式存储系统，支持对象存储、块存储和文件系统存储。
   - 讨论了Ceph在处理大数据集时的性能问题，特别是数据传输的效率和成本。

2. **数据查询优化**：
   - 介绍了通过改变数据处理顺序来优化查询的方法，特别是通过对象存储（如S3）来减少数据传输量。
   - 提到了AWS的S3 Select功能，它允许用户通过API直接在存储层进行数据过滤，从而减少数据传输和处理成本。

3. **Apache Arrow项目**：
   - Apache Arrow是一个内存分析开发平台，旨在提高分析算法的性能和数据传输效率。
   - Arrow通过列式存储优化数据处理，支持高效的计算和数据交换。

4. **Ceph与Apache Arrow的集成**：
   - 讨论了Ceph项目中对Apache Arrow的部分使用，特别是在S3 Select实现中。
   - 提出了未来改进的方向，包括可能的集成和优化。

#### 决定事项
- 确认了Ceph在处理大数据集时的性能挑战，并探讨了通过优化数据查询和使用Apache Arrow来提高效率的可能性。
- 讨论了Ceph与Apache Arrow的当前集成状态，并提出了未来进一步集成的建议。

#### 后续行动计划
- 继续研究和开发Ceph与Apache Arrow的更深层次集成。
- 探索使用其他技术（如GPU）来进一步优化数据处理。
- 关注AWS等云服务提供商的最新动态，以便及时调整和优化Ceph的功能和API。

#### 会议结束
主讲人总结了讨论内容，并邀请与会者提出问题或进一步讨论。