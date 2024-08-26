---
title: "Rook: Enabling Read Affinity for RBD Workloads - Rakshith R, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：
启用RBD工作负载的读取亲和性（Read Affinity）

#### 参会人员：
- **Rakshit**（曾在Red Hat工作，现就职于IBM）

#### 会议议程：
1. **CRUSH算法和CRUSH Maps简介**
2. **OSD拓扑结构**
3. **OSD拓扑与CRUSH位置的相互关系**
4. **客户端读取流程**
5. **读取亲和性的优缺点**
6. **如何在内部和外部集群中启用读取亲和性**

#### 讨论内容：
- **CRUSH算法**：CRUSH算法是Ceph的核心，用于确定数据存储的位置。客户端写入数据时，对象ID通过CRUSH算法映射到PG（Placement Group），再映射到一组OSD，其中一个为主OSD。
- **OSD拓扑结构**：Rook利用Kubernetes的节点标签来实现OSD的拓扑分布，确保数据在不同故障域中的复制。
- **客户端读取流程**：默认情况下，客户端读取数据从主OSD进行。为了提高读取速度，可以通过CSI（Container Storage Interface）将客户端位置信息传递给CRUSH算法，从而允许客户端从最近的次级OSD读取数据。
- **读取亲和性的优缺点**：
  - **优点**：显著提高读取速度，降低延迟，减少跨区域流量，特别适用于云环境。
  - **缺点**：可能导致多个OSD同时服务于同一数据的读取，增加CPU和内存使用。

#### 决定事项：
- **启用读取亲和性**：在Rook部署的内部集群中，通过设置CSI配置项启用读取亲和性。对于外部集群，需要确保节点标签与外部集群的CRUSH Maps匹配。

#### 后续行动计划：
- **内部集群**：在配置文件中设置`CSI_ENABLE_READ_AFFINITY`为`true`，并重启已运行的RBD Pods。
- **外部集群**：确保节点标签与外部集群的CRUSH Maps匹配，并执行相同的配置更改。

#### 参考资料：
- Rook GitHub链接
- Ceph CSI驱动链接

#### 会议结束：
会议在讨论和解答疑问后结束，无其他待办事项。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。