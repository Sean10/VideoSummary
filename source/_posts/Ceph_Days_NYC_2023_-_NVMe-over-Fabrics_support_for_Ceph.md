---
title: "Ceph Days NYC 2023: NVMe-over-Fabrics support for Ceph"
date: 2023-05-17
updated: 2023-05-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph 对 NVMe over Fabrics 的支持

#### 会议时间：[具体时间]

#### 会议地点：[具体地点]

#### 参会人员：[列出主要参会人员]

#### 会议内容总结：

1. **背景与动机**：
   - 项目始于大约三年前，最初是为了探索在 DPU 硬件上支持 Ceph 的可能性。
   - 由于当时市面上的 DPU 硬件性能较低，决定引入 NVMe over Fabrics 以提高性能和集成度。
   - NVMe over Fabrics 已成为访问远程块存储的实际标准，广泛应用于各种系统中。

2. **技术实现**：
   - **架构概述**：Ceph 集群通过 NVMe over Fabrics Gateway 与客户端通信，Gateway 包含多个进程，支持 TCP、RDMA 和 Fiber Channel。
   - **数据路径与控制路径**：控制路径使用 Python 进程通过 gRPC 服务进行配置管理，数据路径采用 SPDK（Storage Performance Development Kit）进行高效数据传输。
   - **多路径与故障容忍**：引入 Gateway 组概念，通过 Ceph 的 watch-notify 机制和轮询机制保持配置同步，支持多路径优化和负载均衡。

3. **性能测试**：
   - 目标是在不使用 Gateway 的情况下尽可能接近原生性能。
   - 在实验室环境中，通过优化和增加并发客户端实例，性能已接近原生性能的 92%。
   - 正在进行更大规模的测试，以验证在更大集群上的性能表现。

4. **未来计划**：
   - 计划引入 Discovery Service 和集中式发现功能。
   - 考虑增加身份验证和加密支持，采用插件架构以灵活支持不同的安全方法。
   - 与 Intel 合作，探索 ADNN（Adaptive Data Network）技术，优化数据路径选择。

5. **可用性与支持**：
   - 当前版本已可下载试用，但仍需更多测试和优化。
   - 计划在 Reef 版本中发布初始版本，支持单 Gateway 和基本配置管理功能。

#### 决定事项：
- 确认了 NVMe over Fabrics 在 Ceph 中的实现方案和性能优化方向。
- 确定了未来版本的功能增强和优化计划。

#### 后续行动计划：
- 继续进行性能测试和优化，特别是在更大规模集群上的测试。
- 开发和集成 Discovery Service、身份验证和加密功能。
- 与社区合作，收集反馈并改进产品。

#### 会议结束：
- 会议在讨论和解答相关问题后结束，感谢所有参与者的贡献和讨论。

---

**备注**：本会议纪要基于会议内容的总结，具体细节和数据可能需要参考原始会议记录或相关技术文档。