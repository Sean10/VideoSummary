---
categories:
- 视频总结
date: 2014-10-29
subtitle: CDS_Hammer_Day_1_-_Calamari_API_Roadmap
tags:
- Ceph
- RESTful API
- OpenStack
title: "CDS Hammer (Day 1) - Calamari API Roadmap"
updated: 2014-10-30
---


本次会议详细讨论了 Calamari API 的现状、目标和未来发展方向。以下是对会议内容的总结：

**Calamari API 概述**

- **Calamari 重新定义**： 将 Calamari 定位为后端服务层和 API 层，去除图形用户界面（GUI），聚焦于 API 本身及其功能。
- **Calamari 目标**： 实现与 Rados、RBD 和 RGW 命令行工具的功能对等，提供一致的 RESTful 接口，并支持异步操作。
- **Calamari 优势**： 提供一致的 RESTful 接口，方便开发者使用；支持异步操作，提高用户体验；与其他 Ceph 管理、监控工具兼容。

**Calamari 目标用户**

- Ceph 社区成员
- Red Hat 社区成员
- 开源社区项目
- OpenStack 等云平台

**Calamari 当前状态**

- 已实现约 30 个 Rados 命令的功能。
- 已覆盖 OSD 和 Pool 相关功能。
- 对 Mon 和 Metadata Server 的支持较少。

**Calamari 1.3 版本计划**

- 改进 Crush 支持功能，包括管理节点和规则。
- 在 GUI 中展示多集群功能。
- 引入基于角色的授权机制。

**社区参与机会**

- 贡献文档
- 报告新功能需求
- 参与邮件列表讨论
- 开发和打包 Calamari
- 贡献代码

**行动计划**

- 完成Calamari 1.3 版本开发。
- 推动Calamari 在更多发行版中打包。
- 加强社区参与和沟通。

**其他**

- 讨论了与其他 Ceph 管理、监控工具的兼容性。
- 讨论了 Calamari GUI 的命名问题。
- 讨论了 Calamari 依赖包的打包问题。

本次会议对 Calamari API 的现状、目标和未来计划进行了详细的讨论，并明确了社区参与的机会。Calamari 作为 Ceph 的一个重要管理工具，将在 Ceph 社区中发挥越来越重要的作用。