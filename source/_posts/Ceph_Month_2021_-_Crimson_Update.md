---
categories:
- 视频总结
date: 2021-06-24
subtitle: Ceph_Month_2021_-_Crimson_Update
tags:
- Ceph
- Crimson OSD
- C
- Store
- Distributed Storage
- Object Storage
title: "'Ceph Month 2021: Crimson Update'"
updated: 2021-06-25
---




### 会议纪要

#### 会议概述
本次Ceph项目的会议重点讨论了两个关键进展：Crimson和C-Store。Crimson是一个新的OSD实现，旨在提高性能并减少CPU开销；C-Store是一个新的对象存储实现，旨在利用新兴存储技术如ZNS和持久内存。

#### 主要议题
1. **Crimson OSD的进展**
   - 使用C-Star框架来减少上下文切换，提高多核环境下的性能。
   - 专注于实现RBD工作负载、数据持久性和可靠性、可见性和调试以及稳定性。

2. **C-Store的详细介绍**
   - 避免使用CPU密集型的元数据设计，如RocksDB，并利用ZNS和持久内存。
   - 使用ZNS减少写放大和垃圾回收，利用持久内存作为数据和元数据的持久缓存。

3. **C-Store的高级设计**
   - 包括根块、O节点索引、Omap树和逻辑地址到物理地址的映射。
   - 使用逻辑地址映射简化垃圾回收和数据重定位。

#### 决定事项
- 继续集中在稳定性和性能优化上。
- 未来工作将包括多核支持、克隆支持、直接突变支持和持久内存支持。

#### 后续行动计划
- 推进Crimson OSD的稳定性测试和功能移植。
- 优化C-Store的垃圾回收机制和性能。
- 探索与NVMe over Fabric网关的潜在集成。

#### 其他讨论
- SPDK将在C-Store之下作为底层I/O细节的插件。
- Crimson OSD目前支持BlueStore，未来可能会有更多与NVMe over Fabric网关的协同工作。

#### 结论
会议强调了Crimson和C-Store在Ceph项目中的重要性，并明确了未来的开发方向和目标。