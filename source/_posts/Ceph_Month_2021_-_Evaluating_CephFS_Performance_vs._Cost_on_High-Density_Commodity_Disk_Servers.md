---
categories:
- 视频总结
date: 2021-06-25
subtitle: Ceph_Month_2021_-_Evaluating_CephFS_Performance_vs._Cost_on_High-Density_Commodity_Disk_Servers
tags:
- Ceph
- CephFS
- 分布式存储
title: "'Ceph Month 2021: Evaluating CephFS Performance vs. Cost on High-Density Commodity Disk Servers'"
updated: 2021-06-25
---



CERN作为全球大型强子对撞机（LHC）的Tier Zero中心，负责处理大量的科学数据。本文主要讨论了CERN在处理高亮度LHC数据时，对CephFS性能的评估及其成本效益。

**会议关键细节**：

- CERN使用名为“Worldwide LHC Computing Grid”的全球性计算网格进行数据处理，拥有约135PB的磁盘存储和近400PB的磁带存储。
- CERN周边有14个Tier 1中心和160个Tier 2中心，总计约100万个CPU核心，每天处理约200万个作业。
- CERN使用多种开源存储软件，如DCache, DPM, EOS, Storm, XRootD等，并使用HTTP, XRootD, GSI-FTP等协议进行站点间传输。
- CERN面临高亮度LHC数据需求增加的挑战，预计到2028年，每年数据需求将增至500PB。

**讨论的主要议题**：

- Ceph作为成熟且功能强大的开源存储软件，可能在未来物理存储系统中扮演重要角色。
- 现有的开源软件缺乏某些高级功能，因此需要在此基础上叠加HEP特定的网关，如CephFS + EOS的组合。
- 通过实验和性能测试，评估了CephFS在高密度商品磁盘服务器和100G网络上的性能。

**决定的事项**：

- 计划在生产环境中进一步测试CephFS + EOS组合，以验证其在实际使用中的性能和操作优势。
- 考虑统一命名空间和本地化I/O，以便客户端可以直接使用原生Ceph客户端，而不需要通过EOS客户端。

**后续行动计划**：

- 继续在生产环境中测试CephFS + EOS组合。
- 优化命名空间和I/O本地化策略。
- 调整内核客户端设置以改善读取性能。
- 探索CephFS快照在同步和共享服务中的应用。

**改进后的总结内容**：

本文主要介绍了CERN在处理高亮度LHC数据时，对CephFS性能的评估及其成本效益。通过实验和性能测试，评估了CephFS在高密度商品磁盘服务器和100G网络上的性能。结果表明，CephFS + EOS组合在高密度商品磁盘服务器和100G网络上展现出出色的性能，具有高度可靠性和灵活性，并可通过QoS进行调整。然而，也指出了某些性能瓶颈和优化空间，如命名空间和I/O本地化策略的优化，以及内核客户端设置的调整。