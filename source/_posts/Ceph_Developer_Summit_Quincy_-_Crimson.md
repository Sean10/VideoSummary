---
title: "Ceph Developer Summit Quincy: Crimson"
date: 2021-04-08
updated: 2021-04-08
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主题一：适应Ceph的Boost ASIO代码到C-Star Reactor
- **讨论内容**：
  - 现有代码依赖Boost ASIO，讨论如何将其适配到C-Star Reactor中。
  - 探讨是否可以通过包装和适当的回调函数来直接在Reactor中运行。
  - 初步认为需要进一步调查是否需要进行此项工作，特别是对于实时RBD（Live RBD）。

- **决定事项**：
  - 需要进一步调查和评估将Boost ASIO代码适配到C-Star Reactor的可行性和必要性。
  - 可能需要一个初始原型来验证代码的适配情况。

- **后续行动计划**：
  - 由熟悉Boost ASIO和C-Star的开发人员进行深入调查和原型开发。

#### 主题二：Rapid CAR Diamond和Rapid CAR Monitor设计
- **讨论内容**：
  - 讨论了如何设计Replica Daemon和Rapid CAR Monitor来管理复制信息。
  - 现有设计涉及在Replica Monitor中维护Replica Daemon的信息，包括RDMA的IP地址和端口等。

- **决定事项**：
  - 需要重新考虑是否需要在Monitor中维护这些信息，可能通过RADOS对象和watch/notify机制来实现更为合适。

- **后续行动计划**：
  - 重新评估和设计Replica Daemon和Rapid CAR Monitor的管理机制，避免对Monitor的过度依赖。
  - 向社区征求反馈和建议，进一步优化设计。

#### 主题三：Crimson的多核支持与M2N映射
- **讨论内容**：
  - 讨论了如何在Crimson中实现多核支持，包括处理客户端连接、PG状态和后端存储实现。
  - 探讨了是否需要在Messenger中实现多核支持，以及如何处理跨核通信。

- **决定事项**：
  - 决定先实现PG在多个核心上的分布，再考虑Messenger和C-Store的多核支持。
  - 需要实现一个跨核服务来管理PG到核心的映射。

- **后续行动计划**：
  - 开发跨核服务，实现PG到核心的映射。
  - 逐步实现Messenger和C-Store的多核支持。

#### 主题四：C-Store的当前状态和未来工作
- **讨论内容**：
  - 回顾了C-Store的当前进展，包括事务层、逻辑块映射、OMAP和垃圾回收等。
  - 讨论了如何支持ZNS设备和其他可变存储设备。

- **决定事项**：
  - 需要进一步的工作来优化C-Store的性能和稳定性，包括引入更多的性能指标和调试工具。

- **后续行动计划**：
  - 引入性能指标和调试工具，优化C-Store的性能和稳定性。
  - 探索和支持新的存储设备，如ZNS和持久内存。

### 总结
本次会议涵盖了多个关键议题，包括Boost ASIO代码的适配、Rapid CAR Monitor的设计、Crimson的多核支持和C-Store的优化。每个议题都有明确的后续行动计划，旨在推动Ceph的进一步发展和优化。