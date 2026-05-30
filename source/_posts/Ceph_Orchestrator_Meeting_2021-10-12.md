---
categories:
- 视频总结
date: 2021-10-12
subtitle: Ceph Orchestrator_Meeting_2021-10-12
tags:
- Ceph Orchestrator
- Cephadm
- Container Registry Management
- Manila Integration
- Ganesha Interaction
title: "Ceph Orchestrator Meeting 2021-10-12"
updated: 2021-10-13
---




本次Ceph Orchestrator会议主要围绕Ceph Orchestrator的多个议题展开讨论，包括Cephadm集成、容器注册表管理、Manila与Ceph及Ganesha的交互等。

1. **Cephadm集成**
   - 冬季项目已启动，Cephadm新增了新的集成功能。
   - 已有两名学生加入项目，并期待更多功能集成到视频演示中。

2. **容器注册表管理**
   - 讨论了如何处理容器注册表版本列表，特别是自定义注册表与上游注册表的差异。
   - 探讨了使用Python库与Docker注册表交互的可行性，但存在维护问题。
   - 讨论了是否需要列出所有标签，以及如何处理最新标签的更新。

3. **Manila与Ceph及Ganesha的交互**
   - 讨论了Manila如何通过Orchestrator与Ceph及Ganesha交互，特别是通过CLI还是API。
   - 探讨了权限问题，特别是非管理员用户如何执行CLI命令。
   - 讨论了如何更新Ganesha配置文件的部分内容，以及如何获取当前Ganesha demon的状态描述。

#### 决定事项

- 继续探索Cephadm的新集成功能，并鼓励更多学生参与。
- 确定使用CLI作为与Orchestrator交互的主要方式，尽管也考虑了API的可能性。
- 确认了非管理员用户执行CLI命令所需的权限，并计划进一步细化这些权限。

#### 后续行动计划

- 继续开发和测试Cephadm的新集成功能。
- 进一步研究如何通过CLI或API与Orchestrator进行更有效的交互。
- 细化非管理员用户的权限设置，确保Manila能够安全地与Ceph及Ganesha交互。
- 探索如何更好地管理和更新Ganesha配置文件，以及如何获取和展示Ganesha demon的当前状态。

#### 其他讨论点

- 讨论了Ingress demon的状态和其在生产环境中的适用性。
- 探讨了如何处理Orchestrator命令的异步性质，以及如何确保数据路径的连续性。

本次会议对Ceph Orchestrator的未来发展方向提供了清晰的指引，并确定了后续的工作重点。