---
title: Architecting Cloud Storage for AI Native Applications - Nathan Goulding, Vultr
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 分布式存储
categories: 
- "视频总结"
subtitle: Architecting_Cloud_Storage_for_AI_Native_Applications_-_Nathan_Goulding_Vultr
---

在本次会议中，Nathan Goulding，Vulture的高级副总裁，深入探讨了Vulture云架构与Ceph存储在AI应用中的应用。以下是会议的关键要点：

1. **Vulture公司简介**：Vulture是全球最大的独立云服务提供商，拥有超过22年的运营历史和遍布全球的32个数据中心，提供低延迟服务，覆盖全球90%的人口。

2. **云基础设施的演进**：从传统的云基础设施到云原生部署，包括微服务、不可变基础设施和基础设施即代码，以及AI原生应用的兴起。

3. **Vulture的云架构**：
   - **云原生应用架构**：支持裸金属、虚拟机、Kubernetes等多种部署方式，通过CI/CD管道部署应用和模型。
   - **AI原生应用架构**：通过微调模型后部署到目标区域，支持低延迟推理和数据治理。

4. **存储解决方案**：
   - **对象存储**：提供S3兼容API，适合对象存储。
   - **块存储**：支持HDD、SSD、NVMe，提供灵活的块存储解决方案。
   - **文件系统存储**：基于Ceph（RADOS）实现，支持多实例同时读写，适合AI工作负载。
   - **Ceph集成**：Vulture使用Ceph作为底层存储技术，已部署超过60PB的Ceph存储。

5. **高性能存储与网络**：与AMD合作，部署AMD MI 300X GPU集群，存储性能要求高达50GB/s每GPU，支持InfiniBand和RoCE网络，确保高带宽和低延迟的存储访问。

6. **未来展望与行动计划**：
   - 继续优化存储架构，支持AI原生应用的快速发展。
   - 提供更多高性能存储选项，满足AI训练和推理的严苛需求。
   - 开放更多API和服务，简化用户对云基础设施的访问和使用。

本次会议强调了Ceph在AI原生应用中的重要性和Vulture在云存储领域的领先技术，通过高性能存储和网络解决方案，Vulture为AI训练和推理提供了强大的支持。