---
title: "Ceph Crimson/SeaStor OSD 2020-07-15"
date: 2020-07-15
updated: 2020-07-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- 日期：[具体日期]
- 参会人员：[参会人员名单]
- 主持人：[主持人姓名]

#### 主要议题
1. **Ceph存储系统的开发进展**
   - 讨论了关于Ceph存储系统中的中断处理机制的改进，特别是关于中断可继续性的问题。
   - 讨论了如何改进PR（Pull Request）的审查流程，以减少不必要的评论和提高效率。

2. **技术细节讨论**
   - 讨论了如何通过使用管道（pipeline）方式来优化文件处理和其他事件处理的性能。
   - 讨论了如何通过检查中断条件来中断正在进行的IO处理。

3. **代码和功能改进**
   - 讨论了如何改进插入逻辑和模板的使用，以便在内部节点中共享相同的逻辑。
   - 讨论了如何准备和分享元素在兄弟节点或同事之间的知识。

4. **项目管理和时间安排**
   - 讨论了项目的时间安排，特别是考虑到即将在英格兰举行的虚拟会议，部分成员将减少工作时间。

#### 决定事项
- 决定继续探索和改进中断处理机制，特别是通过使用管道方式来优化性能。
- 决定简化PR审查流程，减少不必要的评论，提高审查效率。
- 决定在代码中增加更多的检查点，以确保操作在恢复后仍然有效。

#### 后续行动计划
- 继续开发和测试中断处理机制的新方法。
- 优化PR审查流程，确保审查的效率和质量。
- 在代码中实施更多的检查点，以提高系统的稳定性和可靠性。
- 确保项目的时间安排考虑到即将举行的虚拟会议的影响。

#### 其他事项
- 讨论了如何更好地分享和整合系统内存与sISTAR。
- 讨论了如何进行map tree的调查和研究。

#### 会议结束
- 会议在讨论了所有议题和决定后结束，感谢所有参与者的贡献和讨论。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。