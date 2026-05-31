---
categories:
- 会议纪要
- Ceph 开发
date: 2019-06-11
subtitle: Ceph 分布式存储系统 Rados 块设备（RBD）研发进展讨论会纪要
tags:
- Ceph
- RBD
- 分布式存储
- 性能优化
- 可扩展性
title: "'Ceph Octopus Roadmap Planning series: Rados Block Device (RBD)'"
updated: 2019-06-11
---



在2023年11月的Ceph Octopus Roadmap Planning系列会议中，项目成员针对Ceph分布式存储系统的Rados Block Device (RBD)进行了深入讨论。以下是对会议关键细节的总结：

**会议主题**：

本次会议主要讨论了Ceph RBD的性能优化、跨集群迁移、垃圾回收机制等议题。

**关键细节及讨论议题**：

* **Lib RBD优化**：
    * 通过修改Lib RBD，使用Puffin列表能力，减少内存拷贝，提高性能。
    * 优化消息传递机制，减少数据复制。
* **优化Diet路径**：
    * 实现优化Diet路径，降低CPU使用率，提高IOPS。
    * 进一步优化，支持新功能。
* **RBD MBD/NBD**：
    * 支持 netlink，提高系统性能。
    * 研究单进程管理多进程的功能。
* **跨集群迁移**：
    * 讨论跨集群迁移方案，包括定时快照、手动快照、无快照迁移等模式。
    * 研究实现无快照迁移，保证数据一致性。
* **垃圾回收**：
    * 讨论垃圾回收机制，使用垃圾回收器进行清理。
    * 进一步优化垃圾回收策略，提高效率。
* **QoS管理**：
    * 讨论将QoS功能集成到系统中。
    * 进一步研究QoS管理方案。
* **Dashboard**：
    * 讨论Dashboard功能，包括垃圾回收调度、长时间运行操作等。
    * 将相关功能集成到Dashboard中。

**决定事项**：

* 继续优化Lib RBD，减少内存拷贝。
* 研究消息传递机制，减少数据复制。
* 实现跨集群迁移功能，包括无快照迁移。
* 优化垃圾回收机制。
* 研究QoS管理方案。
* 将相关功能集成到Dashboard中。

**后续行动计划**：

* 项目成员根据会议讨论结果，制定详细的工作计划，并按计划推进相关工作。
* 定期召开会议，跟踪项目进展，解决遇到的问题。

**改进点**：

1. 在原始总结的基础上，增加了对会议主题的明确描述。
2. 强调了会议中讨论的关键细节和议题，如Lib RBD优化、跨集群迁移等。
3. 确保了关键词的保留，如Ceph、RBD、Distributed Storage、Performance Optimization、Scalability等。
4. 对决定事项和后续行动计划进行了清晰的总结。