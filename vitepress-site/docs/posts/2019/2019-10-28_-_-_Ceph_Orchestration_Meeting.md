---
title: "2019-10-28 :: Ceph Orchestration Meeting"
date: 2019-11-03
updated: 2019-11-04
tags:
  - "Ceph"
  - "编排"
  - "分布式存储"
  - "存储集群"
  - "云计算"
categories:
  - "视频总结"
outline: deep
---
## 改进后的中文总结内容

### 会议纪要

**会议主题**： Ceph 及相关项目开发进度讨论

**会议时间**： 2023年11月某日

**参会人员**： Active, Mike, Joshua, Kiefer, Emma 等

**会议内容**：

**1. SSH Orchestrator 与 Docker 集成**：

* Active 正在开发 SSH Orchestrator，并已取得进展。
* Mike 与 Joshua 合作，将 SSH Orchestrator 与 Docker 集成，旨在改进 SAP 守护进程方案。
* 讨论了使用 bootstrap 命令的可能性，以及如何适用于更多容器。

**2. Ceph 集群文件系统问题**：

* 讨论了 Ceph 集群中 MDS 进程的分配问题，以确保其在多个文件系统之间均匀分配。
* 发现现有设置无法将 MDS 分配到特定文件系统的问题，并讨论了解决方案。

**3. Rook 项目进度**：

* Active 提到了 Rook 项目的一些开放 PR，并请求其他成员查看。
* 讨论了 Rook 项目中的问题，例如 Python 代码的异步缓存处理。
* 讨论了将验证逻辑移动到 orchestrator 接口的可能性。

**4. Ceph 存储设备信息收集**：

* 讨论了如何从存储设备中收集信息，并将其存储在 Ceph 存储系统中。
* 讨论了将存储设备信息添加到配置映射中，并使用配置映射来存储设备信息。

**5. 其他**：

* 讨论了 Ceph 工作组的一些其他问题，例如工作负载的监控和集成。
* 讨论了将一些 PR 放入 IRC 频道进行讨论。

**后续行动计划**：

* Active 继续开发 SSH Orchestrator。
* Mike 和 Joshua 继续推进 Docker 集成工作。
* 解决 Ceph 集群文件系统问题。
* 完善 Rook 项目的验证逻辑。
* 收集 Ceph 存储设备信息。
* 讨论其他 Ceph 工作组问题。

**备注**：

* 会议中提到了一些计算机科学/ceph 领域的英文关键词，例如 SSH Orchestrator、Docker、SAP 守护进程、MDS、Rook、配置映射等。