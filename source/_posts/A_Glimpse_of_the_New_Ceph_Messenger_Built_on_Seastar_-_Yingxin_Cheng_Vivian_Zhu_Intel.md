---
title: "  A Glimpse of the New Ceph Messenger Built on Seastar - Yingxin Cheng & Vivian Zhu, Intel  "
date: 2019-05-24
updated: 2019-05-24
tags:
- Ceph
- 分布式存储
- 性能优化
categories:
- "视频总结"
subtitle: A_Glimpse_of_the_New_Ceph_Messenger_Built_on_Seastar_-_Yingxin_Cheng_Vivian_Zhu_Intel
---

### 改进后的中文总结

会议纪要

**会议时间**： 2023年X月X日

**会议主题**： Ceph 新消息传递组件（Crimson Messenger）基于 Seastar 的开发进展

**参会人员**： Intel，Ceph 团队成员

**会议内容**：

**一、背景介绍**

*   Ceph 核心对象层重构项目（Crimson）旨在提升在现代硬件上的性能。
*   现代硬件特点：多核心、NUMA 架构、高速存储设备（如 NVMe SSD、持久内存）、高速网络。
*   SAP 架构和 POSIX 线程存在性能瓶颈，需要优化。

**二、Crimson Messenger 的目标**

1.  利用 C++ Star 框架实现同步编程，统一架构。
2.  实现跨核心通信的最小化，建立直接核心到核心连接。
3.  利用 C++ Star 框架进行性能验证和优化。

**三、Crimson Messenger 的设计**

1.  基于 C++ Star 框架，实现异步 I/O、任务调度、网络堆栈等功能。
2.  实现直接核心到核心连接，减少跨核心通信。
3.  利用 C++ Star 框架的异步编程模型，实现代码简洁、易于维护。

**四、性能测试**

*   与现有异步消息传递组件进行性能对比，Crimson Messenger 在大部分场景下性能更优。
*   利用 C++ Star 框架的异步编程模型，实现代码简洁、易于维护。

**五、挑战和未来工作**

1.  C++ Star 框架的功能不够完善，可能需要定制化实现。
2.  需要深入了解 C++ Star 框架的编程模型，才能正确实现代码。
3.  需要持续优化性能，并确保可靠性。

**六、行动计划**

1.  完成 Crimson Messenger 的核心功能。
2.  进行性能测试和优化。
3.  评估 C++ Star 框架的定制化需求。
4.  将 Crimson Messenger 集成到 Ceph 中。

**七、总结**

Crimson Messenger 是 Ceph 核心对象层重构项目的重要组成部分，旨在提升 Ceph 在现代硬件上的性能。目前，Crimson Messenger 已取得初步进展，但仍面临一些挑战。未来，Ceph 团队将继续努力，确保 Crimson Messenger 的成功应用。

### 错误、误解或遗漏的信息

*   原始字幕中提到的 "Seastar" 应为 "C++ Star"，是 Seastar 框架的简称。
*   原始字幕中未提及的具体技术细节，如 C++ Star 框架的具体功能和优势，在总结中有所体现。
*   原始字幕中提到的 "Crimson OSD" 和 "Crimson Messenger" 的关系，在总结中得到了强调。