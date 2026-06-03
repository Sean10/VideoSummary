---
title: "Ceph Crimson / SeaStor OSD 2020-10-06"
date: 2020-10-06
updated: 2020-10-08
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
categories:
  - "视频总结"
outline: deep
---
## 改进后的中文总结内容

### 会议纪要

#### 与会人员
- 主持人：未明确提及
- 参与者：Sam, Johan, Stem 以及其他未明确提及的成员

#### 会议时间
- 日期：未明确提及
- 时间：未明确提及

#### 会议议题
1. **个人工作汇报**
   - Sam 在PTO期间完成了PR清理，并开始审查Stem Care以添加捕获集合，同时关注Amnon的PI和Runes，计划审查hands interrupt。
   - Stem 阅读了Greyhounds相关内容，提交了PR，并正在为e-store编写磁盘后端以进行基本性能测试。
   - 其他成员计划回顾VR，并开始改进测试，特别是scrubbing测试。
   - 一位成员提交了interruptible future PR，并正在修改代码和添加单元测试。

2. **技术讨论**
   - Stem 讨论了使用iou ring支持的问题，指出后端并未使用该功能。
   - Sam 对interruptible future的设计进行了深入讨论，提出了一些改进建议，包括确保中断条件在调用safe then时已设置，并考虑命名问题以提高代码可读性。

#### 决定事项
- Stem 将继续关注iou ring的支持情况，并考虑使用最基本的内置c-star方法进行磁盘写入。
- Sam 建议在interruptible future的设计中，确保中断条件在调用safe then时已设置，并考虑命名问题以提高代码可读性。

#### 后续行动计划
- Stem 继续关注iou ring的支持进展，并考虑使用最基本的内置方法进行磁盘写入。
- Sam 与Johan讨论interruptible future的设计，确保中断条件在调用safe then时已设置，并考虑命名问题。
- 所有成员继续各自的工作，并关注相关技术进展。

#### 其他备注
- 会议中提到了一些具体的技术细节和代码实现问题，需要进一步的技术讨论和代码审查。

#### 会议结束
- 会议在讨论完所有议题后结束，感谢大家的参与。