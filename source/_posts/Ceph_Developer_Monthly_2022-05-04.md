---
title: "Ceph Developer Monthly 2022-05-04"
date: 2022-06-03
updated: 2022-06-03
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要：

1. 主题：讨论IBM存储设备在Ceph中的部署，以及相关插件系统开发和安全模型。
2. 参会人员：Martin Omar（IBM），会议提前准备充分。
3. 讨论内容：
   - Martin介绍了IBM的NVMe存储设备及其在线压缩功能，该设备提供22TB逻辑块，但只占用9.6TB物理存储空间。使用模式与VDO设备类似，通过侧通道报告实际物理块使用情况以避免磁盘故障。
   - 为支持IBM设备，实验了将代码添加到video组件附近，但发现不合适，因此改为创建插件系统。该系统基于erasure code插件系统，并放置在相邻目录中。新系统称为x block device（axtblkdev），用于加载具有所需接口的插件。
   - 创建了VDO设备的插件作为示例，以展示插件系统如何工作。这允许未来添加更多设备插件，如FCM设备。
   - 当前设备的API仍为供应商特定，未开放。插件方法使得能够向各种客户销售插件或在IBM云中使用。
   - 安全问题讨论包括Linux中的keep caps标志，它保持capability集在set uid系统中不变。提出配置选项来限制保留的capabilities，减少潜在攻击面。
   - 确认/查询每个插件所需的特定权限，而不是默认全部保留或不保留任何权限。
4. 后续行动：
   - Martin将继续测试FCM设备，希望获得对设备接口的访问权限以进行更全面的测试。
   - 需要审查和反馈，特别是关于安全方面的考虑。
   - 讨论了自动化测试的困难，因为插件不在仓库中，测试需要在插件所有者的环境中进行。
5. 会议结论：插件系统开发进展顺利，安全性问题正在积极解决。下一步是继续测试、获取反馈，并可能进行更多安全优化。