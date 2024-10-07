---
title: "Ceph: Lessons Learned from Emergency Support - Joachim Kraftmayer, Clyso GmbH"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：紧急支持中的经验教训

#### 主讲人：[主讲人姓名]
- **背景介绍**：
  - 公司创始人，公司名为Glyzone。
  - 曾担任Red Hat存储的高级顾问。
  - 自2012年开始涉足Ceph，2014年起在生产环境中运行Ceph。

#### 会议内容总结：

1. **Ceph的使用案例和经验分享**：
   - 过去两三年中，Ceph在各种环境中的应用案例。
   - 强调了Ceph在虚拟环境（如VMware、OpenStack、超大规模环境）中的多样性。
   - 讨论了Ceph在不同硬件和部署工具（如DeepSea、SaltStack、Ansible）中的应用。

2. **具体案例分析**：
   - **性能问题**：一个只有三个OSD的集群出现性能问题，原因是使用了较旧的Ceph版本（Luminous）。
   - **配置和管理问题**：讨论了PG（Placement Groups）的重要性，以及如何在不中断服务的情况下动态调整集群配置。
   - **硬件和网络问题**：提到了消费者级SSD和桌面旋转磁盘的不适用性，以及网络接口（如1Gbps）的瓶颈问题。

3. **功能和配置建议**：
   - **MDS服务**：建议根据负载合理配置MDS的数量，避免过度配置。
   - **PG Auto Scaler**：建议禁用自动缩放，手动预定义PG数量以确保性能。
   - **缓存层**：不建议使用RBD缓存层，因其不稳定且难以管理。

4. **数据恢复和备份策略**：
   - 强调了备份策略的重要性，特别是在生产环境中。
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
- 主讲人感谢与会者的参与，并鼓励大家继续关注Ceph的发展和最佳实践。

---

以上是对会议内容的详细总结，涵盖了关键细节、讨论的主要议题、决定的事项以及后续的行动计划。