---
title: "  CDS Infernalis (Day 2.2) -- OSD: Transactions  "
date: 2015-03-07
updated: 2015-03-07
tags:
- Ceph
- 分布式存储
categories:
- "视频总结"
subtitle: CDS_Infernalis_Day_2.2_--_OSD_-_Transactions
---



### 会议纪要

**会议主题**： Ceph Rados Gateway的Hadoop文件接口设计与讨论

**参会人员**： SE Patrick，其他相关研发人员

**会议内容**：

**1. 背景介绍**

* 项目旨在为Hadoop提供基于CephFS的参考解决方案，基于Stack Sahara项目，该项目基于Swift和UFS。
* 由于存储服务器与Hadoop集群位于隔离网络，无法使用Hadoop与CephFS插件，因此采用SEF Ros Gateway作为连接器。
* 利用Caching Tier技术，在Rados Skateway服务器中使用SSD缓存数据。

**2. 解决方案概述**

* 方案包含四个组件：Rgw FS、RW Proxy、RW Cluster和Caching Tier。
* Rgw FS作为Hadoop插件，使Hadoop可以与Rados Skateway目录通信。
* RW Proxy负责获取数据块位置，类似于HDFS的NameNode。
* RW Cluster使用Caching Tier技术，将数据缓存到SSD中。

**3. 关键技术讨论**

* **RW Proxy**：
    * 负责获取数据块位置，需要理解Ceph对象到Ceph对象的映射关系。
    * 需要监控RW实例，以便进行故障转移。
    * 可以通过增加Gateway管理RESTful命令来实现。
* **Caching Tier**：
    * 使用SSD缓存数据，提高读取性能。
    * 需要配置专门的chunk size和RW Max chunk size。
* **数据读取流程**：
    * Hadoop作业通过RW FS读取数据。
    * RW Proxy根据数据位置选择最接近的RW实例。
    * RW实例从Caching Tier读取数据。
* **数据写入流程**：
    * Hadoop作业通过RW Proxy写入数据。
    * RW Proxy将数据写入Caching Tier。
    * RW实例将数据写入Ceph集群。

**4. 讨论与决定**

* **RW Proxy**：
    * 可以通过增加Gateway管理RESTful命令来实现故障转移。
    * 可以使用多个副本来提高读取性能。
* **Caching Tier**：
    * 需要配置专门的chunk size和RW Max chunk size。
* **数据写入**：
    * Hadoop作业写入数据时，不会覆盖现有对象，需要配置新的对象名称。

**5. 后续行动计划**

* 完成RW Proxy和Caching Tier的实现。
* 对RW FS进行优化，减少对头对象的读取。
* 将解决方案集成到Stack Sahara项目中。

**6. 其他讨论**

* 讨论了使用Hadoop直接访问CephFS的性能问题。
* 认为在RW和Swift之间引入中间件可以提高性能。

**总结**：

本次会议讨论了Ceph Rados Gateway的Hadoop文件接口设计方案，并确定了后续的行动计划。该方案旨在提高Hadoop在Ceph存储系统上的性能和可靠性。