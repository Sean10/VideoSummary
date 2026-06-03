---
title: "2019-08-22 -- Ceph Performance Meeting"
date: 2019-08-22
updated: 2019-09-06
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
2019年8月22日，Ceph项目团队召开了一次性能会议，讨论了Ceph分布式存储项目的进展、讨论的主要议题、决定的事项以及后续的行动计划。

**会议内容**：

* **项目进展**：
    - 已合并的Pull Requests (PR) 包括增加East Heart缓冲区大小至64K，Sage的64K Yarn调整等。
    - 待处理的PR包括Casey关于扩展LTTE Angie跟踪点的PR，Alec关于64K大小的Yarn的PR，Sam关于扩展LTTE Angie跟踪点的PR，雷达后端复制的PR，Ken Adams的PR，调整MVS缓存内存限制的PR，分布式数据缓存RGW的PR等。
    - 其他进展包括Igor更新了新的较小版本的Blue Store，Eager功能正在开发中，Sam的PR旨在扩展LTTE Angie跟踪点，雷达后端的PR已通过审查，MVS缓存内存限制的调整PR仍在进行中，分布式数据缓存RGW的PR由Mark Hogan负责。
* **讨论议题**：
    - **新的S3基准测试**： 讨论了新的S3基准测试，旨在提供一个轻量级、快速、易于使用的工具，以展示Ceph的功能。
    - **桶重组**： 讨论了桶重组的性能问题，特别是关于CPU使用率和延迟的问题。
    - **对象存储优化**： 讨论了对象存储优化，特别是关于减少写放大和空间放大的问题。
* **决定事项**：
    - 将继续开发新的S3基准测试。
    - 将继续优化桶重组和对象存储。
    - 将审查和合并待处理的PR。
* **后续行动计划**：
    - 继续开发新的S3基准测试。
    - 优化桶重组和对象存储。
    - 审查和合并待处理的PR。

**会议中提到的关键词**：

- Ceph
- Blue Store
- Eager
- LTTE Angie
- OSD
- RGW
- S3
- T-rex DB
- RocksDB
- Rados
- PG
- PG log
- PG info
- CLS
- CLS igw
- OMAP
- Write amplification
- Space amplification

改进后的总结更准确地反映了原始内容的要点，包括会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。同时，保留了计算机科学/ceph相关领域的英文原文关键词，以便读者更好地理解会议内容。