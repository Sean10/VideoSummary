---
title: 9 years of Ceph at Walmart. Pavan Rallabhandi from Walmart
date: 2025-05-08
updated: 2025-05-08
tags:
- 分布式存储
- 存储优化
- 高可用性
categories: 
- "视频总结"
subtitle: 9_years_of_Ceph_at_Walmart._Pavan_Rallabhandi_from_Walmart
---

### 9年Walmart Ceph实践：从起步到挑战与展望

Walmart作为Ceph的长期用户，分享了他们在Ceph上的实践经验与挑战。以下是对Walmart Ceph实践会议的总结：

**会议概述**：

Walmart的Hollandi和Anton Packard分享了Walmart在Ceph上的多年实践经验，包括Ceph的起步阶段、现状以及未来展望。

**Ceph的起步**：

- Walmart使用Ceph已有近十年时间，最初使用Ceph Block Storage（RBD）和Ceph Object Storage（RGW）。
- 早期使用NVMe网络和较低密度的服务器，并解决了RGW的内存问题、Swift对象过期和内存崩溃等问题。
- Walmart也向Ceph社区贡献了代码和功能改进。

**Ceph的现状**：

- Walmart的Ceph集群已从Nautilus升级到Pacific和Quincy版本，并通过自动化工具进行集群管理。
- 优化了Ceph Block Storage的性能，并通过性能测试对不同配置的OSD数量进行了验证。
- 在Ceph Manager（cephadm）问题、硬件故障、性能指标异常、大规模集群管理等方面面临挑战。
- 正在探索为Ceph Block Storage提供更低的延迟，并重点关注Ceph CSI的集成与优化。

**未来的展望**：

- Walmart将继续与Ceph社区合作，解决当前面临的挑战，并推动Ceph在大型集群中的应用。
- 重点关注低延迟工作负载、Ceph CSI的集成、错误报告与监控等方面的改进。

**技术细节与挑战**：

- 在大规模集群中，OpenStack超节点上的临时端口耗尽问题。
- Thundering Herd问题，即大规模虚拟机集群同时发送trim和discard请求时，可能导致Ceph集群性能急剧下降。
- OSD故障恢复延迟问题。
- Ceph Manager在高负载下捕获的性能指标可能出现异常高值。

**总结与后续行动计划**：

- 继续探索大规模集群中的性能瓶颈。
- 与Ceph社区合作，解决Cephadm在高负载下的性能问题。
- 优化Ceph对大规模trim和discard请求的处理。
- 改进Ceph的错误报告机制，确保在硬件故障时能够快速恢复。