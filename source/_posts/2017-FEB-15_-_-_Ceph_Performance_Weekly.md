---
categories:
- 视频总结
date: 2017-02-17
subtitle: 2017-FEB-15_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 性能优化
- 分布式存储
- CRUSH算法
- 高可用性
title: "'2017-FEB-15 :: Ceph Performance Weekly'"
updated: 2017-02-18
---




### 会议纪要

**会议时间**： 2023年11月某日

**会议地点**： 线上会议

**参会人员**： Jeanne、Nick、Sage、Igor、Jaime、Ernesto 等

**会议内容**：

**一、本周工作进展**

* **Sage**： 对快速调度代码进行了拆分，成功移除了一些代码，有望提升性能。
* **Igor**： 正在研究减少镜像使用，以降低存储开销。
* **Jaime**： 发现Ceph存储集群在快照删除时存在延迟问题。
* **Ernesto**： 发现Ceph存储集群内存使用过高，可能是缓存配置问题。

**二、主要议题**

1. **快照删除延迟问题**：
    * **原因**： 快照在删除时进行trim操作，导致IO性能下降。
    * **解决方案**： 降低快照trim操作的并发度，调整相关参数，考虑使用Lucifer优化快照删除性能。
2. **Ceph存储集群内存使用过高**：
    * **原因**： 可能是缓存配置问题或程序bug。
    * **解决方案**： 调整缓存大小，使用`mem_cache_debug`参数进行调试。
3. **FastDispatch优化**：
    * **目标**： 提升Ceph存储集群的性能。
    * **方案**： 优化get reserved maps和release maps调用，优化FastDispatch代码，审计OSD中等待maps的代码。

**三、后续行动计划**

* **Sage**： 继续优化快速调度代码。
* **Igor**： 继续研究减少镜像使用。
* **Jaime**： 继续测试Ceph存储集群，并优化快照删除性能。
* **Ernesto**： 调整缓存大小，并找出内存使用过高的原因。
* **所有人员**： 优化FastDispatch代码，并审计OSD中等待maps的代码。

**四、其他**

* 会议中还讨论了Ceph存储集群的日志性能、BlueStore缓存、缓存驱逐策略等问题。

**五、总结**

本周Ceph存储集群的开发工作主要集中在性能优化和bug修复方面。下周将继续推进相关工作，并关注新的问题和挑战。