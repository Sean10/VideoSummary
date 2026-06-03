---
title: "Opening Ceremony & Land Acknowledgment - Noble Wolf"
date: 2025-11-21
updated: 2025-11-22
tags:
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### Ceph 北美技术交流会纪要

**会议主题**：Ceph North America 技术交流会  
**会议地点**：加拿大温哥华（原住民 Musquam、Squamish 和 Swit 领地）  
**开场致辞**：原住民文化代表 Nova Wolf（Poentin）  
**主持人**：Ceph 社区成员  



#### **一、开场与文化致谢**  
1. **原住民文化分享**：  
   - Nova Wolf（Poentin）以传统语言自我介绍，强调了语言与文化传承的重要性。  
   - 分享了 Musquim Indian Warriors 舞蹈团体的历史，展示其为温哥华加人队设计的 **Truth and Reconciliation Logo**，并阐述了原住民的价值观：“一心一意”（one heart, one mind）。

2. **土地致谢（Land Acknowledgement）**：  
   - 会议在 Musquam、Squamish 和 Swit 原住民的传统领地上举行，表达了对原住民历史与主权的尊重。



#### **二、Ceph 会议核心内容**  
1. **会议目标**：  
   - 促进 Ceph 社区在北美地区的协作，分享分布式存储领域的最新进展。  
   - 重点议题包括：**CRUSH algorithm**、**Bluestore/BlueFS** 优化、**RADOS** 性能调优、多云集成等。

2. **技术讨论重点**：  
   - **存储架构**：讨论了 **OSD** 的故障域配置与恢复策略，以及 **erasure coding** 与 **replication** 的取舍。  
   - **性能优化**：分享了 **RocksDB** 在 **Bluestore** 中的调优实践和分层存储中 **SSD/HDD** 的缓存策略。  
   - **安全与集成**：讨论了 **RGW** 的 **RESTful API** 认证增强和 **Kubernetes** 与 **Ceph** 的容器化集成。

3. **社区动态**：  
   - **Ceph Dashboard** 新增了支持 **iSCSI/NFS** 监控的功能。  
   - 呼吁贡献者参与 **PG** 自动均衡的开发。



#### **三、行动计划**  
1. **短期任务**：  
   - 成立工作组，整理 **CRUSH algorithm** 在多数据中心部署的最佳实践文档。  
   - 针对 **radosgw** 的 **encryption** 功能进行联合测试。

2. **长期协作**：  
   - 推动 **CephFS** 对 **POSIX** 标准的兼容性改进，招募开发者参与。  
   - 计划在下一届会议中展示 **deduplication** 与 **compression** 的基准测试结果。



#### **四、闭幕与致谢**  
- 会议以 Nova Wolf 的 **Musquin paddle song** 结束，象征友好与合作。  
- 主持人感谢社区成员参与，鼓励将会议内容传播至更多技术团队。



**备注**：  
- 原住民文化强调口述历史，本次会议未提供书面记录，但鼓励通过视频传播知识。  
- 下次会议地点待定，可能扩展至欧洲或亚洲。  
- 关键词保留：CRUSH, RADOS, OSD, Bluestore, erasure coding, Kubernetes, RESTful API, tiering.