---
title: "NVMe-over-Fabrics support for Ceph"
date: 2022-11-23
updated: 2022-11-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** NVMe over Fabrics 支持在 Ceph 中的实现

**主讲人：** Jonas Pfefferle 和 Scott Bauer

**会议时间：** [具体时间]

**参会人员：** [参会人员名单]

**会议内容总结：**

1. **背景介绍：**
   - Jonas Pfefferle 和 Scott Bauer 介绍了他们在 Ceph 中实现 NVMe over Fabrics 支持的工作。
   - 强调了这是一个社区合作项目，多家公司参与其中。

2. **NVMe over Fabrics 的重要性：**
   - 解释了为什么需要在 Ceph 中支持 NVMe over Fabrics，包括行业标准的使用、生态系统的兼容性以及利用 DPUs 等硬件优势。

3. **架构概述：**
   - 展示了从 NVMe initiators 到 Ceph 集群的高层次架构图，介绍了 Ceph NVMe over Fabrics Gateway 组件。
   - 讨论了 Gateway 的部署方式，可以是独立节点或与 OSDs 共存。

4. **技术细节：**
   - 详细介绍了 Gateway 的工作原理，包括使用 SPDK（Storage Performance Development Kit）处理数据路径。
   - 讨论了控制路径的配置，包括使用 gRPC API 进行配置管理和持久化配置。

5. **演示环节：**
   - 展示了如何配置和启动 Ceph NVMe over Fabrics Gateway，并通过实际操作演示了从 NVMe initiator 到 Ceph 集群的数据路径。

6. **未来工作：**
   - 讨论了未来的开发计划，包括 Gateway 组（Gateway groups）、多路径支持（multipathing support）、发现服务（Discovery service）、认证和加密（authentication and encryption）以及 ADNN（Asymmetric Distributed Namespace）支持。
   - 强调了这些功能的重要性，并提到了当前的开发进度和未来的目标。

7. **性能讨论：**
   - 讨论了性能问题，包括使用多个 SPDK 线程处理 RBD 图像以避免性能瓶颈。
   - 提到了当前的性能测试结果，显示了良好的性能表现。

8. **社区互动：**
   - 回答了与会者提出的问题，包括关于 Discovery 服务、WireGuard 支持和 ADNN 的具体问题。

**决定事项：**
- 确定了 Ceph NVMe over Fabrics Gateway 的初步实现和未来开发方向。
- 确认了社区会议的时间和地点，以便进一步讨论和开发。

**后续行动计划：**
- 继续开发和完善 Ceph NVMe over Fabrics Gateway 的功能。
- 进行更多的性能测试和集成测试，以确保稳定性和可靠性。
- 定期召开社区会议，跟进项目进度并解决遇到的问题。

**会议结束：**
- 会议按时结束，感谢所有参与者的贡献和讨论。

**附件：**
- 会议演示文稿和相关链接已上传至 Etherpad。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。