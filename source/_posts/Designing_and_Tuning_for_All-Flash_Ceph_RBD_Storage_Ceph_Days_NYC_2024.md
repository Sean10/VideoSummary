---
categories:
- 视频总结
date: 2024-05-15
subtitle: Designing_and_Tuning_for_All-Flash_Ceph_RBD_Storage_Ceph_Days_NYC_2024
tags:
- Ceph
- All
- Flash Storage
- Performance Tuning
- RBD
- CephFS
title: "Designing and Tuning for All-Flash Ceph RBD Storage | Ceph Days NYC 2024"
updated: 2024-05-15
---



会议主题：设计与调优全闪存Ceph RBD存储

会议概要：
- **主讲人背景**：Tyler来自Bloomberg的计算基础设施团队，负责Ceph RBD存储的设计与调优。
- **公司背景**：Bloomberg自2013年开始使用OpenStack和Ceph，致力于高密度计算和深度存储。
- **网络架构**：采用基于L3的网络架构，解决大规模VM部署中的网络挑战。
- **性能优化**：
  - **内存管理**：解决内存交换问题，优化NUMA设置，通过调整内存目标和深入分析，提高了性能。
  - **网络与存储**：利用L3网络架构和全闪存存储，实现无客户影响的升级和维护。
  - **NUMA优化**：通过优化NUMA设置，显著降低上下文切换，提高了性能稳定性。
- **性能挑战与解决方案**：
  - **交换问题**：通过优化NUMA设置解决。
  - **性能波动**：通过禁用scrubs和优化网络带宽使用减少。
  - **内核与驱动优化**：调整NIC驱动设置，优化了RSS处理，减少了CPU核心的热运行。
  - **CRC32性能**：优化CRC32计算，提高性能。
- **决定事项**：
  - 继续优化NUMA设置。
  - 考虑在Ceph中默认使用更高效的CRC32实现。
  - 利用L3网络架构和全闪存存储优化维护和升级流程。
- **后续行动计划**：
  - 加强性能监控。
  - 将优化经验和发现分享给Ceph社区。
  - 持续关注和优化Ceph RBD存储的性能。

关键词：Ceph, OpenStack, L3 Networking, NUMA, CRC32, All-Flash Storage, Performance Tuning