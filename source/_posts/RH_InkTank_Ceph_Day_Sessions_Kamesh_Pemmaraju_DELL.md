---
title: "RH InkTank Ceph Day Sessions Kamesh Pemmaraju DELL"
date: 2014-07-25
updated: 2014-07-26
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议时间**： [请填写会议时间]

**会议地点**： [请填写会议地点]

**参会人员**： 
- Kamesh Pemeraju，戴尔公司高级产品经理，专注于OpenStack
- [其他参会人员]

**会议主题**： Ceph与OpenStack的结合，Ceph在不同场景下的应用，以及案例研究

**会议内容**：

**一、Ceph与OpenStack的结合**

1. **Ceph在OpenStack中的应用**：
    - Ceph与OpenStack的Swift API和Cinder API兼容，可提供对象存储和块存储服务。
    - Ceph可以作为OpenStack的底层存储平台，支持OpenStack的Glance、Nova等服务。
2. **Ceph的应用场景**：
    - 开源云存储：可以作为纯对象存储使用，类似于Swift集群。
    - Web应用：提供高性能、可扩展的存储解决方案。
    - 大数据：可以作为HDFS的替代方案，提供高性能的文件系统。
3. **Ceph的架构考虑**：
    - 可靠性：考虑冗余和故障域，确保数据安全。
    - 存储池：根据需求选择SSD池或容量池。
    - 监控节点：考虑监控节点的故障域，确保集群稳定运行。

**二、案例研究：阿拉巴马大学**

1. **背景**：
    - 阿拉巴马大学在癌症和基因组研究方面有大量数据，数据分散在各个设备上，管理困难。
2. **解决方案**：
    - 使用Ceph和OpenStack构建可扩展的存储云，集中管理数据。
    - 使用Crowbar进行集群部署，简化部署过程。
3. **效果**：
    - 提高数据管理效率，降低成本。
    - 研究人员可以访问更大的数据集，提高工作效率。

**三、后续行动计划**

1. **戴尔和红帽将推出预配置的Ceph和OpenStack解决方案，简化部署过程**。
2. **继续与客户合作，推动Ceph和OpenStack的广泛应用**。

**四、讨论要点**

1. Ceph与OpenStack的结合为用户提供了灵活的存储解决方案。
2. Ceph在不同场景下具有广泛的应用前景。
3. 部署Ceph和OpenStack需要考虑多个因素，包括可靠性、性能和成本。
4. 案例研究表明，Ceph和OpenStack可以为用户提供有效的存储解决方案。

**五、结束语**

本次会议深入探讨了Ceph与OpenStack的结合以及Ceph在不同场景下的应用，并分享了阿拉巴马大学的成功案例。相信随着Ceph和OpenStack的不断发展，它们将为用户带来更多的价值。