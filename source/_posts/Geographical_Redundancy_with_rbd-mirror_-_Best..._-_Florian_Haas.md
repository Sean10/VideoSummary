---
categories:
- 视频总结
date: 2019-05-24
subtitle: Geographical_Redundancy_with_rbd-mirror_-_Best..._-_Florian_Haas
tags:
- 分布式存储
title: "'Geographical Redundancy with rbd-mirror: Best... - Florian Haas'"
updated: 2019-05-24
---



### 会议纪要

**会议主题**： Ceph RBD镜像功能详解及最佳实践

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Lorien（Ceph研发人员），以及通过Twitter提问的观众

**会议内容**：

**一、RBD镜像功能概述**

* RBD镜像是一种异步复制Radice块设备内容到远程集群的功能，已存在三年。
* 主要用于跨地域数据备份和灾难恢复。
* 与传统同步复制相比，RBD镜像不受网络延迟影响，更适用于长距离复制。

**二、RBD镜像工作原理**

* 应用程序写入数据时，RBD镜像通过RBD层进行异步复制，使用RBD日志记录所有写操作。
* RBD镜像守护进程监控日志更新，并将其应用到远程集群的RBD镜像中。

**三、RBD镜像配置**

* 启用RBD日志记录：使用`rbd feature enable pool/image journal`命令。
* 配置RBD镜像守护进程：创建具有适当权限的身份，配置访问本地和远程集群。
* 连接RBD镜像实例：使用`rbd mirror pool peer add`命令。
* 启动RBD镜像服务：使用systemd或容器管理工具启动RBD镜像守护进程。

**四、RBD镜像模式**

* 单向镜像：数据只能从主集群复制到远程集群。
* 双向镜像：数据可以在主集群和远程集群之间双向复制。

**五、RBD镜像性能**

* RBD镜像对读取性能影响较小。
* 写入性能受影响，特别是在使用相同存储池的情况下。
* 可以通过调整RBD日志记录参数来优化性能。

**六、RBD镜像与云平台集成**

* 可以将RBD镜像与OpenStack集成，实现跨地域数据备份和灾难恢复。
* 需要配置OpenStack集群、RBD镜像、存储网络等，并确保OpenStack元数据也得到复制。

**七、最佳实践**

* 评估RBD日志记录的性能影响。
* 选择合适的RBD镜像模式和存储池。
* 使用自动化工具简化RBD镜像配置和管理。

**后续行动计划**：

* 完善RBD镜像文档。
* 优化RBD镜像性能。
* 推进RBD镜像与其他云平台的集成。

**关键词**： RBD镜像、异步复制、日志记录、性能、OpenStack、灾难恢复