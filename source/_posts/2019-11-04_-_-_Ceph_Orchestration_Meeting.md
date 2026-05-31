---
categories:
- 视频总结
date: 2019-11-04
subtitle: 2019-11-04_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- Rook
- 编排
- 分布式存储
- Kubernetes
title: "'2019-11-04 :: Ceph Orchestration Meeting'"
updated: 2019-11-05
---




**会议纪要**

**会议时间**： 2023年11月某日

**会议地点**： 线上会议

**参会人员**： Jerry、Rick、DW、Sebastian、Lauren等

**会议主题**： Rook 项目进展讨论及行动计划

**关键细节及议题**：

* **Orchestrator 工作流**：
    * Jerry 提到 Orchestrator 工作流需要支持多站点设置，并创建区域。
    * Rick 表示 Rook 只支持独立区域，不支持多站点配置。
    * Jerry 认为可能需要一个更高级的工作流，先进行多站点操作，然后再启动 Demon，或者创建其他所需资源。
* **Rook 与 Octopus**：
    * DW 更新了 Rook 的路线图，并确保 Rook 准备好 Octopus 的发布。
    * Rick 提到需要查看 Octopus 的待办事项列表，并确定 Rook 需要实现的功能。
* **Python 客户端库**：
    * Jerry 提到将 Python 客户端库放入 Rook 仓库可以使版本依赖管理更加简洁。
    * DW 同意将 Python 客户端库添加到 Rook 仓库中。
* **驱动器组支持**：
    * Jerry 讨论了将驱动器组集成到 Rook Orchestrator 中的方案。
    * 他建议在 Orchestrator 层面获取驱动器信息，并将其传递给 Rook。
    * 他还提到应该在 Rook 安全集群内部实现卷创建，而不是依赖于外部实现。
* **闪烁灯集成**：
    * Rick 提到闪烁灯集成目前受阻，需要等待相关 pull request 合并。
    * Sebastian 提到可以将闪烁灯集成到 Europe Manager 模块中。
* **远程调用问题**：
    * Lauren 提到远程调用库不支持 SSH 选项参数，需要升级库版本。
    * Jerry 计划使用 pip 安装新版本的远程调用库。

**决定的事项**：

* Jerry 将继续与 Ollie 讨论 RGB 工作内容。
* DW 将更新 Rook 的路线图，确保 Rook 准备好 Octopus 的发布。
* 将 Python 客户端库添加到 Rook 仓库中。
* 探索将驱动器组集成到 Rook Orchestrator 中的方案。
* 解决远程调用库的问题。

**后续行动计划**：

* Jerry 与 Ollie 讨论 RGB 工作内容。
* DW 更新 Rook 路线图。
* 完成将 Python 客户端库添加到 Rook 仓库的工作。
* 探索将驱动器组集成到 Rook Orchestrator 中的方案。
* 解决远程调用库的问题。

**备注**：

* 会议中提到了一些计算机科学/ceph 领域的英文关键词，如：Orchestrator、Rook、Octopus、RBD、Python、SSH、RemoteOH、DRBD、Orchestrator、Rook、Octopus、RBD、Rook、Python、SSH、RemoteOH 等。
* 会议中讨论了一些技术细节，如：工作流、版本依赖管理、驱动器组、闪烁灯、远程调用等。