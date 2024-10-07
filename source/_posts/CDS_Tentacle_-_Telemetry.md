---
title: "CDS Tentacle - Telemetry"
date: 2024-08-22
updated: 2024-08-23
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： Ceph 存储系统 Telemetry 功能讨论

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Ceph 团队成员，包括研发人员、测试人员、用户代表等

**会议内容**：

**一、Stretch 模式指标收集**

*   **讨论背景**： 为了了解 Stretch 模式的实际使用情况，需要收集相关指标。
*   **解决方案**： 
    *   通过 OSD 映射中的标志位收集 Stretch 模式状态信息。
    *   使用 Telemetry 模块收集相关数据，甚至可以追溯到几代版本。
    *   讨论了 Stretch 模式和 Stretch 集群的区别，以及进入 Stretch 模式所需的准备工作和配置。
*   **行动计划**： 
    *   Junior 将研究是否需要收集其他相关信息。
    *   在 Stretch 集群上进行测试，验证指标收集是否正确。

**二、其他指标收集**

*   **讨论背景**： 讨论了其他需要收集的指标，例如：
    *   用户对其他功能的使用情况。
    *   其他未收集的指标，例如 RBD、RGW 和 FFS 的应用层指标。
    *   RGW 多站点集群的统计信息。
    *   蓝存储分配器性能指标。
*   **解决方案**：
    *   讨论了如何收集和分析这些指标，例如：
        *   使用 Grafana 进行可视化。
        *   开发新的 Telemetry 模块。
        *   从性能计数器中推断信息。
*   **行动计划**：
    *   将讨论结果提交给用户开发会议，进一步讨论和确定具体的指标收集方案。

**三、Telemetry 分析报告**

*   **讨论背景**： 讨论了如何向用户提供 Telemetry 分析报告，帮助用户了解其部署状态和潜在问题。
*   **解决方案**：
    *   讨论了两种方案：
        *   在 Telemetry 网页或 Grafana 上提供更个性化的分析报告。
        *   开发一个 Telemetry 命令，生成分析报告。
*   **行动计划**：
    *   研究现有的 AI 工具，例如 SE Report，以获取灵感。
    *   研究如何将敏感信息匿名化。
    *   讨论如何将分析报告集成到现有的工具中。

**四、其他事项**

*   讨论了如何改进升级路径的数据库，以便更好地了解不同版本之间的兼容性。
*   讨论了如何使用 Telemetry 数据来评估版本稳定性，并帮助用户做出升级决策。

**会议总结**：

本次会议讨论了 Ceph 存储系统 Telemetry 功能的多个方面，包括指标收集、分析报告和用户体验等。会议达成了多项共识，并制定了后续行动计划。