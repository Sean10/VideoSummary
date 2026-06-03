---
title: "CDS Infernalis (Day 2.2) -- Ceph Performance"
date: 2015-03-06
updated: 2015-03-06
tags:
  - "Ceph"
categories:
  - "会议纪要"
outline: deep
---
### 会议纪要

**会议时间**： 2023年（具体日期未提及）

**会议主题**： Ceph性能分析框架标准化

**参会人员**： 
- 来自Intel的同事
- Mark Nelson
- 会议主持人及参与者

**会议内容**：

**一、Ceph性能基准测试工具（CBT）与COSBench集成**

1. **背景**： 
   - CBT工具目前主要用于Ceph的性能基准测试，但不支持对象存储基准测试。
   - COSBench作为补充工具被提出，用于对象存储基准测试。

2. **方案**：
   - 将COSBench集成到CBT中，使其支持对象存储基准测试。
   - 通过插件模型，将COSBench配置文件转换为CBT可识别的格式，并执行性能测试。
   - 将COSBench测试结果集成到CBT结果中。

3. **讨论**：
   - 如何在CBT中实现COSBench的部署和配置。
   - 如何确保COSBench和CBT之间的数据一致性。

**二、Ceph性能分析框架（Tracepoint）改进**

1. **背景**：
   - 现有的Ceph性能分析框架在追踪性能瓶颈方面存在困难。
   - 部分Tracepoint缺乏语义，导致分析过程复杂且耗时。

2. **方案**：
   - 使用LTTng和Block和Blockzip作为工具进行性能分析。
   - 引入语义化的Tracepoint，并使用统一的标识符跟踪单个I/O请求。
   - 实现一个通用的Tracepoint框架，包括最重要的Tracepoint和可视化工具。

3. **讨论**：
   - 如何解决服务器系统时间差的问题。
   - 如何在Zipkin中实现更清晰的性能分析结果。

**三、行动计划**

1. 将COSBench集成到CBT中，并实现插件模型。
2. 实现一个通用的Tracepoint框架，并引入语义化的Tracepoint。
3. 将Andrew的Tracepoint补丁合并到Ceph代码库中。
4. 优化Zipkin的Web界面，使其能够更清晰地展示性能分析结果。

**四、其他**

1. 会议中讨论了COSBench对RGW性能的影响，以及如何检测性能退化。
2. 讨论了在Tracepoint中添加不同级别的追踪功能。

**五、总结**

本次会议讨论了Ceph性能分析框架的标准化方案，包括CBT与COSBench的集成和Tracepoint框架的改进。会议达成了初步的共识，并制定了后续行动计划。