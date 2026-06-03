---
title: "Ceph Performance Meeting 2018-11-15"
date: 2018-11-15
updated: 2018-11-16
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "BlueStore"
  - "RocksDB"
  - "缓存"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2018年11月15日

**参会人员**： Radek、Alex、Ben、Jesse等

**会议主题**： Ceph存储项目性能优化进展及讨论

**会议内容**：

**一、Ceph项目性能优化进展**

* **Radek**：
    * 优化buffer管理，移除pen buffer，减少不必要的原子操作。
    * 开发hyper combined buffers，提高buffer列表迭代效率。
    * 处理RDMA相关工作，提升性能。
    * 优化EC striped cache功能。
    * 开发auto-tuner改进方案，优化BlueStore缓存行为。
* **Alex**：
    * 进行BlueStore性能测试，分析读写性能。
    * 发现read ahead机制可能影响测试结果。
    * 分析小随机写性能问题，探讨优化方案。
* **Ben**：
    * 分析BlueStore性能测试结果，探讨优化方向。
    * 探讨RocksDB调优方案，优化小随机写性能。
    * 开发VLA优化方案，减少内存拷贝。
* **Jesse**：
    * 完成GW的VLA优化工作。

**二、讨论的主要议题**

* **buffer优化**： 讨论了优化buffer管理，减少不必要的原子操作，提高效率。
* **hyper combined buffers**： 开发hyper combined buffers，提高buffer列表迭代效率。
* **RDMA优化**： 提升RDMA性能。
* **EC striped cache优化**： 优化EC striped cache功能。
* **BlueStore性能优化**： 分析BlueStore性能测试结果，探讨优化方向，包括read ahead机制、RocksDB调优等。
* **VLA优化**： 开发VLA优化方案，减少内存拷贝。

**三、决定的事项**

* 继续推进Radek的buffer优化和hyper combined buffers开发。
* 进一步分析Alex的BlueStore性能测试结果，确定优化方案。
* 探索RocksDB调优方案，优化小随机写性能。
* 完成Jesse的VLA优化工作。

**四、后续行动计划**

* **Radek**： 完成buffer优化和hyper combined buffers开发。
* **Alex**： 继续进行BlueStore性能测试，分析测试结果，确定优化方案。
* **Ben**： 分析RocksDB调优方案，优化小随机写性能。
* **Jesse**： 完成VLA优化工作。

**五、其他事项**

* 下周将不召开会议，因为感恩节假期。

**总结**：

本次会议重点讨论了Ceph存储项目的性能优化进展，涵盖了buffer优化、hyper combined buffers、RDMA优化、EC striped cache优化、BlueStore性能优化和VLA优化等多个议题。会议明确了后续行动计划，为Ceph存储项目的进一步发展奠定了基础。