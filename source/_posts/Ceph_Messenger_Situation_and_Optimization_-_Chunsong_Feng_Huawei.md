---
categories:
- 技术文章
- 存储技术
- Ceph架构
- 网络优化
- 性能测试
date: 2023-05-05
subtitle: Ceph_Messenger_Situation_and_Optimization_-_Chunsong_Feng_Huawei
tags:
- Ceph
- Distributed Storage
- Performance Optimization
- RDMA
- UCX
title: "Ceph Messenger Situation and Optimization - Chunsong Feng, Huawei"
updated: 2023-05-05
---




### 会议纪要

#### 会议主题：Ceph 消息传递情况与优化

#### 会议议程：
1. **当前RDMA消息模块的不足**
2. **在自消息模块中启用UCX（Unified Communication X）的措施**
3. **性能测试结果**

#### 讨论内容：

1. **当前RDMA消息模块的问题**
   - 流量控制缺失导致性能波动。
   - 数据复制问题在发送和接收路径中存在。
   - 使用限制，客户端和服务器需要使用RDMA连接，但客户端通常没有RDMA设备。
   - 固定长度消息使用影响效率。

2. **UCX架构与关键设计**
   - 引入UCX堆栈，使用UCX连接客户端和服务器。
   - 中断与轮询模型处理设备事件。
   - 使用不同协议处理不同大小的消息。
   - 选择实际消息API实现零拷贝接收。

3. **自RDMA与UCX堆栈的运行模块**
   - 使用RDMA轮询线程和匹配工作者，共享QPL连接。
   - 优化锁和会话调用，使用连接映射，消除日志需求。

4. **零拷贝接收**
   - 实现两个映射分别处理小包和大包。
   - 预分配内存提高接收效率。

5. **性能测试**
   - 基准测试显示UCX堆栈表现出更好的性能和效率。
   - 类性能测试使用RBDs测试，实现约20%的性能提升。

#### 未来计划：
- 性能调优，尝试更多协议和发送接收协议。

#### 提问与回答：
- 与TCP相比，性能提升约10%。
- 尚未进行延迟测试，但UCX可能提供更低的延迟。
- RDMA代码集成问题，需要移除中间层以充分利用RDMA。

#### 决定事项：
- 计划在三周内创建拉取请求，将UCX消息传递整合到主分支。

#### 后续行动计划：
- 整合UCX消息传递。
- 进行延迟测试，特别是尾延迟，以展示UCX的优势。

#### 会议结束：
- 感谢所有参与者的贡献和讨论，会议圆满结束。

[会议纪要结束]