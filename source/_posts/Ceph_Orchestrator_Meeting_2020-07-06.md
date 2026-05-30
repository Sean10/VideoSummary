---
categories:
- 视频总结
date: 2020-07-06
subtitle: Ceph_Orchestrator_Meeting_2020-07-06
tags:
- Ceph
- 分布式存储
- Rook
- Saif EDM
- 管理与运维
title: "Ceph Orchestrator Meeting 2020-07-06"
updated: 2020-07-07
---



### 会议纪要

**会议时间：** 2020年7月6日  
**参会人员：** [列出参会人员]  
**缺席人员：** Sebastian, Miguel

#### 会议议程
1. **NFS配置对象**
2. **Rook Manager测试问题**
3. **Saif EDM的目标和时间线**

#### 会议内容
1. **NFS配置对象**
   - Jeff Leighton提出了该议题，但无人回应。

2. **Rook Manager测试问题**
   - 当前Rook的Manager测试失败，该测试针对master分支运行，以便在发布前发现早期破坏性更改。
   - 发现OSD创建问题，Miguel在上周五提交了PR，希望修复此问题。
   - 由于Sebastian本周不在，建议暂时禁用该测试，待Sebastian回来后再处理。

3. **Saif EDM的目标和时间线**
   - Saif EDM被正式宣布为不使用Rook安装Ceph的推荐方法。
   - 文档中已明确指出，安装时推荐使用Saif EDM。

#### 决定事项
- 暂时禁用Rook Manager测试，待Sebastian回来后再处理。
- 确认Saif EDM作为非Rook安装Ceph的主要方法。

#### 后续行动计划
- 禁用Rook Manager测试。
- 继续关注Saif EDM的文档和实施情况。

#### 会议结束
- 会议在无其他议题提出后结束。
- 下次会议将在Sebastian和Miguel回归后进行。

**会议总结：** 本次会议主要讨论了Rook Manager测试的问题和Saif EDM的实施情况。决定暂时禁用Rook Manager测试，并确认Saif EDM作为安装Ceph的主要方法。下次会议将在关键人员回归后继续进行。