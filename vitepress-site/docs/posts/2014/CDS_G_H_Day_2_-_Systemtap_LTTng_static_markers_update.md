---
title: "CDS G/H (Day 2) - Systemtap/LTTng static markers (update)"
date: 2014-06-26
updated: 2014-06-26
tags:
  - "Ceph"
  - "监控"
  - "性能优化"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： [请填写会议时间]

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph 分布式存储系统监控与性能优化

**会议内容**：

**1. 监控与性能优化路径**

- 会议讨论了并行进行的两个路径：Adam 和其他人员尝试集成 lttng，同时其他人专注于收集数据以便通过 ops 路径获取操作详细信息（写入、读取、权限等）。
- 使用 system tap 进行系统追踪，主要目的是追踪资源竞争并将其与操作关联起来。目标是确保 OSD 中的每个互斥锁在获取时都提供操作信息，以便在日志期间关联资源。
- 目前的工作集中在创建一些超级类以减少混乱，并确保代码中的 Tracepoints 注释能够通用化。

**2. Tracepoints 与系统追踪**

- system tap 和 lttng 都提供了 Tracepoints，可用于在代码中插入追踪信息。
- system tap 在 OSD stap 中用 track_mutex 替换了 mutex，并要求 lock 和 unlock 方法提供 trace_op。
- lttng 具有热传递代码的能力，可以在 SE 端使用编译后的本地代码进行追踪。
- Tracepoints 的格式相似，包括 tracepoint 名称和一系列未解释的信息。

**3. 客户端追踪**

- Noah 正在研究 Oco 路径中时间消耗的原因，以及操作为什么耗时如此之长。
- Adam 正在研究客户端追踪，目标是创建一个标准的客户端库构建版本，能够订阅 Trace 事件流并捕获工作负载的追踪信息。
- 可以使用 system tap 或 lttng 进行客户端追踪，并选择合适的格式写入数据。

**4. 调试与优化**

- 需要关注两条并行路径中的补丁，确保它们不会在合并时产生冲突。
- 通过收集不同客户的追踪数据，可以分析工作负载特征，并在测试集群上进行优化。
- 可以利用其他工具和技术，例如将文件系统追踪转换为 fio 配置文件，以模拟工作负载。

**5. 其他**

- Mam 正在尝试启动 BlueJeans 会议系统。
- Min 建议讨论 copy on read 克隆。

**行动计划**：

- Adam 和 Noah 继续研究追踪和性能优化。
- Mam 尝试解决 BlueJeans 会议系统的问题。
- Min 提出讨论 copy on read 克隆。

**备注**：

- 会议中提到的关键技术包括：lttng、system tap、Tracepoints、OSD stap、mutex、track_mutex、SE、PG、RBD、fio 等。