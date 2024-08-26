---
title: "External Rook Ceph Cluster - Parth Arora & Subham Rai, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议参与者
- **Parth** 和 **Shubham**，IBM 存储部门的研发人员，主要负责 Rook operator 的开发。

#### 会议主题
- 讨论外部 Ceph 集群（external Ceph cluster）的需求、使用场景、实现方式以及未来的工作计划。

#### 主要讨论内容
1. **外部 Ceph 集群的需求和使用场景**
   - **需求背景**：在 Kubernetes 集群中运行存储服务，但可能存在已经运行的外部 Ceph 集群，需要将其集成到 Kubernetes 环境中。
   - **使用场景**：
     - 大型组织可能需要多个 Kubernetes 集群，通过单一的外部 Ceph 集群来管理这些集群的存储需求。
     - 已经拥有 Ceph 集群，希望将其集成到 Kubernetes 环境中以实现自动化管理。
     - 需要实现存储的完全隔离。

2. **外部 Ceph 集群的实现方式**
   - **架构描述**：通过 Rook operator 在外部模式下运行，并结合 CSI 层，从外部 Ceph 集群获取信息并提供给 Kubernetes 集群。
   - **安装和配置**：
     - 使用 Python 脚本从外部 Ceph 集群获取详细信息。
     - 通过导入 JSON 输出，创建 Kubernetes 资源如 Secrets、ConfigMaps 和 StorageClasses。
     - 部署 Rook operator 并配置外部 Ceph 集群的连接。

3. **验证和监控**
   - **验证连接**：通过检查集群的健康状态和连接状态来验证配置是否成功。
   - **监控**：通过不同的 OpenShift 集群（OCP）的仪表盘来监控不同外部 Ceph 集群的使用情况。

4. **未来工作计划**
   - **功能增强**：支持 RADOS 命名空间、卷组和 IPv6 端点。
   - **文档改进**：提供更清晰的文档，以便用户更容易连接和使用外部 Ceph 集群。

#### 决定事项
- 确认了外部 Ceph 集群的实现方式和使用场景。
- 确定了未来工作的重点，包括功能增强和文档改进。

#### 后续行动计划
- 继续开发和测试外部 Ceph 集群的功能。
- 更新和改进相关文档，确保用户能够顺利使用外部 Ceph 集群。
- 监控和收集用户反馈，以便进一步优化和扩展功能。

#### 会议结束
- 感谢与会者的参与和提问。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。