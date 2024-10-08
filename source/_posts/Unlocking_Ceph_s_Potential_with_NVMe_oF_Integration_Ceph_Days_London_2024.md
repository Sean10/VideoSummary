---
title: "Unlocking Ceph's Potential with NVMe oF Integration | Ceph Days London 2024"
date: 2024-08-23
updated: 2024-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： NVMe over Fabrics (NVMe-oF) 项目的进展与讨论

**参会人员**： NVMe-oF 项目成员、Ceph 研发人员等

**会议内容**：

**一、NVMe-oF 介绍**

* NVMe-oF 是一种基于网络协议的存储访问方式，允许用户通过网络访问本地 NVMe 设备。
* NVMe-oF 具有高性能、低延迟和可扩展性等优点，适用于数据中心存储场景。

**二、NVMe-oF 项目的进展**

* NVMe-oF 项目已经取得了显著进展，包括：
    * 支持多种网络协议，如 TCP、iSCSI、RoCE 等。
    * 支持多种 NVMe 设备，如 NVMe SSD、NVMe-oF Target 等。
    * 支持多种访问控制方式，如 ACL、RBAC 等。

**三、NVMe-oF 的优势**

* 相比于传统的 NVMe，NVMe-oF 具有以下优势：
    * 更高的性能：通过网络传输，可以充分利用高速网络带宽，提高访问速度。
    * 更低的延迟：网络传输延迟更低，可以提高数据处理的效率。
    * 更好的可扩展性：可以通过增加网络带宽和 NVMe 设备，实现更高的存储容量和性能。

**四、NVMe-oF 的应用场景**

* NVMe-oF 适用于以下场景：
    * 数据中心存储：提高存储性能和可扩展性。
    * 分布式存储：实现跨地域存储访问。
    * 云计算：提供高性能、可扩展的存储服务。

**五、后续行动计划**

* 将 NVMe-oF CLI 集成到 Ceph 的主 CLI 中。
* 支持 NVMe-oF In-Band 消息通知。
* 支持子系统级别的访问控制。
* 支持名称空间屏蔽功能。
* 支持更广泛的网络协议和设备。
* 提高性能和可扩展性。

**六、讨论要点**

* **NVMe-oF 的网络协议支持**： 讨论了 NVMe-oF 支持的网络协议，并分析了不同协议的优缺点。
* **NVMe-oF 的设备支持**： 讨论了 NVMe-oF 支持的 NVMe 设备，并分析了不同设备的性能特点。
* **NVMe-oF 的访问控制**： 讨论了 NVMe-oF 的访问控制方式，并分析了不同控制方式的适用场景。
* **NVMe-oF 的性能优化**： 讨论了 NVMe-oF 的性能优化方法，并分析了不同方法的适用场景。

**七、会议总结**

NVMe-oF 项目取得了显著进展，具有广阔的应用前景。未来将继续优化 NVMe-oF 的性能和可扩展性，并支持更广泛的网络协议和设备，为用户提供更好的存储服务。