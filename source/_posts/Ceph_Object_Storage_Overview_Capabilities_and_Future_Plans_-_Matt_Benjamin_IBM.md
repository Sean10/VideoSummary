---
categories:
- 视频总结
date: 2023-05-05
subtitle: Ceph_Object_Storage_Overview_Capabilities_and_Future_Plans_-_Matt_Benjamin_IBM
tags:
- Ceph
- 对象存储
- 分布式存储
- RGW
- CephFS
- BlueStore
- BlueFS
- RocksDB
title: "Ceph Object Storage Overview, Capabilities and Future Plans - Matt Benjamin, IBM"
updated: 2023-05-05
---




### 会议纪要

#### 会议概述
本次会议由IBM的Program Director Matt Benjamin主持，主要讨论了Ceph对象存储的能力、路线图和未来计划。

#### 主要议题
1. **Seth对象存储的能力**
   - **RGW (RADOS Gateway)** 作为Ceph集群之上的S3和Swift兼容的HTTP对象存储，具备高保真度。
   - 主要能力包括：
     - 单集群容量可达数百PB。
     - 支持数十万个S3桶或容器。
     - 每个桶可存储至少5亿个对象，目标接近10亿。
     - 动态桶索引缩放。

2. **近期开发和改进**
   - 重构和重写了多站点复制能力，提高规模和鲁棒性。
   - 实现了S3 Select，支持结构化数据操作。
   - 重构内部API为“Zipper”。
   - 支持所有Amazon兼容的加密API。
   - 将计算密集型操作从索引存储移至RADOS上的队列操作。

3. **未来计划和路线图**
   - 更新C++20协程。
   - 增强多站点复制功能，包括并行同步和同步公平性。
   - 开发S3 Inventory，预生成的桶列表。
   - 开发D4N缓存层。
   - 扩展S3 Select功能，支持Parquet和JSON。
   - 实现端到端跟踪，使用Jaeger。
   - 实现索引恢复功能。

4. **新前端协议**
   - 支持HTTP/3和Apache Arrow Flight。

5. **其他增强功能**
   - 增强S3过渡能力，支持远程S3的数据恢复。
   - 增强归档区域功能，包括数据去重。
   - 消除单主节点模型，采用共识协议。

#### 决定事项
- 确认了Seth对象存储的未来发展方向和技术路线图。
- 确定了即将实施的关键功能和技术改进。

#### 后续行动计划
- 推进C++20协程的更新。
- 完成多站点复制功能的增强。
- 开发和测试新前端协议。
- 完善文档和社区支持。

#### 其他讨论
- 讨论了文档更新、过滤器编译、动态脚本插入等技术细节。
- 确认了未来几年的发展目标和预期成果。

#### 结论
会议强调了Seth对象存储在未来的发展方向和技术创新，旨在提供更高效、更灵活的存储解决方案，满足不断变化的市场需求和技术挑战。