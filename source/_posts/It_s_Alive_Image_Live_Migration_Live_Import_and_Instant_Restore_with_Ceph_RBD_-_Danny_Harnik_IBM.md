---
categories:
- 视频总结
date: 2023-05-05
subtitle: It_s_Alive_Image_Live_Migration_Live_Import_and_Instant_Restore_with_Ceph_RBD_-_Danny_Harnik_IBM
tags:
- Ceph
- Live Migration
- Image Import
- Instant Restore
- RBD
title: "It’s Alive! Image Live Migration, Live Import and Instant Restore with Ceph RBD - Danny Harnik, IBM"
updated: 2023-05-05
---




### 改进后的中文总结

**会议主题**：使用Ceph RBD进行图像实时迁移、导入和即时恢复

**会议时间**：[具体时间]

**会议地点**：[具体地点]

**参会人员**：来自IBM研究（Haifa, Israel）的研发团队成员，包括发言人Danny Harnik及其同事Effie。

**会议内容总结**：

1. **图像实时迁移（Image Live Migration）**
   - 自Nautilus版本开始引入，支持同一集群内不同存储池之间的图像迁移，Pacific版本扩展到外部源。
   - 仅支持Librbd，适用于OpenStack、KVM虚拟化等。
   - 使用后复制迁移技术，允许在数据迁移过程中立即在目标端开始工作。
   - 主要应用场景包括集群间实时迁移、即时导入到Ceph和备份与即时恢复。

2. **外部NBD源的实时迁移**
   - 新增NBD格式支持，通过chemo NBD服务器连接，实现更灵活的图像导入。
   - 提供备份与即时恢复的POC，使用qcow2格式进行差异备份，并通过chemo NBD实现即时恢复。

3. **未来计划与改进方向**
   - 推动现有PR上线的进程。
   - 探索对克隆图像的集群间迁移支持。
   - 改进备份与恢复流程，特别是增加对Ceph原生导出格式的索引支持，以实现更高效的即时恢复。

**决定事项**：
- 继续推动图像实时迁移功能的开发和优化。
- 完善文档和教程，确保用户能够充分利用新功能。

**后续行动计划**：
- 完成并上线相关PR。
- 开发和测试对克隆图像的集群间迁移支持。
- 研究和实施对Ceph原生导出格式的索引支持，以优化备份与恢复流程。

**会议结束**：
- 会议在提问和讨论环节后圆满结束，发言人感谢所有参与者的积极参与和反馈。