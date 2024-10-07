---
title: "Ceph Days NYC 2023: Data Security and Storage Hardening in Rook and Ceph"
date: 2023-05-17
updated: 2023-05-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了分布式存储系统Ceph的安全性问题，包括安全实践、威胁模型、加密实现以及产品安全管理等方面。会议由Federico Lucifredi和Sage McTaggart主讲，他们在Ceph和网络安全领域有深入的研究和实践经验。

#### 主要议题
1. **安全实践与威胁模型**
   - 强调了安全实践的重要性，特别是针对特定基础设施点的加固。
   - 讨论了在没有攻击者模型的情况下，单纯选择安全实践的不可行性。
   - 提出了绝对安全的不现实性，强调了定义威胁模型的重要性。

2. **网络安全区划分**
   - 介绍了四种网络安全区的划分：公共安全区、自客户端区、存储访问区和集群区。
   - 讨论了各区域的安全需求和如何通过加密等手段保护数据传输。

3. **产品安全管理**
   - 介绍了IBM的产品安全管理流程，包括安全开发生命周期、定期渗透测试、依赖项清单管理等。
   - 强调了即使在IBM，Ceph的安全修复也会被回溯到上游，确保所有版本的Ceph都保持同等安全。

4. **加密实现**
   - 讨论了服务器端和传输中的数据加密，特别是使用LUKS和Ceph协议的安全性。
   - 介绍了对象存储网关的额外加密能力，包括用户密钥管理和AWS SSE-KMS支持。

5. **身份与访问管理**
   - 讨论了使用共享密钥和AES加密的安全性，以及如何通过良好的实践来管理密钥和用户权限。

6. **审计与数据保留**
   - 讨论了审计日志的重要性，以及如何在数据删除后确保数据不可恢复。
   - 介绍了RBD的垃圾箱功能和rgw的版本控制功能，以及如何通过加密来实现安全删除。

#### 决定事项
- 继续加强Ceph的安全性，特别是在IBM的新环境下，确保所有安全实践和流程都符合IBM的标准。
- 持续关注和改进Ceph的加密实现，特别是在数据传输和存储方面。

#### 后续行动计划
- 继续进行定期的渗透测试和安全审查，确保Ceph的安全性。
- 与IBM的安全团队合作，进一步完善和扩展Ceph的安全流程。
- 持续关注和改进Ceph的身份和访问管理，确保用户数据的安全。

#### 备注
- 会议中提到的所有安全实践和建议都旨在提高Ceph的安全性，特别是在面对不同威胁模型时。
- 会议还提到了一些外部资源，如Kubernetes Secrets管理、存储安全硬化指南等，供进一步阅读和参考。

本次会议为Ceph的安全性提供了一个全面的视角，并为未来的安全改进工作指明了方向。