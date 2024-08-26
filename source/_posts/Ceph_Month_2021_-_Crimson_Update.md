---
title: "Ceph Month 2021: Crimson Update"
date: 2021-06-24
updated: 2021-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Ceph项目的两个关键进展：Crimson和C-Store。Crimson是一个新的OSD（对象存储守护进程）实现，旨在替换现有的Ceph OSD，以更好地适应下一代存储硬件的需求，减少CPU开销。C-Store则是一个新的对象存储实现，专为Crimson的线程回调模型设计，旨在利用新兴存储技术如ZNS和持久内存。

#### 主要议题
1. **Crimson OSD的进展**
   - Crimson OSD的目标是通过减少每个I/O的CPU开销来提高性能，特别是在多核环境下的性能。
   - 使用C-Star框架来减少上下文切换，通过为每个核心分配单一线程并分区数据结构和任务来实现。
   - 近期工作集中在实现RBD（RADOS块设备）工作负载、数据持久性和可靠性、可见性和调试以及稳定性。

2. **C-Store的详细介绍**
   - C-Store设计避免使用CPU密集型的元数据设计，如RocksDB，并利用快速NVMe设备和持久内存。
   - ZNS（Zone Namespace）是一种新的NVMe规范，通过将驱动器分为只能顺序写入的区域来减少写放大和垃圾回收。
   - 持久内存因其低延迟和高写入耐久性，适合作为数据和元数据的持久缓存。

3. **C-Store的高级设计**
   - C-Store的逻辑结构包括根块、O节点索引、Omap树和逻辑地址到物理地址的映射。
   - 使用逻辑地址映射来简化垃圾回收和数据重定位，减少写放大。
   - 日志记录使用原子写入和重放机制，支持逻辑和物理块的变更。

#### 决定事项
- Crimson OSD和C-Store的开发将继续集中在稳定性和性能优化上。
- 未来工作将包括多核支持、克隆支持、直接突变支持和持久内存支持。

#### 后续行动计划
- 继续推进Crimson OSD的稳定性测试和功能移植。
- 优化C-Store的垃圾回收机制和性能。
- 探索与NVMe over Fabric网关的潜在集成。

#### 其他讨论
- SPDK（Storage Performance Development Kit）将在C-Store之下作为底层I/O细节的插件。
- Crimson OSD目前支持BlueStore，未来可能会有更多与NVMe over Fabric网关的协同工作。

#### 结论
会议强调了Crimson和C-Store在Ceph项目中的重要性，并明确了未来的开发方向和目标。感谢Sam的详细介绍和所有参与者的积极参与。