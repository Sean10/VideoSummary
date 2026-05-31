---
title: Ceph Testing Meeting 2018-09-26
date: 2018-09-26
updated: 2018-10-17
tags:
- Ceph
- 分布式存储
- 测试
categories:
- "视频总结"
subtitle: Ceph_Testing_Meeting_2018-09-26
---

### 会议纪要

**会议时间**： 2018年9月26日

**参会人员**： Nathan, David, Greg, Ricardo, Zach, Kier, Ron, Warren等

**会议主题**： Ceph分布式存储项目进展及问题讨论

**关键细节**：

* **测试问题**：
    * Nathan提出，Ceph集群中运行的任务，若运行时间超过12小时，则任务会被超时杀死，导致无法收集日志，影响调试。
    * 讨论了两种解决方案：使用不同信号通知Ceph开始清理过程，或将清理工作拆分到不同进程。
    * 决定优先解决日志收集问题，并在测试中添加超时机制。
* **PR处理**：
    * 讨论了多个待处理的PR，包括Nathan的before teardown和dump context等。
    * 决定合并部分PR，并处理冲突和问题。
* **其他事项**：
    * 讨论了Ceph社区测试页面和Jenkins测试权限问题。
    * 讨论了Python 3兼容性问题。
    * 讨论了SSH pull request的合并问题。

**讨论的主要议题**：

* 如何解决Ceph测试中日志收集问题。
* 如何处理待处理的PR。
* 如何改进Ceph测试和开发流程。

**决定的事项**：

* 优先解决日志收集问题，并考虑在测试中添加超时机制。
* 合并部分PR，并处理冲突和问题。
* 改进Ceph测试和开发流程。

**后续行动计划**：

* Nathan将继续研究日志收集问题，并与团队讨论解决方案。
* Greg将处理待处理的PR，并协助解决冲突和问题。
* David和Zach将改进Ceph测试和开发流程。

**关键词**：
* Ceph
* 分布式存储
* 测试
* 日志收集
* PR
* Jenkins
* Python 3
* SSH
* Ceph社区
* JIRA

