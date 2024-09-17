---
title: "RH InkTank Ceph Day Sessions Casey Bodley COHORTFS"
date: 2014-07-25
updated: 2014-07-26
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议时间**： [请填写具体日期和时间]

**参会人员**： Casey, Hassan 等

**会议主题**： 可扩展的NFS上的元数据

**会议内容**：

**一、会议背景**

- Casey介绍了NFS（网络文件系统）的优势，包括其作为IETF标准、广泛的应用、成熟的技术和可扩展性。
- 讨论了如何利用NFS的扩展性来提高数据存储的效率，例如通过RAD、对象条带化和Crush算法来优化数据放置。

**二、主要议题**

- **Parallel NFS (pnfs)**：介绍pnfs的概念，它允许pnfs客户端直接与存储设备通信，并支持不同的布局类型，包括黑色卷设备（osds）和文件布局。
- **元数据扩展性**：讨论了现有元数据扩展技术的局限性，如Seth的分布和负载均衡技术，以及NFS在当前版本中缺乏利用这些技术的手段。
- **pnfs metastripe**：介绍了一种将pnfs思想应用于元数据的新技术，允许客户端通过初始元数据服务器获取布局信息，并直接访问其他元数据服务器。

**三、讨论要点**

- **布局类型**：pnfs metastripe定义了两种布局类型：文件条带布局和目录条带布局，用于确定文件和目录条带的位置。
- **操作优化**：通过并行读取、并行目录修改和布局提交，pnfs metastripe提高了元数据操作的效率。
- **原型实现**：Casey介绍了基于开源NFS连接服务器和piNFS测试套件的pnfs metastripe原型。

**四、决定事项**

- 继续推进pnfs metastripe的IETF草案。
- 优化布局提交和M时间一致性。
- 支持Seth frag trees。

**五、后续行动计划**

- 完成pnfs metastripe的IETF草案。
- 实现布局提交和M时间一致性。
- 支持Seth frag trees。
- 评估和改进原型性能。

**六、其他事项**

- 会议中未提及具体的时间表和责任人。

**总结**：

本次会议讨论了NFS在元数据扩展性方面的挑战和解决方案，介绍了pnfs metastripe技术，并确定了后续行动计划。