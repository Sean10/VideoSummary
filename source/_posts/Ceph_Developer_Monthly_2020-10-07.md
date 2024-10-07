---
title: "Ceph Developer Monthly 2020-10-07"
date: 2020-10-10
updated: 2020-10-10
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：高效追踪与分布式存储系统优化

#### 关键细节：
1. **高效追踪（Tracing）的重要性**：
   - 追踪系统用于解决系统中未知的性能问题。
   - 传统的调试工具如GDB在处理高并发系统时效率低下，需要用户干预，影响系统性能。
   - 在线追踪（Online Tracing）允许系统在不等待用户输入的情况下继续运行，收集和保存变量变化，用户可以在事后分析数据。

2. **现有追踪系统的局限性**：
   - 简单的日志系统（如syslog）产生大量数据，可能导致系统过载。
   - 动态添加事件追踪点需要重新编译和构建，不灵活。
   - 基于字符串的操作开销大，追踪数据难以管理。

3. **高效追踪系统的设计要求**：
   - 简单易用，无锁操作，不影响正常执行。
   - 数据应高效收集并以二进制格式存储，同时保持人类可读性。
   - 支持在线事件收集过滤，允许用户根据事件类型、对象类型等进行过滤。

4. **实施细节**：
   - 使用全局变量简化事件添加过程。
   - 支持在线添加和移除过滤器，使用GUI界面进行管理。
   - 每个CPU核心独立处理事件日志，使用双缓冲技术减少同步需求。

5. **未来工作**：
   - 集成到现有工具如Wireshark，避免重复工作。
   - 考虑与现有追踪系统（如Jaeger）的兼容性和替代性。

#### 讨论的主要议题：
- 如何设计一个既高效又易于使用的追踪系统。
- 如何在不增加系统负担的情况下收集和分析追踪数据。
- 如何与现有工具和系统（如Jaeger）集成或替代。

#### 决定的事项：
- 开发一个原型来测试和验证高效追踪系统的概念。
- 考虑使用现有开源项目（如SPDK的ADM参考实现）作为基础，避免从零开始。

#### 后续行动计划：
- 开发和测试高效追踪系统的原型。
- 探索与现有追踪工具的集成或替代方案。
- 根据反馈和测试结果调整和优化系统设计。

#### 其他讨论点：
- 分布式NVMe命名空间（ADN）的概念和实现，旨在优化存储系统的连接性和性能。
- 如何将ADN集成到Ceph中，以及可能的技术挑战和解决方案。

通过这次会议，团队对高效追踪系统的需求和设计有了更清晰的认识，并制定了初步的实施计划。