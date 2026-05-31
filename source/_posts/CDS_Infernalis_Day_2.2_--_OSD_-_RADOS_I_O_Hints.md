---
categories:
- 视频总结
date: 2015-03-06
subtitle: CDS_Infernalis_Day_2.2_--_OSD_-_RADOS_I_O_Hints
tags:
- Ceph
- OSD
- RADOS
title: "'CDS Infernalis (Day 2.2) -- OSD: RADOS I/O Hints'"
updated: 2015-03-07
---



### 会议纪要

**会议主题**： OSD I/O 提升方案讨论

**会议时间**： 2023年X月X日

**参会人员**： John, Ping, 研发团队

**会议内容**：

* **议题一：OSD I/O 提升方案**
    * John介绍了Ceph中OSD I/O提升的方案，旨在提高客户端使用Ceph的效率。该方案利用了Ceph的认证框架、Live RBD和RBD库支持，并通过手动修改代码来实现。
    * 该方案使用CodeBunch作为I/O优化器，并通过手动修改代码来支持文件系统操作，优化内存使用和减少磁盘读取操作，以提高系统吞吐量和内存利用率。

* **议题二：IO hints的应用**
    * 讨论了IO hints在Ceph中的应用，包括：
        * 在文件系统中使用mount选项来控制I/O缓存行为。
        * 在RBD中使用不同的缓存策略，如不缓存、使用代理读取等。
        * 在后台操作中使用no-catch选项来避免缓存热点数据。
    * 讨论了IO hints的局限性，例如：
        * Linux内核不支持无缓存读取操作。
        * 需要考虑多客户端同时访问同一对象时的缓存策略。
        * 需要权衡缓存和性能之间的平衡。

* **议题三：后续行动计划**
    * 继续在Hammer版本中实现IO hints框架，并在Live Lab中进行测试。
    * 评估并实现更多IO hints选项，例如：
        * 物理设备缓存选项。
        * 虚拟设备缓存选项。
        * 后台操作缓存选项。
    * 优化IO hints的实现，解决Linux内核不支持无缓存读取操作的问题。

**决定事项**：

* 继续推进IO hints的实现，并评估更多应用场景。
* 在Hammer版本中实现IO hints框架，并在Live Lab中进行测试。
* 优化IO hints的实现，解决Linux内核不支持无缓存读取操作的问题。

**后续行动计划**：

* 研发团队将根据会议讨论结果，继续推进IO hints的实现。
* 研发团队将与内核社区合作，解决Linux内核不支持无缓存读取操作的问题。
* 研发团队将定期更新会议纪要，并汇报项目进展。