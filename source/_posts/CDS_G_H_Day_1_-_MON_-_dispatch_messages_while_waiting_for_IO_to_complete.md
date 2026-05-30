---
categories:
- 视频总结
date: 2014-06-24
subtitle: CDS_G_H_Day_1_-_MON_-_dispatch_messages_while_waiting_for_IO_to_complete
tags:
- Ceph
- Monitor
- I/O操作
- 异步化
- Paxos
- Work Queue
title: "'CDS G/H (Day 1) - MON: dispatch messages while waiting for IO to complete'"
updated: 2014-06-25
---



### 会议纪要

**会议时间**： 2014-06-24

**参会人员**： [请填写参会人员名单]

**会议主题**： Ceph Monitor消息派发及I/O操作优化

**会议内容**：

**1. 问题背景**

- Ceph Monitor在执行I/O操作时，处理消息的能力受限，导致等待时间长，影响整体性能。
- 主要问题在于单线程处理所有消息，当执行I/O操作时，其他消息处理被阻塞。

**2. 解决方案**

- 提出为Monitor添加新的Paxos节点，将控制权交给另一个线程，在等待I/O操作完成期间继续执行其他任务。
- 将I/O操作异步化，避免阻塞消息处理。
- 考虑使用读写锁机制，保护对状态信息的访问。

**3. 实施步骤**

- 异步化I/O操作，将任务提交给Key-Value存储，并等待回调。
- 使用Work Queue类创建工作线程，将事务指针传递给工作线程。
- 在安全的地方异步执行工作，并在完成后进行清理。
- 使用Work Queue的flush方法，等待异步操作完成。

**4. 注意事项**

- 确保异步操作在安全点进行，避免影响其他事件。
- 保持读写操作分离，确保持久化数据不会阻塞临时数据。
- 考虑将存储源分为已提交和未提交两部分，提高性能。

**5. 后续行动计划**

- 完成异步化I/O操作的代码实现。
- 测试新方案，评估性能提升效果。
- 根据测试结果，进一步优化方案。

**关键词**

- Monitor
- 消息派发
- I/O操作
- 异步化
- Paxos
- 读写锁
- Work Queue
- Key-Value存储