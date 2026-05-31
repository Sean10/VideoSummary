---
title: The Challenge of Storing Small Objects on a Large Scale - Luis Domingues & Ján Senko, Proton AG
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 分布式存储
categories: 
- "视频总结"
subtitle: The_Challenge_of_Storing_Small_Objects_on_a_Large_Scale_-_Luis_Domingues_Jan_Senko_Proton_AG
---

## 改进后的中文总结内容

Proton 公司作为一家总部位于日内瓦的互联网服务提供商，在2018年选择了 Ceph 作为其分布式存储解决方案，以应对快速增长的数据存储需求。以下是对其 Ceph 存储系统发展历程与挑战的详细总结：

### 历史背景
- 2018年，Proton 开始使用 Ceph 解决其数据存储问题。
- 初始集群由8台服务器组成，每台服务器配备12块HDD，总容量为1PB。
- 使用Erasure Coding 4+2策略和双数据中心镜像，存储成本降低至3倍。

### 面临的挑战
- **小对象问题**：由于电子邮件头部信息占用大量空间，导致存储效率低下。
- **恢复时间过长**：HDD的随机读写性能差，导致磁盘故障后恢复时间长。
- **OMAP性能问题**：随着数据量增加，OMAP的更新和恢复操作变得缓慢。

### 解决方案
- **Multi Blob**：将多个小对象合并为大对象，以提高恢复效率。
- **OMAP优化**：减少OMAP的更新频率，提升性能。
- **SSD使用**：考虑使用SSD存储小对象，但成本问题限制了实施。

### 部署工具
- **初始工具**：使用Sible进行集群管理，但随着集群规模扩大，部署时间过长。
- **Ceph ADM**：用于较小的内部集群，管理RBD和S3服务。
- **Rook**：基于Kubernetes进行自动化部署，用于用户数据集群。

### 当前状态
- 每个集群存储30PB用户数据，总存储量接近100PB。
- 小对象问题仍存，但已通过优化减少影响。
- MClock调度算法表现更好，减少了调优工作。

### 未来发展
- 从4+2 Erasure Coding升级到8+3。
- 关注Ceph新版本的小对象优化功能。
- 预计未来存储需求将增长10倍，达到Exabyte级别。

### 后续行动计划
- 升级Erasure Coding策略。
- 测试Ceph新版本的小对象优化功能。
- 继续优化OMAP和Multi Blob解决方案。
- 探索Kubernetes和Rook的进一步应用。

通过这些解决方案和策略，Proton成功地使用Ceph应对了快速增长的存储需求，并逐步提升了存储系统的稳定性和效率。