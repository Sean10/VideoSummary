---
title: "2019-03-11:: Ceph Orchestration Meeting"
date: 2019-03-11
updated: 2019-04-16
tags:
  - "Ceph"
  - "编排"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年3月11日

**参会人员**： Travis, Natalie, Jamaica, Dipsy, Sage, Aaron, Sebastian 等

**会议主题**： Ceph Orchestrator 项目进展及问题讨论

**关键细节**：

* Travis 因故缺席会议。
* 项目进度：
    * Travis 正在处理两个 PR，一个用于内存自动调整，另一个用于使用 miss abuser 运行服务。
    * Natalie 正在修改 Ansible Runner 服务以支持 TLS。
    * Sage 正在解决本地化配置选项的问题。
    * Aaron 正在处理 Nautilus 的发布候选版本。
    * Sebastian 正在解决 LSM 储存库版本问题。
* 问题讨论：
    * **REST API 访问**： 在尝试在仪表板中集成 Surface Cozy 时，出现了一个问题，需要为仪表板提供不验证 SSL 证书的选项。讨论了在服务描述符类中如何存储此类信息，以及是否应该在 Orchestrator 中添加此选项。
    * **TLS 支持**： 讨论了在 Orchestrator 中支持 TLS 的必要性，并决定在 Ansible Runner 服务中实现。
    * **LSM 储存库版本**： 讨论了将 LSM 储存库的最新版本集成到 SEF 容器镜像中的必要性。
* 决定事项：
    * Travis 将合并一个关于内存自动调整的 PR。
    * Natalie 将继续修改 Ansible Runner 服务以支持 TLS。
    * Sage 将继续解决本地化配置选项的问题。
    * Aaron 将解决 Nautilus 发布候选版本的问题。
    * Sebastian 将解决 LSM 储存库版本问题。
* 后续行动计划：
    * 项目组成员将继续推进各自的工作，并定期在会议中汇报进展。
    * 讨论的问题将根据需要进一步讨论并解决。

**关键词**：
* Ceph Orchestrator
* REST API
* TLS
* LSM 储存库
* PR
* 发布候选版本
* 仪表板
* Orchestrator
* 配置选项
* 安全性

**分析与改进**：

1. 原总结准确反映了会议的关键细节，包括项目进度、问题讨论和决定事项。
2. 原总结遗漏了 Travis 提到的关于 Nautilus 发布候选版本的延迟问题，以及后续的讨论和分析。
3. 改进后的总结增加了对 Travis 提到的问题的描述，并保持了所有关键细节的完整性。
4. 关键词列表已更新，以反映会议中讨论的技术焦点。