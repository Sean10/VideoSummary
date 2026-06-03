---
title: "Ceph RGW Refactoring Meeting 2025-11-19"
date: 2025-11-19
updated: 2025-12-04
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph RGW 重构会议纪要

#### **会议主题**
本次会议主要讨论了 Ceph RGW 的几个重要改进，包括 DDUP 功能改进、服务器端加密（SSE）复制支持以及 C++20 协程代码问题。



### **1. DDUP 功能改进**
**讨论重点**：
- **版本对象处理**：将每个版本对象视为独立实体，支持 DDUP 操作，无需介入生命周期管理。
- **Split Head 优化**：支持小至 8KB/4KB 对象的去重，涉及 manifest 操作的代码需专家协助审查。
- **加密与压缩对象**：当前 DDUP 不支持加密和压缩对象，未来可能扩展支持。



### **2. 服务器端加密（SSE）复制支持**
**讨论重点**：
- **Marcus 的 PR 长期停滞**：涉及 SSE 复制功能，部分属性更新问题未解决。
- **Cena 的替代方案**：覆盖单区域和多区域复制，已通过 S3 测试。
- **决策**：优先合并 Cena 的单区域复制 PR，多区域复制的重加密功能后续通过独立 PR 实现。



### **3. C++20 协程代码问题**
**讨论重点**：
- **未使用的协程代码**：发现部分已合并的协程代码未被调用，需进一步验证。
- **元数据同步原型**：Casey 将重新开放相关 PR，明确活跃开发分支。
- **后续行动**：Jane 提交具体代码链接供 Adam 审查，Casey 协助更新元数据同步协程原型。



### **行动计划（Action Items）**
| 任务 | 负责人 | 状态 |
||--||
| DDUP Split Head PR 审查 | Gabby、Matt、Casey | 待启动 |
| SSE 单区域复制 PR 合并 | Cena | 待测试 |
| 多区域复制重加密 PR | Cena | 后续阶段 |
| C++20 协程代码验证 | Adam、Jane | 进行中 |
| 元数据同步协程分支更新 | Casey | 待完成 |



**关键词保留**
- **技术术语**：DDUP、manifest、SSE、multi-site、C++20 coroutines、S3 API、PR。
- **Ceph 组件**：RADOS、librados、CRUSH、OSD、PG。



**下次会议重点**：DDUP 审查进展、SSE 复制测试结果、协程代码优化。  
**会议结束时间**：议题覆盖完毕，无其他问题。