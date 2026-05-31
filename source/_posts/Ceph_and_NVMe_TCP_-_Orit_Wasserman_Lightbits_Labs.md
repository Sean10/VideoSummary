---
categories:
- 视频总结
date: 2019-05-28
subtitle: Ceph_and_NVMe_TCP_-_Orit_Wasserman_Lightbits_Labs
tags:
- Ceph
title: "Ceph and NVMe/TCP - Orit Wasserman, Lightbits Labs"
updated: 2019-05-29
---


会议纪要

会议时间：[请填写具体日期和时间]

参会人员：Owen Basserman（Life Bits Lab 架构师），Ceph 开发团队

会议主题：Life Bits Lab 的 Envy Me TCP 技术介绍及与 Ceph 集成的可能性探讨

会议内容：

1. Owen Basserman 自我介绍及 Envy Me TCP 介绍
   - Owen Basserman 介绍了自己的背景，从 Ceph 核心开发者转为 Life Bits Lab 架构师。
   - Envy Me TCP 是一种优化高性能的 NVMe-over-TCP 协议，旨在提高存储性能和降低延迟。
   - 选择 TCP 的原因是其广泛的应用和成熟的技术，无需改变现有网络基础设施。
   - Life Bits Lab 是 Envy Me TCP 的主要发明者之一，与 Facebook、Intel 等公司共同推动其标准化。

2. Envy Me TCP 的优势及应用
   - Envy Me TCP 可在不降低服务器容量的情况下，安全地使用 NVMe TCP 进行元数据存储。
   - 具有复杂的保护机制，单个 SSD 失效不会影响整体性能。
   - 可用于大规模部署和长距离传输，适用于需要高性能存储的场景。

3. Envy Me TCP 与 Ceph 的集成
   - Owen 提出将 Envy Me TCP 与 Ceph 集成，以进一步提高 Ceph 的性能和稳定性。
   - 目前集成尚处于初步阶段，需要解决延迟和成本问题。
   - Life Bits Lab 正在开发键值接口，以实现 Envy Me TCP 与 Ceph 的深度融合，并完全替代 RBD。

4. 后续行动计划
   - Life Bits Lab 将继续优化 Envy Me TCP，并探索与 Ceph 的集成方案。
   - Ceph 开发团队将与 Life Bits Lab 保持沟通，共同推进 Envy Me TCP 的集成工作。

5. 其他事项
   - Owen Basserman 鼓励大家对 Envy Me TCP 进行更多了解，并欢迎感兴趣的人士与其交流。

关键词：Envy Me TCP, NVMe-over-TCP, Ceph, RBD, 高性能存储, 集成