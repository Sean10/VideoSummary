---
title: "Ceph Month 2021: Evaluating CephFS Performance vs. Cost on High-Density Commodity Disk Servers"
date: 2021-06-25
updated: 2021-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 背景信息
- **CERN的计算环境**：CERN使用名为“Worldwide LHC Computing Grid”的全球性计算网格进行数据处理。CERN作为Tier Zero中心，拥有约135PB的磁盘存储（双副本）和近400PB的磁带存储。每年新增数据量约50PB。
- **全球分布**：CERN周边有14个Tier 1中心和160个Tier 2中心（大学和实验室），总计约100万个CPU核心，每天处理约200万个作业。
- **存储和网络**：全球存储总量约1EB，内部总连接速度约1Tbps。去年在全球LHC计算网格上转移了300PB的数据。

#### 存储软件和技术
- **开源存储软件**：CERN使用多种开源存储软件，如DCache, DPM, EOS, Storm, XRootD等，这些软件由高能物理（HEP）社区开发。
- **协议和服务**：使用HTTP, XRootD, GSI-FTP等协议进行站点间传输，通过File Transfer Service (FTS)进行第三方传输，并根据网络约束调度传输。
- **数据协调器**：Rucio作为数据协调器，根据不同策略与FTS交互并放置数据。

#### 未来挑战和解决方案
- **高亮度LHC数据需求**：预计到2028年，每年数据需求将增至500PB。
- **Ceph的角色**：Ceph作为成熟且功能强大的开源存储软件，可能在未来物理存储系统中扮演重要角色。然而，现有的开源软件缺乏某些高级功能。
- **解决方案**：通过在开源存储软件上叠加HEP特定的网关，如CephFS + EOS的组合，来解决这些缺失的功能。

#### 实验和性能测试
- **硬件配置**：使用8台大型新机器进行测试，每台机器配备双Xeon处理器、192GB RAM、100Gbps以太网、60TB硬盘和1TB SSD。
- **CephFS配置**：测试了三种不同的擦除编码布局（4+2, 8+2, 16+2），并使用upmap平衡器确保平衡。
- **性能结果**：在读取性能方面，最多达到20GB/s；在写入性能方面，最多达到34GB/s。发现随着OSD存储空间的增加，写入性能下降。

#### 后续行动计划
- **生产环境测试**：计划在生产环境中进一步测试CephFS + EOS组合，以验证其在实际使用中的性能和操作优势。
- **优化和改进**：考虑统一命名空间和本地化I/O，以便客户端可以直接使用原生Ceph客户端，而不需要通过EOS客户端。

#### 结论
- **CephFS和EOS的组合**：展示了在高密度商品磁盘服务器和100G网络上的出色性能，具有高度可靠性和灵活性，并可通过QoS进行调整。
- **社区支持**：Ceph拥有一个庞大且活跃的用户社区，超越了物理社区。
- **未来工作**：将继续测试和优化这一组合，以满足未来高能物理存储系统的需求。

#### 讨论和问题
- **读取性能问题**：讨论了读取性能在达到一定水平后饱和的原因，可能是由于磁盘寻道延迟。建议调整内核客户端的预读设置以改善性能。
- **CephFS快照的使用**：在特定场景如同步和共享服务中，CephFS快照将得到更有效的使用。

### 后续行动
- 继续在生产环境中测试CephFS + EOS组合。
- 优化命名空间和I/O本地化策略。
- 调整内核客户端设置以改善读取性能。
- 探索CephFS快照在同步和共享服务中的应用。