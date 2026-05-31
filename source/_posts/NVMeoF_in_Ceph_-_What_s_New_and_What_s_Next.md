---
title: NVMeoF in Ceph - Whats New and Whats Next?
date: 2025-06-24
updated: 2025-06-24
tags:
- Ceph
- 高可用性
categories: 
- "视频总结"
subtitle: NVMeoF_in_Ceph_-_What_s_New_and_What_s_Next
---

### **Ceph NVMe over TCP 网关开发进展会议纪要**

#### **1. 会议概述**
- **主持人**: Ail Caro（IBM 工程经理，负责 NVMe over TCP 网关及 Ceph RBD 团队）
- **主要内容**: 
  - **Tentacle** 版本（非 Squid）中实现的 NVMe over TCP 网关功能。
  - 即将在 Tentacle 中发布的新特性。
  - 未来 roadmap 中的规划方向。

#### **2. 核心议题与讨论**

##### **2.1 当前 NVMe over TCP 网关架构**
- **组件分层**: 控制平面（管理配置和同步）和 IO 处理层（基于 SPDK）。
- **数据映射**: NVMe 命名空间对应 Ceph RBD 镜像。

##### **2.2 高可用性（High Availability）**
- **网关组**: 共享配置，通过 NVMe ANA 组实现故障切换。
- **监控机制**: NVMe Monitor 检测故障，触发自动故障转移。
- **故障恢复**: 目标优化至 6-8 秒。

##### **2.3 安全与性能**
- **加密**: 支持传输层 TLS-PSK 和管理接口 mTLS 认证。
- **QoS**: 支持按命名空间限制 IOPS/吞吐量。

##### **2.4 新特性（Tentacle 即将发布）**
- **Cluster Context 优化**: 提升低命名空间数量时的并行性。
- **自动负载均衡**: 动态调整命名空间分布。
- **命名空间掩码**: 精细化控制主机访问权限。
- **In-band 认证**: 子系统与主机双向认证。

##### **2.5 监控与工具**
- **Grafana 看板**: 网关配置总览、性能监控、告警功能。
- **CLI 集成**: 将 NVMe CLI 合并至 Ceph CLI。

##### **2.6 未来 Roadmap**
- **NVMe Reservation**: 支持 Windows 集群访问同一命名空间。
- **Cancel Command**: 解决 Admin Queue 限制问题。
- **硬件加速**: 利用 Intel DSA 优化 CRC 计算。
- **扩展场景**: Stretch Cluster 和 CSI Driver。

#### **3. 行动计划**
- **短期交付**: 完成NVMe Reservation 和 Cancel Command的代码审查，优化故障检测机制。
- **长期规划**: 开发动态命名空间迁移功能和优化 Grafana 监控看板。

#### **4. 关键词保留**
- Ceph, NVMe over TCP, SPDK, ANA groups, RBD, TLS-PSK, mTLS, QoS, Cluster Context, Grafana, CLI, NVMe Reservation, Intel DSA, Stretch Cluster, CSI Driver

#### **5. 问题与后续**
- **待验证**: Intel DSA 和 TLS-PSK 的兼容性。
- **用户反馈**: 命名空间掩码的使用需求。

（会议结束）