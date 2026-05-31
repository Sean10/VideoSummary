---
title: Optimizing Scrub Performance- Balancing Scrub Speed Against Client I/O Demands - Ronen Friedman, IBM
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- 性能优化
- 分布式存储
- CephFS
categories: 
- "视频总结"
subtitle: Optimizing_Scrub_Performance_-_Balancing_Scrub_Speed_Against_Client_I_O_Demands_-_Ronen_Friedman_IBM
---

### 会议概述
IBM的Ronen Friedman在会议上详细介绍了Ceph分布式存储系统中scrub操作的性能优化与调度改进方案。Friedman作为scrub模块的主要开发者，分享了如何减少scrub对客户端IO（尤其是延迟）的影响，并探讨了如何平衡scrub速度与客户端I/O需求。

### 关键技术点

#### Scrub基础流程
- **资源预留**：通过`osd_max_scrubs`参数限制并发scrub数量，Squid版本引入了新的scrub队列设计。
- **监控工具**：使用`ceph pg dump`和`ceph tell osd dump scrub reservations`等工具查看PG状态和OSD的scrub预留情况。
- **性能计数器**：提供scrub启动/失败次数等详细指标。

#### 性能优化
- **Chunk处理**：每个chunk包含一定范围的对象，Squid版本增加了默认chunk大小，并在客户端写操作时中断scrub并减半chunk大小。
- **IO密集型阶段**：Deep scrub会读取所有数据和元数据，通过`osd_deep_scrub_stride`控制数据读取粒度。
- **调度优化**：使用mclock调度器精确控制scrub资源占用。

#### Tentacle版本改进
- **调度分离**：解耦shallow scrub和deep scrub的调度，各自维护独立的状态记录。
- **Deep Scrub调度**：新参数`osd_deep_scrub_interval_cv`控制调度时间分布，健康警告基于`desired_interval * deep_scrub_ratio`。
- **Shallow Scrub调度**：保持原有`interval`和`randomization_ratio`参数，不再自动转换为deep scrub。

### 行动计划
- **代码改进**：修复chunk大小下限问题，优化scrub过程中的不必要yield点，完善性能计数器。
- **参数调整建议**：考虑增加`osd_deep_scrub_stride`，使用mclock时应自定义scrub资源分配，谨慎设置`osd_scrub_sleep`。
- **监控建议**：关注`scrub_chunk_selected`和`scrub_locked_objects`计数器，检查日志中的"in progress"提示信息。

### 遗留问题
- Preempt逻辑是否需要调整。
- 进一步优化EC pools的scrub性能参数。
- 完善mclock与scrub的集成体验。

会议展示了Ceph在scrub性能优化方面的持续改进，特别是在Tentacle版本中引入的调度分离和更灵活的配置选项，将显著提升大规模生产环境的运维体验。