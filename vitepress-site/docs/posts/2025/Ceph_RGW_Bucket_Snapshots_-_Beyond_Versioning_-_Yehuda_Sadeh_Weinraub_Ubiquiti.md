---
title: "Ceph RGW Bucket Snapshots- Beyond Versioning - Yehuda Sadeh Weinraub, Ubiquiti"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "RGW"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph RGW Bucket Snapshots 会议纪要

#### 会议主题
本次会议主要讨论了 Ceph RGW（RADOS Gateway）Bucket Snapshots 功能的开发进展、设计原理、实现细节及未来规划。主讲人 Yehuda Sadeh（前 IBM 员工，现 Ubiquiti 成员）介绍了该功能的背景、技术挑战及当前实现状态，并由 Shilpa（RGW 团队）接手后续开发。

#### 关键讨论内容

##### 背景与动机
- **现有备份方案的局限性**：当前 RGW 备份主要依赖 Activity Logs，但存在同步生成、数据一致性差等问题。
- **S3 Object Versioning 的局限性**：支持归档，但无法保证跨对象的一致性，且可能导致数据膨胀。

##### Bucket Snapshots 功能设计
- **核心能力**：用户可对 Bucket 启用快照功能，支持创建、删除、列出快照（非管理员操作），并访问历史快照中的对象数据。
- **实现原理**：扩展 Object Versioning，引入 snapID 作为新维度，通过 OH（Object Logical Head）跟踪对象在不同快照中的最新实例。

##### 技术挑战与解决方案
- **对象覆盖处理**：通过 snapID 区分不同版本的对象。
- **快照删除与清理**：删除快照时触发 Lifecycle 进程，检查对象是否被其他快照引用，仅清理无引用的对象。
- **多站点限制**：当前为 Zone-local 功能，快照不会跨 Zone 同步。
- **性能与扩展性**：限制单 Bucket 的快照数量，避免 OMAP 数据膨胀和 Bucket Index 过载。

##### 演示与 API 扩展
- **Demo 关键操作**：创建 Bucket → 启用快照 → 生成快照 → 覆盖对象 → 生成新快照。
- **新增 S3 API 参数**：`snap_id`（指定快照版本），`snap_range`（查询快照范围变更）。

##### 后续行动计划
1. **功能完善**：增强多站点支持，优化快照一致性。
2. **测试与验证**：扩大测试覆盖。
3. **性能调优**：监控 Bucket Index 负载，评估 Shard 数量计算公式。

#### 总结
RGW Bucket Snapshots 为 Ceph 提供了更灵活的备份和版本管理能力，目前功能已接近完成，后续将聚焦于多站点集成和性能优化。社区可通过测试和反馈推动其成熟。

#### Q&A 重点摘要
- **快照创建是否加锁**？目前无锁，应用需自行暂停写入以确保一致性。
- **Shard 数量如何规划**？需综合考虑对象数量、快照数量及写入频率。
- **元数据操作是否加剧 PG 压力**？通过限制快照数量缓解，但需长期监控。