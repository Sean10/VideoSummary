---
title: "CDS G/H (Day 1) -  Calamari Intro"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： Calamari 分布式存储介绍及开发讨论

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： John Spray, Gregory Meighan, 以及其他相关人员

**会议内容**：

**1. Calamari 介绍**

* Calamari 是一个基于 JavaScript 的用户界面，通过 HTTP 与 Calamari 服务器通信。
* Calamari 服务器作为前端，负责处理所有运行在其上的功能，包括 Apache、Graphite、Calamari REST 和 Calamari Web。
* Lulu 是 Calamari 的业务逻辑组件，负责运行远程操作和检查进度。
* SaltStack 用于远程操作和配置管理。
* Calamari 与 Ceph 集群的接口通过 VAR 和 Liberate 实现。

**2. Calamari 与其他 API 的关系**

* Calamari 与 Ceph REST API 有重叠，但 Calamari 提供更高级别的视图和功能。
* Calamari API 旨在简化与 Ceph 的集成，并提供更易于使用的工具。

**3. Calamari 的部署**

* Calamari 的部署相对复杂，需要处理许多依赖项。
* 社区正在努力简化 Calamari 的部署，包括打包和测试。
* Calamari 的部署需要依赖较新的软件版本，例如 SaltStack。

**4. Calamari 用户界面**

* Calamari 提供一个直观的用户界面，用于监控和管理工作负载。
* 用户界面包括仪表板、OSD 工作台、主机视图、集群配置、池管理和存储池视图。
* Calamari 支持扩展，可以通过编写额外的 Python 服务来实现。

**5. Calamari 的扩展**

* Calamari 使用现有的插件接口，例如 SaltStack 和 Django。
* 可以通过编写额外的 Python 服务来扩展 Calamari 的功能。

**6. 讨论要点**

* 如何简化 Calamari 的部署。
* 如何提高 Calamari 的安全性，例如通过角色访问控制。
* 如何扩展 Calamari 的功能。

**后续行动计划**：

* 社区将共同努力简化 Calamari 的部署。
* Calamari 团队将继续开发新的功能，并提高 Calamari 的安全性。
* Calamari 社区将继续讨论和改进 Calamari。