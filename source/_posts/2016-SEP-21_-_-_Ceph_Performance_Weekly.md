---
categories:
- 视频总结
date: 2017-01-11
subtitle: 2016-SEP-21_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 性能优化
- BlueStore
title: "'2016-SEP-21 :: Ceph Performance Weekly'"
updated: 2017-01-12
---


**会议纪要**

**会议时间**： 2023年11月某日

**参会人员**： Mark、Sage、Paige、David、Peter、Nick、Ben、Josh等

**会议主题**：

* Ceph项目进展报告
* Pull Requests讨论
* 性能优化
* 测试与监控

**会议内容**：

**1. Pull Requests进展**

* Sage介绍了多个Pull Requests，包括两个新的压缩Pull Requests和一个减少脏元数据写入量的Pull Requests。
* FIO引擎已合并，可用于进行Blue Store测试和其他对象存储测试。
* Fast Dean代码通过初步测试，预计将很快合并。

**2. 性能优化**

* Mark指出随机读取性能出现50%的回归，原因与ASIC Messenger默认合并相关。
* Sage提到Blue Store性能提升，归功于编码/解码工作和减少数据传输。
* 需要进一步关注顺序读取性能和bitmap alligator中的阻塞降速问题。

**3. 测试与监控**

* Nick分享了新的测试结果，包括不同大小的OSD节点所需的CPU资源。
* Sage提到CBT将添加更多关于恢复的数据点。
* Ben正在开发一个更可配置的监控框架。
* Josh研究将CBT的恢复功能与新的监控框架相结合。

**4. 其他**

* Sage建议将CBT的代码库拆分，以减少连接问题并提高性能。
* Sage提到CBT的基准测试需要改进。

**行动计划**：

* Sage继续跟进Pull Requests的审查和测试工作。
* Sage继续关注性能优化问题。
* Nick继续进行测试工作。
* Ben完成CBT监控框架的开发工作。
* Josh研究CBT与新的监控框架的结合。

**下次会议**：

* 预计下周将合并新的编码/解码代码，并了解更多关于异步Messenger的信息。

**备注**：

* 会议中提到了Ceph相关领域的英文关键词，例如Pull Requests、FIO、Blue Store、ASIC Messenger、bitmap alligator、CBT等。
* 会议纪要中保留了部分关键词的英文原文。