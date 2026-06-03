---
title: "2019-06-17:: Ceph Orchestration Meeting"
date: 2019-06-17
updated: 2019-06-17
tags:
  - "Ceph"
  - "分布式存储"
  - "编排"
categories:
  - "视频总结"
outline: deep
---
本次Ceph Orchestration会议主要讨论了Octopus项目的路线图，包括以下关键议题：

1. **SSH Orchestrator**： 会议重点讨论了SSH Orchestrator，目前存在API断裂的风险，团队决定等待问题解决后再考虑对Rope Orchestrator的修改。行动计划包括关注SSH Orchestrator的进展，等待API断裂问题解决，研究Rope Orchestrator的修改方案。

2. **Rook Traverse**： 由于Rook Traverse项目成员缺席，未进行具体讨论。

3. **动态生成STI**： 针对云环境，提出动态生成STI的请求，以支持集群扩展。行动计划包括完成设计文档，研究将所有T设备背后的存储池信息集成到本地存储集群中。

4. **ESS Afton**： ESS Afton项目需要一些架构变更，以支持将核心功能迁移到上游。行动计划包括组建文档，为后续讨论提供基础，Sebastian将加入会议并提供贡献。

5. **升级测试**： 针对Octopus的升级测试，确保所有组件都经过充分测试。行动计划包括确保所有组件都经过升级测试，考虑在下一个周期进行全面的升级测试。

6. **资源分配**： 讨论了Octopus项目的资源分配。行动计划包括Octopus项目团队专注于Rook和Rook Traverse的开发，研究如何将一些部署自动化功能集成到Orchestrator层或其之上。

7. **其他讨论**： 讨论了如何将部署自动化功能集成到Orchestrator层或其之上，简化集群部署流程，以及解决容器镜像管理问题。

会议强调了后续行动计划的重要性，各团队成员将根据会议讨论的内容执行相应的行动计划，并定期召开会议跟踪项目进展。