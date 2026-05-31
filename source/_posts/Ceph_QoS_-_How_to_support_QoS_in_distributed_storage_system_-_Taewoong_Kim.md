---
categories:
- 会议纪要
date: 2018-04-23
subtitle: Ceph_QoS_-_How_to_support_QoS_in_distributed_storage_system_-_Taewoong_Kim
tags:
- Ceph
- 虚拟化
title: "'Ceph QoS: How to support QoS in distributed storage system - Taewoong Kim'"
updated: 2018-04-23
---


### 会议纪要

**会议时间**： 2023年（具体日期未提及）

**会议地点**： （未提及）

**参会人员**： Tim King（SK Telecom），其他与会人员

**会议主题**： SK Telecom在Ceph存储系统上的研发工作及未来计划

**会议内容**：

**一、介绍与背景**

- Tim King代表SK Telecom介绍其公司在Ceph存储系统上的研发成果和相关工作。
- SK Telecom作为韩国领先的电信公司，旗下拥有SK Broadband和SK Hynix等子公司，分别提供互联网服务和存储解决方案。
- SK Telecom希望通过与OpenStack Ceph社区的协作，实现ICT公司之间的协同效应，并利用其子公司SK Hynix提供的SSD来优化Ceph存储环境。

**二、Ceph存储系统优化**

- 针对Ceph存储系统在虚拟化环境下的资源竞争和性能问题，SK Telecom提出了以下优化方案：
  - **资源分配方法**： 引入优先级队列和最小-最大权重算法，以满足不同用户的需求。
  - **服务质量保证**： 通过预留、限制控制和比例共享QoS控制，确保关键业务的服务质量。

**三、Ceph功能增强**

- SK Telecom计划在Ceph中引入以下功能增强：
  - **用户空间（US）功能**： 实现更细粒度的资源分配和调度。
  - **去重功能**： 提高存储空间的利用率。
  - **私有云和虚拟桌面**： 利用Ceph构建私有云和虚拟桌面，为企业用户提供便捷的存储服务。

**四、未来计划**

- SK Telecom将继续参与Ceph社区的开发工作，并计划在以下方面进行拓展：
  - **支持更多存储系统**： 扩展Ceph的功能，支持更多存储系统。
  - **社区合作**： 与Ceph社区紧密合作，共同推动Ceph的发展。

**五、讨论与总结**

- 与会人员就Ceph存储系统的优化和功能增强进行了讨论，并提出了以下建议：
  - **DM Clock**： 将DM Clock应用于其他SEFs项目，如文件系统中的元数据服务器。
  - **US功能**： 进一步完善US功能，支持更多存储系统。

**后续行动计划**：

- SK Telecom将继续参与Ceph社区的开发工作，并推动Ceph存储系统的优化和功能增强。
- 与Ceph社区保持紧密合作，共同推动Ceph的发展。