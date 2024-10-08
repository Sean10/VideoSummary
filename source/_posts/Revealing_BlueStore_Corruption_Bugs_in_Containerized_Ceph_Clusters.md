---
title: "Revealing BlueStore Corruption Bugs in Containerized Ceph Clusters"
date: 2022-11-15
updated: 2022-11-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Cyborgs公司容器化Ceph存储系统开发中的数据损坏问题及改进建议

#### 会议参与者：Cyborgs公司Ceph存储系统维护团队

#### 会议日期：[具体日期]

#### 会议地点：[具体地点]

#### 会议内容总结：

1. **公司及基础设施介绍**
   - Cyborgs是一家日本公司，提供软件支持团队协作。
   - 公司目前使用基于传统虚拟机的系统，已有10-20年的历史，存在存储容量和性能的限制。
   - 正在开发新的基于Kubernetes的现代化容器化基础设施，使用Rook Ceph作为存储解决方案。

2. **开发中遇到的问题**
   - 在容器化Ceph存储系统的开发过程中，发现了多种数据损坏相关的bug，包括OSD创建失败和重启后数据请求损坏等问题。
   - 这些问题主要在HDD上被检测到，推测是因为HDD的慢速特性更容易引发某些条件下的错误。

3. **开发策略**
   - 开发策略包括三个步骤：每次更改通过PR提交，触发基于虚拟机的集成测试，测试通过后应用到预生产系统，最终部署到生产系统。
   - 在开发过程中，频繁创建和重启OSD，每天进行多次集成测试，每周重启预生产环境的所有节点以验证基础设施的可用性和更新节点固件。

4. **问题分析与改进建议**
   - 分析发现，这些问题在传统的非容器化Ceph集群中较少出现，推测与容器化环境中频繁的OSD创建和重启有关。
   - 提出的改进建议包括增加对OSD重启的应力测试，以及在QA过程中使用HDD以更好地检测潜在问题。

5. **后续行动计划**
   - 将继续与Ceph社区合作，验证和修复已报告的bug。
   - 考虑在QA流程中增加更多的应力测试和使用HDD，以提高系统的稳定性和可靠性。

#### 会议结束语
- 会议结束时，发言人感谢大家的参与，并表示希望这些信息对大家有所帮助。

#### 后续行动：
- 与Ceph社区的QA工程师联系，讨论并实施改进建议。
- 持续监控和更新Ceph存储系统的性能和稳定性。

---

**注：** 以上内容基于会议发言人的介绍和讨论，具体实施细节和时间表将根据后续讨论和决策确定。