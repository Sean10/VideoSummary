---
title: "Asok Gems and How To Polish Them - Marcel Lauhoff, Clyso"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
本次会议主要围绕 Ceph Admin Socket 的功能、应用及工具开发展开，深入探讨了如何利用 Admin Socket 获取集群内部信息、探索未文档化命令，以及如何通过工具优化数据可视化和管理效率。

#### 主要议题与讨论内容

1. **Admin Socket 简介**
   - Ceph Admin Socket 是一种通过 Unix Socket 文件与 Ceph 守护进程（如 OSD、MON、MDS、RGW）交互的接口，支持查询状态、配置和性能指标。
   - 访问方式包括原生工具 `ceph daemon`、`ceph tell` 和 `librados`，以及通过 `netcat` + JSON 直接与 Socket 通信。
   - 开发者可以轻松添加自定义命令。

2. **Admin Socket 命令生态**
   - 目前共 179 个命令，分布在 OSD、MDS 等服务中，另有 25 个通用命令。
   - 近半数命令未在官方文档中提及，但可通过 `help` 查看功能说明。
   - 高频实用命令包括 `dump_historic_ops`、`counter dump`、`config diff` 等。

3. **工具开发与数据可视化**
   - 配置管理工具如 `config diff` 可用于解析和可视化配置差异。
   - 网络诊断工具如 `messenger dump` 可用于获取 TCP 连接状态和性能指标。
   - 性能分析工具如 `dump_historic_ops` 可用于展示操作耗时分布。

4. **未来计划**
   - 工具生态扩展，开发 TUI 工具、Ceph 插件等。
   - 标准化 Admin Socket 命令，提升工具兼容性。
   - 社区协作，鼓励贡献更多工具。

#### 关键决定

- 优先探索未文档化命令。
- 推广工具开发范式，基于 JSON 输出 + `jq`/Python 快速构建诊断工具。
- 整合监控能力，将 `messenger dump` 和 `counter dump` 数据接入 Prometheus/Grafana。

#### 后续行动计划

- 完善 `CN-top` 功能。
- 提交 `config diff` 可视化工具到 Ceph 生态库。
- 调研 `dump_historic_ops` 的图表化方案。
- 组织 Admin Socket 命令文档补全计划。

#### 问答环节亮点

- Admin Socket 查询可能轻微影响性能。
- 未来计划将 Admin Socket 数据纳入自动化分析工具链。
- RBD Mirror 专用命令需补充到现有命令统计中。

本次会议强调了 Admin Socket 在 Ceph 运维中的重要性，并鼓励社区开发和利用相关的工具，以提升 Ceph 集群的管理效率和性能。