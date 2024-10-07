---
title: "Ceph Orchestrator Meeting 2020-08-24"
date: 2020-08-24
updated: 2020-08-25
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间与参与人员
- **时间：** 会议开始时稍有延迟，大约晚了2分钟。
- **参与人员：** 会议中提到了多位参与者，包括但不限于Karen Deck, Sebastian, 以及其他未明确提及姓名的团队成员。

#### 主要议题与讨论内容
1. **日志处理问题**
   - **问题描述：** 当前容器日志通过systemd处理后，默认配置下会转发到syslog，导致日志管理变得复杂且难以使用。
   - **讨论焦点：** 是否应该中断日志转发链，以及如何在不破坏现有系统服务处理方式的前提下解决此问题。
   - **提议解决方案：** 探讨使用journald namespaces来解决日志管理问题，但未有明确结论。

2. **Python版本支持问题**
   - **讨论内容：** 由于CentOS 7默认安装Python 2，而Python 2已不再维护，团队讨论是否继续支持CentOS 7。
   - **决策：** 多数意见倾向于不再支持CentOS 7，以简化开发和部署过程。

3. **新功能提议：硬件信息收集**
   - **提议内容：** 提出一个新的pull request，旨在通过新的gather facts命令收集系统硬件详细信息，如CPU核心数、内存大小和网络接口等。
   - **讨论结果：** 团队认为这一功能对于用户了解硬件配置和优化部署流程非常有用，支持进一步开发和完善。

4. **文档更新与简化**
   - **工作进展：** Sebastian和另一位成员正在努力简化文档结构，特别是减少重复内容，但发现不同文档服务于不同用例，需要进一步分类和整合。
   - **后续计划：** 计划在9月1日前完成初步的文档更新，包括改进安装指南的呈现方式。

#### 后续行动计划
- **日志处理：** 继续探讨和测试使用journald namespaces的可行性。
- **Python版本：** 确定不再支持CentOS 7，更新相关文档和部署指南。
- **硬件信息收集：** 完善gather facts命令的功能，确保提供准确和有用的硬件信息。
- **文档更新：** 继续进行文档的分类和简化工作，确保信息清晰且易于导航。

#### 会议结束
- **会议时长：** 约17分钟。
- **下次会议：** 计划下周再次同步。

会议在简短而高效的讨论后结束，团队成员对未来的工作方向有了更清晰的认识。