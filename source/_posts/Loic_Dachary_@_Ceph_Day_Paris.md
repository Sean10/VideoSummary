---
categories:
- 视频总结
- 技术讨论
date: 2014-11-10
subtitle: Loic_Dachary_@_Ceph_Day_Paris
tags:
- Ceph
- 分布式存储
- CephFS
- RADOS
- 存储优化
title: "Loic Dachary @ Ceph Day Paris"
updated: 2014-11-10
---




### 会议纪要

**会议主题**： Ceph分布式存储中Erasure Code（纠删码）技术的深入讨论与展望

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 
- 会议主讲人：Ceph Erasure Code开发人员
- 与会者：Ceph社区成员、开发人员

**会议内容**：

**一、Erasure Code介绍**

Erasure Code是一种节省空间的特性，旨在减少存储需求，提高存储效率。该技术的开发是社区驱动的，主讲人并非Red Hat员工，但在Red Hat的支持下完成了这项工作。

**二、Erasure Code工作原理**

Erasure Code可以在不牺牲数据安全性的前提下，减少存储空间占用。它通过数学公式将数据分割成多个编码块，并在不同存储节点上存储。

**三、Erasure Code的优势与挑战**

Erasure Code的优势在于减少存储空间占用，提高数据恢复效率，支持多数据中心部署。然而，实现复杂，需要大量计算资源，恢复过程中可能出现单点故障。

**四、Erasure Code的应用**

Ceph通过Steering机制，可以将不再活跃的数据迁移到Erasure Code存储池，实现透明存储。新的本地恢复功能可以在不跨越数据中心边界的情况下，快速恢复丢失的数据块。

**五、未来计划**

Ceph社区计划支持ARM处理器上的优化，进一步提升Erasure Code的性能。Hammer版本将支持新的优化功能，包括ARM优化和本地恢复。

**六、总结**

Erasure Code是Ceph分布式存储中的一项重要技术，可以有效地降低存储成本，提高数据恢复效率。随着技术的不断优化和发展，Erasure Code将在未来得到更广泛的应用。

**七、行动计划**

- 与会者将继续关注Erasure Code的发展，积极参与社区讨论。
- Red Hat和Ceph社区将持续优化Erasure Code技术，提升其性能和可靠性。
- 未来版本将引入更多优化功能，满足用户需求。