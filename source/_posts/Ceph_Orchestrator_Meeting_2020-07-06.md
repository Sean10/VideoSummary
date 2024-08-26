---
title: "Ceph Orchestrator Meeting 2020-07-06"
date: 2020-07-06
updated: 2020-07-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议时间：** [具体日期]  
**参会人员：** [列出参会人员]  
**缺席人员：** Sebastian, Miguel

#### 会议议程
1. **NFS Config Objects**
2. **Rook Manager Test 问题**
3. **Saif EDM 的目标和时间线**

#### 会议内容
1. **NFS Config Objects**
   - Jeff Leighton 添加了此议题，但无人回应。

2. **Rook Manager Test 问题**
   - 当前 Rook 的 Manager Test 失败，该测试针对 master 分支运行，以便在发布前发现早期破坏性更改。
   - 发现 OSD 创建问题，Miguel 在上周五提交了 PR，希望修复此问题。
   - 由于 Sebastian 本周不在，建议暂时禁用该测试，待 Sebastian 回来后再处理。

3. **Saif EDM 的目标和时间线**
   - Saif EDM 被正式宣布为不使用 Rook 安装 Ceph 的首选方法。
   - 文档中已明确指出，安装时推荐使用 Saif EDM。

#### 决定事项
- 暂时禁用 Rook Manager Test，待 Sebastian 回来后再处理。
- 确认 Saif EDM 作为非 Rook 安装 Ceph 的主要方法。

#### 后续行动计划
- 禁用 Rook Manager Test。
- 继续关注 Saif EDM 的文档和实施情况。

#### 会议结束
- 会议在无其他议题提出后结束。
- 下次会议将在 Sebastian 和 Miguel 回归后进行。

**会议总结：** 本次会议主要讨论了 Rook Manager Test 的问题和 Saif EDM 的实施情况，决定暂时禁用 Rook Manager Test，并确认 Saif EDM 作为安装 Ceph 的主要方法。下次会议将在关键人员回归后继续进行。