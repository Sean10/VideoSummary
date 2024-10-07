---
title: "Ceph Orchestrator Meeting 2021-06-22"
date: 2021-06-24
updated: 2021-06-24
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Orchestrator 周例会

#### 会议时间：[具体日期]

#### 参会人员：[参会人员名单]

#### 会议议程：
1. **KCLI 项目进展**
2. **Paramecio 适用性问题**

#### 会议内容：

##### 1. KCLI 项目进展
- **项目介绍**：介绍了使用 KCLI 项目来设置 Kubernetes 集群并通过 Rook 操作符启动 Ceph 集群的新计划。
- **技术细节**：讨论了在个人笔记本上进行测试所需的资源（如足够的内存和硬盘空间），并探讨了如何简化开发和集成测试过程。
- **工具对比**：比较了 KCLI 和 Vagrant 的相似性，讨论了各自的优缺点，以及是否需要安装额外的工具。
- **团队反馈**：欢迎团队成员提出意见和建议。

##### 2. Paramecio 适用性问题
- **问题描述**：讨论了 Paramecio 作为 SSH 的封装层，存在功能限制和错误信息隐藏的问题。
- **替代方案**：探讨了使用 ZincSSH 或其他库的可能性，以及是否需要一个同步库。
- **技术挑战**：讨论了如何处理远程主机上的多命令执行问题，包括使用持久性 SSH 连接或远程 Python 解释器。
- **团队决策**：初步决定尝试使用 AsyncSSH，并考虑移除对 Remoto 的依赖，以简化实现。

#### 决定事项：
- **KCLI 项目**：继续推进 KCLI 项目，收集团队反馈以优化工具选择和使用。
- **Paramecio 问题**：尝试使用 AsyncSSH 作为替代方案，评估其适用性和性能。

#### 后续行动计划：
- **KCLI 项目**：团队成员需提供关于 KCLI 和 Vagrant 的使用反馈，以便进一步优化开发环境。
- **Paramecio 问题**：进行 AsyncSSH 的实验性测试，评估其是否能满足项目需求，并解决多命令执行的问题。

#### 其他事项：
- **RGW 集成测试**：确认 RGW 集成测试的进展，计划进行测试套件的转换工作。
- **NFS 和 Dashboard 工作**：继续推进 NFS 相关工作和 Dashboard 模块的改进。

#### 会议结束：
会议于[具体时间]结束，下次会议定于下周进行。

---

以上是本次会议的详细纪要，涵盖了会议的主要议题、讨论内容、决定事项及后续行动计划。