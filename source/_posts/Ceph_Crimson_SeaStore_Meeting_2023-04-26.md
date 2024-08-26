---
title: "Ceph Crimson/SeaStore Meeting 2023-04-26"
date: 2023-05-03
updated: 2023-05-03
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** [具体日期]

**参会人员：** Rocky, Isaiah, June, Phil

**会议议题：**
1. 项目进展汇报
2. 技术问题讨论
3. 后续行动计划

**会议内容：**

1. **自我介绍：**
   - June 加入了 Hari 团队，并参与了 GitHub 命令的相关工作。

2. **项目进展：**
   - Rocky 在 Cephalocon 后主要跟进代码审查工作。
   - Engine 汇报了 mod core system 和 connection reference 的变更，感谢 Sam 的贡献。已审查并合并了 circular Journal space for random block manager，以及 mod core messenger 的多核 socket 接受和连接功能。单元测试已完成，当前挑战是确保内存分配正确。
   - Engine 还提到了 OSD 操作消息缓冲列表的跨云约束可能未正确执行，但未触发任何故障。
   - Engine 将跳过下一次会议，因为即将放假。

3. **技术讨论：**
   - 讨论了 buffer lists 使用 Atomic reference Counting 的问题，认为虽然可能存在性能问题，但只要不频繁操作引用计数，可能不需要立即修复。建议进行性能分析。
   - 讨论了 c-star allocator 的工作原理，指出在释放其他核心分配的内存时需要发送消息回其他核心，但确实有效。
   - 讨论了 PR 中的 lva point 修改，建议在测试通过后尽快合并，以避免重构困难。
   - 讨论了 debug 构建中的 get connection pipeline 问题，认为 debug 模式下的行为是正确的，应修复。
   - 讨论了 SMP 设置为三的测试结果，建议通过 debug 输出检查核心运行情况。

**后续行动计划：**
- 继续进行性能分析和代码审查。
- 修复 debug 构建中的 get connection pipeline 问题。
- 确保 PR 的测试通过后尽快合并。
- 通过 debug 输出检查 SMP 设置的正确性。

**会议结束：**
- 会议在确认无其他议题后结束，祝大家下周工作顺利。

**备注：**
- 保留了部分计算机科学/ceph 相关领域英文原文的关键词，如 Cephalocon, mod core system, connection reference, Atomic reference Counting 等。