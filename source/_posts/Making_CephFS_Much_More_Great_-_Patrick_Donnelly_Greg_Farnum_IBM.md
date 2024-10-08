---
title: "Making CephFS (Much More) Great! - Patrick Donnelly & Greg Farnum, IBM"
date: 2023-05-09
updated: 2023-05-09
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议基本信息
- **主持人**: Patrick（前CFS团队负责人，现参与Sepafest项目）
- **参与者**: Greg（SEF Fest团队经理，前STL长期贡献者）及其他与会者

#### 会议议题
1. **CFS多集群恢复能力**
   - 讨论了多集群故障恢复的难度和当前的不完善状态。
   - 提出了改进建议，包括查看相关故障报告、社区讨论以及配置或升级解决方案。

2. **MDS故障恢复**
   - 讨论了MDS在某些情况下会放弃的问题，通常在故障转移情况下可以恢复。
   - 强调了Red Hat Ceph团队现在有更多客户，这些问题的出现频率增加，成为业务优先事项。

3. **SMB与CephFS的集成**
   - 讨论了使用Samba VFS与CephFS集成的问题，包括Samba的工作方式和潜在的问题。
   - 提出了改进建议，但目前没有具体的开发重点。

4. **升级问题**
   - 讨论了从Nautilus升级到Quincy时的多活动MDS问题，特别是升级过程中的挑战。
   - 提出了新的升级选项，如关闭整个CephFS文件系统进行升级，以避免不同版本的MDS相互通信的问题。

5. **性能和稳定性改进**
   - 讨论了MDS缓存大小、客户端性能问题以及如何通过配置调整来改善。
   - 提出了关于CephFS top工具的改进，以及如何更好地监控和收集客户端性能数据。

#### 决定事项
- 需要进一步研究和改进CephFS的多集群恢复能力和MDS故障恢复机制。
- 需要关注和解决SMB与CephFS集成中的问题。
- 需要改进升级过程，特别是多活动MDS的升级策略。
- 需要增强CephFS的监控和性能数据收集能力。

#### 后续行动计划
- 继续研究和开发多集群恢复和MDS故障恢复的解决方案。
- 关注和解决SMB与CephFS集成中的具体问题。
- 改进和优化CephFS的升级流程。
- 增强CephFS的监控和性能数据收集功能，特别是在客户端性能方面。

#### 其他讨论点
- 讨论了CephFS的快照和克隆功能的限制和改进建议。
- 讨论了CephFS的扩展属性和统计功能的实际应用和潜在改进。

#### 会议总结
会议主要围绕CephFS的多个关键问题进行了深入讨论，包括故障恢复、集成问题、升级挑战和性能监控。会议强调了持续改进和用户反馈的重要性，并提出了具体的改进方向和行动计划。感谢所有参与者的积极讨论和贡献。