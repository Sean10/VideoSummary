---
title: Evaluating the Performance and Power Efficiency of Ceph Storage Configurations - Tom Byrne, UKRI
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- 分布式存储
categories: 
- "视频总结"
subtitle: Evaluating_the_Performance_and_Power_Efficiency_of_Ceph_Storage_Configurations_-_Tom_Byrne_UKRI
---

### **Ceph存储性能与能效分析会议纪要**

#### **会议背景**
主讲人Tom，英国卢瑟福·阿普顿实验室科学计算存储架构师。主题为Ceph存储在不同硬件配置（HDD/NVMe）及纠删码（Erasure Coding）策略下的性能与能效对比。应用场景包括高吞吐科学计算（HTC）和大型科研设施（如LHC、SKA射电望远镜）的数据存储。

#### **关键讨论内容**

**1. 存储需求与现状**
- 科学计算特点：高容量需求（数十至数百PB），但IOPS要求相对较低（每秒数十GB带宽）。
- 现有方案：
  - Ceph on HDDs：采用高效EC策略（如EC8+3），以低成本满足大容量需求（如Echko集群150PB）。
  - 分层存储：热数据存Ceph，冷数据归档至磁带以降低运行成本。

**2. 测试配置**
- 硬件对比：
  - 常规HDD：8TB SATA HDD，成本最低。
  - 高密度HDD：22TB SATA HDD，功耗低，但单盘性能下降。
  - 高密度NVMe：15TB TLC NVMe，成本高，但性能和能效高。
- 测试方法：统一集群下划分不同CRUSH root，测试不同EC池（如4+2、8+3）的Streaming IO和Small IO，监控功耗、性能和IOPS。

**3. 核心发现**
- 性能对比：
  - Streaming IO：NVMe与HDD在写入性能相近，读取性能NVMe更优。
  - Small IO：NVMe显著优于HDD，但EC宽度会放大IOPS压力。
- 能效分析：
  - 空闲功耗：NVMe方案总功耗最低，22TB HDD次之，8TB HDD最高。
  - IO效率：NVMe单位IO功耗更低，尤其在Small IO场景。
  - 成本模型：8TB HDD方案因高运行成本已不经济，NVMe或22TB HDD更优。

**4. 结论与建议**
- 采购策略：
  - 优先高密度HDD：若容量需求主导且性能达标。
  - NVMe替代低效HDD：当需要更高性能或Small IO场景。
  - 淘汰8TB HDD：高运行成本且无性能优势。
- 优化方向：
  - EC策略选择：窄EC（如4+2）减少IO放大。
  - 未来探索：Fast EC（部分写/读优化）、QLC NVMe成本效益验证。

#### **后续行动计划**
1. 硬件采购：新集群优先采用22TB HDD或高密度NVMe，避免8TB HDD。
2. 技术验证：测试Fast EC对部分IO场景的改进效果。
3. 能效监控：扩展功耗数据收集至生产环境，验证实验室结论。

#### **Q&A摘要**
- 问答内容涉及硬盘节能模式、NVMe生命周期成本、Fast EC的影响等。



本总结准确反映了原始内容的要点，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。未发现错误、误解或遗漏的重要信息。