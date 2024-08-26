---
title: "DisTRaC: Accelerating High-Performance Compute Processing for Temporary Data Storage"
date: 2022-11-15
updated: 2022-11-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：介绍Distract - 用于加速高性能计算处理的分布式瞬态存储

#### 主讲人：Gabriel Mason Williams

#### 背景介绍：
- **机构背景**：Gabriel Mason Williams介绍了罗斯和弗兰克研究所（Rose and Frank Institute），这是一个位于英国的研究机构，专注于开发新技术以解决重要的健康研究挑战。该机构位于哈威尔（Harwell）校区和迪德科特（Didcot），并由英国EPSRC（Engineering and Physical Sciences Research Council）资助。
- **个人背景**：Gabriel目前是伦敦女王玛丽大学的人工智能硕士学生，并在罗斯和弗兰克研究所担任研究软件助理，同时正在寻找博士机会。

#### 项目背景：
- **项目起源**：Distract项目起源于钻石光源（Diamond Light Source），由Mark Basham和Dave Bond发起，并与布里斯托大学（University of Bristol）合作进行。

#### 会议内容概述：
- **问题背景**：传统的HPC集群设置存在I/O瓶颈问题，主要是因为网络连接到高性能存储集群的限制，以及共享资源的竞争问题。
- **解决方案**：Gabriel提出了Distract作为解决方案，这是一个用于在HPC基础设施上部署瞬态存储集群的程序，利用RAM进行可扩展和高效的管理。

#### Distract的特点：
- **快速部署**：Distract利用MPI和网络文件系统（NFS）进行快速部署，部署时间大约为22秒。
- **快速移除**：同样利用MPI进行快速移除，移除时间大约为1.5分钟。
- **隔离资源**：Distract创建了一个作业辅助和隔离的内存文件或对象存储，确保作业间的资源隔离。

#### 案例研究：
- **案例一：Relyon**：通过使用Distract，处理时间减少了5.51倍，总时间减少了4.37倍。
- **案例二：Cyber**：通过使用Distract，处理时间减少了8.32%，I/O开销减少了81.04%。

#### 结论：
- **Distract的优势**：Distract通过利用集群的RAM创建了一个超融合的HPC集群，减少了网络文件系统的I/O开销，并提供了数据处理性能的潜在提升。
- **灵活性**：Distract支持使用对象存储或文件系统，提供了更多的灵活性。

#### 后续行动计划：
- **进一步开发**：考虑在每个节点上扩展MDS服务，并探索在本地NVMe上部署的可能性。

#### 参考文献：
- Gabriel提供了相关的参考文献，并对会议进行了总结。

#### 会议结束：
- Gabriel感谢大家的参与，并邀请大家提问。

#### 提问环节：
- **Stefan提问**：是否使用Ceph进行开发？Gabriel回答说，他们使用Ceph的原生功能，如Rados和FFS，并解释了为什么对象存储在处理图像数据时更有效。

---

本次会议详细介绍了Distract项目的目标、实施方法和实际应用效果，展示了其在高性能计算领域的潜在价值和优势。