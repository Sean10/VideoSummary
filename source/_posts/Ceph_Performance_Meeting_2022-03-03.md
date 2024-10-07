---
title: "Ceph Performance Meeting 2022-03-03"
date: 2022-03-04
updated: 2022-03-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** Opencast 分布式存储缓存技术介绍

**主讲人：** Mikhail Sadinsky, 英特尔云软件架构师

**会议时间：** [具体时间]

**会议地点：** 波兰

**参会人员：** [参会人员名单]

**会议内容总结：**

1. **Opencast 概述：**
   - Opencast 是一种用于 Linux 的存储缓存软件，工作在块层。
   - 主要功能是将慢速存储介质上的数据缓存到快速存储介质上，以加速存储操作。
   - 支持多种缓存模式，包括写通（write-through）、写回（write-back）、只写（write-only）和直通（pass-through）。

2. **主要特性：**
   - **缓存模式：** 提供多种缓存模式以适应不同的应用场景。
   - **清理策略：** 包括基于访问时间的清理策略（LRU）和基于脏数据区域的清理策略（ICP）。
   - **提升策略：** 支持基于访问次数的数据提升策略。
   - **选择性和优先级缓存：** 允许用户根据数据的重要性和访问频率配置缓存策略。
   - **顺序流截断：** 避免大顺序流数据污染缓存。
   - **可管理性：** 提供命令行工具和配置文件支持，便于管理和监控。

3. **架构和技术细节：**
   - Opencast 架构包括一个核心缓存框架和针对不同平台的适配器（如 Linux 内核和 SPDK）。
   - 缓存空间组织：支持从 4K 到 64K 的缓存行大小，优化缓存利用率和性能。
   - 数据管理：通过精细的元数据管理，减少写放大和读放大。

4. **与 Ceph 的集成：**
   - Opencast 可以作为 Ceph 存储系统的加速层，通过创建缓存实例来优化 OSD 的性能。
   - 支持一对一和一对多的缓存配置，根据流量分布选择合适的部署方式。

5. **性能和优化：**
   - Opencast 通过精细的缓存管理和优化策略，相比其他缓存解决方案（如 dm-cache）在处理小请求时具有更低的读写放大。
   - 正在进行性能基准测试，预计将提供更多详细的性能数据。

**后续行动计划：**
- 继续进行性能基准测试，并计划在未来的会议中分享测试结果。
- 考虑分享之前的性能比较数据（与 dm-cache 的比较），待确认是否受 NDA 限制。

**会议结束：**
- 会议在主讲人感谢与会者的参与和提问后结束，提醒大家下周再见。

**备注：**
- 会议中提到的“Opencast for SPDK”是指将 Opencast 缓存框架集成到 SPDK 环境中。
- 对于缓存行大小的选择，建议根据典型工作负载的平均请求大小进行匹配，以优化缓存利用率和性能。

**会议记录人：** [记录人姓名]

**会议日期：** [具体日期]