---
title: "  Keynote: What's Planned for Ceph Octopus - Sage Weil, Co-Creator, Chief Architect Ceph  "
date: 2019-05-24
updated: 2019-05-24
tags:
- 分布式存储
- 开源
categories:
- "视频总结"
subtitle: Keynote_-_What_s_Planned_for_Ceph_Octopus_-_Sage_Weil_Co-Creator_Chief_Architect_Ceph
---



Ceph 项目联合创始人兼首席架构师 Sage Weil 在本次演讲中详细介绍了 Ceph Octopus 版本的发展方向和社区参与方式。以下是对会议内容的总结：

**会议内容**

1. **Ceph Octopus 版本重点**：

   - **易用性提升**：改进 Orchestrator API，增强集群与 Rook 或裸金属编排工具的交互能力。提供端到端 GUI 体验，简化操作流程。自动化升级过程，提高升级效率。
   - **质量提升**：优化 Nautilus 和 Telemetry 功能，提供更全面的监控和故障报告。加强文档质量，提升用户体验。完善测试套件，确保代码质量。
   - **性能优化**：改进 BlueStore 性能，包括 RocksDB 的优化和 T-RocksDB 的引入。异步化创建和删除操作，提升性能。
   - **多站点、多集群支持**：优化 GW 多站点功能，包括桶粒度控制、透传存储、双向复制等。探索 SouthFS 的更多功能，如灾难恢复和双向复制。
   - **生态系统建设**：加强与 Kubernetes、OpenStack 等生态系统的集成。关注大数据、机器学习等新兴领域。

2. **社区参与方式**：

   - **贡献代码**：通过 GitHub 提交 pull request，参与代码审查。
   - **提交 bug**：在 Ceph 用户邮件列表或 GitHub 上提交 bug。
   - **完善文档**：参与 Ceph 文档的编写和修订。
   - **参与会议**：加入 Ceph 社区会议，交流经验。
   - **组织活动**：参与 Ceph 社区活动，如 CephDay。

**决定事项**

1. Ceph 项目将继续关注易用性、质量、性能、多站点/多集群支持以及生态系统建设等方面。
2. 鼓励社区成员积极参与 Ceph 项目的开发、测试和文档编写。

**后续行动计划**

1. Ceph 项目团队将继续推进 Octopus 版本的开发工作。
2. 社区成员可以关注 Ceph 项目邮件列表和 GitHub，了解项目进展。
3. Ceph 项目团队将定期举办线上和线下活动，促进社区交流。