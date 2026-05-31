---
categories:
- 视频总结
date: 2023-05-10
subtitle: Ceph_RGW_Refactoring_Meeting_2023-05-10
tags:
- Ceph
- RGW
- 分布式存储
title: "Ceph RGW Refactoring Meeting 2023-05-10"
updated: 2023-05-11
---




### 会议纪要

#### 会议主题：Kafka库在RGW中的应用与代码走查讨论

#### 与会人员：Yuval, Daniel, Thomas 等

#### 会议时间：2023年5月10日

#### 主要议题：

1. **Kafka库实现问题讨论**
   - **问题背景**：用户在使用Kafka库时报告了回归问题，特别是在设置ACK级别时出现重试。
   - **问题分析**：Yuval发现，问题源于Kafka库内部的重试机制与我们代码库中的机制冲突。我们的机制需要能够应对崩溃和重启等情况，而Kafka库的机制则无法持久化。
   - **解决方案讨论**：
     - 讨论了禁用Kafka库内部重试机制的可行性。
     - 提出允许用户通过配置文件控制Kafka库某些行为，以增加灵活性。
     - 最终决定，在ACK级别为“broker”时允许内部重试，而在ACK级别为“none”时禁用。

2. **代码走查提议**
   - **提议人**：Daniel
   - **提议内容**：提议进行代码走查，以传播关于RGW代码库的知识，特别是tracing和Lua代码的走查。
   - **反馈**：Yuval表示对tracing的走查感兴趣，但希望在OSD编码问题解决后再进行。Thomas表示愿意进行Lua代码的走查。

#### 决定事项：

- 对于Kafka库的重试机制，决定在ACK级别为“broker”时允许内部重试，而在ACK级别为“none”时禁用。
- 允许用户通过配置文件控制Kafka库的某些行为，以增加灵活性。
- 计划进行代码走查，特别是关于tracing和Lua代码的走查。

#### 后续行动计划：

- Yuval将对Kafka库的重试机制进行调整，并提交相关Pull Request（PR）。
- Daniel和Thomas将准备进行代码走查，具体时间待定。
- 需要关注OSD编码问题的解决进展，以便进行tracing的代码走查。

#### 会议结束：感谢所有参与者的贡献，会议圆满结束。