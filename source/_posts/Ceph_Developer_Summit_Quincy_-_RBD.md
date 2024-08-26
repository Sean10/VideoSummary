---
title: "Ceph Developer Summit Quincy: RBD"
date: 2021-04-12
updated: 2021-04-13
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph Dashboard、NVMe over Fabrics、RBD Mirroring Monitoring、Volume Groups on Snap Mirroring、Prometheus Scale Out、Image Encryption

#### 会议时间：[具体日期]

#### 参会人员：Jeff, Ernesto, Ilias, Michael, Danny, Orr, 以及其他相关人员

#### 会议内容总结：

1. **Ceph Dashboard 演示**
   - Ernesto 展示了 Ceph Dashboard 的功能，重点介绍了 RBD 镜像和 RBD 镜像功能。
   - 演示了如何在 Dashboard 中创建 RBD 镜像、启用日志记录、设置条带化选项和 QoS 选项。
   - 讨论了 RBD 镜像的配置和操作，包括镜像保护和克隆。
   - 提到了命名空间支持和对旧版本 RBD 镜像的兼容性。

2. **NVMe over Fabrics 状态和下一步计划**
   - 讨论了 NVMe over Fabrics 的工作进展，包括设置网关和使用 SPDK。
   - 提到了需要实现发现服务，以便在集群中找到目标和命名空间。
   - 预计未来几个月会有更多工作进展。

3. **RBD Mirroring Monitoring**
   - Ilias 介绍了 RBD 镜像监控的目标，包括改进和统一不同镜像解决方案的指标。
   - 讨论了 Prometheus 指标的暴露和收集，以及如何解决管理器过载的问题。
   - 提到了需要实现每个镜像守护进程的独立 Prometheus 端点。

4. **Volume Groups on Snap Mirroring**
   - Michael 讨论了在快照镜像中使用卷组的可能性，以便创建一致性快照组进行镜像。
   - 提到了现有的快照镜像功能和未来的扩展计划。

5. **Prometheus Scale Out**
   - 讨论了 Prometheus 的扩展问题，特别是在 Kubernetes 环境中直接从客户端收集指标的可行性。
   - 提到了需要避免管理器过载，并考虑客户端直接发送指标到 Prometheus 的方案。

6. **Image Encryption**
   - Danny 和 Orr 介绍了在 librbd 中添加加密功能的工作，特别是基于 Lux 格式的加密。
   - 讨论了加密功能的性能优势和未来的改进方向，包括支持不同密钥的克隆功能。

#### 决定事项：
- 继续推进 Ceph Dashboard 的功能完善，特别是 RBD 镜像和监控部分。
- 持续关注 NVMe over Fabrics 的工作进展，并计划实现发现服务。
- 改进 RBD 镜像监控，实现每个镜像守护进程的独立 Prometheus 端点。
- 探索在快照镜像中使用卷组的可能性，并考虑 Kubernetes 集成。
- 解决 Prometheus 扩展问题，特别是在 Kubernetes 环境中的指标收集。
- 完成图像加密功能的代码审查和测试，特别是支持不同密钥的克隆功能。

#### 后续行动计划：
- 继续完善 Ceph Dashboard 的功能，特别是 RBD 镜像和监控部分。
- 推进 NVMe over Fabrics 的工作，实现发现服务和其他必要的增强功能。
- 实现 RBD 镜像监控的改进，特别是每个镜像守护进程的独立 Prometheus 端点。
- 探索在快照镜像中使用卷组的可能性，并考虑 Kubernetes 集成。
- 解决 Prometheus 扩展问题，特别是在 Kubernetes 环境中的指标收集。
- 完成图像加密功能的代码审查和测试，特别是支持不同密钥的克隆功能。

#### 会议结束：
- 会议在讨论完所有议题后结束，参会人员感谢彼此的参与，并期待明天的会议。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。