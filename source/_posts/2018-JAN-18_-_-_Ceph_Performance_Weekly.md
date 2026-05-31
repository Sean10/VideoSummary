---
categories:
- 视频总结
date: 2018-01-20
subtitle: 2018-JAN-18_-_-_Ceph_Performance_Weekly
tags:
- Ceph
- 分布式存储
- 性能优化
title: "'2018-JAN-18 :: Ceph Performance Weekly'"
updated: 2018-01-20
---



### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Ron, Adam, Jason, Igor, Josh, Greg, Mark, Chimay, Stephanie, Avi, Georgia, 以及其他相关人员

**会议主题**：

* Ceph 存储系统最新进展
* VPP 集成方案探讨
* 性能优化策略讨论
* Specter 漏洞影响评估

### 会议内容：

**1. Ceph 存储系统最新进展**

* **代码合并与优化**：
    * Jason 审核并合并了 Igor 的几个小优化，包括近似眼睛（aprox eyes）功能。
    * Jason 还合并了一个 pull request，该 pull request 通过优化读取操作来提高性能。
    * Ron 考虑完全消除对象存储接口中的 applied 回调，并使用跟踪和快速操作。
    * Ron 关闭了旧的同步请求，因为他已经完成了读操作的一半工作，但不确定是否要继续进行写操作。
* **性能优化**：
    * Ron 考虑使用构建购买概念来测试性能影响。
    * Josh 提交了一个 pull request，用于将随机拆分阈值随机化，以提高 Jewel 版本的性能。
    * Ron 提到了一个 QAT 等级类，但不确定其最新更新。

**2. VPP 集成方案探讨**

* **VPP 简介**：
    * Stephanie 介绍了 VPP（虚拟包处理）软件栈，该软件栈提供了一种高效的网络处理方式。
    * VPP 支持多种接口，包括 VPP 通信库、TCL API 和 DPDK 内存接口。
    * Stephanie 使用了预加载模式，即 VPP 库钩子到 POSIX 套接字层，从而在用户空间中处理网络操作。
* **集成方案讨论**：
    * Ron 认为直接使用 VPP API 可能更合适，因为它可以提供更好的性能和异步操作。
    * 讨论了 VPP 与 CStar 网络编程框架的兼容性，以及如何使用 CStar API 与 VPP 通信。
    * 讨论了将 VPP 作为 RGW 插件的可能性。

**3. 性能优化策略讨论**

* **Boost 优化**：
    * Mark 总结了 Boost 优化方案的测试结果，发现一些优化方案对性能提升有限，例如批处理事务和跳表。
    * Ron 认为使用多个提示符（hints）的 RocksDB 内部功能可能有助于提高性能，但需要进一步测试。
* **Specter 漏洞影响评估**：
    * Ron 认为 Specter 漏洞可能会对 Intel 处理器的性能产生严重影响，尤其是在进行大量 CPU 密集型操作时。
    * Red Hat 性能团队正在研究 Specter 漏洞的解决方案。

**4. 其他讨论**

* **Wall Clock Profiler**：
    * Adam 介绍了 Wall Clock Profiler 工具，该工具可以模拟 Marc 的 Wall Clock Profiler 的行为，并提供更快的采样率。
    * Adam 还表示，他愿意将 Wall Clock Profiler 集成到 CBT 中，以便在测试过程中进行性能分析。
* **New Store 与 Blue Store 比较**：
    * Ron 回顾了 New Store 和 Blue Store 的性能比较，发现 Blue Store 在大写和随机写操作方面表现更好。
    * Ron 认为读取预取在 Blue Store 中非常重要。
* **EC Bug Regression**：
    * Ron 讨论了对象存储层中未读回调的问题，并提出了一种简化代码的方案。

### 行动计划：

* **VPP 集成**：
    * 与 Avi 和 Georgia 讨论将 VPP 集成到 Ceph 的可能性。
    * 对 VPP 进行性能测试，并评估其与 CStar 的兼容性。
* **性能优化**：
    * 进一步测试 RocksDB 内部功能，并评估其对性能的影响。
    * 研究 Specter 漏洞的解决方案，并评估其对 Ceph 性能的影响。
* **代码简化**：
    * 简化对象存储接口，以消除未读回调和锁。
    * 将 Wall Clock Profiler 集成到 CBT 中。

### 总结：

本次会议讨论了 Ceph 存储系统的最新进展、VPP 集成方案、性能优化策略和 Specter 漏洞影响评估。会议确定了行动计划，并推动了 Ceph 存储系统的进一步发展。