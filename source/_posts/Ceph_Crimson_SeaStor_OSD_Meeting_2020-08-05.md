---
categories:
- 视频总结
date: 2020-08-05
subtitle: Ceph_Crimson_SeaStor_OSD_Meeting_2020-08-05
tags:
- Ceph
- 分布式存储
- Bluestore
- Pull Request
- 内存数据结构管理
title: "Ceph Crimson/SeaStor OSD Meeting 2020-08-05"
updated: 2020-08-06
---



### 会议纪要

#### 会议概要
本次会议主要讨论了Ceph分布式存储系统的发展，重点关注了代码重构、测试结果分析、Pull Request更新、内存数据结构管理等议题。

#### 主要议题
1. **代码重构与测试**
   - 创建了一个修复问题的Pull Request，以启用小规模运行测试。
   - 测试结果显示，部分失败与Bluestore相关，但并非Ceph核心问题。
   - 计划进一步调查Bluestore中的失败原因。

2. **Pull Request更新与审查**
   - 根据评论更新了Pull Request，并请求团队成员审查。
   - 讨论了在旧节点中启动扩展映射树的问题，决定不在外部映射树中存储。
   - 代码重构涉及Sam的RBA pin patch，发现了一些问题，等待更新后重新重构。

3. **内存数据结构管理**
   - 讨论了在固定KV节点布局中使用cipher_le64的问题，因缺乏常量操作接口，需要提供自己的包装结构。
   - 讨论了在事务结束后保持对扩展的引用的安全性，建议在同一事务内保持引用，但不要在事务间保持。

4. **未来工作计划**
   - 继续开发可中断的叙述未来（interruptible narrative future），并实现一系列错误率版本的未来设施。
   - 计划实现跟踪设施，以便在树查找中保持节点可用性。

#### 决定事项
- 调查Bluestore中的测试失败原因。
- 完成Pull Request的修改和审查。
- 在内存数据结构管理中，避免在事务间保持对节点的引用。

#### 后续行动计划
- 调查Bluestore的测试失败原因。
- 继续更新和审查Pull Request。
- 开发和实现可中断的叙述未来及相关设施。
- 实现跟踪设施，确保在树查找中节点的可用性。

#### 关键词
- Ceph
- Bluestore
- Pull Request (Pull Request)
- extend map tree
- RBA pin patch
- cipher_le64
- interruptible narrative future