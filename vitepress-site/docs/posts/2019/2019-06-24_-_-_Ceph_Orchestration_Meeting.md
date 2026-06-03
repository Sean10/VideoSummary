---
title: "2019-06-24:: Ceph Orchestration Meeting"
date: 2019-06-24
updated: 2019-06-28
tags:
  - "Ceph"
  - "编排"
  - "RGW"
  - "Rook"
  - "CI/CD"
categories:
  - "会议纪要"
outline: deep
---
在2019年6月24日的Ceph Orchestration Meeting中，Orchestrator团队成员讨论了多个关键议题：

1. **RGW区域设置讨论**：会议中提到了在实施RGW区域设置时遇到的问题，特别是配置Amazon S3组时的复杂性。团队成员讨论了Rook的设计，并决定将节点管理和配置分开处理，同时邀请Matt Benjamin团队的人员参与审查和提供建议。

2. **Orchestrator自命名空间包**：讨论了将Python代码抽取到公共包中的想法，但由于可能带来的风险和代码重构，决定在Sebastian返回后，再次会议讨论。

3. **Rook进展**：Sebastian介绍了Rook的最新进展，包括连接外部集群和部署NFS的PR，并讨论了其中的冲突。

4. **治理和CI/CD**：讨论了治理的更新，以及如何处理CI/CD中的问题，包括Skip CI标志和构建失败的情况。

5. **基于PVC的OSD设计**：讨论了基于PVC的OSD设计进展，以及设备集的考虑。

6. **OSD重设计**：讨论了Peter提出的OSD重设计，包括合并冲突和功能不匹配等问题，并提出了使用命令运行器框架和Semoran检查器的建议。

会议还确定了后续行动计划，包括与Matt Benjamin团队沟通、讨论Orchestrator自命名空间包、推进Rook的PR、解决CI/CD中的问题、完成基于PVC的OSD设计和OSD重设计。