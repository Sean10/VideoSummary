---
title: "Kubernetes Stateful Application Disaster Recovery with Zero Data Loss - Daniel Parkes, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Kubernetes中状态应用的同步复制策略

#### 主讲人：Daniel Parks（IBM产品管理团队）

#### 会议内容总结：

1. **背景介绍**：
   - Daniel Parks介绍了在Kubernetes中运行关键应用的需求日益增长，这些应用需要持久化数据，因此对数据复制（DR）的需求也在增加。
   - 讨论了不同类型的数据复制选项，包括备份与恢复、异步复制和同步复制（Metro DR）。

2. **备份与恢复**：
   - 使用Velero API进行备份和恢复，适用于逻辑故障的覆盖，但RPO（恢复点目标）和RTO（恢复时间目标）容忍度较高。

3. **异步复制（Regional DR）**：
   - 使用Open Cluster Manager进行应用的故障转移和恢复，RPO在几分钟范围内，RTO依赖于应用启动时间等因素。

4. **同步复制（Metro DR）**：
   - 提供了零数据丢失的同步复制解决方案，主要依赖于Ceph的stretch模式。
   - 使用Rook在Kubernetes集群中部署Ceph，并通过RBD镜像进行块卷的同步复制。
   - 需要低延迟（约10毫秒）以保证性能，适用于非常关键的应用。

5. **Ceph Stretch模式**：
   - 讨论了Ceph在stretch模式下的部署细节，包括使用Arbiter节点作为仲裁者，确保在网络分区情况下仍能维持高可用性。
   - 强调了在这种模式下，Ceph集群的自动调整和恢复机制。

6. **应用故障转移演示**：
   - 展示了如何在Open Cluster Manager中进行应用的故障转移和恢复，确保RPO为零，没有数据丢失。

#### 决定事项：
- 确认了同步复制（Metro DR）作为关键应用的高可用性解决方案。
- 讨论了Ceph在stretch模式下的部署和操作细节。

#### 后续行动计划：
- 继续优化和测试同步复制解决方案，确保其在实际应用中的稳定性和性能。
- 探索更多自动化选项，以减少手动操作在故障转移过程中的需求。
- 提供更多文档和资源，帮助用户理解和部署这些高可用性解决方案。

#### 其他讨论点：
- 讨论了CFS（Ceph File System）在同步复制中的应用潜力和可能的改进。
- 确认了所有演示和讨论的组件均为开源项目，鼓励社区参与和贡献。

#### 会议结束：
- 会议在感谢和掌声中结束，Daniel Parks鼓励大家如果有任何问题或需要进一步的信息，可以随时联系。