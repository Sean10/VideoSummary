---
title: "  2019-07-09 :: Crimson SeaStor OSD Weekly Meeting  "
date: 2019-07-11
updated: 2019-07-12
tags:
- Ceph
- 分布式存储
- CI/CD
categories:
- "视频总结"
subtitle: 2019-07-09_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
---

**会议纪要**

**会议时间**： 2019年7月9日

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph分布式存储项目进展及讨论

**会议内容**：

**一、Crimson存储引擎讨论**

*   **问题**： Crimson存储引擎在处理大量客户端请求时，存在队列深度不足的问题，可能导致性能瓶颈。
*   **解决方案**： 提高队列深度并增加客户端请求时间，以避免性能问题。
*   **关键点**： 需要更新Crimson存储引擎，以支持更高的队列深度和客户端请求时间。

**二、输入缓冲区工厂**

*   **问题**： 输入缓冲区工厂的细节讨论，特别是用户空间IP/TCP在Crimson中的实现。
*   **解决方案**： 
    *   研究内存复制操作在原生堆栈中的实现，特别是在运行助手应用程序时。
    *   引入iommu和PTEs来提高安全性。
    *   优化DMA和内存复制操作，以支持不同的硬件平台。
*   **关键点**： 
    *   需要支持不同的DMA技术，如InfiniBand和RoCE。
    *   需要抽象内存复制操作，以便在不同平台之间进行替换。

**三、CI/CD流程**

*   **问题**： Jenkins不支持CBT，且无法访问Pelagic。
*   **解决方案**： 
    *   创建本地CI/CD流程，使用Docker进行测试。
    *   使用脚本启动和停止测试实例。
*   **关键点**： 
    *   需要创建脚本，用于启动和停止测试实例。
    *   需要选择合适的CI/CD工具。

**四、错误处理**

*   **问题**： 需要处理从对象存储传播的错误。
*   **解决方案**： 
    *   使用error handling primitives，如ignore和fork。
    *   优化现有代码，以使用新的error handling primitives。
*   **关键点**： 
    *   需要确定最佳的error handling strategy。
    *   需要测试新的error handling primitives。

**五、其他**

*   **Crimson协议**： 
    *   修复与Crimson消息传递相关的bug。
    *   清理协议v2的日志。
    *   理解握手过程。
*   **工具**： 
    *   需要一个通用的工具，用于捕获和发送Crimson协议v2包。
    *   需要一个Crimson协议v2的Wireshark插件。

**后续行动计划**：

*   **Crimson存储引擎**： 更新Crimson存储引擎，以支持更高的队列深度和客户端请求时间。
*   **输入缓冲区工厂**： 优化内存复制操作，支持不同的硬件平台。
*   **CI/CD流程**： 创建本地CI/CD流程，使用Docker进行测试。
*   **错误处理**： 确定最佳的error handling strategy，并优化现有代码。
*   **Crimson协议**： 修复与Crimson消息传递相关的bug，清理协议v2的日志，理解握手过程。
*   **工具**： 开发一个通用的工具，用于捕获和发送Crimson协议v2包，以及一个Crimson协议v2的Wireshark插件。

**备注**：

*   部分计算机科学/ceph相关领域英文原文的关键词已保留在会议纪要中。
*   会议纪要已涵盖会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。