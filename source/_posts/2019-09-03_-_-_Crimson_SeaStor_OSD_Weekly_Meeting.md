---
categories:
- 视频总结
date: 2019-09-06
subtitle: 2019-09-03_-_-_Crimson_SeaStor_OSD_Weekly_Meeting
tags:
- Ceph
- 分布式存储
- 测试
title: "'2019-09-03 :: Crimson SeaStor OSD Weekly Meeting'"
updated: 2019-09-07
---



### 改进后的中文总结内容

会议纪要

会议时间：2019年9月3日
会议地点：[请填写会议地点]
参会人员：Keefer，其他研发人员

会议内容：

1. **性能测试与集成**
   - Keefer汇报了上周的性能测试工作，比较了基准测试与改进后的结果。
   - 计划将测试结果集成到Jenkins中，并探索不同的集成方法，如GitHub API。
   - 预计本周内完成集成，以便在GitHub上展示测试结果的差异。

2. **GitHub API使用**
   - 讨论了使用GitHub API展示测试结果的可行性，包括在PR页面添加检查标签。
   - 决定利用GitHub API的灵活性来展示更详细的测试结果。

3. **调试与代码问题**
   - Keefer在调试过程中遇到问题，特别是在GDB环境中。
   - 讨论了代码在不同环境下的行为差异，以及如何解决这些问题。

4. **Crimson项目**
   - 讨论了Crimson项目的以下议题：
     - 观察通知机制的实施。
     - 对大PG对象上下文的细粒度锁定。
     - 系统的预定订单。
   - 讨论了即将到来的峰会，并确认了参会人员。

5. **Sister项目**
   - 讨论了Sister项目的以下议题：
     - 修复一个小的bug。
     - 支持UNIX域套接字。
     - 关于连接接受的讨论，包括POSIX套接字的处理方式。
   - 决定将修复的代码提交到Sister项目的分支，并定期与上游合并。

6. **性能测试**
   - 讨论了在性能测试中使用Rkt和CBT进行性能比较的必要性。
   - 提出在测试中关闭单元测试以避免性能影响的建议。

7. **后续行动计划**
   - Keefer将继续工作，解决调试问题和性能测试。
   - 其他研发人员将继续工作在各自的项目中，并准备即将到来的峰会。

备注：
- 会议中提到了一些计算机科学/ceph相关领域的英文关键词，包括：GitHub API, Jenkins, performance tests, POSIX sockets, UNIX domain sockets, PG objects, connection acceptance, debugging, performance comparison, Rkt, CBT等。