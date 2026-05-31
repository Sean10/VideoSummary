---
categories:
- 视频总结
date: 2015-08-04
subtitle: CDS_Jewel_--_Hadoop_over_Ceph_RGW
tags:
- Ceph
- RGW
- 分布式存储
- 测试
title: "CDS Jewel -- Hadoop over Ceph RGW"
updated: 2015-08-04
---



会议纪要：

**会议主题**： Hadoop over Ceph RGW 状态更新

**会议时间**： 未提及

**参会人员**： Patrick、Yawn、Jen、Earning（远程）

**会议内容**：

**1. Hadoop over Ceph RGW 设计回顾**

- 该方案包括三个主要组件：Rgw Skidaway FS（Hadoop 兼容文件系统插件）、Rgw Skidaway Web Proxy（基于 Restful 服务的代理）、Rgw Skidaway with SSD Cache（使用 SSD 缓存的后端存储）。
- 设计流程：调度器请求数据位置，Rgw Skidaway Web Proxy 返回最近的数据节点，调度器在数据节点附近的服务器上分配任务，任务尝试从最近的数据节点访问数据。

**2. 自 Infiniscale 以来更新**

- **Rgw Skidaway Web Proxy**：已完成基于 Pass whiskey 模块的演示，可以通过 Restful 请求获取数据位置。
- **Rgw Skidaway File System**：已完成 70% 的代码开发，实现了与多个 Rgw Skidaway 实例的通信，并添加了块级位置信息，提高了读取性能。
- **性能测试**：与 HDFS 和 Swift 进行了基准性能测试，Swift 读取性能比 HDFS 低约 20%。

**3. Rgw Skidaway File System 详细更新**

- 新的文件系统 URL 将以 GW 前缀开头，可以使用该协议让 Hadoop 访问 Rgw Skidaway 集群。
- 已添加块级概念，基于块级位置信息提高读取性能。
- 存在问题：对于大于 5GB 的对象，存在零字节清单文件和大量小块，需要进一步解决。

**4. Rgw Skidaway Proxy 详细更新**

- 使用 Lister API 获取清单文件，查找每个块的节点位置。
- 使用 Oil API 跟踪 crush map，获取每个块的节点位置。
- 根据节点位置查找最近的 Rgw Skidaway 实例。

**5. Rgw Skidaway File System 性能测试**

- 使用 HDFS 和 Swift 进行了基准性能测试，Swift 读取性能比 HDFS 低约 20%。
- 分析了性能差异的原因，发现 Swift 重命名操作较为复杂。

**6. 下一步计划**

- 完成代码开发，进行基准性能测试。
- 解决大于 5GB 对象的零字节清单文件和小块问题。
- 研究复制实现，以解决性能问题。
- 将代码开源。

**7. 其他讨论**

- 讨论了禁用桶索引功能以提高性能的可能性。
- 讨论了网络瓶颈的可能性。
- 讨论了增加 Rgw Skidaway 与后端之间的连接数以提高性能的可能性。

**行动计划**：

- Yawn 和 Jen 继续开发代码。
- Earning 进行基准性能测试。
- 研究复制实现和性能问题。
- 将代码开源。