---
categories:
- 会议纪要
date: 2018-10-18
subtitle: Ceph_Performance_Meeting_2018-10-04
tags:
- Ceph
- 分布式存储
- 性能
- BlueStore
title: Ceph Performance Meeting 2018-10-04
updated: 2018-10-18
---



会议纪要

**会议时间**： 2018年10月4日

**参会人员**： Adam, Nick, Sage, Casey, Jason 以及其他未具名成员

**会议主题**： Ceph 存储系统开发进展和讨论

**会议内容**：

**1. 新 pull requests**

* Radek 提交的 pull request 改进了字符串处理，这是一个相对较小的改动，但效果显著。
* Lebar 和 BD 共享的持久只读 RBD 缓存工作正在进行中，可能即将有新的代码提交。

**2. Quick Blue Store 评估**

* Nick 对 Quick Blue Store 进行了实际评估，发现其性能表现良好，但存在一些问题。
* **优点**：
    * 压缩率约为 1.5 倍。
    * 重写操作简单。
    * SSD 预测写入性能提升。
    * 快照性能更好。
* **缺点**：
    * 部分用例中性能较差。
    * 延迟写入对新对象不适用，导致性能下降。
    * 中等大小的写入操作（64KB 到 512KB）性能较差，因为超过延迟写入阈值后，所有操作都依赖于底层磁盘速度。
    * 缺少合并，导致磁盘利用率过高。
* **建议**：
    * 增加延迟写入阈值，以覆盖更大尺寸的写入操作。
    * 考虑在 Blue Store 中使用缓存撕裂和写回技术。
    * 使用 RAID 控制器和电池备份缓存，以改善性能。

**3. ASIO 和 C++ 异步库**

* Adam 介绍了 ASIO 异步网络和 I/O 层，它基于反应器模式，可以减少线程数量并提高效率。
* ASIO 库的目的是：
    * 提供一个原生异步和集成到 Ceph 中的库。
    * 避免不必要的内存分配。
    * 提供更高级别的功能，例如命名空间和定位键。
    * 统一 Rados 的各种线程执行上下文。
* Sage 和 Casey 讨论了 ASIO 库在 RGW 中的应用，包括协程和线程池。

**4. 后续行动计划**

* Nick 将继续对 Quick Blue Store 进行测试和评估。
* Adam 将继续开发 ASIO 库，并与其他开发者合作改进其性能。
* Sage 和 Casey 将探索 ASIO 库在 RGW 中的应用。
* Jason Dolman 将参与性能测试和评估。

**会议总结**：

本次会议讨论了 Ceph 存储系统开发中的多个重要议题，包括 Quick Blue Store 的性能评估和 ASIO 异步库的开发。与会者就这些问题进行了深入讨论，并制定了后续行动计划。