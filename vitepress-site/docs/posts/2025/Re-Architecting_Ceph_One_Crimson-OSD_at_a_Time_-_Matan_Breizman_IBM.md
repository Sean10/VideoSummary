---
title: "Re-Architecting Ceph, One Crimson-OSD at a Time - Matan Breizman, IBM"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### **Ceph Crimson项目进展会议纪要**

#### **会议概述**

本次会议由Ceph核心开发团队成员Matan主持，重点介绍了Crimson项目的背景、目标、当前进展及未来规划。Crimson项目旨在通过重构Ceph的OSD（对象存储守护进程）来提升性能，特别是在多核CPU和NVMe SSD等现代存储设备上的表现。

#### **关键讨论议题**

##### **1. Crimson项目的背景与动机**

- **CPU架构趋势**：自2008年以来，CPU核心数大幅增加，但时钟频率趋于稳定，因此并发性成为提升性能的关键。
- **现有Classical OSD的瓶颈**：多线程架构导致高锁争用、频繁上下文切换和CPU缓存局部性差，影响性能。

##### **2. Crimson架构的核心改进**

- **共享无状态设计**：每个核心拥有一个线程，通过SeaStar框架实现无锁化，提高数据局部性和CPU利用率。
- **技术挑战与解决方案**：采用C++20协程简化异步代码，引入`errorator`机制强制编译期错误检查，提升调试体验。

##### **3. 性能对比与测试结果**

- **Perf工具分析**：Crimson OSD在上下文切换、CPU迁移、低利用率和缓存命中率方面优于Classical OSD。
- **IOPS与延迟测试**：Crimson在随机读性能上达到Classical的4倍以上，但在随机写性能上仍有提升空间。

##### **4. 项目进展与Roadmap**

- **已实现功能**：Squid版本支持BlueStore后端、多核并发、PG分裂；Tentacle版本提供Systo后端技术预览和性能优化。
- **Umbrella版本计划**：Seamless部署、RGW支持、FastEC、Scrub调度、PG合并以支持Autoscaler。
- **未来方向**：验证混合集群可行性，持续优化随机写性能。

##### **行动计划与待办事项**

- **性能优化**：提升随机写性能，扩展FastEC支持至Crimson。
- **功能完善**：完成Systo的完整恢复能力，更新用户文档。
- **测试与反馈**：扩大夜间测试覆盖范围，邀请社区参与早期部署测试。
- **社区协作**：鼓励贡献者加入，特别感谢Joy Han和Yingen对Systo的贡献。

#### **问答环节摘要**

- **Q**：随机读写测试是否支持EC（Erasure Coding）？
  - **A**：当前仅支持副本（replication），FastEC将在未来支持。
- **Q**：Crimson何时达到功能完备？
  - **A**：Umbrella版本后可作为技术预览，但生产环境需待关键功能稳定。
- **Q**：新增监控指标？
  - **A**：新增Crimson专属指标，如reactor利用率、冲突事件统计。

#### **总结**

Crimson项目通过架构革新显著提升了Ceph在多核环境下的性能，尤其在随机读场景表现突出。下一步将聚焦随机写优化、生态兼容性及用户体验，并呼吁社区参与测试，共同推动项目成熟。