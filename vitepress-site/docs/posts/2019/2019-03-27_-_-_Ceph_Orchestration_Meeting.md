---
title: "2019-03-27:: Ceph Orchestration Meeting"
date: 2019-03-27
updated: 2019-04-10
tags:
  - "Ceph"
  - "编排"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
categories:
  - "会议纪要"
  - "存储技术"
  - "Ceph 文档"
outline: deep
---
### 会议纪要

**会议时间**： 2019年3月27日

**参会人员**： Tim, Brooke, Matt, Tomica 等

**会议主题**： Ceph Orchestrator 模块版本兼容性及测试问题讨论

**会议内容**：

**1. 版本依赖性问题**

*   Ceph Orchestrator 模块与外部 orchestrator 存在兼容性问题，可能导致版本依赖性问题。
*   例如，Rook Orchestrator 在 Nautilus 首次模块发布版本中与 Ceph Orchestrator 不兼容。
*   已知问题：Orchestrator 模块与外部 orchestrator 之间的依赖关系需要解决。

**2. 解决方案讨论**

*   **版本检查**：
    *   在 Orchestrator 模型中添加版本检查机制，确保 Orchestrator 模块与外部 orchestrator 版本兼容。
    *   使用 `Ana status 18` 方法检查 Orchestrator 模型状态，并警告使用不稳定版本。
    *   各个模块内部实现版本检查，确保与对应 manager 模块兼容。
*   **测试**：
    *   在 Rook CI、DeepSea CI 等环境测试 Orchestrator 模块，确保与外部 orchestrator 版本兼容。
    *   进行 smoke test 测试 Orchestrator 模块功能。
    *   在生产环境中，GUI 应防止更改外部 orchestrator 导致的问题。

**3. 行动计划**

*   **Tim**：
    *   持续跟进 Orchestrator 模块的版本兼容性问题。
    *   修复相关 bug，并提交 pull request。
*   **Brooke**：
    *   研究解决版本依赖问题的方案。
*   **Matt**：
    *   在 DeepSea 中部署 Orchestrator 模块，并打印出 IceCozy 和 Ganesha 端点 URL。
*   **Tomica**：
    *   解决 Ansible 运行服务的问题，并修复相关 bug。

**4. 其他**

*   Tim 遇到音频连接问题，会议中部分内容可能存在遗漏。

**备注**：

*   本次会议讨论了 Ceph Orchestrator 模块的版本兼容性及测试问题，并提出了相应的解决方案和行动计划。
*   需要进一步测试和验证解决方案的有效性。