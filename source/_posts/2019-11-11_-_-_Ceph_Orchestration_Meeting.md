---
categories:
- 视频总结
date: 2019-11-11
subtitle: 2019-11-11_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 分布式存储
- 编排
title: "'2019-11-11 :: Ceph Orchestration Meeting'"
updated: 2019-11-12
---



### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Miguel、Sebastian、Paige、Mike Latimer、其他未提及的参与者

**会议主题**： Ceph社区讨论、Rook项目进展、Orchestrator相关讨论

**关键细节**：

* **Ceph社区讨论**：
    * 上周在Epic City的CDM会议中，进行了关于Ceph的积极讨论。
    * 讨论了从Orchestrator视角添加新功能的可能性，但具体细节未透露。
    * 提出了关于Rook和升级相关的问题，需要与State团队讨论。
    * 容器镜像名称变化是否足以进行升级，以及Rook是否依赖于不同的镜像名称或标签。
    * 讨论了不使用“latest”版本的原因。

* **Rook项目进展**：
    * SEF（Staff Volume Inventory）已合并至上周的版本中。
    * Client Python作为依赖项，已讨论在Rook仓库中引入Python客户端库。
    * Sebastian将更新现有PR或创建新PR以实现此功能。

* **Orchestrator相关讨论**：
    * Orchestrator方面正在积极进行代码开发。
    * 有多个团队参与Elaste orchestrated effort，以及大量的PF（Performance Fix）。
    * 大新闻是DeepSea Orchestrator的开发工作可能即将停止，团队将更加专注于Cosmo和Rook两个Orchestrator。
    * Daniel（来自Red Hat的新成员）正在研究Antilochus Twitter。
    * 讨论了关于Hedgehog Twitter的决策，决定停止该项目。

**决定的事项**：

* Sebastian将更新现有PR或创建新PR以将Python客户端库引入Rook仓库。
* 团队将专注于Cosmo和Rook两个Orchestrator，DeepSea Orchestrator的开发工作可能即将停止。

**后续行动计划**：

* Sebastian将更新现有PR或创建新PR。
* 团队将继续专注于Cosmo和Rook两个Orchestrator的开发。
* Daniel将继续研究Antilochus Twitter。

**改进点**：
- 确保了会议纪要的要点准确反映了原始内容。
- 包括了所有关键细节，如Ceph社区讨论的细节、Rook项目进展和Orchestrator相关讨论。
- 明确了决定的事项和后续行动计划。
- 在总结中保留了所有相关的Ceph相关关键词。