---
title: "NVMe-Over-Fabrics Support for Ceph | Ceph Days NYC 2024"
date: 2024-05-24
updated: 2024-05-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：NVMe over TCP 和 NVMe-oF Gateway 的集成与性能优化

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 参会人员：
- **Mike Burkhart** - IBM 产品经理，负责 NVMe over TCP 和 VMware 集成

#### 会议内容概要：

1. **NVMe 驱动介绍**
   - NVMe 驱动具有高耐用性、并行处理能力和高度可扩展性。
   - NVM fabric 规范自2018-2019年成熟，支持通过不同传输介质（如光纤通道、RDMA 和 NVMe over TCP）访问 NVMe 磁盘。

2. **NVMe over TCP 的优势**
   - 通过网络传输实现 NVMe 驱动的高容量、可扩展性和耐用性。
   - 利用 SEF（Scalable Ethernet Fabric）的扩展能力，增强 NVMe 的耐用性和并行处理能力。

3. **TCP 连接模型**
   - 每个 TCP 连接实例使用用户空间驱动，每个连接对应一个独立的会话和 NVMe 命名空间控制器。
   - 这种一对一的连接模型支持高度的可扩展性和控制灵活性。

4. **性能优化与传统技术对比**
   - 与传统的 iSCSI 技术相比，NVMe over TCP 提供了更高的吞吐量、更好的 IOPS 和更低的延迟。
   - RBD（RADOS Block Device）作为底层实现，已经过充分测试和验证。

5. **架构与集成**
   - NVMe-oF Gateway 采用用户空间驱动，基于 SPDK（Storage Performance Development Kit）开发。
   - 支持多路径和负载均衡，每个 Gateway 可以加载所有可用的子系统，实现环境隔离。

6. **控制器与子系统管理**
   - 控制器是临时性的，客户端断开连接后，控制器可以被回收利用。
   - 子系统用于协调命名空间，支持多子系统和多 Gateway 的扩展。

7. **配置与安全性**
   - Gateway 的配置存储在 omap 中，支持配置在实例间的迁移。
   - 使用 SPDK 和 TLS PSK 实现加密通信，未来计划支持 inband o。

8. **性能测试结果**
   - 与 iSCSI 相比，NVMe over TCP 在多个性能指标上显示出显著优势，特别是在多节点和多反应器配置下。

9. **VMware 集成**
   - 支持通过 VMware vSphere APIs for Storage Awareness (VASA) 进行存储加速和卸载。

#### 决定事项：
- 确认 NVMe over TCP 作为下一代存储解决方案的技术优势和性能表现。
- 继续推进与 VMware 的集成工作，优化存储性能和效率。

#### 后续行动计划：
- 完成 NVMe over TCP 与现有 RBD 接口的完全映射。
- 继续进行性能测试和优化，确保在不同工作负载下的稳定性和高效性。
- 推进与 VMware 的深度集成，实现更高效的存储管理和优化。

#### 会议结束时间：[具体时间]

---

以上为本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。