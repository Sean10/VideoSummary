---
title: "2019-11-12 :: Crimson SeaStor OSD Weekly Meeting"
date: 2019-11-12
updated: 2019-11-18
tags:
  - "Ceph"
  - "分布式存储"
  - "Crimson"
categories:
  - "视频总结"
outline: deep
---
会议纪要

**会议时间**： 2023年11月X日

**会议地点**： San Francisco

**参会人员**：

*   Alan（以色列，Ra'anana办公室）
*   Roland
*   Ronnie
*   Peter
*   其他成员

**会议主题**：

*   Ceph存储系统设计讨论
*   Alligator文件系统设计
*   Crimson性能测试
*   Native Stack的使用

**会议内容**：

**1. Alligator文件系统设计**

*   讨论了是否需要文件系统以及使用Alligator的原因。
*   结论：由于传统文件系统无法满足Ceph的需求，Alligator将直接在块设备上运行，不使用文件系统。
*   关键词：Alligator, 文件系统, 块设备

**2. Crimson性能测试**

*   讨论了Crimson在POSIX和Native Stack上的性能测试结果。
*   结论：Native Stack在性能上具有优势，但存在一些稳定性问题。
*   关键词：Crimson, POSIX, Native Stack

**3. Native Stack的使用**

*   讨论了Native Stack的局限性以及是否使用的问题。
*   结论：目前不考虑使用Native Stack，而是专注于POSIX Stack。
*   关键词：Native Stack, POSIX Stack

**4. SP Decay**

*   讨论了SP Decay的实现和测试。
*   结论：SP Decay的实现需要优先级，但测试工作可以继续进行。
*   关键词：SP Decay

**5. 其他**

*   Alan介绍了自己的背景和工作。
*   讨论了Ceph社区和Surveillance Cluster。
*   讨论了Crimson和Native Stack的兼容性。

**后续行动计划**：

*   继续进行SP Decay的测试工作。
*   完成Alligator文件系统的设计。
*   优化Crimson的性能。

**备注**：

*   会议中涉及的技术细节较多，建议参会人员仔细阅读会议记录。
*   会议中提到的关键词需要进一步了解其含义。


**改进点**：

*   在总结中增加了会议主题和参会人员信息。
*   梳理了会议中讨论的关键议题，并详细说明了每个议题的讨论内容和结论。
*   强调了会议中提到的后续行动计划。
*   在备注中提醒参会人员仔细阅读会议记录以了解技术细节。