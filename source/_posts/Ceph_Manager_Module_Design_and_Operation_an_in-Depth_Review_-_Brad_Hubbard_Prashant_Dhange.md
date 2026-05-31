---
title: Ceph Manager Module Design and Operation, an in-Depth Review - Brad Hubbard & Prashant Dhange
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 分布式存储
- 可扩展性
- 性能优化
categories: 
- "视频总结"
subtitle: Ceph_Manager_Module_Design_and_Operation_an_in-Depth_Review_-_Brad_Hubbard_Prashant_Dhange
---

### 会议纪要：Ceph Manager 架构与未来发展

**会议主题**: Ceph Manager 的架构、功能及未来发展讨论

**主讲人**: Brad Hubbard (Red Hat) 和 Prashant Dhange (IBM)

**会议时间**: 未知



#### 1. **Ceph Manager 的背景与目的**
   - **目的**: Ceph Manager (MGR) 的设计初衷是为了减轻 Ceph Monitor 的负载，提供实时集群操作的管理和高级管理功能，如性能优化、数据分布、故障管理等。
   - **功能**: 负责处理复杂的任务，并通过模块化设计（如 Damon Server、Base Module 等）确保灵活性和适应性。
   - **历史**: MGR 由 John Spray 等人于 Infernalis 版本期间贡献给 Ceph。

#### 2. **Ceph Manager 架构概述**
   - **用户命令处理流程**: 用户发送命令到 MGR，通过模块 API 与 MGR 核心组件（如 MON、OSD、MDS）交互。
   - **核心组件**: 包括 MON、OSD、MDS 等，提供配置和集群状态信息。
   - **模块加载机制**: MGR 通过 Python 子解释器加载模块，支持模块的 standby 和 active 模式。

#### 3. **模块加载与状态切换**
   - **模块加载**: MGR 通过扫描文件系统中的模块目录，动态加载 Python 模块。
   - **状态切换**: 
     - **Standby 到 Active**: 当不存在 active MGR 或 active MGR 失败时，MON 通过更新 Manager Map 来选择并提升 standby MGR 为 active。
     - **故障处理**: 如果 active MGR 失败，MON 会自动选择 standby MGR 接管。

#### 4. **Python Global Interpreter Lock (GIL) 的使用**
   - **GIL 管理**: MGR 使用 GIL 来管理 Python 对象和 C API 调用，确保线程安全。
   - **性能问题**: GIL 可能导致性能瓶颈，特别是在多线程环境下。
   - **未来改进**: 讨论了使用 Python 子解释器和模块分布式加载来缓解 GIL 问题。

#### 5. **Op Tracker 功能介绍**
   - **目的**: Op Tracker 用于跟踪 MGR 模块的操作，帮助快速定位性能问题和故障。
   - **关键指标**: 
     - **Op Latency**: 跟踪操作的延迟，识别性能瓶颈。
     - **Op Backlog**: 显示当前正在处理的操作队列。
     - **Historic Slow Ops**: 记录超过 30 秒的慢操作。
   - **未来改进**: 计划增加模块级别的操作跟踪，使用 Python 装饰器和 OpenTracing API 来实现更细粒度的跟踪。

#### 6. **未来发展与改进方向**
   - **性能优化**: 
     - **模块分布式加载**: 将部分模块分布到 standby MGR 上，以平衡负载。
     - **PG 统计优化**: 减少从大量 OSD 收集 PG 统计数据的频率，避免性能瓶颈。
   - **审计日志模块**: 计划增加审计日志模块，记录离线工具（如 CephFS 恢复工具）的操作历史。
   - **集群历史信息**: 计划记录集群的创建、升级等历史信息，便于故障排查和未来优化。

#### 7. **问答环节**
   - **Python 与 Rust 兼容性问题**: 讨论了 Python 模块加载 Rust 库时可能出现的兼容性问题，特别是在子解释器中。
   - **模块持久化数据**: MGR 模块不持久化数据，数据通过 MON 进行持久化。

#### 8. **后续行动计划**
   - **性能优化**: 进一步测试和验证模块分布式加载和 GIL 优化方案。
   - **Op Tracker 改进**: 增加模块级别的操作跟踪，提升故障排查效率。
   - **审计日志模块**: 开发审计日志模块，记录离线工具的操作历史。
   - **集群历史信息**: 记录集群的历史信息，便于未来故障排查和优化。



**总结**: 本次会议详细讨论了 Ceph Manager 的架构、模块加载机制、状态切换、GIL 管理以及 Op Tracker 的功能。未来将重点优化 MGR 的性能和可扩展性，增加模块级别的操作跟踪和审计日志功能，以提升集群的管理和故障排查效率。