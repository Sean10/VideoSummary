---
title: "Ceph Crimson/SeaStore 2021-07-07"
date: 2021-08-24
updated: 2021-08-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- Aaron
- Jeremy
- Riddick
- 其他相关研发人员

#### 主要议题
1. **Crimson项目的清理和讨论**
   - Aaron分享了上周在Crimson项目中进行的一些随机清理工作，并讨论了与Jihan关于扩展分配管理器的PR。

2. **IOCTL和控制支持的补丁更新**
   - Aaron提到正在开发Ceph的IOCTL和控制支持的下一个补丁版本，并已提交并接收了一些评审意见。同时，他开始在Ceph的Segment Manager中实现相应的接口。

3. **Extent内容的更新问题**
   - Aaron报告了一个关于Extent内容更新的问题，特别是在并发操作中，Extent内容可能会被其他操作更新，导致最终获取到错误的地址。他提出了一个临时的解决方案，并进行了一些测试。

4. **MLIS案例分析**
   - Riddick分享了关于MLIS（Multi-Level Index Structure）案例的分析，指出问题可能与消息处理有关，特别是在OSD重启时可能发生的竞态条件。

5. **Extent Placement Manager的修改**
   - 某位参会者（未明确姓名）讨论了Extent Placement Manager的修改，包括如何处理Extent的写入和日志记录。

6. **C-Store性能分析**
   - 另一位参会者（未明确姓名）提到正在进行C-Store的性能分析，并尝试添加矩阵以帮助诊断性能问题。

#### 决定事项
- Aaron将继续优化Extent内容的更新问题，并寻找更稳定的解决方案。
- Riddick将继续分析MLIS案例，特别是关注消息处理和OSD重启时的竞态条件。
- 对于Extent Placement Manager的修改，将继续进行多设备支持的实现。

#### 后续行动计划
- Aaron将提交更新的补丁版本，并继续在Segment Manager中实现接口。
- Riddick将深入研究MLIS案例，并寻找可能的解决方案。
- 所有参会者将继续关注各自负责的模块，确保Ceph的稳定性和性能优化。

#### 其他讨论
- 会议中还讨论了关于消息处理的防御性编程，以及如何在集群中处理可能的错误消息。

#### 会议结束
- 会议在讨论了所有议题后结束，参会者表示将继续跟进各自的任务，并保持沟通。

---

**注：** 会议中提到的具体技术细节和代码问题需要进一步的技术文档和代码审查来详细理解和解决。