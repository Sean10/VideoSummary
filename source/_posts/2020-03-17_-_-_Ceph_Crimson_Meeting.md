---
categories:
- 视频总结
date: 2020-04-03
subtitle: 2020-03-17_-_Ceph_Crimson_Meeting
tags:
- Ceph
- BlueStore
- OSD
- Distributed Storage
- BlueFS
title: "'2020-03-17 :: Ceph Crimson Meeting'"
updated: 2020-04-04
---




### 会议纪要

#### 会议概要
本次Ceph Crimson会议主要讨论了Ceph分布式存储系统的研发进展，包括技术问题、解决方案和后续行动计划。会议重点涉及了Ceph BlueStore的实现、对象类（CLS）的函数实现、OSD的恢复和清理工作，以及技术问题和解决方案等议题。

#### 主要议题
1. **Ceph BlueStore的实现**
   - 讨论了使用BlueJeans进行视频会议的体验，包括白板和屏幕共享功能。
   - 分析了BlueStore的具体实现细节，如节点在树中的实现和团队讨论。

2. **对象类（CLS）的函数实现**
   - 跟踪了CLS法律项目的进展，包括CBT更新请求和产品审查。
   - 发现并分析了某些函数在测试中出现的回归问题。

3. **OSD的恢复和清理工作**
   - 讨论了OSD中的恢复和清理工作，包括任务分配和具体实施。
   - 讨论了OSD中的加密和传统T的比较，以及在恢复工作中可能遇到的问题。

4. **技术问题和解决方案**
   - 讨论了OSD中处理OSD map消息时的问题，以及通过调试解决这些问题的方法。
   - 提到了心跳竞赛问题和messenger连接接口的修改。

5. **文档和协作**
   - 强调了文档的重要性，并建议在Google Docs中进行协作。
   - 讨论了如何通过文档来协调和记录恢复和清理工作的进展。

#### 决定事项
- 确认了BlueStore中的一些实现细节和团队讨论的结果。
- 确定了CLS法律项目的进展和需要解决的回归问题。
- 分配了OSD中的恢复和清理工作的具体任务。
- 强调了文档和协作的重要性，建议在Google Docs中进行协作。

#### 后续行动计划
- 继续分析和修复CLS法律项目中的回归问题。
- 分配和执行OSD中的恢复和清理工作的具体任务。
- 在Google Docs中进行文档协作，记录和协调工作进展。
- 继续测试和优化BlueStore的实现。

#### 关键词
- Ceph
- BlueStore
- CLS law
- OSD
- 恢复工作
- 清理工作
- Google Docs
- 文档协作