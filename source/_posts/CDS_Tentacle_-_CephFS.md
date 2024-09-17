---
title: "CDS Tentacle - CephFS"
date: 2024-08-22
updated: 2024-08-23
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 多位Ceph研发人员，包括负责self FS for the tentacle release的团队成员

**会议主题**：

*   self FS for the tentacle release相关议题
*   Ceph相关功能讨论

**会议内容**：

**1.  sensor directory功能**

*   Patrick介绍了sensor directory功能，该功能将支持客户端驱动的大小写敏感度实现，依赖于新增的alternate name元数据。
*   该功能将是tentacle release的优先事项，并可能回滚到squid。
*   目前已经开始相关工作，预计不久完成。
*   任何对该功能的反馈或问题，请在此处提出。

**2.  layout transformation功能**

*   Beny介绍了layout transformation功能，该功能允许用户设置目录中文件的期望布局，MDS将逐步迁移数据以适应新的布局。
*   该功能将使用现有的迁移机制和代码，但需要进行详细的代码审查，以确保正确性和安全性。
*   有关该功能的讨论将持续进行，并将在tentacle release中进行评估。

**3.  manager volume switch功能**

*   该功能涉及将subvolume元数据从文件存储迁移到SQLite数据库。
*   该迁移将提高元数据的可靠性和可扩展性，并支持事务操作。
*   讨论了数据库恢复、数据迁移和审计等问题。
*   该功能将在tentacle release中进行评估。

**4.  MDS manager identify metadata heavy workloads功能**

*   该功能旨在通过分析MDS性能指标来识别潜在的瓶颈和问题。
*   讨论了性能指标收集、存储和分析的方法。
*   该功能将在tentacle release中进行评估。

**5.  Implement of the script and use功能**

*   Chris介绍了ecript加密功能的实现情况，该功能已在libsefs和sefuse中实现。
*   目前已完成读写路径，并正在进行测试。
*   该功能将在tentacle release中进行评估。

**6.  reference for fast clone from snapshots功能**

*   该功能旨在解决硬链接文件快照的问题。
*   讨论了升级和数据扫描工具等问题。
*   该功能将在tentacle release中进行评估。

**后续行动计划**：

*   各功能负责人将根据会议讨论结果，进一步完善相关设计和实现。
*   定期召开会议，跟踪项目进展。
*   及时更新相关跟踪项和文档。

**其他事项**：

*   会议时间超过预定时间，后续将安排时间继续讨论。
*   将会议纪要更新到相关跟踪项和文档中。