---
title: "Ceph Days NYC 2023: SQL on Ceph"
date: 2023-05-17
updated: 2023-05-18
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** SQL Lite on Ceph 的介绍与应用

**主讲人：** Patrick Donnelly，IBM 的 Ceph 研发人员

**会议内容概述：**
Patrick Donnelly 介绍了如何在 Ceph 上使用 SQL Lite，特别是通过 libsef sqlite 库将 SQLite 数据库分布式存储在 Ceph 的 RADOS 上。他讨论了 Ceph 管理器（Ceph Manager）如何利用 SQLite 进行持久化存储，并详细说明了实现这一功能的架构和技术细节。

**关键讨论点：**
1. **Ceph 管理器架构：** Ceph Manager 通过模块化设计，允许运行 Python 脚本管理集群操作。这些模块包括 orchestration、升级、设备健康监控等，且不依赖于 CFS、RBD 等服务。
2. **SQLite 与 Ceph 的结合：** 通过 libsef sqlite，SQLite 数据库可以分布式存储在 Ceph 的 RADOS 上，无需修改应用程序代码。这通过 SQLite 的 VFS（Virtual File System）接口实现，允许数据库文件分布在多个 OSD 上。
3. **性能优化：** 提供了多个性能优化建议，如增加页面大小、使用更大的缓存、避免删除数据库文件等，以减少对 RADOS 的 IO 操作。

**决定事项：**
- Ceph Manager 已经开始使用 libsef sqlite 进行数据持久化，特别是在设备健康模块中。
- 计划进一步优化 libsef sqlite 库，支持多读者和读取预取性能。

**后续行动计划：**
- 继续优化 libsef sqlite 库，解决存在的 bug 和性能问题。
- 探索在更多 Ceph Manager 模块中使用 SQLite 进行数据持久化。
- 考虑未来可能将其他数据库系统（如 PostgreSQL）集成到 Ceph 中。

**其他信息：**
- 提供了详细的性能优化建议和使用指南。
- 讨论了未来可能的工作方向，包括支持多读者和读取预取性能。

**会议结束：**
Patrick Donnelly 回答了现场提出的问题，并提供了他的联系信息和相关文档链接，以便参与者进一步了解和使用 libsef sqlite。

**备注：**
- 会议中提到的 libsef sqlite 和其他相关技术细节可在提供的文档和博客文章中找到。
- 会议纪要和相关资料将在会议结束后提供给参与者。