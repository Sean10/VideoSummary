---
title: "Ceph on Arm64/Ampere- IOPs/Watt Demystified - Federico Lucifredi, IBM"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "性能"
categories:
  - "视频总结"
outline: deep
---
本文针对由Federico Lucifredi（IBM代表）在Ceph会议上发表的"Ampere ARM处理器在分布式存储中的性能与能效分析"进行总结。以下为会议要点：

## 会议概览
- **主题**：Ampere ARM处理器在Ceph分布式存储中的性能与能效表现
- **主讲人**：IBM代表（代Ampere团队分享）
- **关键议题**：Ampere Altra与AmpereOne（MR1）处理器在Ceph集群中的IOPS/watt指标对比，探讨ARM架构在Ceph优化潜力。

## 核心讨论内容
### 1. Ampere ARM处理器的Ceph性能测试
- **测试目标**：评估IOPS/watt（每瓦特IOPS）作为能效核心指标。
- **测试配置**：
  - Ampere Altra：4节点集群（Ubuntu + Quincy），64核/节点，200K IOPS（写入），900W总功耗。
  - AmpereOne (MR1)：3节点集群（Ubuntu + Squid），192核/节点，400K IOPS（写入），1430W总功耗。
  - 其他参数：8 SSDs/OSD，100Gbps网络，replica=2，6000 PGs。
- **关键发现**：
  - MR1性能翻倍：写入性能从200K → 400K IOPS，IOPS/watt从223 → 285，提升28%。
  - 线性扩展性：在当前规模（24 OSDs）下未遇到瓶颈，未来计划测试12 OSDs以探索饱和点。
  - 读性能差异：写入提升2倍，但读取仅1.8倍，需进一步调查。

### 2. 能效与成本优势
- **核心价值主张**：
  - 降低OPEX：通过高密度核心（192C/节点）减少物理节点数量，优化机架空间与功耗。
  - 环境可持续性：SSD比HDD更节能（但HDD闲置时功耗更低）。

### 3. 挑战与未解问题
- **跨架构对比困难**：与Intel/AMD的公平对比需控制预算（$/性能）而非硬件配置，否则结果易偏颇。
- **ARM生态进展**：IBM/Red Hat计划：Ceph Quincy（v16.2）支持ARM客户端，Pacific（v17.2）支持ARM服务端集群。

### 4. 后续行动计划
- **Ampere团队**：
  - 扩大测试规模至12 OSDs，验证扩展性上限。
  - 分析读取性能未达预期的原因。
- **社区建议**：
  - 推广IOPS/watt作为存储集群的TCO评估指标。
  - 探索单插槽高核数设计对能效的进一步优化。

## 技术关键词保留
- **Ceph组件**：OSD, MON, PG, RADOS, CRUSH algorithm
- **存储类型**：object storage (RGW), block storage (RBD), file system (CephFS)
- **性能相关**：IOPS, latency, replication, erasure coding, tiering

## 开放问题
- **低功耗编码优化**：是否值得为ARM架构重构代码以提升并行性（vs. 单核性能）？
  - 初步反馈：需实测验证，但高核数设计已显优势。