---
title: "Ceph: A Journey to 1 TiB/s | Ceph Days NYC 2024"
date: 2024-05-16
updated: 2024-05-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：
**实现每秒一万亿字节的存储性能之旅**

#### 会议时间：
2024年某月某日

#### 参会人员：
Seth，以及其他相关技术人员和客户代表

#### 会议内容总结：

1. **项目背景与客户需求**：
   - 客户提出一个具有挑战性的使用案例，已初步设计架构，希望得到专业建议。
   - 客户要求硬件必须是Dell品牌，且每个机架最多部署四个节点，共七个机架，以确保故障域隔离。
   - 客户原有集群基于HDD，希望迁移到基于NVMe的集群，且要求零停机时间。

2. **硬件与网络配置**：
   - 客户已具备高速网络基础设施，具体细节未透露，但参考了Bloomberg的网络配置。
   - 硬件设计采用了100 GigE网络，测试环境使用的是focal auntu系统。

3. **性能优化与挑战**：
   - 通过Numa调优和BIOS设置，以及使用单处理器节点，提高了性能。
   - 发现并解决了多个性能瓶颈，包括C States和IMU的禁用，以及Upstream davan auntu构建问题。
   - 通过单个OSD和节点的测试，逐步排查并解决了性能下降的问题。

4. **测试与结果**：
   - 在优化设置后，集群性能显著提升，特别是在320个OSD的配置下实现了线性扩展。
   - 最终在3x复制模式下实现了每秒一万亿字节的读取性能，写入性能虽稍逊，但仍达到了预期目标。
   - 使用Eraser编码时，读取性能受到网络影响较大，但写入性能有所提升。

5. **后续行动计划**：
   - 客户将继续优化其应用以充分利用新集群的性能。
   - 社区合作将继续推进，目标是超越现有行业标准，如Vast和DDN W。

#### 决定事项：
- 确认了硬件配置和网络设置的最佳实践。
- 确定了性能优化的关键步骤和解决方案。
- 客户集群成功迁移并开始运行在新的NVMe集群上。

#### 后续行动计划：
- 继续监控和优化集群性能。
- 探索进一步的性能提升方法，如改进TCP堆栈。
- 加强社区合作，共同推动存储技术的进步。

#### 备注：
- 会议中提到的具体技术和配置细节，如C States、IMU、Eraser编码等，是优化性能的关键技术点，需在后续工作中重点关注和应用。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。