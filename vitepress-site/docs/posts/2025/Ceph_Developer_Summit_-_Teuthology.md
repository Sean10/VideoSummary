---
title: "Ceph Developer Summit - Teuthology"
date: 2025-09-11
updated: 2025-09-11
tags:
  - "Ceph"
  - "Teuthology"
  - "OpenStack"
  - "性能优化"
categories:
  - "存储技术"
  - "Ceph 概述"
outline: deep
---
本次Ceph Developer Summit会议集中讨论了Ceph分布式存储相关工具链的未来发展，包括Toology、DevStack、OpenStack集成和性能优化等关键议题。

**会议主要议题及讨论内容**：

1. **Toology在VM环境中的应用**：Valerie介绍了在IBM Cloud VMs上成功部署Ceph集群的经验，并计划定期在VM上运行Toology测试，以识别潜在改进点。

2. **Ceph DevStack工具开发**：Parfait分享了使用Podman容器化DevStack的进展，简化本地Ceph集成测试，并计划支持动态调整存储设备大小，直接使用主机空闲设备。

3. **OpenStack集成与维护**：讨论了OpenStack后端修复和用于补充上游监控的Deep Chika维护工作，以及探索OpenShift虚拟化支持的潜在方向。

4. **性能优化：日志压缩**：Junior介绍了日志压缩性能优化工作，提出使用`zstd-mt`算法，比`gzip`快36%，压缩率优23%。

5. **代码抽象化与架构改进**：John Mulligan提出了通过抽象化提升代码可维护性的目标，并展示了封装Job Queue的示例。

6. **新基础设施：Metal-as-a-Service (MaaS)**：讨论了IBM新实验室采用Canonical的MaaS管理裸机，并计划实现Toology的MaaS后端。

7. **工具链迁移：UV替代传统Python工具**：讨论了使用UV工具替代传统Python工具的优势和状态。

**决定的事项及后续行动计划**：

1. **VM测试**：Valerie将牵头定期运行Toology测试，并反馈问题。

2. **DevStack CI**：推进非强制PR检查，监控回归问题。

3. **OpenStack**：Deep Chika维护后端，探索`sepsible`集成。

4. **日志压缩**：Junior提交`zstd-mt`替换代码。

5. **MaaS集成**：Kier协助测试，社区协调资源访问。

6. **代码抽象**：John继续优化PR，细化模块设计。

本次会议对Ceph分布式存储工具链的未来发展具有重要意义，为参与者提供了宝贵的交流和合作机会。