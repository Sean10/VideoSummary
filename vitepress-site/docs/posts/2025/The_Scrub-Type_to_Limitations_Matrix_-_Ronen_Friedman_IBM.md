---
title: "The ‘Scrub-Type to Limitations’ Matrix - Ronen Friedman, IBM"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "分布式存储"
  - "性能"
categories:
  - "视频总结"
outline: deep
---
在这次Ceph技术会议的最后时段，Ronan Friedman，Ceph Scrub代码维护者，分享了关于Ceph Scrub配置选项及其限制的讨论。以下是对会议内容的总结和改进：

### 会议纪要：Ceph Scrub配置与限制讨论

**会议时间**：某次Ceph技术会议的最后时段

**主讲人**：Ronan Friedman，Ceph Scrub代码维护者，过去五年专注于该领域。

**会议主题**：Ceph Scrub的配置选项及其对不同类型Scrub的影响，特别是在Tentacle版本中的改进。



#### 主要讨论内容：

1. **Scrub类型及其优先级**：
   - Scrub类型分为六种，按优先级递增排列，包括：
     - 周期性Scrub（Periodic Scrub）
     - 操作员请求的Scrub（Operator Requested Scrub）
     - 修复后Scrub（After Repair Scrub）
     - 修复Scrub（Repair Scrub）
     - 大规模Scrub（Mass Scrub）
   - 操作员请求的Scrub优先级最高，几乎总是会被执行，除非PG状态不允许。

2. **Scrub的限制条件**：
   - **时间限制**：通过配置选项限制Scrub在特定时间段内执行。
   - **CPU负载限制**：当CPU负载过高时，Scrub会被延迟或暂停。
   - **副本资源预留**：每个OSD会统计参与的Scrub数量，达到OSD Max Scrubs时，新的Scrub请求会被排队。
   - **最大并发Scrub数**：每个OSD作为Primary时，不会启动超过OSD Max Concurrency的Scrub。

3. **Tentacle版本中的改进**：
   - **修复Scrub**：修复Scrub会忽略大多数限制条件，确保修复后的数据一致性检查。
   - **大规模Scrub**：主要用于新PG的首次Scrub，优先级较低，遵循大多数限制。
   - **内部过期机制的移除**：Tentacle版本中移除了内部过期机制，仅保留健康警告。

4. **Scrub调度机制的改进**：
   - 浅Scrub和深Scrub的调度机制被分离，避免了相互影响。
   - 操作员可以通过配置参数控制深Scrub的调度间隔和随机化因子。

5. **CPU负载限制的保留**：
   - CPU负载限制仍然保留，但可以通过设置高阈值来忽略该限制。
   - 在Crimson调度器中，CPU负载显示为100%，但实际Scrub对CPU的影响较小。

6. **未来改进方向**：
   - 主讲人呼吁社区反馈，特别是关于Scrub性能和调优的需求。
   - Yit团队正在计划在下一个Ceph版本中引入Scrub相关的性能计数器。



#### 决定事项：
- 继续保留CPU负载限制，但允许通过配置高阈值来忽略该限制。
- 移除内部过期机制，简化Scrub调度逻辑。
- 社区反馈将用于进一步优化Scrub性能和调度机制。

#### 后续行动计划：
- Yit团队将在下一个Ceph版本中引入Scrub性能计数器。
- 主讲人将继续收集社区反馈，特别是关于Scrub调优和性能改进的需求。



**会议总结**：本次会议详细讨论了Ceph Scrub的配置选项及其在Tentacle版本中的改进，特别是如何通过配置限制Scrub对集群性能的影响。会议还呼吁社区提供更多关于Scrub性能的反馈，以便进一步优化。