---
categories:
- 视频总结
date: 2015-08-03
subtitle: CDS_Jewel_--_RADOS_QoS
tags:
- Ceph
- 分布式存储
- RADOS
title: "CDS Jewel -- RADOS QoS"
updated: 2015-08-04
---




### 会议纪要

**会议主题**： Ceph分布式存储服务质量（QoS）策略讨论

**会议时间**： 2023年11月

**参会人员**： Ray、Clark、Sam、Josh等

**会议内容**：

**一、QoS策略概述**

*   会议讨论了Ceph分布式存储中的服务质量（QoS）策略，旨在为不同类型的存储请求提供差异化的服务质量。
*   当前Ceph的I/O调度器采用公平共享调度器，但需要进一步优化以支持QoS策略。

**二、QoS策略实现方案**

*   **基于EM算法的I/O调度器优化**：
    *   引入EM算法，为客户端提供最小IOPS和最大IOPS的配置选项。
    *   当客户端的IOPS请求超过最大限制时，系统将进行限制。
    *   当最小IOPS得到保证时，超出部分将按照公平共享原则进行分配。
*   **资源预留与容量控制**：
    *   引入资源预留机制，以确保高优先级客户端的IOPS需求得到满足。
    *   通过配置选项或管理工具设置资源预留策略。
*   **性能自动检测**：
    *   引入性能自动检测机制，实时评估存储集群的性能。
    *   通过辅助工具或自研代码进行性能测试。

**三、相关讨论**

*   **网络QoS**：
    *   讨论了网络QoS对存储系统的影响，并探讨了如何将网络QoS与存储QoS相结合。
*   **OSD性能自动检测**：
    *   讨论了如何自动检测OSD的性能，并提出了基于OSD操作性能进行检测的方案。
*   **客户端信任度**：
    *   讨论了如何处理不信任的客户端，并提出了限制IOPS或拒绝QoS配置的方案。

**四、后续行动计划**

*   Ray将继续开发基于EM算法的I/O调度器优化方案。
*   Sam将研究性能自动检测机制。
*   Clark将探讨网络QoS与存储QoS的结合方案。
*   全体成员将继续讨论客户端信任度问题。

**五、关键术语**

*   **QoS**： 服务质量
*   **I/O调度器**： Input/Output scheduler
*   **EM算法**： Expectation-Maximization algorithm
*   **OSD**： Object Storage Device
*   **PG**： Placement Group
*   **RBD**： RADOS Block Device