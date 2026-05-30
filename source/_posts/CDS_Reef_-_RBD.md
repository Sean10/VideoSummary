---
categories:
- 视频总结
date: 2022-04-22
subtitle: CDS_Reef_-_RBD
tags:
- Ceph
- RBD
- Distributed Storage
- Storage Cluster
- Scalability
title: "'CDS Reef: RBD'"
updated: 2022-04-23
---




本次会议主要讨论了Ceph RBD（块存储）在CDS Reef版本中的开发计划和改进方向。以下是会议的关键点：

1. **RBD镜像相关问题和改进**：
   - 优化快照和镜像计划，以减少性能影响。
   - 改善rbd mirroring的状态机文档，方便开发者理解。
   - 迁移rbd套件至使用sap area，并实现多集群支持。
   - 在rv mirror代码库中添加状态机图，方便新手理解代码。
   - 处理和解决rbd mirroring的bug，包括错误和边缘情况处理、脑裂条件处理等。

2. **日志记录和监控**：
   - 改进日志配置，使其更易于在Kubernetes环境中配置。
   - 优化日志流，使日志更易于识别和跟踪。
   - 提供一致的图像级别指标，并通过admin socket暴露给性能监控工具。

3. **性能测试和优化**：
   - 扩展RBD镜像的性能测试，支持更多图像数量。
   - 检查和修复多副本镜像中可能存在的问题。

4. **功能增强**：
   - 支持加密克隆，允许使用不同的密码和加密格式。
   - 支持NBD流，改进RBD实时迁移功能。
   - 改进持久性宽背缓存，使用pmem模式。

5. **测试套件改进**：
   - 修复测试不稳定的问题，确保测试套件的稳定性。

6. **容器化和自动化**：
   - 改进容器化部署，优化用户交互体验。
   - 探索将客户端组件运行在容器中的可能性。

7. **NVMe和 fabrics网关**：
   - 开发新的NVMe和 fabrics网关，以替代现有的iSCSI网关。

本次会议明确了CDS Reef版本中RBD开发的主要方向和任务，为后续的开发工作提供了指导。