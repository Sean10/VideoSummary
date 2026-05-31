---
categories:
- 视频总结
date: 2018-12-20
subtitle: Crimson_Seastar_OSD_Meeting_2018-12-11
tags:
- Ceph
- 分布式存储
- OSD
title: "Crimson/Seastar OSD Meeting 2018-12-11"
updated: 2018-12-20
---




### 会议纪要

**会议时间**： 2018年12月11日

**参会人员**： Michael、Divya、Riddick、Bobby等

**会议主题**： Ceph分布式存储系统OSD服务模型、Promise调度器、Crimson消息传递框架及ZooKeeper集成讨论

**关键细节**：

* **OSD服务模型**： 讨论了OSD服务的模型设计，包括如何管理OSD和对象存储之间的关系，提出了创建一个新的OSD服务类。
* **Promise调度器**： 讨论了Promise调度器的修改，以确保磁盘操作的顺序。
* **Crimson消息传递框架**： 讨论了Crimson消息传递框架的集成和改进，包括日志记录、PID地址问题等。
* **ZooKeeper集成**： 讨论了ZooKeeper集成的工作进展，包括隐私保护和Crimson对象存储实现。

**讨论的主要议题**：

* 如何设计OSD服务模型以更好地管理服务、对象存储和OSD之间的关系。
* 如何修改Promise调度器以确保操作的顺序。
* 如何集成和改进Crimson消息传递框架。
* 如何实现ZooKeeper集成，以提供更好的隐私保护和数据一致性。

**决定的事项**：

* 创建一个新的OSD服务类，用于管理OSD和对象存储。
* 修改Promise调度器以确保操作的顺序。
* 集成和改进Crimson消息传递框架。
* 实现ZooKeeper集成。

**后续行动计划**：

* Michael将负责设计OSD服务模型。
* Divya将负责修改Promise调度器。
* Riddick将负责集成和改进Crimson消息传递框架。
* Bobby将负责实现ZooKeeper集成。
* 所有参与者将参与讨论和审查相关代码。

**其他事项**：

* 会议还讨论了内存管理、缓存策略等技术问题。
* 会议结束后，所有参与者将分享他们的进展和遇到的问题。

**关键词**：

* OSD（对象存储守护进程）
* Promise调度器
* Crimson消息传递框架
* ZooKeeper
* Privacy
* Performance
* Reliability