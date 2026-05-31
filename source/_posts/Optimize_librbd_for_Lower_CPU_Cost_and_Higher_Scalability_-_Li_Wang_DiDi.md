---
categories:
- 视频总结
date: 2019-05-24
subtitle: Optimize_librbd_for_Lower_CPU_Cost_and_Higher_Scalability_-_Li_Wang_DiDi
tags:
- Ceph
- 性能优化
- 可扩展性
title: "Optimize librbd for Lower CPU Cost and Higher Scalability - Li Wang, DiDi"
updated: 2019-05-24
---



会议纪要

会议时间：[请填写会议时间]
会议地点：[请填写会议地点]
参会人员：[请填写参会人员名单]
主持人：[请填写主持人姓名]

一、会议内容

1. **Liberty优化工作分享**

   主持人来自PD云存储团队，介绍了Liberty优化工作的进展，主要包括以下内容：

   - **Liberty架构概述**：Liberty是Ceph的一个分布式存储解决方案，适用于虚拟化场景，其数据流涉及磁盘访问请求、OSD、CRUSH算法等。
   - **IBD LPS优化**：针对IBD LPS在随机写测试中不随集群规模扩展的问题，提出了并行化闪存工作、优化单线程设计为多线程设计等解决方案。
   - **客户端镜像缓存**：利用Ceph的快照功能，通过优化镜像缓存机制，提高虚拟机启动速度。
   - **写操作CPU开销优化**：提出升级Ceph版本、使用新的API调用方式等优化方案，以降低Liberty导致的CPU使用率过高问题。
   - **数据恢复优化**：介绍数据恢复过程中的优化策略，包括使用Rebalance优化请求逻辑、回调机制等。

2. **社区合作与经验分享**

   主持人分享了与社区合作的经验和遇到的问题：

   - **Liberty延迟问题**：Liberty在SSD和NVMe存储上的延迟较高，可能影响数据库等对延迟敏感的应用。
   - **硬件利用率问题**：当平均负载超过60%时，可能出现延迟和缓慢请求。
   - **价格与性能平衡**：社区在硬件优化方面投入较多，但客户更关注价格和性能平衡。
   - **CPU使用率问题**：Liberty导致CPU使用率过高，限制了SSD的性能。

二、会议决定

1. 与社区合作，共同优化Liberty性能，特别是延迟、硬件利用率和CPU使用率等问题。
2. 探索新的优化方案，提高Liberty在虚拟化场景下的性能和稳定性。

三、后续行动计划

1. 优化Liberty代码，提高性能和稳定性。
2. 与社区合作，共同解决Liberty在虚拟化场景下的性能瓶颈。
3. 收集用户反馈，持续改进Liberty产品。

改进后的总结更准确地反映了原始内容的要点，包括会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。同时，保留了相关的Ceph领域英文关键词，如librbd、Ceph、CRUSH algorithm、OSD等。