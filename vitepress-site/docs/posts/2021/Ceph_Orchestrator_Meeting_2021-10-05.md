---
title: "Ceph Orchestrator Meeting 2021-10-05"
date: 2021-10-07
updated: 2021-10-08
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "监控"
categories:
  - "视频总结"
outline: deep
---
在2021年10月5日的Ceph Orchestrator会议中，Ceph研发团队讨论并解决了几个关键问题：

1. **Indiana Loopback配置问题**：
   - 讨论了在CentOS 8和Ubuntu系统上配置Indiana Loopback的最新进展。
   - 确认在CentOS 8上所有功能运行良好，但配置工具`nvme-cli`使用不便。
   - 在Ubuntu上，默认内核不支持NVMe Loopback，存在bug，需要寻找更好的内核版本。
   - 决定选择合适的内核版本支持NVMe Loopback，并编写技术任务文档，指导如何在LVM LVS前端添加NVMe Loopback配置。
   - 测试相关功能，确保驱动组和设备应用的重装OSDs功能正常。

2. **Dashboard监控堆栈问题**：
   - 讨论了如何在Rook项目中手动配置Dashboard监控堆栈以支持Grafana和其他管理工具。
   - 默认情况下，这些功能在Rook启动的Ceph集群中未启用。
   - 决定提供详细的文档和步骤，指导用户手动配置监控堆栈。
   - 提供演示视频和文档，帮助用户理解和配置监控堆栈。

会议还确认了设备在Linux系统中的表现正常，不会影响正常操作，并讨论了监控堆栈配置的问题，提出了相应的解决方案。

会议总结：本次会议主要解决了Indiana Loopback配置和Dashboard监控堆栈的问题，并制定了相应的后续行动计划。会议结束时，团队成员确认没有其他紧急议题需要讨论。