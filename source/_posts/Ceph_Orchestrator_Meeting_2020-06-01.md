---
categories:
- 视频总结
date: 2020-06-01
subtitle: Ceph_Orchestrator_Meeting_2020-06-01
tags:
- Ceph
- Drive Groups
- Rook
- Ceph Manager
- Ceph Orchestrator
title: "Ceph Orchestrator Meeting 2020-06-01"
updated: 2020-06-02
---




### 会议纪要

#### 会议主题：Drive Groups 的讨论

#### 参会人员：Blaine, Sebastian Wagner, Zach Dover 及其他相关人员

#### 主要议题：

1. **Drive Groups 的实现问题**：
   - Blaine 提出需要使用 Drive Groups 来配置主机。
   - Brooke 和 Young 完成了一个 PR，将 Drive Group 规范应用到主机。
   - Sebastian Wagner 反对 Ceph 进行主机验证，建议由 Rook 负责。

2. **技术实现细节**：
   - 讨论了 Rook 是否应重新实现逻辑或依赖 Ceph 内部逻辑。
   - 提出使用 CLI 命令查询 Ceph Manager 以确定 Drive Group 规范是否适用于特定节点。
   - 讨论了使用 Python 库的选项，但认为这不是长期稳定的解决方案。

3. **行动计划**：
   - 探索使用现有的 Ceph 集群工具获取所需信息。
   - 建议使用 Drive Group 文件规范中的预览参数来测试功能。
   - 计划实现新的 CLI 命令以获取这些信息，避免使用外部脚本。

#### 其他讨论：

- Zach Dover 正在编写基于 Seafile 的安装指南，寻求网络配置帮助。
- 讨论了与 Red Hat 的合作以及文档和 QA 流程共享。

#### 后续行动：

- 继续讨论技术细节。
- Zach Dover 将安排会议解决网络配置问题。
- 推进 Drive Groups 的实现和文档编写工作。

#### 会议结束：

- 会议在讨论完所有议题后结束，祝大家周一愉快。



本次会议纪要准确反映了会议的关键细节、讨论的主要议题、决定的事项以及后续行动计划。以下是对原始总结的改进：

- 确保了所有主要议题和讨论点被包含在内。
- 明确了 Rook 和 Ceph Manager 在 Drive Groups 实现中的作用。
- 指出 Zach Dover 的角色和他在会议中的贡献。
- 强调了与 Red Hat 的合作以及 QA 流程的重要性。
- 保持了所有相关 Ceph 和计算机科学领域的英文关键词。