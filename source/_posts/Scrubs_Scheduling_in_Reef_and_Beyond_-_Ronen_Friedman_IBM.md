---
categories:
- 视频总结
date: 2023-05-05
subtitle: Scrubs_Scheduling_in_Reef_and_Beyond_-_Ronen_Friedman_IBM
tags:
- Ceph
- Scrub 代码
- Ceph 存储系统
- 性能优化
- 分布式存储
title: "Scrubs Scheduling in Reef and Beyond - Ronen Friedman, IBM"
updated: 2023-05-05
---



会议纪要

#### 会议基本信息

- **主讲人**: London Friedman
- **时间**: 会议持续约40分钟
- **主题**: Ceph 存储系统中的 scrub 代码维护和改进

#### 会议内容总结

1. **Scrub 代码维护**:
   - London Friedman 过去三年持续维护 Ceph 中的 scrub 代码，并得到 Sam 及其他贡献者的协助。
   - 在这段时间内，对 scrubbing 过程进行了多项改进。

2. **改进成果**:
   - 改进了 scrub 状态的更新机制，确保每几秒钟发送一次更新，便于通过 PG dump 或 query 命令获取最新的 scrub 信息。
   - 优化了 scrub 的 chunk size，以提升 deep scrub 和 shallow scrub 的性能。
   - 引入了 M clock 调度器，减少对客户端 IO 的影响，增强集群管理的灵活性。

3. **重要变更**:
   - **Chunk Size**: 调整了 scrub 的 chunk size，优化不同 scrub 类型的性能。
   - **M clock Scheduler**: 新的调度器在执行 scrub 时对客户端 IO 的影响更小，增加了集群管理的灵活性。

4. **未来计划**:
   - 继续增强对系统中超时和慢响应部分的自检、警告和修复功能。
   - 设计新的 scrub 调度器，解决现有系统中的代码维护复杂性和调度效率问题。

5. **新调度器设计**:
   - 引入新的 scrub 目标（Target）概念，每个 PG 维护 shallow 和 deep scrub 的独立目标。
   - 使用 urgency 参数来决定 scrub 的优先级，取代旧的基于 flags 的系统。
   - 引入“not before”机制，避免对暂时无法 scrub 的 PG 进行重复检查。

6. **性能和维护**:
   - 讨论了 scrub 代码的性能优化和维护问题，强调了代码的清晰性和可维护性的重要性。

#### 后续行动计划

- 继续开发和测试新的 scrub 调度器。
- 监控和调整 scrub 相关的配置参数，尤其是 chunk size 和调度器相关参数。
- 收集用户反馈，进一步优化 scrub 过程的性能和可靠性。

#### 结论

本次会议详细讨论了 Ceph 存储系统中 scrub 代码的维护和改进工作，展示了过去几年的成果，并提出了未来的改进方向和计划。通过引入新的调度器和优化参数设置，目标是提高 scrub 过程的效率和系统的整体性能。