---
categories:
- 视频总结
date: 2018-02-14
subtitle: Ceph_Day_Germany_-_Ceph_for_Big_Science
tags:
- Ceph
- 分布式存储
- 高可用性
- 可扩展性
title: "Ceph Day Germany - Ceph for Big Science"
updated: 2018-02-15
---




### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**与会人员**： CERN存储团队，Ceph社区开发者

**会议主题**： CERN在Ceph存储上的使用经验及反馈

**会议内容**：

**一、CERN存储架构概述**

* CERN拥有两个数据中心，分别位于瑞士和布达佩斯，使用Ceph存储系统进行数据存储，包括文件存储、块存储和对象存储。
* 当前运行着两个生产集群，其中最大的集群容量为5.5PB，另一个数据中心容量为0.5PB。
* CERN使用Ceph进行物理实验数据存储、物理分析、S3存储和HPC模拟数据存储。

**二、Ceph存储应用案例**

* **物理实验数据存储**： 使用Ceph存储CMS、ALICE、ATLAS和LHCb等实验数据，每年存储约50PB数据。
* **物理分析**： 使用Ceph存储分析批处理目标数据，并使用Ceph作为虚拟化NFS文件系统。
* **S3存储**： 使用Ceph作为S3存储后端，提供S3服务。
* **HPC**： 使用Ceph存储HPC模拟数据，并使用Ceph作为NFS文件系统。

**三、Ceph存储使用经验及反馈**

* **Ceph性能**： Ceph在I/O吞吐量方面表现良好，但在元数据性能方面存在一些问题。
* **Ceph稳定性**： Ceph在Luminous版本中表现出良好的稳定性，但需要进一步优化。
* **Ceph可扩展性**： Ceph的可扩展性较好，但需要改进某些功能，例如替换OSD。
* **Ceph管理**： Ceph的管理较为复杂，需要进一步简化。
* **Ceph工具**： Ceph提供的工具需要改进，例如osdmap工具和scrub工具。

**四、后续行动计划**

* 与Ceph社区合作，改进Ceph的元数据性能和可扩展性。
* 开发Ceph管理工具，简化Ceph的管理。
* 开发Ceph存储的备份工具。
* 探索Ceph在更多场景下的应用。

**五、会议总结**

CERN在Ceph存储上的使用经验表明，Ceph是一个功能强大且可扩展的存储系统，但在某些方面仍需改进。CERN将与Ceph社区合作，共同推动Ceph的发展。