---
categories:
- 视频总结
date: 2018-11-29
subtitle: Ceph_Testing_Weekly_2018-11-28
tags:
- Ceph
title: "Ceph Testing Weekly 2018-11-28"
updated: 2018-11-29
---



### 会议纪要

**会议时间**： 2018年11月（具体日期未提及）

**参会人员**： 多位Ceph研发人员（包括但不限于Nathan, David Galloway, Alfredo, Sebastian等）

**会议主题**： 讨论Ceph项目中Python 3的支持、安装器接口、Orchestrator模块以及OpenSUSE测试等议题。

**会议内容**：

**1. Python 3支持**

*   讨论了在Ceph项目中引入Python 3的必要性，以及如何在openSUSE上实现Python 3环境。
*   提到了使用Mach工具进行OpenSUSE构建的可行性，并讨论了如何解决Shaman构建工具的限制。
*   认为需要投入资源来支持OpenSUSE的构建，并考虑使用OBS或mock工具。

**2. 安装器接口**

*   讨论了Ceph安装器接口的改进，包括Ansible和Sensu等工具的使用。
*   讨论了安装器接口的抽象化，以及如何支持不同类型的安装器。
*   认为需要创建一个产品跟踪器（tracker），以便跟踪相关需求和问题。

**3. Orchestrator模块**

*   讨论了Orchestrator模块的设计和实现，以及其与Ceph Manager的集成。
*   认为Orchestrator模块可以提供统一的命令接口，支持不同类型的Orchestrator，例如Ansible、DeepSea和Rook等。
*   认为Orchestrator模块的开发需要与安装器接口的改进同步进行。

**4. OpenSUSE测试**

*   讨论了在OpenSUSE上测试Ceph项目的可行性，以及如何解决Shaman构建工具的限制。
*   认为需要投入资源来支持OpenSUSE的构建，并考虑使用OBS或mock工具。

**行动计划**：

*   Nathan将继续开发Orchestrator模块，并与安装器接口的改进同步进行。
*   David Galloway将创建一个产品跟踪器，以便跟踪相关需求和问题。
*   讨论如何支持OpenSUSE的构建，并考虑使用OBS或mock工具。

**关键信息**：

*   Ceph项目正在积极推动Python 3的支持。
*   Ceph项目正在改进安装器接口，并引入Orchestrator模块。
*   OpenSUSE测试是Ceph项目的一个重要目标。

**备注**：

*   会议中提到了一些技术细节，例如Mach、mock、OBS、Shaman等，这些内容对于理解会议内容可能有所帮助。
*   会议中提到了一些资源问题，例如构建资源、测试环境等，这些内容对于后续工作可能有所帮助。