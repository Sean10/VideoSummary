---
categories:
- 视频总结
date: 2014-07-25
subtitle: RH_InkTank_Ceph_Day_Sessions_Casey_Bodley_COHORTFS
tags:
- Ceph
- NFS
- Scalability
- Parallel NFS
- Metadata
title: "RH InkTank Ceph Day Sessions Casey Bodley COHORTFS"
updated: 2014-07-26
---


在本次RH InkTank Ceph Day Sessions中，Casey Bodley就NFS上可扩展的元数据进行了深入探讨。以下是会议内容的详细总结：

### 会议背景

Casey首先介绍了NFS的优势，包括其作为IETF标准、广泛的应用、成熟的技术和可扩展性。他提到了如何利用RAD、对象条带化和CRUSH算法来优化数据放置，并探讨了NFS如何通过Parallel NFS (pnfs)来提高数据存储效率。

### 主要议题

- **Parallel NFS (pnfs)**: pnfs允许客户端直接与存储设备通信，支持不同的布局类型，包括黑色卷设备（osds）和文件布局。
- **元数据扩展性**: 讨论了现有元数据扩展技术的局限性，如Seth的分布和负载均衡技术，以及NFS在当前版本中缺乏利用这些技术的手段。
- **pnfs metastripe**: 介绍了这种将pnfs思想应用于元数据的新技术，允许客户端通过初始元数据服务器获取布局信息，并直接访问其他元数据服务器。

### 讨论要点

- **布局类型**: pnfs metastripe定义了两种布局类型：文件条带布局和目录条带布局，用于确定文件和目录条带的位置。
- **操作优化**: 通过并行读取、并行目录修改和布局提交，pnfs metastripe提高了元数据操作的效率。
- **原型实现**: Casey介绍了基于开源NFS连接服务器和piNFS测试套件的pnfs metastripe原型。

### 决定事项

- 继续推进pnfs metastripe的IETF草案。
- 优化布局提交和M时间一致性。
- 支持Seth frag trees。

### 后续行动计划

- 完成pnfs metastripe的IETF草案。
- 实现布局提交和M时间一致性。
- 支持Seth frag trees。
- 评估和改进原型性能。

### 其他事项

- 会议中未提及具体的时间表和责任人。

本次会议重点讨论了NFS元数据扩展性的挑战和解决方案，介绍了pnfs metastripe技术，并确定了后续行动计划。