---
categories:
- 视频总结
date: 2015-08-03
subtitle: CDS_Jewel_--_RBD_Journal
tags:
- Ceph
title: "CDS Jewel -- RBD Journal"
updated: 2015-08-04
---




会议纪要

**会议时间**： 2023年某月某日

**会议地点**： 线上会议

**参会人员**： Jason、Hank、John、Vanessa等

**会议主题**： RBD Journal Blueprint设计讨论

**会议内容**：

1. **RBD Journal Blueprint概述**
   -Jason介绍了RBD Journal Blueprint的设计，旨在支持RBD镜像跨数据中心复制。
   -该设计目标是实现通用性，不仅适用于lib rbd，未来也可能适用于MDS或其他客户端。
   -设计基于liberated us API，与现有RBD代码和Journaling代码有所不同。

2. **设计决策**
   -使用RNG算法将日志条目分散到多个对象上，提高效率。
   -引入软最大大小限制，当日志对象满时，将关闭整个活动集，而不是单个对象。
   -支持多读者和潜在的多写者，例如RBD镜像多磁盘的场景。
   -引入新的工具来帮助恢复损坏的日志对象。

3. **与RBD的集成**
   -新的RBD功能代码将允许动态启用和禁用日志记录功能。
   -所有可变I/O操作（例如读写、快照操作）都将记录到日志中。
   -首次打开镜像时，将进行回放模式，以同步日志。

4. **后续行动**
   -Jason将提供代码链接，供大家查看和讨论。
   -团队将继续改进和优化RBD Journal Blueprint。

**关键术语**：

- RBD (RADOS Block Device)
- Journaling (日志记录)
- MDS (Metadata Server)
- OSD (Object Storage Device)
- liberate us API
- RNG (随机数生成器)
- Soft maximum size
- Replay mode

**总结**：

本次会议深入讨论了RBD Journal Blueprint的设计，旨在提升RBD镜像的可靠性和可用性，支持跨数据中心复制。设计采用了多种优化措施，包括日志条目分散、软最大大小限制和多读者支持等。团队将继续优化和改进该设计。