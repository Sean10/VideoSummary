---
categories:
- 视频总结
date: 2018-01-11
subtitle: 2018-JAN-04_-_-_Ceph_Performance_Weekly
tags:
- 性能优化
- 分布式存储
- BlueStore
title: "'2018-JAN-04 :: Ceph Performance Weekly'"
updated: 2018-01-12
---




会议纪要

**会议时间**： 新年后的首次会议

**参会人员**： 多位研发人员

**会议内容**：

**一、关键细节**

*   会议开始，大家相互问候，并庆祝新年。
*   会议主要讨论了Ceph项目的多个pull request，包括新增的QAT支持、Blue Store的异步读取优化、CRC缓存补丁等。
*   会议还讨论了Ceph的性能优化，特别是针对随机读写操作的性能回归问题。
*   会议最后讨论了Ceph的存储后端接口（OST）的异步化改造。

**二、讨论的主要议题**

1.  **QAT支持补丁**： 补丁已提交，正在审查中。
2.  **Blue Store异步读取**： 
    *   补丁已提交，但存在性能回归问题，需要进一步调查。
    *   需要考虑在特定情况下使用传统的同步方式，以避免性能问题。
3.  **CRC缓存补丁**： 补丁简单且有效，已标记为QA测试。
4.  **性能优化**：
    *   针对随机读写操作的性能回归问题，需要进一步调查原因。
    *   需要关注缓存对性能的影响。
5.  **OST异步化**：
    *   讨论了如何将OST接口异步化，以及如何处理事务和同步操作。
    *   需要进一步研究并确定最佳方案。

**三、决定的事项**

*   继续调查Blue Store异步读取的性能回归问题。
*   对CRC缓存补丁进行QA测试。
*   进一步研究OST异步化方案。

**四、后续行动计划**

*   相关研发人员将继续调查Blue Store异步读取的性能回归问题，并找出解决方案。
*   QA团队将对CRC缓存补丁进行测试。
*   相关人员将继续研究OST异步化方案，并制定详细的实施计划。

**五、英文原文关键词**

*   QAT (Quick Assist Technology)
*   Blue Store
*   async read
*   CRC cache
*   performance regression
*   object store (OST)
*   transaction
*   API unification