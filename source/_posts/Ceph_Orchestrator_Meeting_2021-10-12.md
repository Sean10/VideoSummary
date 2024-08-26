---
title: "Ceph Orchestrator Meeting 2021-10-12"
date: 2021-10-12
updated: 2021-10-13
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概览
本次会议主要讨论了Ceph Orchestrator的多个议题，包括Cephadm集成、容器注册表管理、Manila与Ceph及Ganesha的交互等。

#### 主要议题及讨论内容

1. **Cephadm集成**
   - 冬季项目已经开始，Cephadm已添加了新的集成功能。
   - 已有两名学生对项目感兴趣，期待更多集成到视频中的可能性。

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

#### 会议结束

- 会议在讨论了所有议题后圆满结束，参与者对未来的工作方向有了更清晰的认识。
- 感谢所有参与者的贡献，并期待下周的进一步讨论和进展。

---

以上是本次Ceph Orchestrator会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。