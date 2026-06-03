---
title: "Configuring Ceph Deployments with an Easy to Use Calculator - Karl Vietmeier, Intel Corporation"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
  - "存储优化"
categories:
  - "视频总结"
outline: deep
---
### 改进后的中文总结

在本次会议中，Intel数据中心组织的云解决方案架构师Carl Vietmeier讨论了Ceph存储系统中WAL（Write-Ahead Logging）和DB（Database）分区的大小以及所需空间配置。以下是会议的关键要点和改进后的内容：

**会议背景和主题**： Carl介绍了Intel数据中心组织，并提出了关于Ceph存储系统中WAL和DB分区大小的问题，这是一个常被用户询问的问题。

**问题提出**： 由于对WAL和DB分区大小的疑问较多，且现有文档给出的建议过大，因此决定进行实证测试以确定更合适的大小。

**测试方法**： 使用现有的基准测试服务器和集群，对不同大小的对象进行测试，以确定WAL和DB分区的大小。

**测试结果**：
- WAL大小主要取决于元数据量和处理速度。
- 建议将元数据大小设置为每个对象20KB，每个OSD需要约5GB的元数据空间。
- 实际所需空间可能在2-3GB之间，而非文档中推荐的4%。
- WAL大小主要与数据变化率有关，建议设置80秒的缓冲区。

**结论**：
- 建议根据实际使用情况调整WAL和DB分区大小，并进行测试验证。
- WAL分区空间可能在2-3GB之间，DB分区空间约为5GB。

**行动计划**：
- 将测试结果整理成文档，供相关人员参考。
- 鼓励用户根据实际使用情况调整WAL和DB分区大小，并进行测试验证。

**关键词和术语**：
- WAL
- DB
- 元数据
- OSD
- RocksDB
- CBT
- I/O大小
- 缓冲区
- 网络带宽

通过本次会议，我们得到了关于Ceph存储系统中WAL和DB分区大小配置的实证测试结果，为用户提供了更准确的配置建议，并强调了根据实际使用情况进行测试验证的重要性。