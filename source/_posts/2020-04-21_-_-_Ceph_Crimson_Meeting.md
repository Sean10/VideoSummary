---
title: "2020-04-21 :: Ceph Crimson Meeting"
date: 2020-04-29
updated: 2020-04-30
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期**: 未明确
- **参与者**: 未列出具体人员
- **议程**: 讨论了Ceph存储系统中的一些技术问题，包括节点大小调整、数据结构设计、代码实现和测试等。

#### 主要议题
1. **节点大小调整问题**:
   - 讨论了在Ceph中调整节点大小的可行性和效率问题。
   - 决定简化处理，不考虑双分裂情况，但节点一旦存储在树中，其大小不可更改。
   - 提出了通过写入新的大块来处理节点大小扩展的方法。

2. **数据结构设计**:
   - 讨论了O节点（Onoda notes）的内部结构设计，包括固定大小和可变大小部分的分离。
   - 提出了将O节点分为固定大小和可变大小两部分的设计思路。

3. **代码实现和测试**:
   - 讨论了代码实现的进展，包括已经实现的专利函数和即将进行的提取重设计。
   - 提到了正在进行单元测试的开发，包括FS和LBA树的插入和分裂操作。
   - 强调了文档编写和代码提交的重要性。

4. **其他技术问题**:
   - 讨论了日志恢复、树节点类设计、块布局和哈希碰撞处理等问题。
   - 提出了优先考虑空间效率而非计算效率的设计原则。

#### 决定事项
- 简化节点大小调整的处理逻辑。
- 设计O节点的内部结构，分为固定大小和可变大小两部分。
- 继续推进代码实现和单元测试的开发。
- 编写相关文档并提交代码审查。

#### 后续行动计划
- 完成单元测试的开发，并编写相关文档。
- 提交代码审查，并根据反馈进行调整。
- 继续进行提取重设计和日志恢复的开发。
- 关注并处理网络和会议时间安排的问题。

#### 其他备注
- 会议中提到了网络问题和会议时间安排的调整，需要进一步确认和处理。
- 会议记录和讨论内容将更新到共享文档中，供后续参考。

### 结束语
感谢所有参与者的贡献，期待下周的会议继续推进项目进展。祝大家有一个愉快的一周！