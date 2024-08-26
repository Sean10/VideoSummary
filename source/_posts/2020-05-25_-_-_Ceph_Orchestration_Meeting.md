---
title: "2020-05-25 :: Ceph Orchestration Meeting"
date: 2020-05-26
updated: 2020-05-26
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要

会议主题：Ceph存储系统的监控与升级策略讨论

会议地点：渥太华（Ottawa）与纽约（New York）

会议时间：具体日期未提及

参会人员：Erika、Cedrick、Josef（GM-Manager）等

主要议题：
1. **监控系统基础建设**：讨论了直接监控（direct monitoring）的重要性，特别是在容器（containers）环境中，确保问题能够及时被发现和解决。
2. **私有注册表（Private Registry）**：Cedrick提到了私有注册表的必要性，以及如何确保其安全性和可用性。
3. **升级策略**：讨论了如何优化升级过程，包括连续交易更新服务（continous traded update service）和安全升级（safety and means that you cannot job in the upgrade）。强调了升级过程中的风险和必要性。
4. **文档更新**：提到了上游文档（upstream documentation）的升级需求，以及如何确保文档的及时更新和准确性。
5. **配置优化**：讨论了如何在支持配置（support configuration）中减少步骤，优化前序步骤（predecessor little steps），以提高效率和减少历史维度（historical dimension）的影响。

决定事项：
- 需要建立一个基础的监控系统，特别是在容器环境中。
- 私有注册表的安全性和可用性需要进一步加强。
- 升级过程需要优化，确保安全和高效。
- 上游文档需要定期更新，确保信息的准确性和及时性。
- 支持配置需要优化，减少不必要的步骤，提高效率。

后续行动计划：
- 制定详细的监控系统建设方案，并开始实施。
- 对私有注册表进行安全性和可用性评估，并制定改进措施。
- 制定升级过程的优化方案，并开始实施。
- 定期更新上游文档，确保信息的准确性和及时性。
- 优化支持配置，减少不必要的步骤，提高效率。

会议结束语：Erika总结了会议内容，并强调了各项任务的重要性和紧迫性。会议在确认后续行动计划后结束。