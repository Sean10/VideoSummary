---
title: Ceph User + Dev Monthly - November 2025
date: 2025-11-20
updated: 2025-11-20
tags:
- Ceph
- 分布式存储
- 性能优化
categories: 
- "视频总结"
subtitle: Ceph_User_+_Dev_Monthly_-_November_2025
---

### Ceph 用户开发会议纪要

**会议时间**：未注明（近期）  
**参会人员**：Laura（主持人）、Anthony、Alexander、Enrico、Stefan、Casey、Gregory 等



#### **1. 议程概览**

- 回顾既往行动项进展
- 讨论关键议题（灾难恢复工具、内存问题、进度指示器等）
- 新功能与社区参与计划
- 其他议题（IPv6支持、健康告警优化等）



#### **2. 关键讨论议题**

**a. 灾难恢复工具改进**

- **问题**：
  - `cephfs` 灾难恢复工具（如 `scan_links`、`recover_entries`）存在内存消耗过高问题（可达 2TB Swap）。
  - 文档不完善，未明确大内存需求或并行操作指导（如 `range` 参数的使用）。
  - 进度指示缺失，操作耗时难以预估。
- **解决方案**：
  - 新增 Tracker 以优化进度显示（已提交 PR，待合并至 Squid/Tentacle）。
  - 建议文档补充 `range` 参数用法及内存需求警告。
  - 长期目标：工具与核心代码解耦，支持跨版本兼容（如 Reef → Squid）。

**b. 内存管理问题**

- **案例**：`recover_entries` 需手动分段执行以避免 OOM，缺乏自动化工具定位日志范围。
- **建议**：
  - 工具应主动报告内存需求（如预检阶段）。
  - 新增健康告警，标识受 Elastic Shared Blob Bug 影响的 OSD（需基于 `ceph-osd-metadata` 版本检测）。

**c. IPv6 与运维优化**

- **IPv6 支持**：`ceph-exporter` 默认不监听 IPv6 地址（需新 Tracker 跟踪）。
- **健康告警**：维护模式下主机 Demon 状态误报，建议优化为“已检测但预期中”的 muted 状态。



#### **3. 决策与行动计划**

| **事项**                          | **负责人**       | **下一步**                                                                 |
|--||--|
| 创建 `recover_entries` 进度追踪器 | Alexander        | 提交新 Tracker，关联现有 PR [#63191]。                                  |
| 文档补充灾难恢复工具内存警告       | Enrico/Laura     | 在现有 Tracker 中补充操作经验，明确并行化步骤。                              |
| IPv6 监听问题修复                 | Stefan           | 创建新 Tracker 并标记 `user-dev` 标签。                                    |
| Elastic Blob Bug 健康告警         | Laura            | 联系 Bluestore 团队（Adam Coopcheck）评估可行性。                          |
| 社区测试计划（Tentacle）          | Laura/Njo        | 下月会议讨论早期测试参与流程。                                              |



#### **4. 社区与协作**

- **Pillar Leaders 招募**：征求性能、编排、安全等领域的讨论牵头人。
- **社区参与**：
  - Anthony 推广贡献者表单及社区调研，鼓励反馈。
  - 建议用户参与 `cephadm` 和 RGW 新功能测试（如 S3 桶策略改进）。



#### **5. 其他事项**

- **RGW 对象 ACL 修复**：Casey 建议使用 `put-object-acl` API 替代 `touch` 命令处理大对象。
- **后续会议**：下月聚焦社区测试、安全/可扩展性主题，开发者将受邀参与实时讨论。



**会议记录人**：AI 摘要  
**备注**：完整讨论详见[议程文档](https://pad.example.com)及关联 Tracker。  
**关键词保留**：CephFS、PG、OSD、CRUSH、RADOS、Bluestore、cephadm、Squid/Tentacle、Elastic Shared Blob Bug、IPv6、健康告警、灾难恢复。