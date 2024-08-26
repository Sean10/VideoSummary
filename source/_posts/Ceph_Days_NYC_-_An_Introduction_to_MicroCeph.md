---
title: "Ceph Days NYC: An Introduction to MicroCeph"
date: 2023-05-19
updated: 2023-05-20
tags:
categories:
- "视频总结"
subtitle: tech
---


---
title: "Ceph Days NYC: An Introduction to MicroCeph"
date: 2023-05-19
updated: 2023-05-20
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Microsoft Snap 在 Ceph 集群管理中的应用

#### 主讲人：Chris

#### 会议内容总结：

1. **Snap 介绍**：
   - Chris 介绍了 Microsoft Snap，这是一个由 Canonical 开发的集群管理工具。
   - Snap 使用 Dqlite，一个兼容 SQLite 的数据库，采用 Raft 共识算法。
   - 管理 Daemon 允许构建任意节点的集群，用于管理各种 Ceph 守护进程（如 Monitors、Managers、OSDs、Metadata Servers 等）。

2. **使用场景**：
   - 支持单节点 Ceph 部署，适合在笔记本电脑上运行，严格限制权限，类似于手机应用。
   - 支持小型边缘集群部署，快速、可预测，适合非 Ceph 专家的普通部署者。

3. **演示环节**：
   - 展示了如何通过 Snap 快速部署 Ceph 集群，包括启动集群、添加节点、配置管理 Daemon 等。
   - 演示了如何添加 OSDs 和设置 Ceph 集群，尽管集群初始化时没有存储。
   - 展示了如何启用和配置 Ceph 的 RGW（Red House Gateway），并进行了简单的 S3 操作演示。

4. **后续计划**：
   - 未来工作包括自动化加密、网络配置、升级管理等。
   - 强调了用户反馈的重要性，鼓励用户尝试并提供意见。

5. **技术细节**：
   - Snap 不使用 LDM，而是直接使用块设备，以便更好地进行权限限制。
   - 讨论了从单机部署扩展到数据中心部署的可能性。

6. **问题与回答**：
   - 回答了关于 Snap 使用的管理 Daemon 和集群状态管理的问题。
   - 讨论了 Snap 在不同环境下的部署和扩展性。

#### 决定事项：
- 继续开发和完善 Snap 的功能，特别是自动化加密和升级管理。
- 鼓励用户尝试并提供反馈，以便进一步改进产品。

#### 后续行动计划：
- 继续进行技术开发和功能完善。
- 收集和分析用户反馈，优化产品体验。
- 探索更多部署和扩展场景，提高产品的适应性和灵活性。

#### 会议结束：
- 会议在感谢和掌声中结束。