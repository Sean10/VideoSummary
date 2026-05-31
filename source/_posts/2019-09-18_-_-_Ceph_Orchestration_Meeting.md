---
categories:
- 视频总结
date: 2019-09-30
subtitle: 2019-09-18_-_-_Ceph_Orchestration_Meeting
tags:
- Rook
title: "'2019-09-18 :: Ceph Orchestration Meeting'"
updated: 2019-10-01
---



## 改进后的中文总结内容

**会议纪要**

**会议时间**： 2023年3月24日

**参会人员**： 集合会议参与者

**会议主题**： Ceph分布式存储项目相关议题讨论

**会议内容**：

**1. Pod管理外部Kubernetes集群功能**

- 销售人员提出Pod管理功能需要支持连接外部Kubernetes集群。
- 目前存在一个bug，阻止了事件推送到外部Kubernetes节点。
- 开发人员正在修复该bug，并添加代码以允许将消息推送到外部Kubernetes集群。
- 修复预计将在明天完成，并提交Pull Request。

**2. Rook与Kubernetes资源整合**

- Arun正在研究Rook与Kubernetes资源整合的工作。
- 讨论了将Rook和Kubernetes事件创建资源的方式统一，以简化代码和维护。
- 认为可以使用Cuban客户端代码对象，或者自动生成Python类来处理自定义资源定义。
- 决定在Pull Request中实现使用Cuban客户端代码对象的功能。

**3. Rook与Cuban客户端代码对象**

- 讨论了Rook模块主要使用字典而不是Cuban客户端代码对象的原因。
- 认为使用Cuban客户端代码对象可以简化代码并提高可维护性。
- 讨论了自动生成Python类来处理自定义资源定义的方案。

**4. 主机方程**

- Kiefer完成了主机方程的mock-ups，并已合并。
- 讨论了主机方程的演示和文档工作。
- 认为需要更多的资源和努力来推动主机方程的进展。

**5. 安全性部署**

- 讨论了安全性部署的废弃问题。
- 认为应该逐步淘汰安全性部署，并寻找替代方案。

**行动计划**：

- 开发人员将在明天完成Pod管理外部Kubernetes集群功能的修复，并提交Pull Request。
- Arun将继续研究Rook与Kubernetes资源整合的工作。
- 讨论使用Cuban客户端代码对象或自动生成Python类来处理自定义资源定义的方案。
- Kiefer将推动主机方程的进展，并完成演示和文档工作。
- 讨论安全性部署的替代方案。

**备注**：

- 会议中讨论了一些计算机科学/ceph相关领域英文原文的关键词，例如：Kubernetes, Rook, Cuban, custom resource definitions, Python classes等。

### 错误、误解或遗漏的重要信息

1. 原始字幕中提到的bug修复，总结中未明确指出是针对Pod管理功能。
2. 原始字幕中提到的Cuban客户端代码对象的使用，总结中未明确指出为首选方案。
3. 原始字幕中提到的Rook模块使用字典的原因，总结中未详细说明。
4. 原始字幕中提到的主机方程的mock-ups合并和后续工作，总结中未提及。
5. 原始字幕中提到的安全性部署的废弃问题，总结中未详细说明需要寻找的替代方案。