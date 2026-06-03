---
title: "Ceph Developer Summit Telemetry and Ceph MGR"
date: 2025-09-11
updated: 2025-09-12
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph 开发者峰会：遥测与 Ceph MGR

#### **会议基本信息**

- **会议主题**：Ceph 自管理（Self-Manager）与遥测（Telemetry）讨论
- **时间**：近期开发周期内
- **参会人员**：Anthony、Junior、Radic、Ital、Nan、Jer、Laura 等（部分成员未全程参与）



#### **讨论议题与关键细节**

##### 1. 遥测（Telemetry）功能改进

- **Bluestore 数据收集**：
  - Tentacle 版本中未实现对 Bluestore 默认分配器的数据收集，需后续与 Adam/Egore 确认需求并可能回迁至稳定分支。
  - 用户需重新启用以接收新增的遥测数据。
- **RGW 多站点（RGW Multisite）信息**：
  - 需 RGW 团队支持添加相关指标，当前无团队成员在场，需后续跟进。
- **Crimson OSD 性能计数器支持**：
  - Crimson 使用独立的 Seastar 性能计数器基础设施，与经典 OSD 不同，需进一步讨论如何兼容 Python 模块暴露。

##### 2. 自管理（Self-Manager）功能优化

- **TTL Cache 改进**：
  - 当前 TTL Cache 默认禁用，计划改为 Manager Cache，解决内存/CPU 消耗高及数据陈旧问题。
  - 已有草案 PR，目标纳入 Umbrella 版本。
- **Manager Stats 周期自动调节（Autotuning）**：
  - 根据 OSD 队列负载动态调整统计周期，避免单 MGR 实例过载。
- **模块加载优化（Module Loading Improvements）**：
  - Laura 的 PR 改进模块加载顺序，已接近完成，将合入 Tentacle 版本。
- **模块性能计数器（Perf Counters for Modules）**：
  - 新增指标包括 CPU、内存占用及命令平均耗时，帮助识别资源密集型模块。
  - 通过 C++ 层统计，需注意共享资源（如缓存）的归属问题。

##### 3. 集群内容遥测（Cluster Content Telemetry）

- **低优先级**：因实现复杂且可能显著影响性能，Umbrella 版本暂不包含。
- 未来可能设计独立进程爬取集群数据，供遥测调用。

##### 4. CRUSH 规则与设备类优化

- **问题背景**：默认 CRUSH 规则与设备专用规则重叠时，Autoscaler 无法准确计算 PG 目标值。
- **解决方案**：提供更明确的健康警告，研究自动分配管理器池至设备类规则的启发式方法。

##### 5. Manager 测试覆盖率提升

- **现状**：单元测试不足，尤其是 API 调用和模块实际场景测试。
- **计划**：由 Nan 牵头补充测试用例，重点覆盖内存泄漏、进程崩溃等常见问题。



#### **决议事项**

1. **Telemetry**：跟进 Bluestore 和 RGW Multisite 指标收集。
2. **Manager Cache**：合并 TTL Cache 改进 PR 至 Umbrella 版本。
3. **Autotuning & Perf Counters**：优先实现 Manager Stats 自动调节和模块性能计数器。
4. **CRUSH 规则**：优化用户体验（健康警告 + 文档），暂不自动迁移管理器池。
5. **测试**：全员协作补充 Manager 测试用例，提升稳定性验证。



#### **后续行动计划**

| 任务 | 负责人 | 时间线 |
||--|--|
| Bluestore 数据收集需求确认 | Anthony/Adam/Egore | Tentacle 版本后 |
| Manager Cache PR 审核与合并 | Ital/团队 | Umbrella 开发周期内 |
| Autotuning 逻辑实现 | Brad/Radic | 3 月前 |
| CRUSH 规则警告增强 | Jer | Umbrella 发布前 |
| 模块测试用例补充 | Nan/Stephen | 持续进行 |



#### **遗留问题与待跟进**

- Crimson OSD 性能计数器与 Python 模块的集成路径。
- 管理器池是否包含设备健康指标。
- 集群内容遥测的轻量级设计方案。

#### **下次会议**

RADOS 相关讨论（周四），可能涉及 Manager 交叉议题。