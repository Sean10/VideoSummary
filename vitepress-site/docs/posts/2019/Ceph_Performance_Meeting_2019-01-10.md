---
title: "Ceph Performance Meeting 2019-01-10"
date: 2019-01-10
updated: 2019-01-16
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年1月10日

**参会人员**： (此处应填写参会人员名单)

**会议主题**： Ceph分布式存储项目进展及Crimson项目讨论

**会议内容**：

**一、Ceph项目进展**

1. **Pull Requests审查**：
    - 会议讨论了多个Pull Requests，包括Stack Streams、FS分配、优先级缓存大小调整、EC Cash等。
    - 部分Pull Requests已合并，如优先级缓存大小调整。
    - 需要进一步审查的Pull Requests包括EC Cash、共享LRU等。

2. **Crimson项目讨论**：
    - Crimson项目旨在优化Ceph的性能，特别是对象存储层。
    - 项目初期目标是验证假设，包括验证Crimson对性能的帮助。
    - 项目设计采用简化设计，以降低维护成本和复杂性。
    - 讨论了Crimson的OSD概念，包括如何实现多线程OSD。
    - 讨论了使用mstar线程模型的可能性，以及如何与SPDK集成。

**二、行动计划**

1. **Ceph项目**：
    - 继续审查和合并Pull Requests。
    - 对EC Cash、共享LRU等Pull Requests进行进一步审查。

2. **Crimson项目**：
    - 完成Crimson的简化设计。
    - 与SPDK团队合作，确定最佳线程模型。
    - 开展Crimson的测试工作。

**三、后续会议**

- 下次会议将于近期举行，届时将讨论Crimson项目的进展和后续计划。

**四、其他事项**

- 会议中讨论了RocksDB的使用，以及如何将其与Ceph集成。
- 讨论了Crimson项目对性能的影响，以及如何评估其效果。

**五、关键词**

- Pull Requests
- Stack Streams
- FS分配
- 优先级缓存大小调整
- EC Cash
- 共享LRU
- Crimson项目
- OSD
- mstar线程模型
- SPDK