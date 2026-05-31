---
title: Ceph Operations at Scale. Alex Marangone from DigitalOcean
date: 2025-05-08
updated: 2025-05-09
tags: 
- Ceph
- 分布式存储
- 自动化
- 容器化
- 云计算
categories: 
- "视频总结"
subtitle: Ceph_Operations_at_Scale._Alex_Marangone_from_DigitalOcean
---

Ceph 运维规模化实践分享会议中，Alex Marangone，DigitalOcean 存储系统团队成员，详细介绍了公司在 Ceph 运维方面的经验和实践。以下是对会议内容的总结：

### 会议概述

Alex 分享了 DigitalOcean 如何通过自动化、创新解决方案和高效的运维策略来管理其庞大的 Ceph 集群。DigitalOcean 拥有近 70 个 Ceph 集群，超过 250PB 的原始数据，30,000 多个 OSD，分布在全球 1,700 多个节点上，由一个仅五人的团队管理。

### 主要议题

1. **自动化与效率**：DigitalOcean 强调自动化在提高运维效率、减少人为错误和确保操作安全性和一致性方面的重要性。

2. **容器化应用**：容器化帮助 DigitalOcean 解决了早期 Ceph 集群的稳定性问题，通过容器化实现了 OS 与 Ceph 版本的解耦，简化了升级过程。

3. **自定义部署工具**：DigitalOcean 使用自定义的部署工具，而非上游的 Ceph 部署工具，以提高效率和适应性。

4. **操作安全性与自动化**：DigitalOcean 使用 RADOS 锁机制来协调操作，确保同一时间只有一个操作可以修改集群状态。

5. **OSD 生命周期管理**：DigitalOcean 开发了内部工具 Forman Storage Manager，用于管理 OSD 的整个生命周期，包括驱动器的更换、重新部署和健康检查。

6. **社区参与与贡献**：DigitalOcean 加入 Ceph 基金会，并计划开源一些内部工具，如 Ceph 的 exporter 和 OSD 级别的监控工具。

### 决定事项

1. 继续推进自动化和容器化，以提高运维效率和稳定性。
2. 开源内部工具，如 OSD 生命周期管理工具和监控 exporter。
3. 积极参与 Ceph 社区项目，特别是在容器化、自动化和 Crimson 测试方面。

### 后续行动计划

1. 优化自动化流程，减少人为干预。
2. 开源内部工具，并准备相关文档。
3. 积极参与 Ceph 社区，贡献资源和知识。

### 会议总结

本次会议详细介绍了 DigitalOcean 在 Ceph 运维方面的创新实践，为其他 Ceph 用户提供了宝贵的参考，尤其是在如何通过自动化和创新解决方案来应对大规模集群管理的挑战方面。此外，DigitalOcean 还表达了增加对 Ceph 社区贡献的意愿，并计划开源一些内部工具，推动 Ceph 生态的发展。