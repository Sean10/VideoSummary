---
title: "RH InkTank Ceph Day Sessions Matt Benjamin COHORTFS"
date: 2014-07-25
updated: 2014-07-26
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议时间**： [请填写会议时间]

**会议地点**： [请填写会议地点]

**参会人员**： Matt Benjamin（CTO of Word and），其他与会人员

**会议主题**： Ceph项目进展及Accelio集成

**会议内容**：

**一、项目背景**

- Word and是一家位于密歇根州安阿伯的初创公司，专注于将新功能引入并行NFS，以应对新的应用工作负载。
- 该项目最初由NSF资助，后来扩展到SAP存储堆栈，以增强其功能。

**二、Accelio集成**

- Accelio是一个高性能异步和可靠的消息库，支持硬件加速，旨在构建高性能RPC传输。
- 该项目与Melanox合作，将Ceph代码库与Accelio集成，以实现高效的传输和消息传递。
- 该项目的主要目标是提高Ceph的性能，特别是在单位级别的高性能I/O性能。

**三、Accelio关键特性**

- 支持RMA传输，未来将支持多种传输。
- 支持请求/响应协议和单向协议，支持多种交付语义。
- 支持零拷贝，内部消息路径几乎无锁。
- 优化线程/CPU并行，减少应用参与度。
- 支持高达三百万个应用程序，能够饱和单个端口。

**四、XIO Messenger**

- XIO Messenger是Accelio的适配器，用于将Ceph网络或消息传递映射到Infiniband。
- 它是一个可插入的替代品，可以与当前的TCP消息封装一起使用。
- XIO Messenger旨在实现零拷贝和线程级别的并行。

**五、Ceph代码库重构**

- 为了更好地集成Accelio，Ceph代码库正在进行重构。
- 重构的目标是提取通用代码，以便所有消息传递器都可以使用。

**六、性能测试**

- 使用Accelio进行性能测试，结果表明其性能良好。
- 在64k消息大小下，几乎饱和了XIO的可用带宽。

**七、项目状态**

- XIO Messenger堆栈已完成，已集成到Ceph中。
- 项目正在进行中，旨在使Ceph集群能够在XIO上运行。
- 项目代码可在Accelio和Ceph的GitHub仓库中找到。

**八、后续行动计划**

- 继续优化Ceph代码库。
- 完成Ceph集群在XIO上的测试和验证。
- 将XIO集成到Ceph的主要分支中。

**九、其他事项**

- 项目团队将继续关注Ceph和Accelio的最新动态，以确保项目的顺利进行。

**总结**：

本次会议介绍了Ceph项目进展和Accelio集成的情况。项目团队正在努力提高Ceph的性能，并使其能够支持更高效的消息传递。项目进展顺利，预计将在未来推出全新的Ceph版本。