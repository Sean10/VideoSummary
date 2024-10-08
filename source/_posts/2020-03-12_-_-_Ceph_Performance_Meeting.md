---
title: "2020-03-12 :: Ceph Performance Meeting"
date: 2020-04-03
updated: 2020-04-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议时间与参与人员
- **时间：** 早晨6:30
- **参与人员：** Mark, Greg, Igor, Adam, 及其他团队成员

#### 会议议题与讨论内容
1. **项目进展更新**
   - **PR更新：** 本周没有新的或即将关闭的PR。团队成员主要集中在现有问题的处理上。
   - **更新PR：** Igor更新了关于hybrid alligator的PR，但具体内容未详细讨论。

2. **IO 500测试套件后端开发**
   - **进展：** 后端已成功开发并显示出高性能，甚至超过内核客户端。
   - **性能分析：** 发现内核部分可能存在需要修复的问题。
   - **测试结果：** 在IO 500测试中，团队目前排名第9，接近第8。
   - **硬件分类问题：** 讨论了IO 500测试中硬件分类不明确的问题，以及如何在不同系统配置下进行有效竞争。

3. **性能优化讨论**
   - **Adam的测试发现：** 所有alligators在磁盘使用率达到80%后，性能迅速下降。讨论了是否应关注超过80%的磁盘使用情况。
   - **Igor的优化工作：** 介绍了针对4k min alaq size的优化，包括hybrid alligator和deferred writes的改进。展示了性能数据，并讨论了未来的优化方向。

#### 决定事项
- **Hybrid Alligator的合并：** 计划将hybrid alligator合并到主分支，但不作为默认设置。
- **Deferred Writes的调整：** 对于deferred writes的调整，团队决定等待进一步测试和评估。

#### 后续行动计划
- **继续优化：** 团队将继续优化IO 500测试套件的后端，并关注特定测试案例的性能问题。
- **性能测试：** Adam将继续进行性能测试，并在下次会议中分享详细数据。
- **代码审查与合并：** Igor将继续进行代码审查，并计划将改进合并到主分支。

#### 其他事项
- **文档共享问题：** 讨论了Google Doc的访问权限问题，Adam将尝试解决文档共享的访问问题。

#### 会议结束
- **时间：** 会议在预定时间结束后结束。
- **下次会议：** 团队成员将在下次会议中继续讨论和评估性能优化进展。

---

本次会议主要集中在Ceph存储系统的性能优化和IO 500测试套件的开发进展上，团队成员分享了各自的发现和优化策略，并制定了后续的行动计划。