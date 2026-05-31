---
categories:
- 视频总结
date: 2019-02-02
subtitle: Ceph_Performance_meeting_2019-01-17
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
- 对象存储
- 块存储
- 文件系统存储
- 性能
- BlueStore
- BlueFS
- RocksDB
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- RBD
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 复制
- 快照
- 克隆
- 虚拟化
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 多云
- 存储集群
- SSD
- HDD
- SAN
- NAS
- 网络
- 弹性
- 恢复
- 负载均衡
- 缓存
- 压缩
- 去重
title: "Ceph Performance meeting 2019-01-17"
updated: 2019-02-03
---



### 会议纪要

**会议时间**： 2019年1月17日

**参会人员**： Casey, Mark, Sage, John, Keith, Haeju, Jason, Peter, Orlando, Radek, Linda, Adrian

**会议主题**： Ceph 项目进展、问题讨论及后续行动计划

**关键细节**：

* **Ceph 项目进展**：
    * Mark 提到在 Minneapolis F Meetup 上了解到 RGW 多站点存在分布式复制问题，数据未能正确复制，可能是静默失败。
    * Sage 提到最近进行了核心会议，讨论了异步和 RGW 的工作，希望 Nautilus 版本能成为默认选项。
    * Haeju 开发了一个新命令，可以轻松显示每个 OSD 的存储和网络 Numa 节点，并可以轻松固定。
    * Jason 正在重新审查代码，以优化缓存和线程。
    * Sage 提到已将 Cass 开源，并可以将其用于 Ceph。
    * Adrian 提到正在尝试重新编写 Blue Store，以支持更多存储设备。
* **问题讨论**：
    * Mark 询问 Sage 是否已合并新的 Numa 节点命令。
    * Sage 回答已合并，并提到该命令可以帮助优化参考架构。
    * Radek 提到正在尝试获取 Bdev 驱动程序，以支持 NVMe。
    * Orlando 提到正在尝试获取 Quanta 系统的报价，以获取平衡的 NVMe 系统。
    * Linda 提到正在尝试解决网络配置问题，以确保数据包正确路由。
    * Adrian 提到正在尝试获取 Quanta 系统的报价，以获取平衡的 NVMe 系统。
* **后续行动计划**：
    * Sage 将继续关注 RGW 多站点问题。
    * Haeju 将继续优化缓存和线程。
    * Jason 将继续审查代码。
    * Sage 将尝试将 Cass 开源。
    * Adrian 将尝试重新编写 Blue Store。
    * Orlando 将尝试获取 Quanta 系统的报价。
    * Linda 将尝试解决网络配置问题。

**计算机科学/ceph相关领域英文原文关键词**：

* RGW multi-site
* distributed replication
* OMAP
* asynchrony
* rgw
* Nautilus
* OSD
* Numa
* NVMe
* Bdev
* Cass
* reference architecture
* network configuration

**总结**：

本次会议讨论了 Ceph 项目的最新进展、存在的问题以及后续行动计划。参会人员就 RGW 多站点问题、异步和 RGW 的工作、Blue Store 优化等问题进行了深入讨论，并制定了相应的解决方案。会议特别强调了 Numa 节点优化、NVMe 支持和网络配置问题的重要性。