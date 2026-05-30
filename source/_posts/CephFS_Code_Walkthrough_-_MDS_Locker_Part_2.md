---
categories:
- 视频总结
date: 2021-12-09
subtitle: CephFS_Code_Walkthrough_-_MDS_Locker_Part_2
tags:
- CephFS
- MDS Locker
- Ceph 存储系统
- 分布式存储
- 代码分析
title: "'CephFS Code Walkthrough: MDS Locker, Part 2'"
updated: 2021-12-10
---




CephFS代码走读系列的第二部分会议深入探讨了Ceph分布式存储系统中MDS（元数据服务器）锁管理器（MDS Locker）的内部机制。以下是会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划：

### 会议概述

本次会议是CephFS代码走读系列的第二部分，主题为MDS Locker。由于MDS Locker内容丰富，难以在一次会议中完全覆盖，预计还将有第三部分会议。

### 主要议题

1. **文档更新**：
   - 会议中提到将编写一份关于MDS Locker内部实现的文档，并计划将其作为Pull Request提交，以便社区成员可以审查和提供反馈。

2. **MDS Locker概述**：
   - MDS使用日志（logs）来保护inode和dentry中的各种元数据。
   - MDS不同于单一的大锁，而是为不同的元数据片段使用不同类型的锁。
   - 锁类型（log types）和锁类别（log classes）的定义和使用。

3. **锁类型和锁类别**：
   - MDS定义了多种锁类型，每种类型保护inode或dentry中的特定元数据片段。
   - 锁类别定义了不同锁类型的锁定行为，以处理分布式锁的需求，包括Local Lock、Simple Lock、Scatter Lock和File Lock。

4. **锁状态和状态机**：
   - MDS定义了多种锁状态，每个状态决定了是否允许某种类型的锁。
   - 状态机（state machine）描述了锁从一种状态到另一种状态的转换过程，以Simple Lock为例进行了详细讲解。

### 决定事项

- 将继续编写和完善关于MDS Locker的文档，并计划将其作为Pull Request提交。

### 后续行动计划

- 预计将举行第三部分会议，继续深入探讨MDS Locker的内部机制，特别是Scatter Lock和File Lock的细节。
- 社区成员应关注即将发布的Pull Request，并积极参与文档的审查和讨论。

### 其他注意事项

- 会议中提到的代码和文档将在后续通过Pull Request的形式发布，社区成员应关注并参与讨论。
- 对于锁状态和状态机的理解，建议从Simple Lock开始，逐步深入，以便更好地理解复杂的锁机制。

本次会议为Ceph社区成员提供了一个深入了解MDS Locker内部机制的机会，并为后续的文档编写和代码优化奠定了基础。