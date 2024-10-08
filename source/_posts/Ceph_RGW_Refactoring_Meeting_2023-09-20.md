---
title: "Ceph RGW Refactoring Meeting 2023-09-20"
date: 2023-10-04
updated: 2023-10-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：每周RGW会议

#### 日期：[具体日期]

#### 参会人员：[参会人员名单]

#### 主要议题：

1. **通知和SNS主题策略**
   - **讨论内容**：
     - Matt介绍了关于通知和SNS主题策略的讨论，涉及IAM和S3策略，特别是SNS API的使用。
     - 讨论了服务控制策略（Service Control Policy, SCP）和站点控制策略（Site Control Policy），这些策略可能需要通过扩展API或仪表板来支持。
   - **决定事项**：
     - 计划实现SNS主题策略，并考虑通过RGW管理命令和API来设置，如果标准IAM或S3 REST API不支持。
   - **后续行动**：
     - 继续探讨和实现SNS主题策略，并考虑添加相关API扩展。

2. **持久通知的性能**
   - **讨论内容**：
     - Yuvall介绍了持久通知性能的PR，讨论了当前使用单个工作线程从队列读取通知并发送至Kafka的机制。
     - 讨论了增加更多工作线程的可能性，以及这可能带来的性能影响。
   - **决定事项**：
     - 认为增加更多工作线程可能不会显著提升性能，因为瓶颈可能在写入队列的操作。
   - **后续行动**：
     - 考虑添加更多Kafka客户端统计信息，以更好地理解系统性能和潜在瓶颈。
     - 进行测试以验证单线程是否是瓶颈，并评估增加线程的影响。

#### 其他讨论：

- 讨论了队列填充的两种场景：队列未及时清空和Kafka代理响应慢。
- 提出了通过增加Kafka客户端统计信息来更好地诊断问题。

#### 结论：

- 会议决定继续探索和实现SNS主题策略，并通过增加Kafka客户端统计信息来优化持久通知的性能。
- 将继续进行性能测试，以验证单线程是否是瓶颈，并评估增加线程的影响。

#### 下次会议预告：

- 下次会议将继续讨论相关议题，并根据测试结果调整优化策略。

#### 会议结束：

- 感谢所有参会人员，下次会议再见。

---

**注：** 以上纪要涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。