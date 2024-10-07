---
title: "2019-12-17 :: Crimson SeaStor OSD Weekly Meeting"
date: 2020-01-10
updated: 2020-01-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **会议日期**: [具体日期]
- **参会人员**: [列出主要参会人员]
- **会议时长**: [会议持续时间]

#### 讨论的主要议题
1. **Ceph BlueStore性能问题**:
   - **问题描述**: 在特定工作负载下，特别是当工作负载为单个任务且块大小较大时，Crimson OSD的性能不如Classic OSD。
   - **原因分析**: 发现与Ceph的分配器（allocator）有关，特别是在使用C-star分配器时，无法分配特定页码（如81、92），导致错误。
   - **解决方案**: 建议使用默认分配器来构建版本，并考虑增加页码限制或调整分配策略。

2. **提交策略改进**:
   - **建议**: 提交代码时，应详细说明变更策略和具体改动，而不仅仅是单一标题，以便于评审人员理解。
   - **行动**: 将在提交中添加更多注释和详细说明。

3. **性能回归问题**:
   - **讨论**: 当块大小大于4K时，性能下降被认为是预期的，需要通过改进策略来解决。
   - **后续行动**: 需要进一步研究并决定是否采用DPDK或POSIX堆栈作为首选驱动程序。

4. **其他议题**:
   - **F2FS文件系统**: 讨论了F2FS中的段和区域的概念，以及是否需要在Ceph中引入类似的层次结构。
   - **会议安排**: 由于即将到来的假期，决定取消接下来两周的会议。

#### 决定的事项
- **性能问题**: 确认了性能下降的原因，并决定使用默认分配器来解决当前问题。
- **提交策略**: 同意改进提交信息，增加详细说明以帮助评审。
- **驱动程序选择**: 暂定使用POSIX堆栈，但需要进一步测试和调整以优化性能。

#### 后续行动计划
- **性能优化**: 继续研究和测试不同的分配器和堆栈选项，以找到最佳性能配置。
- **代码提交**: 改进提交信息的详细程度，确保包含足够的上下文和策略说明。
- **假期安排**: 确认了假期期间的会议取消，并计划在假期后恢复会议。

#### 其他备注
- **假期通知**: 部分团队成员将在接下来的两周内休假，会议将暂停。
- **技术讨论**: 对于F2FS的段和区域概念进行了初步讨论，但未做出最终决定。

### 结束语
感谢所有参会人员的积极参与和贡献，期待在假期后继续推进项目进展。祝大家假期愉快！