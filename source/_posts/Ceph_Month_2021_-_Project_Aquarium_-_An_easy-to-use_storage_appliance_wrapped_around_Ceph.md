---
title: "  Ceph Month 2021: Project Aquarium - An easy-to-use storage appliance wrapped around Ceph  "
date: 2021-06-16
updated: 2021-06-17
tags:
- Ceph
- Storage Appliance
- Project Aquarium
- Distributed Storage
- Ceph Management
categories:
- "视频总结"
subtitle: Ceph_Month_2021_-_Project_Aquarium_-_An_easy-to-use_storage_appliance_wrapped_around_Ceph
---



### 会议纪要：Project Aquarium 介绍与讨论

#### 会议概述
本次会议由Alex Saddle主持，他是Souza公司的软件工程经理和Project Aquarium的产品负责人。会议重点介绍了Project Aquarium的目标、架构、演示以及未来发展规划。

#### 关键细节
- **项目名称**：Project Aquarium
- **项目目标**：简化Ceph的开发、部署和管理，提供一个开源的存储设备解决方案。
- **项目团队**：由Souza公司的存储团队开发，Alex Saddle担任产品负责人，另一位高级工程师担任后端负责人。
- **项目架构**：分为后端“Gravel”和前端“Glass”，后端使用Python，前端使用Angular。
- **技术选择**：作为系统服务运行，依赖fadm等系统工具，使用WebSockets进行通信，并利用fcd维护集群状态。
- **用户界面**：提供简化的、引导式的安装和操作界面，抽象复杂概念，不直接暴露底层配置细节。
- **演示内容**：展示了安装过程、集群管理以及数据操作和管理。

#### 后续行动计划
- **短期目标**：改进仪表板，实现对象服务，测试USB启动和Pixie booting。
- **中期目标**：关注升级过程，开发块服务和资源约束求解器。
- **长期目标**：社区发展和项目扩展，实现“世界统治”（幽默提及）。

#### 讨论与问答
- **经验教训**：从Ceph Dashboard的经验中学习，但Aquarium项目有其独特性，不直接竞争，而是提供不同的使用场景。
- **技术细节**：使用Python Librados直接与Ceph通信，而不是依赖Dashboard API。
- **硬件选择**：目前不特定于特定硬件模型，但未来可能会更具体化。
- **使用fcd的原因**：确保Aquarium在Ceph故障时仍能运行，fcd提供必要的集群状态管理。

#### 结论
Project Aquarium是一个新兴的开源项目，旨在简化Ceph的使用和管理。团队欢迎社区的参与和反馈，并计划通过一系列的改进和扩展来推动项目的发展。