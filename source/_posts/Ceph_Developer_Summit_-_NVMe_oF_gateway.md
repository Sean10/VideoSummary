---
title: Ceph Developer Summit - NVMe oF gateway
date: 2025-09-11
updated: 2025-09-12
tags:
- Ceph
- 存储优化
categories: 
- "视频总结"
subtitle: Ceph_Developer_Summit_-_NVMe_oF_gateway
---

Ceph NVMe-oF 网关功能优化会议纪要

本次会议重点讨论了Ceph NVMe-oF网关的功能优化计划，包括故障转移时间缩短、Active-Active网关支持、自动化管理增强以及性能优化等多个议题。

### 关键讨论内容

#### 1. 故障转移时间优化
- **当前问题**：故障转移时间约为12秒，主要因等待10秒确认网关离线，且beacon频率为5秒（需错过2次beacon才触发）。
- **改进方案**：优化beacon机制，仅发送状态差异（delta），降低数据量以支持1秒/次的高频beacon。
- **目标**：故障转移时间目标缩短至5-7秒（可配置，依赖网络稳定性）。
- **风险**：网络不稳定时可能导致误判（需用户根据环境调整参数）。

#### 2. Active-Active 网关支持
- **当前限制**：每个namespace仅由单一网关服务，多网关利用率低。
- **目标**：支持多网关同时写入（需解决IO顺序一致性问题）。
- **挑战**：数据损坏风险；需要开发重试/一致性逻辑；验证Initiator兼容性。

#### 3. 自动化管理增强
- **自动监听器（Auto Listeners）**：用户无需手动为每个子系统配置监听器，网关将根据网络掩码（CIDR）自动匹配节点IP并创建监听器。
- **元数据池（Metadata Pool）**：首次部署网关时自动生成，无需用户手动创建。

#### 4. 性能与功能优化
- **批量创建 Namespace**：支持单命令创建多个同名/同大小的namespace。
- **SPDK 实时统计**：新增CLI命令动态展示IOPS/延迟等指标。
- **加密支持**：讨论TLS（网关-Initiator）与RBD/OSD层加密的整合方案。
- **负载均衡改进**：未来引入实际负载（IOPS/吞吐量）均衡。

#### 5. 其他计划
- **CSI Driver 支持**：为Kubernetes提供NVMe-oF存储接口。
- **Stretch Cluster 优化**：故障转移时优先选择同站点网关。
- **SOS 报告增强**：完善NVMe相关日志收集。

### 后续行动计划
- 开发优先级：优先实现beacon优化和自动监听器。
- 测试验证：与多种Initiator进行兼容性测试，进行性能基准测试。
- 文档更新：新增配置参数说明。

此次优化旨在显著提升Ceph NVMe-oF网关的可用性、性能和易用性，为未来多活架构奠定基础。