---
title: "Ceph on Windows - Alessandro Pilotti, Cloudbase Solutions"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要

**会议主题：** Ceph与Windows集成解决方案介绍

**主讲人：** Alessandra Pilotti, CEO at Cloud-based Solutions

**会议内容总结：**

1. **背景介绍：**
   - Ceph是最受欢迎的开源存储解决方案之一。
   - Windows Server在企业市场中占有很大份额。
   - 传统的Ceph iSCSI Gateway在性能上存在问题。

2. **合作伙伴关系：**
   - Cloud-based Solutions与Ceph合作，旨在改善Windows环境下的Ceph性能。
   - 合作成果已开源，并集成到Ceph社区中。

3. **技术目标：**
   - 提供与Linux环境下相似的用户体验和命令行接口。
   - 确保Ceph在Windows上运行时，Windows管理员也能感到熟悉。
   - 实现高性能，目标是超越传统的iSCSI Gateway，并接近Linux原生性能。

4. **架构与实现：**
   - OSD运行在Linux上，Windows上运行一个用户空间进程（RBD Windows）。
   - 开发了一个新的内核驱动（wimbd.sys）来处理磁盘操作。
   - 支持的Windows版本包括Windows Server 2016, 2019, 2022，以及Windows 10和11用于开发。

5. **性能优化：**
   - 通过实现Device I/O Control和改进I/O并发性来提升性能。
   - 测试结果显示，性能显著优于iSCSI Gateway。

6. **安全性与认证：**
   - 驱动程序已通过Cloud-based Solutions的认证，未来计划通过Microsoft认证。
   - Microsoft认证版本将支持安全启动功能。

7. **未来工作：**
   - 增加对Windows集群的支持，包括集群共享卷和扩展文件服务器。
   - 持续的维护和改进工作，包括错误修复和社区集成。

8. **演示内容：**
   - 展示了如何在Windows Server上安装和配置Ceph。
   - 演示了Ceph卷的创建、映射和管理。
   - 展示了Ceph文件系统（CephFS）在Windows上的使用。
   - 演示了Hyper-V与Ceph的集成，以及如何在集群环境中使用Ceph。

**后续行动计划：**
- 继续与Ceph社区合作，推动技术发展和集成。
- 提供持续的技术支持和咨询服务。
- 完成Microsoft认证流程，发布认证驱动程序。

**会议结束语：**
- Alessandra Pilotti感谢大家的参与，并表示愿意进一步讨论项目细节和提供支持。

**备注：**
- 会议中提到的所有技术细节和演示步骤均为Ceph与Windows集成解决方案的关键组成部分。