---
categories:
- 视频总结
date: 2022-06-27
subtitle: Ceph_Orchestrator_Meeting_2022-06-21
tags:
- Ceph
- Distributed Storage
- GANESHA
- NFS
- Failover
title: "Ceph Orchestrator Meeting 2022-06-21"
updated: 2022-06-28
---




在2022年6月21日的Ceph Orchestrator会议中，与会者讨论了NFS和GANESHA集群的故障转移、部署和管理问题，以及CEPH和Rook项目间的集成。以下是会议的主要内容和决策：

1. **GANESHA集群的故障转移**：讨论了GANESHA集群在节点故障时可能无法运作的问题，并提出了使用ZAPFIMO实现自动故障转移的解决方案。

2. **NFS服务和客户端配置**：探讨了NFS服务和客户端配置在同一主机上的位置问题，以及该问题对最佳实践的影响。

3. **CEPH与Rook项目的集成**：讨论了Cepheiu与Rook项目未来集成方向，包括更新后的提案和测试计划。

4. **GANESHA和NFS协议理解**：深入理解GANESHA和NFS协议，探讨它们在实际环境中的行为和预期。

5. **节点故障后的NFS操作处理**：针对特定技术问题进行进一步调查，例如节点故障后如何处理已打开的NFS操作。

6. **现有解决方案评估**：评估现有解决方案，并寻找改进方法以增强系统的稳定性和可用性。

会议还讨论了以下技术细节：

- GANESHA集群配置和部署
- Ceph Manager状态存储和获取存储功能
- Keppler d配置变更
- Ingress Spec的额外设置
- Ganesha和Ingress Demon之间的连接
- 非本地绑定和虚拟IP的部署

后续行动计划包括：

- 对GANESHA和NFS协议的深入测试和验证
- 实施Ceph与Rook项目的集成
- 优化NFS服务和客户端配置
- 评估并实施故障转移解决方案