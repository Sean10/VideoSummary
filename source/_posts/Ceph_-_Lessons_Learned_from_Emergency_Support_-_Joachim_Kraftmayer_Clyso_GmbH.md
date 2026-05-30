---
categories:
- 视频总结
date: 2023-05-05
subtitle: Ceph_-_Lessons_Learned_from_Emergency_Support_-_Joachim_Kraftmayer_Clyso_GmbH
tags:
- Ceph
- 分布式存储
- 紧急支持
- 高可用性
- 性能优化
title: "'Ceph: Lessons Learned from Emergency Support - Joachim Kraftmayer, Clyso GmbH'"
updated: 2023-05-05
---



### 会议纪要

#### 会议主题：紧急支持中的经验教训

#### 主讲人：Joachim Kraftmayer，Clyso GmbH

#### 会议内容总结：

1. **Ceph使用案例和经验分享**：
   - Joachim Kraftmayer分享了Ceph在过去两三年中的多种应用案例，强调了其在虚拟环境、大型集群和超大规模环境中的多样性。
   - 讨论了Ceph在不同硬件和部署工具中的应用，如VMware、OpenStack、DeepSea、SaltStack、Ansible等。

2. **具体案例分析**：
   - **性能问题**：一个仅含三个OSD的集群因使用较旧的Ceph版本（Luminous）而出现性能问题。
   - **配置和管理问题**：强调了PG（Placement Groups）的重要性，并讨论了如何在不中断服务的情况下动态调整集群配置。
   - **硬件和网络问题**：指出消费者级SSD、桌面旋转磁盘、CPU功率不足和网络接口带宽瓶颈等问题。

3. **功能和配置建议**：
   - **MDS服务**：建议根据负载合理配置MDS数量，避免过度配置。
   - **PG Auto Scaler**：建议禁用自动缩放，手动预定义PG数量以确保性能。
   - **缓存层**：不建议使用RBD缓存层，因其不稳定且难以管理。

4. **数据恢复和备份策略**：
   - 强调了备份策略的重要性，尤其是在生产环境中。
   - 讨论了数据恢复的复杂性和潜在风险，特别是在使用大容量磁盘时。

5. **操作和管理建议**：
   - 建议定期进行硬件和性能测试，以确保集群的健康运行。
   - 强调了在生产环境中进行彻底测试的重要性，避免盲目信任自动配置。

#### 后续行动计划：
- **社区和培训**：计划在德国组织Ceph日活动，以加强与社区的联系并分享生产经验。
- **硬件和配置优化**：继续研究和优化Ceph在不同硬件和配置下的性能。
- **备份和恢复策略**：为生产环境制定和实施更有效的备份和恢复策略。

#### 会议反馈和讨论：
- 与会者就MDS数量、PG配置、硬件选择等问题进行了深入讨论。
- 主讲人强调了Ceph在大型集群中的应用和管理挑战，以及如何通过合理的配置和策略来应对这些挑战。

#### 结束语：
- Joachim Kraftmayer感谢与会者的参与，并鼓励大家继续关注Ceph的发展和最佳实践。