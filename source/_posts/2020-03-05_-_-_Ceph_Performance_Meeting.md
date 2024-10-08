---
title: "2020-03-05 :: Ceph Performance Meeting"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间：[具体日期]
#### 参会人员：[具体人员名单]

#### 主要议题：
1. **性能优化更新**
   - 本周没有太多新的或更新的性能相关的Pull Requests (PRs)，团队主要集中在为下一个版本Octopus的修复工作上。
   - 关闭的PR包括：
     - 对BlueStore的NVMe设备后端的小优化，移除了不必要的操作。
     - Igor提交的一个小PR，增加了日志分配统计，用于4K Metallic大小测试。
     - Casey合并的PR，允许修改配置索引卡，主要改变了默认的桶索引分片数量，以提高列表桶索引的速度。

2. **IO 500测试进展**
   - 继续进行SELinux测试与IO 500评分提升工作。
   - 发现内核客户端在大尺寸读取时性能较慢，Fuse客户端也因多种原因性能极差。
   - 开发了一个后端用于IOR和MD测试，直接与Loops FFS集成，初步结果显示在大尺寸顺序读取上显著更快。

3. **PG日志更新优化**
   - 讨论了移除PG日志调用的实验，结果显示延迟显著降低，IOPS每核心有所提升。
   - 建议将PG日志更新从brats TB移至其他不引起大量光放大的地方。

#### 决定事项：
- 继续优化和测试IO 500性能，特别是比较内核客户端和Loops FFS的性能。
- 进一步研究和实施PG日志更新的优化策略。

#### 后续行动计划：
- 继续关注和处理性能相关的PRs。
- 完成IO 500测试，并根据结果调整策略。
- 实施PG日志更新的优化，并监测其对性能的影响。

#### 其他讨论：
- 讨论了使用不同客户端（如Fuse和Loops FFS）的性能差异及其原因。
- 探讨了未来可能尝试的其他用户空间文件系统内核模块。

#### 会议结束：
- 会议在讨论了所有议题后结束，团队成员将继续专注于各自的任务，并计划下周再次会议。

#### 备注：
- 会议中提到的具体技术细节和代码优化建议，需要进一步的技术文档和代码审查来确保实施的正确性和有效性。

---

以上为会议的详细纪要，涵盖了会议的主要讨论点、决定和后续行动计划。