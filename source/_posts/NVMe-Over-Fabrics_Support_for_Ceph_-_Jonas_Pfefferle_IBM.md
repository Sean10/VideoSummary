---
title: "NVMe-Over-Fabrics Support for Ceph - Jonas Pfefferle, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph中Envy me over Fabrics的概述

#### 主讲人：Jonas, IBM Research

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 会议内容总结：

1. **背景介绍**：
   - Jonas首先介绍了Envy me over Fabrics（NVMe-oF）在Ceph中的应用，强调了其与现有RBD（RADOS Block Device）的区别和优势。
   - 主要原因包括提高与其他系统的互操作性，支持现有生态系统中的远程存储访问，以及利用DPU（Data Processing Unit）的硬件加速能力。

2. **技术细节**：
   - **架构设计**：NVMe-oF Gateway作为中间层，将NVMe-oF协议转换为RADOS协议，支持TCP和RDMA两种传输方式。
   - **控制路径**：使用Python编写的控制守护进程，通过gRPC进行配置管理，支持RBD图像到子系统命名空间的映射。
   - **数据路径**：采用SPDK（Storage Performance Development Kit）处理数据路径，支持多种块设备类型。
   - **多路径和故障转移**：通过NVMe-oF的多路径规范，实现Gateway Group的概念，支持配置持久化和多Gateway的协同工作。

3. **性能测试**：
   - 展示了单客户端和多客户端场景下的性能测试结果，表明NVMe-oF Gateway能够接近直接使用RBD的性能。
   - 测试了不同数量卷的扩展性，表明系统能够处理大量并发IO。

4. **未来计划**：
   - 计划实现Discovery服务，支持动态路径发现和更新。
   - 考虑增加身份验证和加密功能，以及全局QoS（Quality of Service）控制。
   - 探索直接在Ceph OSD中使用NVMe-oF的可能性，以优化数据路径。

5. **项目状态**：
   - 当前项目处于开发阶段，计划在Reef版本中发布初始版本，支持单Gateway配置。
   - 多Gateway功能已经合并到代码库中，未来将逐步增加更多功能。

6. **参与者和资源**：
   - 项目由多个公司和团队共同参与，提供代码库和社区支持。
   - 鼓励社区成员参与测试和反馈，共同推动项目发展。

#### 后续行动计划：
- 继续优化性能和扩展性，特别是在多客户端和高并发场景下。
- 实现Discovery服务，增强系统的动态适应能力。
- 探索和实现身份验证、加密和全局QoS控制。
- 加强社区合作，通过定期会议和Slack频道收集反馈和建议。

#### 会议结束：
- 会议在提问和讨论环节后圆满结束，Jonas感谢所有参与者的积极互动和支持。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。