---
title: "2018-FEB-08 :: Ceph Performance Weekly"
date: 2018-02-13
updated: 2018-02-14
tags:
  - "性能优化"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议时间**： 2023年11月某日

**参会人员**： 多位Ceph研发人员

**会议主题**： 讨论和审查Ceph项目的代码提交、性能优化以及相关技术问题。

**关键细节**：

* **代码审查**：
    * 重点关注了优化D级性能的PR（PR 2029），MD配置的Kasher，以及更改OathStreams的PR等。
    * 讨论了使用静态声明的第二个补丁，并同意将其改为更合适的方法。
    * 优化了减少CPU使用率的OathStreams PR，并建议进行更深入的分析。
    * 讨论了indirection layers for a shorted op work queue的PR，并建议等待合并tiny vector PR后再进行合并。
    * 讨论了EC后端使用本地读取路径的PR，以及延迟PG统计计算的PR。
* **性能优化**：
    * 讨论了配置值观察者的优化，建议使用更高效的方法来更新观察者。
    * 优化了get_val函数的性能，建议避免不必要的键规范化。
    * 讨论了reactor的性能优化，建议减少任务的大小以适应微架构缓存。
* **其他**：
    * 讨论了使用reactor进行任务分组的可能性。
    * 讨论了micro-op流水线的性能优化。

**决定的事项**：

* 对多个代码提交进行审查和合并。
* 对性能优化方案进行进一步的分析和测试。
* 考虑使用reactor进行任务分组。

**后续行动计划**：

* 继续审查和合并代码提交。
* 进行性能优化方案的测试和评估。
* 考虑使用reactor进行任务分组。

**计算机科学/ceph相关领域英文原文关键词**：

* pull request
* D out pass
* MD config
* OathStreams
* indirection layers
* EC back-end
* PG stats calculations
* config value observer
* get_val
* reactor
* micro-op
* task grouping