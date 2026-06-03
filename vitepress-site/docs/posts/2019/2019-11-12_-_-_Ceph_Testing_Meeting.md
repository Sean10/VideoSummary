---
title: "2019-11-12 :: Ceph Testing Meeting"
date: 2019-11-12
updated: 2019-11-18
tags:
  - "Ceph"
  - "分布式存储"
  - "测试"
  - "OpenStack"
  - "Kubernetes"
  - "Docker"
outline: deep
---
categories:
- "视频总结"
subtitle: 2019-11-12_-_-_Ceph_Testing_Meeting



### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Kira, Yuri, Nathan, Sage, Jason, 安德鲁，以及其他未具名成员

**会议主题**： Ceph项目进展、问题讨论和后续行动计划

**关键细节**：

* **Ceph Mimic版本**： Sage发布了一个针对Mimic的PR，旨在解决升级和客户端测试失败的问题。Nathan已开始测试该PR，并计划将其合并到Mimic的候选版本中。会议决定合并该PR，并运行测试以验证其效果。
* **Ceph Luminous版本**： 目前没有针对Luminous的PR，主要关注Nautilus版本。会议决定将Luminous版本作为最后一个LTS版本，并给予更多时间来完善。
* **Ceph Nautilus版本**： Sage提到一个潜在回归，其中BlueStore在某些情况下会导致数据损坏。如果有人提交修复该问题的PR，则将立即进行热修复。
* **Ceph Octopus版本**： Timothy九有一个关于Oculus的PR。会议讨论了测试和部署Oculus的进展。
* **Ceph测试**： Sage正在编写新的测试用例，用于测试Ceph集群管理器。讨论了在OpenStack上进行测试的可能性。
* **Ceph任务**： Sage正在重构Ceph任务，以提高其效率和可靠性。讨论了使用容器进行任务升级的可能性。
* **Ceph PR管理**： 讨论了一些旧的PR，并决定关闭一些不再需要的PR。

**决定的事项**：

* 合并Sage的Mimic PR，并运行测试以验证其效果。
* 继续关注Luminous版本，并给予更多时间来完善。
* 如果有人提交修复BlueStore回归问题的PR，则立即进行热修复。
* 继续推进Oculus的测试和部署。
* 继续重构Ceph任务，并提高其效率和可靠性。
* 关闭一些不再需要的PR。

**后续行动计划**：

* Nathan将合并Sage的Mimic PR，并运行测试。
* Sage将继续推进Oculus的测试和部署。
* Sage将继续重构Ceph任务，并提高其效率和可靠性。
* 会议参与者将继续关注Ceph项目的进展，并积极参与。