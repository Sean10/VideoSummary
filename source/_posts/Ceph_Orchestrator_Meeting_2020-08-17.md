---
categories:
- 视频总结
date: 2020-08-17
subtitle: Ceph_Orchestrator_Meeting_2020-08-17
tags:
- Ceph
- 分布式存储
- 自动化
title: "Ceph Orchestrator Meeting 2020-08-17"
updated: 2020-08-18
---



本次 Ceph Orchestrator 周会主要讨论了以下议题：

1. **德国构建问题**：由于容器未推送到 CPR 容器注册表，以及 I 容器构建出现问题，导致无法合并任何内容。会议决定联系 David Galloway 解决问题，因为他是唯一有权访问 quiet.io 的人员。同时，建议联系 Christina Venus 团队成员协助。

2. **Cepheidiam 二进制文件的重组**：需要对 Cepheidiam 二进制文件进行重构，讨论了重构的必要性和步骤，建议逐步进行。涉及将 self-adm 作为适当的包进行分发，并确保其能在远程机器上正常工作。

3. **文档整合**：讨论了关于安装指南的整合问题。建议将现有的两个安装指南合并为一个，并分为基础安装和附加功能（如 Ganesha 和 MDS）的多个页面。计划本周内开始整合工作，并发送 Pull Request 进行进一步讨论。

会议的决定事项包括：
- 联系Christina Venus团队成员协助解决德国构建问题。
- 开始对Cepheidiam二进制文件进行重构工作。
- 合并现有的两个安装指南为一个，并分为基础和附加功能的不同页面。

后续行动计划：
- 联系David Galloway或Christina Venus团队成员解决容器推送问题。
- 开始Cepheidiam二进制文件的重构工作，并逐步实施。
- 整合安装指南，并发送Pull Request进行团队讨论和反馈。

此外，会议还讨论了文档的详细程度和新手友好性，强调了为初学者提供详细步骤的重要性。计划制作视频教程，以辅助文档说明。