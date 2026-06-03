---
title: "2015-MAR-26 -- Ceph Tech Talks: RGW"
date: 2015-03-30
updated: 2015-03-30
tags:
  - "Ceph"
  - "RGW"
  - "分布式存储"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议主题**： Ceph Rados Gateway（RGW）架构与工作原理

**参会人员**： Yehuda（技术负责人）、Patrick（主持人）、Eric、Lucas、Derek、Tyler、Abhishek 等

**会议内容**：

* **Ceph 架构概述**： Ceph 是一个可扩展的分布式存储系统，核心包括对象存储（Rados）、块存储（RBD）和文件系统（CephFS）。RGW 作为 Ceph 的对象存储网关，提供 S3 和 Swift 兼容接口。
* **RGW 工作原理**：
    * RGW 利用 Librados 接口与 Ceph 存储集群通信，通过多个进程处理 S3 或 Swift 请求。
    * RGW 支持多种前端，包括 FastCGI 服务器和 CivetWeb 内置服务器。
    * RGW 内部模块包括：前端、RESTful API、执行层、数据管理、用户管理、认证、垃圾回收等。
    * RGW 对象存储与传统对象存储在对象大小、可变性、索引等方面有所不同。
    * RGW 使用对象类（Object Class）扩展功能，例如桶索引维护、使用情况记录、垃圾回收、建议锁定等。
    * RGW 支持多区域配置，包括主区域、副本区域和灾难恢复区域。
    * RGW 支持数据同步、元数据同步和用户管理。
* **未来工作计划**：
    * 多区域配置的主动架构
    * 多租户支持
    * 对象过期功能
    * 通过 NFS 导出 RGW 对象
    * 探索其他功能，例如元数据缓存、对象类扩展等。

**讨论要点**：

* CivetWeb 服务器是否可用于生产环境：CivetWeb 服务器已准备好用于生产，性能和稳定性良好。
* 不同版本的 RGW 和 Ceph 是否兼容：完全解耦于 Librados，理论上应兼容不同版本的 Ceph，但建议使用相同版本以获得最佳性能。
* RGW 实例数量限制：RGW 实例数量过多可能导致性能问题，建议根据实际情况进行调整。
* 列出非所有者桶的功能：目前 S3 接口不支持此功能，但可以通过管理员元数据 API 列出所有桶。
* 上传对象时生成 MD5 校验和：目前没有计划实现此功能，但可以使用提供的 ETag 作为校验和。
* 将 RGW 作为 OpenStack Swift 的替代方案：RGW 可以作为 OpenStack Swift 的替代方案，但可能存在一些功能差异。

**行动计划**：

* Yehuda 将继续完善 RGW 的功能和性能。
* 社区成员将参与测试和反馈，推动 RGW 的发展。
* 下一期技术研讨会将于 4 月 23 日举办，主题为 Calamari。