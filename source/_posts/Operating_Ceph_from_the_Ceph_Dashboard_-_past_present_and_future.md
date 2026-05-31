---
categories:
- 视频总结
date: 2022-11-22
subtitle: Ceph Dashboard：过去、现在与未来
tags:
- Ceph
- Dashboard
- 分布式存储
- CephFS
title: "'Operating Ceph from the Ceph Dashboard: past, present and future'"
updated: 2022-11-23
---


Ceph Dashboard 是一个功能全面的分布式存储管理系统，它不仅提供监控功能，还实现了高级的 Ceph 管理操作。以下是对 Nizamudi 在会议中关于 Ceph Dashboard 介绍和回顾的总结：

1. **Ceph Dashboard 简介**：
   - Nizamudi 是 Red Hat 的软件工程师，自 2020 年加入 Ceph Dashboard 团队。
   - Ceph Dashboard 不再只是一个监控工具，而是一个具备完整管理功能的用户界面。
   - 它的历史可以追溯到 2013 年，目前是 Ceph Manager 模块的一部分。

2. **主要功能**：
   - **管理与监控**：提供集群配置、日志查看、性能监控等高级管理操作。
   - **集成与优化**：直接消费 Ceph Manager 模块的 API，实现高效的数据交互。
   - **用户界面**：提供直观的用户界面，简化复杂操作，如集群扩展、OSD 管理、RBD 镜像等。

3. **架构与技术细节**：
   - **架构**：Ceph Dashboard 通过 REST API 与后端的 Python 模块交互，获取集群数据。
   - **技术栈**：使用 Angular 和 Bootstrap 框架，未来将升级到 Angular 13 和 Bootstrap 5。

4. **发展路线图**：
   - **Reef 版本**：将重点改进 RBD 和 OSD 的管理功能，引入多站点等新特性。
   - **长期目标**：计划替换 Grafana 为内置的监控组件，增强 CephFS 的集成。

5. **用户反馈与社区贡献**：
   - **用户调查**：2022 年的用户调查显示，约 50% 的用户使用 Ceph Dashboard 进行监控。
   - **社区贡献**：鼓励用户、文档编写者和开发者参与贡献，提供多种参与方式。

6. **后续行动计划**：
   - **技术优化**：继续改进用户界面和交互体验，增强系统的可维护性和可访问性。
   - **社区互动**：通过邮件列表、IRC 和开发者指南等方式，加强与社区的沟通和协作。

会议中还讨论了以下内容：
- Ceph Dashboard 的历史和演变过程。
- 与其他 Ceph 监控工具（如 Prometheus、Grafana）的比较。
- Ceph Dashboard 的社区贡献和参与方式。
- 未来发展计划和目标。

[相关标签]
- Ceph
- Dashboard
- Distributed Storage
- Management UI
- CephFS