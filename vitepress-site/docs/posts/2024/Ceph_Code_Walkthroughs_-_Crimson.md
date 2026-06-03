---
title: "Ceph Code Walkthroughs: Crimson"
date: 2024-03-06
updated: 2024-03-07
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "性能"
  - "BlueStore"
  - "BlueFS"
  - "RocksDB"
  - "OSD"
  - "MON"
  - "MDS"
  - "PG"
  - "RADOS"
  - "librados"
  - "libcephfs"
  - "RBD"
  - "RGW"
  - "RESTful API"
  - "Erasure Coding"
  - "iSCSI"
  - "NFS"
  - "CIFS"
  - "POSIX"
  - "监控"
  - "Dashboard"
  - "编排"
  - "自动化"
  - "容器化"
  - "Kubernetes"
  - "Docker"
  - "云计算"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "存储集群"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
categories:
  - "视频总结"
outline: deep
---
### 改进的中文总结

Ceph 代码分析会议 "Crimson" 主要讨论了Ceph存储系统中Crimson代码与经典代码的差异，特别是使用seastar框架的情况。以下是会议的关键细节和讨论要点：

#### 关键细节
- **主题**: 分析Crimson代码与经典代码的差异，特别是使用seastar框架。
- **参与者**: Ceph分布式存储研发人员。
- **时间/地点**: 未提供具体时间与地点，为线上视频会议。

#### 讨论的主要议题
1. **代码比较**：
   - 经典代码为同步代码，处理请求简单直接。
   - Crimson代码采用seastar框架，使用Futures和Continuation。
   - Continuation为C++ Lambda表达式，用于在Future就绪或赋值时调用。

2. **指针捕获**：
   - 讨论在Lambda表达式中捕获`this`指针的安全性，建议避免捕获`con`和`request`以防生命周期问题。

3. **消息处理**：
   - 介绍messenger组件，作为Ceph通信层，处理如mosd_op等不同类型的消息。
   - mosd_op代表OSD操作，是实际的RADOS操作，包含对象ID和操作（如删除、写入等）。

4. **对象上下文**：
   - 对象上下文用于跟踪对象的修改状态，是一个缓存数据结构。
   - 讨论了获取对象上下文的逻辑，包括从缓存中获取或从后端加载。

5. **代码目录结构**：
   - Crimson代码主要位于Crimson目录中，是经典OSD的替代品。
   - 讨论了Crimson代码中使用的一些特殊宏和适配问题。

6. **客户端请求管道**：
   - 介绍了Crimson中的客户端请求管道，包括等待地图阶段、活动等待阶段等。
   - 强调了处理请求时需要满足的依赖条件，如OSD地图版本匹配。

7. **错误处理**：
   - 讨论了使用erator处理非严重错误的情况，确保程序在遇到错误时不会崩溃。

#### 决定的事项
- 确认了在Crimson代码中使用seastar框架的必要性和优势。
- 确定了处理请求时需要满足的依赖条件，并讨论了如何处理不满足的情况。
- 讨论了错误处理的策略，特别是使用erator来处理非严重错误。

#### 后续行动计划
- 继续优化Crimson代码，特别是在错误处理和依赖条件满足方面的逻辑。
- 深入研究seastar框架的使用，确保代码的高效和稳定。
- 定期审查和更新代码，以保持与Ceph其他部分的兼容性和一致性。

#### 备注
- 会议中提到了一些技术细节和代码示例，对于深入理解Crimson代码的实现非常重要。
- 会议强调了代码的可维护性和错误处理策略，这些都是确保系统稳定运行的关键因素。