---
title: "Implementing a Resilient Ceph RGW Object Storage with Erasure Coded Data Pool as the Foundation..."
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议由Bahid主持，他是Digicolor的云工程师，分享了公司在设计和实施对象存储服务方面的经验。由于主讲人Yavash无法现场出席，他的演讲以预录视频形式播放。

#### 主要议题
1. **Digicolor简介**：Digicolor是中东地区最大的电子商务平台，每日页面浏览量超过1800万，促销期间可达2亿。
2. **问题定义**：公司面临高流量和高数据存储需求，原有硬件资源共享导致成本上升。
3. **解决方案**：设计并实施自有的对象存储服务，以降低成本并提高性能。
4. **技术细节**：
   - **架构设计**：采用三层架构，包括Nginx作为缓存服务器和负载均衡器，Ceph RGW处理对象存储。
   - **硬件环境**：利用公司闲置硬件资源，部署8个节点，使用HP 10G网络设备。
   - **软件环境**：测试了Octopus和Pacific版本的Ceph，使用Ubuntu LTS和OpenResty构建模块。
   - **性能优化**：通过自定义CRUSH映射、SSD作为后端存储、分离公共和集群网络等措施优化性能。
   - **数据缓存**：设计了多层缓存机制，包括CDN、图像大小调整和Nginx缓存。
5. **测试与结果**：
   - **负载测试**：使用Locust框架和实际图像数据进行测试，设计了两种场景以模拟真实流量。
   - **性能指标**：通过基准测试，选择了Azure RBD以提高存储容量和性能。
   - **最终配置**：确定了9个RGW实例，每个实例的线程池大小为2008和2048，以优化CPU核心分配。

#### 决定事项
1. **采用Ceph RGW作为对象存储服务**。
2. **优化Nginx配置和RGW实例数量**。
3. **实施多层缓存策略以提高性能**。

#### 后续行动计划
1. **继续监控和优化系统性能**。
2. **探索更多性能优化技术，如进一步调整CRUSH映射和网络配置**。
3. **分享经验和技术细节，与社区进行交流**。

#### 结论
Digicolor通过设计和实施自有的对象存储服务，成功降低了成本并提高了系统性能，满足了公司的高流量和高存储需求。会议最后，Bahid邀请与会者提问，并表示愿意分享更多细节和经验。