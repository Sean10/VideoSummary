---
title: "Exploring the Performance Limits of CephFS in Nautilus - Manoj Pillai, Red Hat"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "CephFS"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2023年（具体日期未提及）

**参会人员**： Manoj Pillai（Red Hat 性能工程团队），其他与会人员

**会议主题**： 探索 Nautilus 中 CephFS 的性能限制

**会议内容**：

* **背景介绍**： Manoj Pillai 介绍了他从 Red Hat 软件定义存储项目 Cluster 转移到 Safe 项目的过程，并分享了他对性能问题的关注和解决方法。
* **性能测试**： 
    * 使用 FIO 和 smallfile 工具进行性能测试，评估 CephFS 在 Nautilus 版本中的 I/O 性能。
    * 测试内容包括大型文件顺序 I/O、随机 I/O 和小型文件 I/O，以及一些日常管理员和用户常使用的命令。
    * 测试硬件配置包括高性能 NVMe 驱动、25G 以太网和高端 CPU。
* **测试结果**：
    * CephFS 在顺序 I/O 和随机读方面表现出色，但随机写和小型文件 I/O 性能较差。
    * MDS 可能是性能瓶颈之一。
* **未来工作**：
    * 研究提高 MDS 可扩展性和性能的方法。
    * 探索可能的调整和修复方案，以提高 CephFS 的 I/O 性能。

**关键细节**：

* **性能瓶颈**： MDS 可能是性能瓶颈之一。
* **测试结果**： CephFS 在顺序 I/O 和随机读方面表现出色，但随机写和小型文件 I/O 性能较差。
* **未来工作**： 研究提高 MDS 可扩展性和性能的方法。

**讨论的主要议题**：

* CephFS 的性能限制。
* MDS 可能是性能瓶颈之一。
* 提高 MDS 可扩展性和性能的方法。

**决定的事项**：

* 研究提高 MDS 可扩展性和性能的方法。
* 探索可能的调整和修复方案，以提高 CephFS 的 I/O 性能。

**后续行动计划**：

* Manoj Pillai 将继续研究 MDS 的性能和可扩展性问题。
* 与社区合作，探索可能的调整和修复方案。

**关键词**：

* CephFS
* Nautilus
* MDS
* I/O 性能
* 可扩展性
* 性能瓶颈
* FIO
* smallfile
* NVMe
* 25G 以太网
