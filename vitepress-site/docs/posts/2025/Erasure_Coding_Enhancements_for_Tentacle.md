---
title: "Erasure Coding Enhancements for Tentacle"
date: 2025-06-24
updated: 2025-06-24
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "BlueStore"
categories:
  - "视频总结"
outline: deep
---
### Ceph 分布式存储 Erasure Coding 性能优化进展

**会议主题**：Ceph 的 Erasure Coding (EC) 性能优化进展  
**主讲人**：Bill（IBM 高级技术专家）、Alex Aninsko（IBM 高级技术成员）  
**会议时间**：近期（具体日期未标注）



#### 1. 会议背景与目标
- **背景**：Ceph 的 EC 编码（如 3-way 副本）存储效率较低，成本较高。
- **目标**：通过算法优化减少 IO 操作，提升 BlueStore 效率，降低 CPU 和网络开销，最终降低 TCO。
- **核心优化点**：
  - 减少对存储设备的 IO 请求。
  - 与 Crimson 等其他性能优化方案互补。



#### 2. 主要优化内容
#### (1) 功能实现
- **部分读取/写入**：旧版 EC 需读取完整条带，新版仅读取所需块，减少冗余 IO。
- **优化写入**：经典方法与 Parity Delta Writes 技术结合，减少数据读取和写入量。
- **空间效率提升**：小对象写入时避免零填充，实际存储空间占用显著降低。

#### (2) 恢复与校验优化
- **Rebalance**：仅迁移必要数据，减少迁移过程中的 IO 操作。
- **Deep Scrub**：新增对 EC 池的 CRC 校验支持，提升性能。

#### (3) 兼容性与部署
- **向后兼容**：升级后默认禁用优化，需通过 `allow_ec_optimizations` 标志启用。
- **客户端兼容性**：仅需升级核心组件，无需更新客户端。



#### 3. 性能数据
- **读性能**：接近 replica 3 的延迟表现，未来通过 Direct Reads 进一步优化。
- **写性能**：所有测试场景均优于旧版，随机写入吞吐量提升显著。
- **CPU 与网络**：CPU 开销减少，网络流量下降。



#### 4. 配置建议
- **条带大小**：默认 4K，新池推荐 16K 条带。
- **启用命令**：`ceph osd pool set <pool> allow_ec_optimizations true`



#### 5. 后续计划
- **待实现功能**：Direct Reads/Writes、分布式 Parity Delta Writes。
- **性能持续优化**：对齐 replica 3 的成熟度。



#### 6. Q&A 摘要
- 新版 EC 性能优于旧版，16K 条带效果最佳。
- CPU 利用率降低，性能提升。



#### 行动项
- IBM 团队继续收集性能数据，发布优化细节博客。
- 社区用户测试 Tentacle RC 版本，反馈实际场景性能。
- 文档团队更新 EC 配置指南，明确 16K 条带建议。