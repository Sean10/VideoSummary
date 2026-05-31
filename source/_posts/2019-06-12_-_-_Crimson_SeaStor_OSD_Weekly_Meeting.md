---
categories:
- 视频总结
date: 2019-06-12
subtitle: 2019-06-12_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
tags:
- Ceph
- 分布式存储
- 测试
- 性能优化
title: "'2019-06-12:: Crimson SeaStor OSD Weekly Meeting'"
updated: 2019-06-13
---



### 会议纪要

**会议时间**： 2023年11月X日

**参会人员**： Lisa, Sam, Riddick, Robin, Tamara 等

**会议主题**： Ceph分布式存储项目开发讨论

**会议内容**：

**一、Crimson Flavor 新特性**

1. 引入新的 Crimson Flavor，用于病理学安装任务和 CBD 测试，作为性能基准与 CI 中的性能测试进行比较。
2. 将进行性能测试，使用 Crimson 包验证 PR，并逐步将其纳入夜间测试。

**二、Jenkins 和 Make Check 集成**

1. 使用与 CBT 相同的简单测试集，用于 Jenkins 和 Make Check 的验证。
2. 需要能够运行低级和崩溃测试，以验证 OSD 功能。

**三、输入缓冲区概念**

1. 推出支持输入缓冲区概念的 RFC 第三版，该概念支持基本对齐和额外部分。
2. 进行了性能测试，并提供了测试结果。

**四、内存对齐问题**

1. 使用 scatter gather 读取大块数据时，可能会遇到内存对齐问题。
2. 推出输入缓冲区工厂，以提供更灵活的内存管理，并解决对齐问题。

**五、其他讨论**

1. 讨论了在连接中使用 private 接口的问题，以确保不会滥用该接口。
2. 讨论了如何正确读取数据段，并确保数据对齐。

**后续行动计划**：

1. 完成输入缓冲区概念的实现。
2. 更新安装任务，以使用 Crimson Flavor。
3. 完成性能测试，并逐步将其纳入夜间测试。
4. 完成RFC第三版的审查和反馈。

**备注**：

* 会议中提到了一些计算机科学/ceph相关领域英文原文的关键词，如：Crimson Flavor、performance testing、input buffer factory、scatter gather、private interface 等。
* 会议讨论的内容涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。