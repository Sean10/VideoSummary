---
categories:
- 视频总结
date: 2023-08-16
subtitle: RGW_Refactoring_Meeting_2023-08-16
tags:
- Ceph
- RGW
title: RGW Refactoring Meeting 2023-08-16
updated: 2023-08-17
---




### 会议纪要

#### 会议主题：
本次会议主要讨论了Ali关于标记性能计数器(labeled perf counters)和RGW（RADOS Gateway）集成的进展，以及Tobias在处理S3测试中粗选项请求的工作。

#### 主要讨论内容：
1. **Ali的工作进展**：
   - Ali提交了一个PR，包含性能计数器的初始草案，并对RGW的前端操作计数器进行了标记。
   - 计划进行更大规模的测试，并欢迎反馈。
   - PR中创建了多个性能计数器实例，针对不同的操作（如put, get, delete等）。

2. **性能计数器实例的合并**：
   - Casey建议将所有前端操作计数器合并到一个实例中，以便按桶名或用户名进行缓存。
   - Ali解释了当前设计的原因，主要是为了未来的灵活性和多站点计数器的集成。

3. **缓存和Prometheus集成**：
   - 讨论了缓存驱逐的工作原理和配置。
   - 确认了每个RGW节点需要一个单独的exporter，用于将计数器数据发送到Prometheus。

4. **下一步行动计划**：
   - Ali将继续测试并优化性能计数器的实现。
   - Mark和Ali将在Folio实验室的机器上进行大规模测试，以验证exporter和Prometheus的集成性能。

5. **其他议题**：
   - Tobias分享了关于处理粗选项请求的工作进展，并寻求反馈。
   - 讨论了S3测试的默认认证路径（V2 vs V4），并计划进一步验证和优化。

#### 决定事项：
- Ali将继续优化性能计数器的实现，并进行大规模测试。
- Tobias将寻找更合适的位置来放置认证验证逻辑。

#### 后续行动计划：
- Ali和Mark将进行大规模测试，以验证性能计数器和Prometheus的集成。
- Tobias将继续优化S3测试和认证逻辑的实现。