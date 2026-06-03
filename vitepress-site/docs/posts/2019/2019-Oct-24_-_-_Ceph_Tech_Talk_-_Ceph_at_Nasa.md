---
title: "2019-Oct-24 :: Ceph Tech Talk - Ceph at NASA"
date: 2019-10-31
updated: 2019-11-01
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议主题**： NASA大气科学数据存储与处理中的Ceph应用

**会议时间**： 2019年10月24日

**参会人员**： NASA大气科学团队成员、数据科学家、工程师等

**会议内容**：

* **NASA大气科学数据存储现状**：
    * NASA大气科学团队负责处理和分析来自多颗卫星的原始数据，包括US-10、NOAA-20、JPSS-2等。
    * 数据量巨大，每年产生约10PB的数据，需要高效的存储和数据处理方案。
    * 目前主要使用Ceph作为数据存储平台，包括Rados、RGW和S3。
    * 使用FusedFS作为POSIX文件系统层，方便科学家访问数据。
    * 使用PostgreSQL数据库跟踪文件元数据，并确保数据完整性。
* **Ceph的使用情况**：
    * NASA团队直接使用Ceph，未使用Ceph Gateway。
    * 使用Python绑定的库Fredo4CEPH进行数据访问。
    * 使用PDS服务器进行数据索引和分块，提高数据处理效率。
    * 使用Kubernetes管理Ceph集群和应用程序。
* **面临的挑战**：
    * 数据量增长迅速，需要更大的存储容量和更高的性能。
    * Ceph集群出现了一些故障，需要改进集群稳定性和可靠性。
    * 需要更好的数据访问方式，例如支持变量级别的数据访问。
* **未来计划**：
    * 考虑迁移到BlueStore后端，提高性能。
    * 研究使用Striper进行数据分块，提高数据访问效率。
    * 使用upmap进行集群升级，提高集群性能和可靠性。
    * 探索使用Geospatial Data Abstraction Library (GDAL)进行数据访问。

**行动计划**：

* 继续使用Ceph作为数据存储平台，并改进集群性能和可靠性。
* 研究使用BlueStore后端和Striper进行数据分块。
* 使用upmap进行集群升级。
* 探索使用GDAL进行数据访问。

**关键词**： NASA、大气科学、Ceph、Rados、RGW、S3、FusedFS、PostgreSQL、BlueStore、Striper、upmap、GDAL