---
title: "  CDS Hammer (Day 1) - Accelio RDMA Messenger  "
date: 2014-10-29
updated: 2014-10-30
tags:
- Ceph
- 分布式存储
categories:
- "视频总结"
subtitle: CDS_Hammer_Day_1_-_Accelio_RDMA_Messenger
---



在本次 CDS Hammer (Day 1) 会议中，Accelio RDMA Messenger 的工作讨论是重点。以下是会议内容的总结：

**会议主题**：Accelio RDMA Messenger 工作讨论

**会议内容**：

* **Accelio RDMA Messenger 最新进展**：
    * Melanox 团队在 Accelio 中增加了多传输支持，并使 TCP 传输更加功能丰富。
    * 开发了新的显式流控制接口，以允许应用程序更好地控制 XIO 消耗的资源。
    * 集成了不同的 RDMA 内存模型、传输内存模型和缓冲区模型。
    * Ceph 团队完成了 XL Messenger 的重大重构，以提高效率。
    * 开发了新的会话管理功能，以支持更多的 Messenger 接口。
* **Ceph 团队的工作**：
    * 开发了一个新的内存缓冲区模型，以提高效率。
    * 开发了一个新的流控制机制，以避免内存池耗尽。
    * 开发了一个新的测试套件，以测试不同的 Messenger 实现。
* **后续行动计划**：
    * Ceph 团队将在未来几周内提交相关代码更改。
    * 将与其他团队合作，以确保代码的兼容性和稳定性。
    * 开发新的测试套件，以测试 Messenger 实现。

**关键细节**：

* **Accelio RDMA Messenger**：用于 Ceph 分布式存储的 RDMA Messenger。
* **多传输支持**：支持多种传输协议，例如 TCP 和 RDMA。
* **流控制**：用于控制资源使用和避免资源耗尽。
* **内存缓冲区模型**：用于管理内存缓冲区。
* **会话管理**：用于管理 Messenger 会话。

**讨论的主要议题**：

* Accelio RDMA Messenger 的最新进展。
* Ceph 团队的工作。
* 代码集成和测试。

**决定的事项**：

* Ceph 团队将在未来几周内提交相关代码更改。
* 将与其他团队合作，以确保代码的兼容性和稳定性。
* 将开发新的测试套件，以测试 Messenger 实现。

**后续行动计划**：

* Ceph 团队将在未来几周内提交相关代码更改。
* 将与其他团队合作，以确保代码的兼容性和稳定性。
* 将开发新的测试套件，以测试 Messenger 实现。