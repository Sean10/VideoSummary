---
title: "2019-04-16:: Crimson SeaStor OSD Weekly Meeting"
date: 2019-04-17
updated: 2019-04-17
tags:
  - "Ceph"
  - "Crimson"
  - "OSD"
  - "性能优化"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年4月16日
**参会人员**： [未提供具体名单，请补充]
**会议主题**： Ceph Crimson项目进展及讨论

**会议内容**：

**1. CFX Austin厨房支持费用问题**
- 项目方要求支付费用以支持Crimson项目的CFX Austin厨房。
- 讨论了支付方式和费用问题。

**2. Crimson项目进展**
- **Crimson项目测试**：
  - 已经完成了Crimson项目的测试，测试结果显示性能有所提升。
  - 目前正在集成，预计下周完成。
  - 已完成Crimson编译，并进行了初步测试。
- **性能优化**：
  - 讨论了Crimson项目的性能优化，包括：
    - 执行阶段优化：通过减少参数传递和任务调度，提高性能。
    - 异步编程优化：利用Future和Continuation提高性能。
- **性能监控**：
  - 讨论了性能监控问题，包括：
    - 引入新的性能计数器，用于测量批处理消息的平均大小。
    - 开发人员将实现新的性能计数器。

**3. 其他讨论**
- **Crimson项目与经典OSD的兼容性**：
  - 讨论了Crimson项目与经典OSD的兼容性问题。
  - 认为Crimson项目与经典OSD的兼容性是重要的。
- **Crimson项目与BlueStore的集成**：
  - 讨论了Crimson项目与BlueStore的集成问题。
  - 认为短期内将采用BlueStore进行集成。
- **Crimson项目与RBD的集成**：
  - 讨论了Crimson项目与RBD的集成问题。
  - 认为Crimson项目与RBD的集成是长期目标。

**4. 行动计划**
- **Crimson项目测试**：
  - 完成Crimson项目的集成，并进行测试。
- **性能优化**：
  - 继续进行性能优化，提高Crimson项目的性能。
- **性能监控**：
  - 开发新的性能计数器，用于监控Crimson项目的性能。

**5. 其他**
- 新同事Ron将加入Crimson项目团队。
- 讨论了Crimson项目与经典OSD的兼容性问题。

**备注**：
- 部分内容涉及Ceph相关技术，如Crimson、BlueStore、RBD、Future、Continuation等。
- 会议中使用了部分英文关键词，如Crimson、BlueStore、RBD、Future、Continuation等。