---
title: "Ceph Developer Summit - Crimson SeaStore"
date: 2025-09-12
updated: 2025-09-12
tags:
  - "Ceph"
  - "分布式存储"
  - "Crimson"
  - "性能优化"
categories:
  - "视频总结"
outline: deep
---
Ceph开发者峰会-Crimson SeaStore会议纪要

**会议主题**: Crimson EU版本（伞形版本）规划与进展

**日期**: [会议日期]

**参会人员**: Matan, Jose, Sam, Radic等核心开发成员



**会议目标**: 

- 回顾Crimson在EU版本（V21）中的目标功能、已知问题及优化方向。
- 讨论关键技术进展，包括PG管理、性能优化、后端存储支持等。
- 确定后续行动计划。



**主要议题与讨论**:

1. **PG分裂与合并（PG Splitting & Merging）**:
   - PG分裂功能已合并至`main`分支，正在进行稳定性测试。
   - PG合并功能开发将在稳定性验证后推进。

2. **Crimson构建类型分离**:
   - 将Crimson构建分为`debug`和`release`两种类型，分别用于开发调试和生产环境。

3. **后端存储支持（Systore vs. Bluestore）**:
   - 在EU版本中支持Systore作为Crimson的默认后端存储。
   - 部分基础支持已合并，首次通过`cephadm`部署Systore的测试任务成功运行。

4. **QoS与MClock调度**:
   - PR已提交，但依赖项（如DMClock子模块的垃圾回收线程适配）待解决。
   - 需调整Crimson架构以兼容MClock的异步特性。

5. **文档与用户体验优化**:
   - 新增用户指南，仅包含部署、测试等必要信息。
   - 完整分离文档计划在EU版本中完成。

6. **性能基准测试与发布**:
   - 开始定期发布Crimson性能数据，包括IOPS、延迟等指标。
   - 4K随机读场景中Crimson优于Classic，但随机写仍需优化。

7. **其他功能开发**:
   - EC Pool支持、RGW支持、混合集群（Crimson + Classic OSD）支持、Scrub增强等。



**性能优化专题（Sam分享）**: 

- 随机写性能瓶颈分析，改进Journal批处理，提升大块写入效率。
- 并发优化，增加后台操作的并行度。



**开放问题与讨论**:

- 性能分析工具（Flame graphs）的适用性及改进建议。
- 内存局部性（Cross-CPU操作）的验证。



**后续行动计划**: 

- PG合并功能开发、Systore集成测试、EC Pool通用代码合并、性能数据发布、用户指南文档分离等。



**其他资源**:

- Slack频道、GitHub Tracker、周会等。

**会议结束时间**: [具体时间]  

**备注**: 请与会成员在Etherpad补充遗漏内容，后续通过邮件同步更新。