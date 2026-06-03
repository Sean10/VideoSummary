---
title: "Ceph Day Melbourne Roundtable Q&A"
date: 2015-11-13
updated: 2015-11-13
tags:
  - "Ceph"
  - "分布式存储"
  - "Erasure Coding"
categories:
  - "会议纪要"
outline: deep
---
### 会议纪要

**会议主题**： Ceph 存储系统讨论会

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Ceph 开发者、用户、技术专家等

**会议内容**：

1. **损坏编码（Erasure Coding）**：
   - 讨论了损坏编码中奇偶校验块的数量，以及如何确定最佳配置。
   - 分析了不同存储介质（如闪存）上的性能差异。
   - 探讨了地理复制和异步复制在实现高可用性和性能方面的作用。

2. **地理复制（Geo Replication）**：
   - 讨论了在公共互联网上进行地理复制的情况。
   - 提到了正在尝试地理复制的组织，如马来西亚政府。
   - 讨论了实现最终一致性和选择合适工作负载的方法。

3. **多租户（Multi-tenancy）和命名空间**：
   - 讨论了多租户和命名空间在 Ceph 中的实现，以及如何隔离数据。
   - 强调了安全性和性能方面的挑战。

4. **Ceph 存储集群配置**：
   - 讨论了如何配置 Ceph 存储集群以处理不同类型的工作负载（对象存储、块设备存储和文件系统存储）。
   - 强调了 Ceph 架构的优势，如并行化工作负载和灵活的配置选项。

5. **Ceph 的监控和管理**：
   - 讨论了 Ceph 的监控和管理工具，如 Calamari、Roma 和 USM。
   - 强调了社区开发工具的重要性以及选择合适工具的方法。

6. **自动化部署**：
   - 讨论了 Ceph 的自动化部署工具，如 Ceph Deploy 和其他编排工具（如 Puppet、Ansible 等）。
   - 讨论了不同工具的优缺点以及如何选择合适的工具。

**后续行动计划**：

- 继续开发和完善 Ceph 的监控和管理工具。
- 探索地理复制和最终一致性的实现。
- 支持更多用户和应用程序的多租户需求。
- 优化 Ceph 存储集群的配置和性能。

**关键词**：

- 损坏编码（Erasure Coding）
- 地理复制（Geo Replication）
- 多租户（Multi-tenancy）
- 命名空间（Namespaces）
- 监控和管理（Monitoring and Management）
- 自动化部署（Automation Deployment）
- Ceph Deploy
- Puppet
- Ansible
