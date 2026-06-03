---
title: "Monitoring Ceph with Prometheus - Jan Fajerski, SUSE"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
  - "监控"
  - "存储"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： [请填写会议时间]

**参会人员**： [请填写参会人员]

**会议主题**： Prometheus监控工具介绍与Ceph应用

**会议内容**：

* **Prometheus 简介**：
    * Prometheus由SoundCloud于2012年开发，是CNCF会员项目，适用于高维数值数据监控。
    * Prometheus基于拉取模式，从端点拉取指标，具有可扩展性。
    * Prometheus包含强大的查询语言PromQL，支持标签匹配、算术运算、聚合操作等。
    * Prometheus的关键组件包括Exporter（暴露指标的组件）和Alert Manager（处理警报的组件）。
* **Prometheus 配置**：
    * Prometheus使用YAML文件进行配置，包括Scrape配置、Service Discovery等。
    * Service Discovery支持静态配置、Kubernetes、文件SD等。
    * 监控应具备弹性和可扩展性，可使用多个Prometheus实例进行水平扩展。
* **Prometheus 查询语言 (PromQL)**：
    * PromQL是Prometheus的查询语言，支持瞬时向量、范围向量等类型。
    * 示例查询包括计算文件系统使用率、计算指标每秒速率、联合不同Exporter的指标等。
* **Prometheus 警报**：
    * Prometheus警报使用PromQL表达式，支持条件、持续时间、标签等。
    * Prometheus提供了默认的警报和仪表板，用户可以根据需求进行定制。
* **Ceph监控与Prometheus结合**：
    * Ceph的manager模块可以作为Exporter使用，暴露Ceph集群的指标。
    * Prometheus可以监控Ceph集群的各种指标，如存储使用率、性能、可用性等。
    * 用户可以根据需要添加自定义警报和仪表板。

**行动计划**：

* 推广Prometheus在Ceph集群中的应用。
* 提供Prometheus配置和查询语言的文档。
* 开发Ceph的Prometheus Exporter。
* 收集用户反馈，改进Prometheus功能。

**会议总结**：

本次会议介绍了Prometheus监控工具及其在Ceph集群中的应用。Prometheus具有强大的功能和易用性，是Ceph集群监控的理想选择。