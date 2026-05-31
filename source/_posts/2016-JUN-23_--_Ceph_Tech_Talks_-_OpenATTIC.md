---
title: " 2016-JUN-23 -- Ceph Tech Talks: OpenATTIC "
date: 2016-07-22
updated: 2016-07-23
tags:
- Ceph
- 分布式存储
- RESTful API
- 自动化
categories:
- "视频总结"
subtitle: 2016-JUN-23_--_Ceph_Tech_Talks_-_OpenATTIC
---


### 会议纪要

**会议时间**： 2016年6月23日

**参会人员**： Lens Scrimer（Open Attic），会议主持人

**会议主题**： Open Attic与Ceph的集成

**会议内容**：

* **Open Attic介绍**：
    * Open Attic是一个开源的存储管理平台，旨在简化企业级存储的部署和管理。
    * 支持多种存储协议和文件系统，包括NFS、iSCSI、CIFS和ZFS等。
    * 提供Web界面和RESTful API，方便用户进行管理和自动化。
* **Open Attic与Ceph的集成**：
    * 重点开发Ceph管理功能，以满足用户对大规模存储的需求。
    * 集成工作主要集中在以下几个方面：
        * **Ceph集群管理**： 使用Librados和LibRBD API进行集群管理，包括池、OSD和RBD的管理。
        * **集群健康和性能监控**： 使用Nagios和RRDtool进行监控，并提供图形化的仪表板。
        * **自动化**： 使用Saltstack进行远程节点管理，并支持自动化任务执行。
        * **用户界面**： 开发新的Ceph管理仪表板，提供更直观的用户体验。
* **开发计划**：
    * Open Attic将继续每月发布新版本，并逐步完善Ceph管理功能。
    * 下周，Open Attic团队将与SUSE开发者一起进行Hack Week，专注于Ceph特定功能的开发。
    * 欢迎用户反馈和建议，共同推动Open Attic的发展。

**行动计划**：

* Open Attic团队将继续开发Ceph管理功能，并定期发布新版本。
* 用户可以访问Open Attic官网和GitHub仓库，获取最新信息和代码。
* 用户可以参与Open Attic社区，提供反馈和建议。

**关键词**：

* Open Attic
* Ceph
* 分布式存储
* 存储管理
* RESTful API
* Nagios
* RRDtool
* Saltstack
* Hack Week