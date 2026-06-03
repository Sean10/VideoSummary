---
title: "Ceph Orchestrator Meeting 2020-08-24"
date: 2020-08-24
updated: 2020-08-25
tags:
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
本次Ceph Orchestrator会议主要讨论了以下几个议题：

1. **日志处理问题**
   - 由于容器日志默认通过systemd转发到syslog，导致日志管理复杂。
   - 讨论了中断日志转发链的可行性，并探讨了使用journald namespaces作为解决方案。

2. **Python版本支持问题**
   - 由于Python 2已不再维护，团队讨论了是否继续支持CentOS 7，多数意见倾向于不再支持。

3. **新功能提议：硬件信息收集**
   - 提出通过新的gather facts命令收集系统硬件详细信息，如CPU核心数、内存大小和网络接口等。
   - 团队认为这一功能对用户了解硬件配置和优化部署流程非常有用。

4. **文档更新与简化**
   - Sebastian和另一位成员正在简化文档结构，减少重复内容。
   - 计划在9月1日前完成初步的文档更新，包括改进安装指南。

会议还确定了以下后续行动计划：
- 继续探讨和测试使用journald namespaces的可行性。
- 确定不再支持CentOS 7，并更新相关文档和部署指南。
- 完善gather facts命令的功能。
- 继续进行文档的分类和简化工作。

整个会议时长约17分钟，讨论内容简洁高效。