---
title: "  Ceph Developer Monthly 2022-05-04  "
date: 2022-06-03
updated: 2022-06-03
tags:
- Ceph
- Distributed Storage
- Plugin System
- Security
- IBM Storage
categories:
- "视频总结"
subtitle: Ceph_Developer_Monthly_2022-05-04
---



在2022年5月4日的Ceph开发者月度会议中，主要讨论了IBM存储设备在Ceph中的部署和相关插件系统的开发，以及安全模型的构建。

会议中，IBM的Martin Omar介绍了IBM的NVMe存储设备，该设备具备在线压缩功能，能够提供22TB的逻辑块，但只占用9.6TB的物理存储空间。此外，他还提到了设备的故障预警机制，类似于VDO设备，通过侧通道报告物理块的实际使用情况。

为了支持IBM设备，Martin尝试将代码添加到video组件附近，但发现不合适，因此改为创建插件系统。新系统基于erasure code插件系统，并命名为x block device（axtblkdev），用于加载具有所需接口的插件。他还创建了VDO设备的插件作为示例，以展示插件系统的工作原理。

目前，设备的API仍为供应商特定，未开放。插件方法使得能够向各种客户销售插件或在IBM云中使用。安全方面，讨论了Linux中的keep caps标志，它保持capability集在set uid系统中不变，并提出了配置选项来限制保留的capabilities，减少潜在攻击面。

后续行动计划包括：
- Martin将继续测试FCM设备，并希望获得对设备接口的访问权限以进行更全面的测试。
- 需要审查和反馈，特别是关于安全方面的考虑。
- 讨论了自动化测试的困难，因为插件不在仓库中，测试需要在插件所有者的环境中进行。

会议结论是，插件系统开发进展顺利，安全性问题正在积极解决。下一步是继续测试、获取反馈，并可能进行更多安全优化。