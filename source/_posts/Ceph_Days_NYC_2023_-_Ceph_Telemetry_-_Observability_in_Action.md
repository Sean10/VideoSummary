---
title: "Ceph Days NYC 2023: Ceph Telemetry - Observability in Action"
date: 2023-05-17
updated: 2023-05-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Ceph项目的Telemetry模块，包括其项目概述、动机、架构、成功案例以及如何部署自己的Telemetry服务。

#### 讨论的主要议题
1. **Telemetry模块的动机和目标**：
   - 了解Ceph集群的分布、版本、存储容量、驱动模型、崩溃情况和使用特性。
   - 通过收集匿名和非识别数据，帮助开发者和用户更好地理解和改进Ceph。

2. **Telemetry模块的架构和功能**：
   - Telemetry模块通过拦截器内置于Ceph，默认上报给上游Ceph。
   - 用户可以通过CLI命令或仪表板向导选择加入，并预览Telemetry报告。
   - 报告包括基本信息、崩溃信息、设备健康指标、识别信息和性能计数器等。

3. **隐私保护措施**：
   - 数据匿名化处理，不包含敏感或识别信息。
   - 通过分离报告端点增强隐私保护。

4. **成功案例和实际应用**：
   - 通过Telemetry数据，开发团队能够及时发现并修复新出现的bug。
   - 用户可以通过Telemetry数据验证自己的安装，并贡献驱动健康指标的开放数据集。

5. **部署自己的Telemetry服务**：
   - 需要设置Telemetry服务器和配置Telemetry模块。
   - 提供了详细的安装指南和配置选项。

#### 决定的事项
- Telemetry模块的隐私保护措施得到了强调和确认。
- 确定了Telemetry数据在开发和用户支持中的重要作用。
- 讨论了未来可能的改进方向，如离线Telemetry能力和更公开的驱动健康报告。

#### 后续行动计划
- 继续优化Telemetry模块的数据收集和报告机制。
- 探索和实施离线Telemetry能力。
- 研究并公开更多关于驱动健康和性能的统计数据。

#### 其他讨论点
- 讨论了如何区分和过滤硬件故障导致的崩溃。
- 探讨了设备健康指标的预测效率和改进方向。
- 讨论了性能通道的启用及其可能的性能开销。
- 讨论了集群报告的持续性和数据的有效性。
- 探讨了公开驱动模型可靠性和性能报告的可能性。

#### 结论
Telemetry模块是Ceph项目中一个重要的组成部分，它不仅帮助开发者更好地理解用户的使用情况，还为用户提供了验证和改进自己安装的工具。未来将继续优化和扩展Telemetry的功能，以更好地服务于Ceph社区。