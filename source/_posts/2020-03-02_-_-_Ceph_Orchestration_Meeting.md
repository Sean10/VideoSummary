---
title: "2020-03-02 :: Ceph Orchestration Meeting"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
本次会议主要讨论了分布式存储系统Ceph的相关开发进展，特别是与Rook项目和Octopus版本的集成测试。会议中还涉及了天气闲聊、个人健康状况以及一些技术问题的讨论。

#### 主要议题
1. **天气与个人状况**：
   - 与会者讨论了各自地区的天气情况，包括雪和春天的到来。
   - Sebastian因病未能参加会议，会议对此表示遗憾。

2. **Rook项目进展**：
   - 讨论了在Rook项目中创建新的Python客户端仓库的决策，并将Python客户端代码从现有仓库迁移到Rook中。
   - 提到了Rook项目中对Octopus RC版本的测试，已有PR（Pull Request）开放进行集成测试。

3. **Ceph Octopus测试**：
   - 讨论了如何对Octopus版本进行更频繁的测试，包括设置夜间构建以便持续测试最新主分支。
   - 强调了需要一个可靠的镜像来进行测试。

4. **技术问题与解决方案**：
   - 讨论了在设置Ceph集群时遇到的问题，特别是与监控节点和操作符的连接问题。
   - 提到了一些正在进行的技术改进，如改进调度器和服务描述的更新。

5. **后续行动计划**：
   - 继续进行Octopus版本的测试，并确保所有相关的PR得到适当的审查和合并。
   - 解决技术问题，如改进Ceph集群的部署和管理，以及优化Rook项目的集成。

#### 决定事项
- 创建新的Rook仓库用于Python客户端，并迁移相关代码。
- 继续推进Octopus版本的测试工作，确保测试的可靠性和频繁性。

#### 后续行动
- 完成Rook项目中Python客户端代码的迁移工作。
- 继续进行Octopus版本的集成测试，并解决测试中遇到的问题。
- 解决Ceph集群部署中的技术问题，优化集群管理和操作。

#### 其他
- 会议中还讨论了个人健康、天气等非技术话题，增强了团队的凝聚力。

本次会议为Ceph和Rook项目的进一步发展奠定了基础，并明确了下一步的工作重点和行动计划。