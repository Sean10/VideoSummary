---
title: "Afternoon Lightning Talks | Ceph Days London 2024"
date: 2024-08-23
updated: 2024-08-24
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议时间**： [请填写会议时间]

**会议地点**： [请填写会议地点]

**参会人员**： Gabriel Miss Williams (Rosen Franklin Institute 研究软件工程师)，Lee Sanders (IBM)，Mike Burkart (Ceph 产品经理)

**会议主题**： 分布式存储Ceph相关技术探讨

**会议内容**：

**一、Gabriel Miss Williams：分布式存储Ceph在HPC集群中的应用**

* **背景**： Rosen Franklin Institute拥有高性能计算集群，但存在网络连接限制、存储成本高、资源使用效率低等问题。
* **解决方案**： 使用分布式临时RAM存储（DistTrack）技术，将Ceph集群部署在计算节点上，利用节点内存进行高效存储。
* **工作原理**： DistTrack通过并行部署OSD，创建隔离的内存文件或对象存储，将IO瓶颈转移到节点间网络连接，提高性能并降低存储成本。
* **案例研究**： 使用DistTrack技术处理生物样本结构分析应用，将处理时间缩短5.1%，IO开销降低100%。
* **结论**： DistTrack是一种高效、可扩展的Ceph部署工具，可提高HPC应用性能并优化资源使用。

**二、Lee Sanders：Ceph性能分析工具CBT**

* **CBT简介**： CBT是一个开源的性能评估工具，用于测试Ceph集群性能。
* **CBT局限性**： CBT输出结果有限，无法展示整体性能，需要手动处理大量数据。
* **CBT改进方向**： 改进YAML格式以支持更复杂的测试配置，生成更多性能曲线，提高自动化程度，生成完整的性能报告。
* **CBT愿景**： 建立一个社区通用的性能评估方法，使Ceph性能结果具有可比性。

**三、Mike Burkart：Ceph与VMware集成**

* **Ceph与VMware集成**： IBM开发了Ceph与VMware的集成插件，使Ceph集群易于在VMware环境中部署和管理。
* **插件功能**： 插件提供管理界面，支持部署、扩展和生命周期管理等功能。
* **未来计划**： 支持数据路径支持、数据保护等功能。

**四、讨论**

* **DistTrack的适用场景**： 适用于IO密集型应用，可提高性能并降低存储成本。
* **CBT的改进方向**： 提高自动化程度，生成更多性能曲线，提高结果的可比性。
* **Ceph与VMware集成**： 可简化Ceph集群在VMware环境中的部署和管理。

**五、行动计划**

* 继续改进DistTrack和CBT工具。
* 推动Ceph与VMware的集成。
* 建立社区通用的性能评估方法。

**会议总结**：

本次会议探讨了分布式存储Ceph在HPC集群中的应用、Ceph性能分析工具CBT以及Ceph与VMware集成等技术。参会人员分享了各自的经验和见解，并提出了改进和发展的建议。