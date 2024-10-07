---
title: "RGW Refactoring Meeting 2022-09-28"
date: 2022-09-29
updated: 2022-09-30
tags:
categories:
- "视频总结"
subtitle: tech
---


会议纪要：

1. 讨论主题：Ceph分布式存储系统的性能指标优化和模块化进程。
   - 主要关注点：如何管理和优化大量的性能计数器，并处理模块化过程中遇到的问题。

2. 参与者：
   - Yvonne（Ceph导出器开发者）
   - Ilya（RBD领导）
   - Casey（参与讨论并提出问题和建议）

3. 关键议题：
   - 性能计数器的管理和优化：Yvonne提到她有支持标签化性能计数器的工具，而Ilya表示不需要太多标记的性能计数器。Casey询问了关于性能计数器爆炸性增长的问题以及如何进行过滤。
   - 自动化策略的探讨：Casey提出一个自动化的方法来识别“热用户”和“热存储桶”，从而只启用那些被认定为“热”的标记性能计数器。
   - 模块化进程：Ilya谈到了他在管理admin APIs时进行的模块化进程，并提出了在S3层操作中分离pub/sub操作的问题。

4. 决定事项：
   - 短期内，将重点放在优化现有的性能计数器管理上，不立即实施复杂的自动化策略。
   - 长期解决方案可能需要构建一个新的系统，该系统能够根据用户的需求动态地启用或禁用特定的性能计数器。
   - 需要进一步讨论如何处理Prometheus无法处理大量性能计数器的问题。

5. 后续行动计划：
   - Yvonne将继续完善她的标签化性能计数器工具，并在下一周展示新版接口。
   - Ilya和团队将继续进行模块化进程，特别是解决pub/sub操作的分离问题。
   - Casey将探索自动化策略，以更有效地管理性能计数器。

6. 其他讨论：
   - 讨论了HTTP 3前端原型的开发和测试，欢迎感兴趣的成员参与。

7. 结论：
   - 会议围绕Ceph的性能优化和模块化进程进行了深入讨论，确定了短期和长期的行动计划，并鼓励团队成员继续在这些领域进行探索和开发。