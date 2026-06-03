---
title: "NVMeoF in Ceph - Whats New and Performance Best Practices - Mike Burkhart & Aviv Caro, IBM"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
  - "高可用性"
categories:
  - "视频总结"
outline: deep
---
### Ceph NVMe over Fabric (NVMe-oF) 技术分享会议纪要

#### 会议基本信息
- 主题：Ceph NVMe-oF 最新进展与性能最佳实践
- 主讲人：Mike Burkheart (IBM, NVMe-oF 产品经理) & Aviv Carol (IBM, NVMe-oF 及 RBD 开发团队负责人)
- 主要内容：Ceph Tentacle 版本中 NVMe-oF 的首发支持，高可用性架构，性能优化，自动化改进等

#### 关键讨论议题

##### 1. Ceph Tentacle 对 NVMe-oF 的支持
- 首次上游集成，支持多网关部署，实现高可用性和负载均衡。
- 支持 Linux 和 VMware 发起端，要求 Linux kernel ≥5.4，VMware ≥8.0U3。

##### 2. 高可用性（HA）设计
- 使用 Paxos 服务监控网关状态，触发故障转移。
- ANA 协议实现命名空间级别的读写隔离和负载均衡。

##### 3. 安全与访问控制
- 支持单向和双向认证，密钥加密存储于 OMAP。
- 命名空间掩码支持精细化控制，限制主机访问特定命名空间。

##### 4. 新功能与改进计划
- Kubernetes CSI 驱动开发中，目标支持 OpenShift。
- 自动化改进，合并元数据池与数据池管理，简化部署流程。
- 性能优化，缩短故障转移时间，CRC 校验复用，探索 DPU/SmartNIC 支持。

##### 5. 性能测试结果
- 在双路 32 核 CPU，24 NVMe 盘，4/8/12 节点集群上进行测试。
- 随机读写（70/30）测试中，12 网关组可达 100 万 IOPS，延迟 <2ms。

#### 问答环节摘要
- 问答环节涵盖了 NVMe-oF 与 RBD 的性能对比，生产环境命名空间规划，DPU/SmartNIC 支持，池迁移工具兼容性等问题。

#### 后续行动计划
- 完善 Kubernetes CSI 驱动，实现 Active-Active 写入模式，扩展性能基准测试，补充文档等。

#### 关键词保留（Ceph/NVMe-oF 术语）
- Ceph: CRUSH algorithm, OSD, MON, RADOS, librados, PG, bluestore
- NVMe-oF: ANA protocol, SPDK, subsystem, namespace, initiator, QoS
- 存储：object storage, block storage (RBD), file system (CephFS)
- 高可用：failover, gateway group, Paxos
- 性能优化：failover time, CRC, DPU/SmartNIC
- 自动化：CLI, automation, Kubernetes CSI