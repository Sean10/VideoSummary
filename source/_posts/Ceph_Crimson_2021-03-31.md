---
title: "Ceph Crimson 2021-03-31"
date: 2021-04-01
updated: 2021-04-01
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **时间**: 最近一周
- **参与者**: 团队成员
- **主要议题**: 技术问题讨论、代码测试、文档更新、项目进展

#### 讨论的主要议题
1. **MBD测试问题**:
   - 使用Sam的新PR进行MBD测试，但存在间歇性的segmentation fault问题。
   - 尝试复现问题，但条件不明确，仍在追踪中。
   - 阅读Sam的segmentation clear代码和journal代码，发现并修复了一个小问题。

2. **FIO测试问题**:
   - 设置较大的offset（例如50GB）时，FIO无法运行。
   - 不确定是FIO问题还是其他代码问题，需要进一步调试和确认。

3. **文档更新**:
   - 继续更新上周提到的恢复文档，解决了几个问题，预计下周完成。
   - 讨论了使用unique ptr或foreign ptr进行连接重构的问题，决定继续使用unique ptr，但保留未来切换到foreign ptr的可能性。

4. **状态机更新**:
   - 更新了经典SD的状态机，以匹配Queensland中的更改，已准备好提交。
   - 计划阅读Erased在Queensland中的事务处理，以便后续使用。

5. **逻辑扩展**:
   - 开发了一种方案，将所有相关分配信息嵌入到LBA层，避免使用extent map。
   - 正在实施中，虽然更复杂，但可以消除第二个映射。

6. **Ceph存储问题**:
   - 实现了C store中的get和set地址方法。
   - 正在尝试实现read和write meta方法，并调查可能的Marx问题。

7. **树级别环境不变性**:
   - 解决了管理树级别环境不变性的问题，正在进行最后的子节点合并工作。
   - 下一步将推进布局和阶段级别的实现。

8. **C-star原生堆栈改进**:
   - 注意到C-star原生堆栈的一些改进，主要涉及零拷贝传递和一些bug修复。

9. **单元测试问题**:
   - 解决了Jenkins中单元测试不完整的问题，通过添加步骤在检查作业中止时终止运行中的单元测试。

#### 决定的事项
- 继续使用unique ptr进行连接重构，但保留未来切换到foreign ptr的可能性。
- 解决Jenkins中单元测试不完整的问题。

#### 后续行动计划
- 继续追踪和解决MBD测试中的segmentation fault问题。
- 进一步调试和确认FIO测试中的问题。
- 完成恢复文档的更新。
- 实施逻辑扩展方案，消除extent map的使用。
- 推进Ceph存储和树级别环境不变性的实现。
- 阅读Raft论文，准备下周讨论。

#### 其他事项
- 下周将举行CTS会议，欢迎大家添加感兴趣的话题。

### 结束语
会议结束，感谢大家的参与，祝大家工作顺利。