---
title: "Supporting 3 Availability Zones Stretch Cluster - Kamoltat (Junior) Sirivadhna, IBM"
date: 2025-01-23
updated: 2025-01-24
tags:
  - "Ceph"
  - "分布式存储"
  - "高可用性"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：支持三可用区的Ceph Stretch Cluster

**会议主题**: 支持三可用区的Ceph Stretch Cluster  
**主讲人**: Junior, Ceph RADOS团队的工程师  
**时间**: 会议结束时的最后一场演讲  
**参会人员**: Ceph社区成员



#### 会议内容概述：

1. **自我介绍与背景**：
   - Junior介绍了自己的背景，作为Ceph RADOS团队的工程师，他为Ceph贡献了四年多，主要负责Stretch Cluster、Stretch Mode、Autoscaler等功能。

2. **Stretch Cluster简介**：
   - Stretch Cluster是一种跨多个地理位置的分布式存储集群，通常用于跨数据中心的场景，能够在数据中心故障时继续提供服务。

3. **传统Stretch Cluster的挑战**：
   - **网络分裂**：当两个数据中心之间的网络连接中断时，可能导致集群无法正常工作。
   - **Peering规则**：在某些情况下可能导致数据丢失。

4. **Stretch Mode的解决方案**：
   - 引入第三个数据中心的Monitor（Tiebreaker Monitor）解决网络分裂问题。
   - 在网络分裂时，将一个数据中心置于“黑暗模式”，集群在降级模式下运行。

5. **Peering规则改进**：
   - 新的Peering规则要求PG的acting set必须包含来自多个数据中心的OSD，以防止数据丢失。

6. **扩展到三可用区的挑战**：
   - 需要调整Peering规则，确保数据的分布和安全性。

7. **当前的限制与解决方案**：
   - **网络分裂问题**：需要实现机制来选择一个数据中心作为“黑暗模式”，并确保集群在两个可用区上继续运行。
   - **短期解决方案**：Monitor中增加网络分裂检测功能。
   - **长期解决方案**：选择一个数据中心作为“黑暗模式”。

8. **三可用区的实现现状**：
   - 三可用区的支持已经在Ceph的Squid版本和主分支中实现。

9. **Q&A环节**：
   - 回答了关于负载、纠删码支持、三可用区与AAL集群兼容性的问题。



#### 决定事项与后续行动计划：
- **测试与验证**：社区成员应测试三可用区的功能。
- **长期解决方案开发**：继续开发网络分裂检测和处理机制。
- **纠删码支持**：未来计划支持纠删码。



**会议结束**：感谢所有参会者的参与和支持，会议圆满结束。