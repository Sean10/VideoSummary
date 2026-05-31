---
title: Detect, Decide, Fence- Resolving Netsplits in 3-AZ Stretch Cluster - Kamoltat (Junior) Sirivadhna
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 分布式存储
- 高可用性
categories: 
- "视频总结"
subtitle: Detect_Decide_Fence_-_Resolving_Netsplits_in_3-AZ_Stretch_Cluster_-_Kamoltat_Junior_Sirivadhna
---

### Ceph 3AZ Stretch Cluster 网络分裂解决方案会议纪要

#### 会议概述
- **主讲人**: Kamotad（Junior），Ceph贡献者，专注于分布式存储领域
- **主题**: 3AZ Stretch Cluster中的网络分裂问题及解决方案
- **核心问题**: 在3AZ（三数据中心）架构中，如何检测和解决网络分裂，避免split-brain现象，确保集群高可用性。

#### 关键讨论点

#### 1. **问题背景**
- **3AZ架构**: 数据分布在三个DC，每个DC包含两份数据副本，允许单个DC完全故障。
- **网络分裂场景**: DC1与DC2断开连接，但均与DC3保持连通。此时，OSDs因心跳失败报告对方为`down`，导致PGs频繁切换状态，IO暂停。
- **挑战**: 需快速隔离一个DC，确保剩余DC继续服务。

#### 2. **解决方案设计**
- **网络分裂检测**: 利用monitor间的**connection scores**构建连接图，识别断开的数据中心，并在`ceph status`中显示健康警告。
- **选择幸存DC的算法**（BK算法）: 找到最大连通子图，确保最多DC参与服务。通过启发式规则选择最优clique，优先级包括OSD总权重、存活monitor数量、monitor连接分数等。
- **隔离（Fencing）执行**:
  - **预检查**: 模拟排除被隔离DC后的PG acting set，确保不违反`min_size`。
  - **全局标记**: 设置`no_recover`和`no_backfill`，避免数据迁移干扰。
  - **隔离生效**: Monitor忽略被隔离DC的OSD故障报告，PG acting set排除其OSD。

#### 3. **隔离恢复与边界场景**
- **恢复条件**: 网络分裂消失且持续超过`lift_fencing_threshold`。
- **动态调整**: 若网络状态变化导致更优clique出现，需超过`switch_fence_threshold`才切换隔离目标。

#### 4. **扩展性与优化建议**
- **多DC支持**: 当前算法支持3-5个DC，未来可扩展。
- **链路感知**: 考虑数据中心间延迟，优化clique选择。
- **用户自定义**: 允许管理员配置DC优先级或权重。
- **RGW集成**: 需在RGW中暴露隔离状态，确保客户端请求路由到幸存DC。

#### 5. **行动计划**
- **代码落地**: 将解决方案集成至Ceph主线，完善`switch_fence_threshold`逻辑。
- **测试验证**: 模拟多DC网络分裂场景，验证算法效率与稳定性。
- **用户侧增强**: 提供配置选项，完善文档说明。

#### 遗留问题
- **RGW集成**: 需明确如何在高层级服务中传递隔离状态。
- **动态权重**: 是否引入链路质量指标优化clique选择？

#### 专业术语保留（中英对照）
- Split-brain（脑裂）
- CRUSH algorithm
- OSD/MON/MDS/PG
- RADOS/librados
- Erasure coding（纠删码）
- Acting set
- Clique（最大连通子图）
- Fencing（隔离）
- Stretch cluster