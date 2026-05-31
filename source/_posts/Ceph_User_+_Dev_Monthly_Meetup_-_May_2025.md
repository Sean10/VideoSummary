---
title: Ceph User + Dev Monthly Meetup - May 2025
date: 2025-05-21
updated: 2025-05-22
tags:
- Ceph
- 分布式存储
- 高可用性
- 可扩展性
categories: 
- "视频总结"
subtitle: Ceph_User_+_Dev_Monthly_Meetup_-_May_2025
---

### 会议基本信息

- **会议主题**: Ceph 高级用户讨论会 - 来自 Cephalocon 的反馈总结
- **主持人**: Dan Vanderster
- **会议时间**: 近期周会
- **参与人员**: Dan Vanderster, Laura, Enrico, Casey, Brian 等核心开发成员及社区用户

### 关键讨论议题

1. **集群再平衡优化 (Balancer/Upmap)**: 讨论了将 `upmap remapped` 和 `PG remapper` 逻辑整合到 Balancer 模块，以及处理 degraded PGs 的情况。计划将 upmap 逻辑集成到 balancer 模块，并增加配置选项以允许在 degraded 状态下继续运行 balancer。

2. **OSD 重启与维护优化**: 讨论了 OSD 重启时产生的延迟峰值和 PG peering 过程对性能的影响。建议在维护模式下自动设置 `no-up` 和 `primary-affinity=0`，分阶段重启 OSD，并在所有 PGs 完成peering后解除 `no-out` 标志。

3. **RGW 性能调优**: 讨论了慢速 OSD 对 RGW 索引操作的影响以及默认线程池配置在高负载场景下的不足。建议增加 `rgw_thread_pool_size` 和 `rgw_max_concurrent_requests`，推进 async 化改造，并创建 RGW 性能调优文档。

4. **CephFS 灾难恢复**: 讨论了现有灾难恢复文档步骤复杂，自动化程度低的问题。建议添加流程图明确各步骤执行条件和风险，并考虑让 MDS 在启动失败时自动执行部分恢复步骤。

5. **MClock 与 WPQ 调度器**: 讨论了 MClock 基准测试结果与实际 HDD 性能存在差异，以及用户对 MClock 稳定性仍存疑虑的问题。建议改进 OSD 基准测试工具准确性，提供标准 `fio` 测试方法验证设备性能，并计划开展技术讲座展示 MClock 工作原理和调优方法。

### 决议事项

- 将 upmap 逻辑整合到 balancer 模块（目标版本：U release）
- 优化 sephadm 主机维护流程，自动处理 `no-up` 和 primary-affinity
- 编写 RGW 性能调优最佳实践文档
- 改进 CephFS 灾难恢复文档的可操作性
- 组织 MClock 技术讲座并改进基准测试工具

### 后续行动计划

| 任务项 | 负责人 | 时间节点 |
|--|--|-|
| 研究 upmap 集成方案 | NA & Casey | U release周期 |
| 验证 OSD map 修剪行为 | Brian & Rados团队 | 1个月内 |
| 创建 RGW 调优文档 | Anscar | 下月会议前 |
| 改进 CephFS DR 文档 | MDS团队 | Tentacle发布后 |
| 组织 MClock 技术讲座 | NA & Joel | 下季度 |

### 未完成讨论

- sephadm 和容器化改进
- PG autoscaler 算法优化
- 多站点部署挑战

下次会议时间: 待定（预计1个月后）