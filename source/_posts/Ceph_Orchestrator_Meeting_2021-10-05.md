---
title: "Ceph Orchestrator Meeting 2021-10-05"
date: 2021-10-07
updated: 2021-10-08
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph 存储系统相关问题讨论

#### 参会人员：Ceph 研发团队

#### 会议日期：[具体日期]

#### 会议内容：

1. **Indiana Loopback 配置问题**
   - **讨论内容**：
     - 发言人分享了关于 Indiana Loopback 配置的最新进展。
     - 在 CentOS 8 内核上，所有功能运行良好，但配置工具 `nvme-cli` 使用不便，需要安装特定包并处理复杂的 JSON 配置。
     - 在 Ubuntu 系统上，默认内核不支持 NVMe Loopback，存在 bug，需要寻找更好的内核版本。
   - **决定事项**：
     - 需要进一步研究并选择合适的内核版本以支持 NVMe Loopback。
   - **后续行动**：
     - 编写技术任务文档，指导如何在 LVM LVS 前端添加 NVMe Loopback 配置。
     - 测试相关功能，确保驱动组和设备应用的重装 OSDs 功能正常。

2. **Dashboard 监控堆栈问题**
   - **讨论内容**：
     - 讨论了在 Rook 项目中，如何手动配置 Dashboard 监控堆栈以支持 Grafana 和其他管理工具。
     - 默认情况下，这些功能在 Rook 启动的 Ceph 集群中未启用。
   - **决定事项**：
     - 需要提供详细的文档和步骤，指导用户手动配置监控堆栈。
   - **后续行动**：
     - 提供演示视频和文档，帮助用户理解和配置监控堆栈。

#### 其他讨论：
- 确认了设备在 Linux 系统中的表现正常，不会影响正常操作。
- 确认了监控堆栈配置的问题，并提出了相应的解决方案。

#### 会议总结：
- 本次会议主要解决了 Indiana Loopback 配置和 Dashboard 监控堆栈的问题，并制定了相应的后续行动计划。
- 会议结束时，团队成员确认没有其他紧急议题需要讨论。

#### 会议结束：
- 会议在确认所有议题讨论完毕后结束，团队成员感谢彼此的参与并祝愿大家工作顺利。

#### 备注：
- 会议记录由视频会议字幕总结人员整理，保留了部分计算机科学/Ceph 相关领域英文原文的关键词。