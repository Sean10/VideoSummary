---
title: "Venkat Kolli -- Ceph on All-Flash Storage"
date: 2015-11-13
updated: 2015-11-14
tags:
  - "Ceph"
  - "性能优化"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 未知
**参会人员**： Venkat Kolli（Sandisk 产品经理）、Simon、Andrews（主持人）、其他与会人员
**会议主题**： Sandisk 无限闪存系统与 Ceph 的结合及优化

**会议内容**：

**一、会议背景**

* Sandisk 于两年半前开始研发无限闪存系统，主要针对 Seth 和 OpenStack，旨在提供高性能、大容量的全闪存存储解决方案。
* 无限闪存系统采用 3U 机箱，可容纳 512TB 闪存，支持热插拔，具备高可靠性。
* Sandisk 对 Ceph 进行了优化，使其在无限闪存系统上运行更加高效。

**二、无限闪存系统介绍**

* 系统基于 SAS 接口，提供高密度、高容量存储。
* 系统不包含服务器和计算资源，可与其他服务器连接。

**三、Ceph 与无限闪存系统的结合**

* Sandisk 优化了 Ceph 的数据路径、锁优化、队列优化等方面，使 Ceph 在无限闪存系统上的性能提升了 10 倍以上。
* 优化主要集中在数据路径、锁优化、队列优化等方面。

**四、性能测试**

* 测试结果显示，Ceph 在无限闪存系统上具有极高的性能：
    * 读取性能：约 250 万 IOPS
    * 写入性能：约 100 万 IOPS
    * 延迟：约 2 毫秒

**五、未来计划**

* Sandisk 将继续优化 Ceph，使其在无限闪存系统上运行更加高效。
* Sandisk 将与社区合作，推动 Ceph 在全闪存存储领域的应用。
* Sandisk 将开源其开发的 Key-Value 存储引擎，并将其集成到 Ceph 中。

**六、其他讨论**

* Sandisk 与 Mellanox 合作，优化 Ceph 的网络性能。
* Sandisk 开发了新的 Key-Value 存储引擎，用于优化全闪存存储性能。
* Sandisk 将提供 Ceph 的安装和配置工具，降低用户的使用门槛。

**七、行动计划**

* Sandisk 将继续优化 Ceph，提升其在无限闪存系统上的性能。
* Sandisk 将与社区合作，推动 Ceph 在全闪存存储领域的应用。
* Sandisk 将开源其开发的 Key-Value 存储引擎，并将其集成到 Ceph 中。

**八、会议总结**

本次会议介绍了 Sandisk 无限闪存系统与 Ceph 的结合及优化情况，展示了 Ceph 在无限闪存系统上优异的性能。Sandisk 将继续优化 Ceph，推动其在全闪存存储领域的应用。