---
categories:
- 会议纪要
- 视频总结
date: 2014-11-21
subtitle: Florian_Haas_@_Ceph_Day_London
tags:
- 性能优化
- 分布式存储
title: "Florian Haas @ Ceph Day London"
updated: 2014-11-21
---




Florian Haas在Ceph Day London会议上就Ceph性能优化与基准测试进行了深入探讨。他强调了理解Ceph性能的重要性，并提出性能优化需要关注多个维度，包括延迟、吞吐量和IOPS。

会议内容主要涉及以下几个方面：

* **Ceph性能优化的重要性**： Floren强调，在部署和优化Ceph集群时，理解Ceph性能至关重要。性能优化需要关注多个维度，包括延迟、吞吐量和IOPS，并应根据具体应用场景选择合适的指标。
* **Ceph性能影响因素**： 包括硬件（如OSD的本地块存储和网络性能）和软件（如文件系统、OSD配置、网络连接和客户端堆栈）。
* **Ceph性能基准测试工具**： 包括DD工具、FIO工具、netperf工具、Ceph OSD bench、Ceph rados bench、FIO RBD引擎、restbench工具等。
* **性能优化建议**： 在部署Ceph集群之前，对硬件进行基准测试；根据应用场景选择合适的性能指标；优化OSD配置和文件系统参数；确保网络性能满足需求；使用合适的基准测试工具评估性能。

会议中提到的Ceph组件包括OSD、Journal、Filestore、Rados、RBD、CephFS和rados gateway。Floren还介绍了多种Ceph性能基准测试工具，并提供了使用建议。

**关键词**：

* Ceph
* 性能优化
* 基准测试
* 硬件
* 软件
* 延迟
* 吞吐量
* IOPS
* OSD
* Journal
* Filestore
* Rados
* RBD
* CephFS
* rados gateway
* FIO
* netperf
* Ceph OSD bench
* Ceph rados bench
* FIO RBD引擎
* restbench
* iozone
* Bonnie Plus+