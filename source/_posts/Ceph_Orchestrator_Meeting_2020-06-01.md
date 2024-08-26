---
title: "Ceph Orchestrator Meeting 2020-06-01"
date: 2020-06-01
updated: 2020-06-02
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Drive Groups 的讨论

#### 参会人员：Blaine, Sebastian Wagner, 以及其他相关人员

#### 主要议题：
1. **Drive Groups 的实现问题**：
   - Blaine 提到需要使用 Drive Groups 来配置主机。
   - Brooke 和 Young 已经完成了一个 PR，该 PR 将根据 Drive Group 规范在卷中应用到主机。
   - Sebastian Wagner 反对让 Ceph 进行主机验证，建议将此功能推给 Rook。

2. **技术实现细节**：
   - 讨论了是否应该在 Rook 中重新实现逻辑，或者依赖于 Ceph 的内部逻辑。
   - 提出了使用 CLI 命令查询 Ceph Manager 的方案，以确定 Drive Group 规范是否适用于特定节点。
   - 讨论了使用 Python 库的选项，但认为这不是一个长期稳定的解决方案。

3. **行动计划**：
   - 决定探索使用现有的 Ceph 集群工具来获取所需信息。
   - 建议使用 Drive Group 文件规范中的预览参数来测试功能。
   - 计划在未来实现一个新的 CLI 命令来获取这些信息，以避免使用外部脚本。

#### 其他讨论：
- Zach Dover 介绍了他的工作，他正在编写一个基于 Seafile 的安装指南，并寻求关于网络配置的帮助。
- 讨论了与 Red Hat 的合作，以及如何共享文档和 QA 流程。

#### 后续行动：
- 继续与 Sebastian Wagner 讨论技术细节。
- Zach Dover 将与相关人员安排进一步的会议，以解决网络配置的具体问题。
- 继续推进 Drive Groups 的实现和文档编写工作。

#### 会议结束：
- 会议在讨论完所有议题后结束，祝大家周一愉快。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。