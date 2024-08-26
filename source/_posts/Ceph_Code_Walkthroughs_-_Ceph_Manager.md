---
title: "Ceph Code Walkthroughs: Ceph Manager"
date: 2021-12-14
updated: 2021-12-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph Manager 架构与功能概述

#### 会议时间：[具体时间]

#### 参会人员：[参会人员名单]

#### 会议内容总结：

1. **Ceph Manager 的创建背景与目的**
   - Ceph Manager 最初是为了减轻 Ceph Monitor 的负担而创建的，特别是在大型集群中，Monitor 需要处理大量的统计数据收集任务，这些任务原本由 OSD 和 MDS 等守护进程处理。
   - Manager 被设计为一个无状态的服务，不需要通过 Paxos 协议或持久化到磁盘，可以独立运行，并能根据需要将信息持久化到 Monitor 或 Rados 中。

2. **Manager 的核心组件与技术栈**
   - Manager 主要使用 C++ 和 Python 编写，核心组件类似于其他 Ceph 守护进程，使用相同的网络通信基础设施。
   - Manager 作为一个选择客户端连接到 Monitor，并订阅相关的应用以获取集群信息。

3. **Manager 的运行模式**
   - Manager 设计为活动-备用模式，其中只有一个 Manager 实例是活动的，负责与 Monitor 通信并发送心跳以表明其存活状态。
   - 如果活动 Manager 停止响应，Monitor 会选择另一个备用 Manager 成为活动 Manager。

4. **Manager 的功能扩展**
   - 除了处理集群统计数据，Manager 还支持多种模块，包括预测、编排、内部集群任务（如平衡 EGs）以及管理长时间运行的操作（如 RBD 或 CephFS）。

5. **Manager 的代码结构与初始化流程**
   - Manager 的入口点在 `src/mgr/Mgr.cc` 文件中，遵循典型的守护进程设置流程，包括解析命令行参数、环境变量、初始化网络地址绑定等。
   - Manager 初始化时会创建一个 Manager Standby 类，该类包含与集群通信所需的基础设施，如 Messenger、Monitor 客户端、Objecter 等。

6. **Python 模块的集成与管理**
   - Manager 使用 Python 模块来扩展功能，这些模块在 Manager 启动时从磁盘加载。
   - Python 模块运行在自己的主线程中，使用独立的 Python 解释器，避免模块间的状态共享和潜在的冲突。

7. **后续行动计划**
   - 继续深入研究 Manager 的各个模块和功能细节。
   - 探索 Manager 在处理集群统计数据和性能指标方面的优化潜力。
   - 定期回顾和更新 Manager 的文档，确保其与代码实现保持一致。

#### 会议结论：
- 本次会议对 Ceph Manager 的架构、功能和代码结构进行了全面的概述，为后续的深入研究和开发工作奠定了基础。

#### 后续跟进：
- 参会人员将继续关注 Manager 的开发进展，并根据需要提出进一步的问题和建议。

#### 会议记录人：[记录人姓名]

#### 会议结束时间：[具体时间]