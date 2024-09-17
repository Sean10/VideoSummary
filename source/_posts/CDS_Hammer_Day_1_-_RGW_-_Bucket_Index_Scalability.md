---
title: "CDS Hammer (Day 1) - RGW: Bucket Index Scalability"
date: 2014-10-29
updated: 2014-10-30
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： Ceph 分布式存储项目讨论

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 未提及具体姓名，但提到了 Guang、Patrick 等人

**会议内容**：

**一、bucket 可扩展性**

*   **背景**： bucket 可扩展性是 Ceph 分布式存储项目的一个重要议题，涉及 bucket 索引的扩展性。
*   **进展**： 目前该功能进展顺利，已经完成了大部分工作，但与多区域、多区的功能集成尚未完成。主要问题在于后台索引中存在一些日志，需要确保多区域环境下一切正常工作。
*   **解决方案**： 可以通过使用不同类型的标记来实现多区域下的 bucket 索引，或者在 bucket 列表中使用标记来识别不同 bucket 的位置。
*   **下一步**： 等待 Guang 回来后，进一步讨论该功能的细节。

**二、list 命令**

*   **讨论**： 讨论了添加两个不同的 list 命令：传统的有序 list 命令和新的无序 list 命令。
*   **进展**： 无序 list 命令尚未实现，但应该比较容易添加。
*   **问题**： 位置标识符需要从键名对象改为元组，以支持无序 list 命令。

**三、multi-object 上传的原子性**

*   **讨论**： 讨论了 multi-object 上传的原子性问题。
*   **结论**： multi-object 上传需要所有条目都在同一个 bucket 中，因此不会影响原子性。

**四、blind buckets**

*   **讨论**： 讨论了 blind buckets 的实现情况。
*   **结论**： 目前没有实现 blind buckets，因为它会牺牲多区域、多区和对象版本化等功能。

**五、object engine 分支**

*   **讨论**： 讨论了 object engine 分支与 bucket 可扩展性功能的冲突。
*   **结论**： 由于两个功能没有涉及到相同的代码区域，因此不太可能存在冲突。

**六、radi Gateway agent**

*   **讨论**： 讨论了 Guang 是否会继续工作在 radi Gateway agent 上。
*   **结论**： 希望有新加入的成员能够帮助 Guang 工作。

**七、bucket 分片**

*   **讨论**： 讨论了 bucket 分片的实现方式。
*   **结论**： 可以通过以下步骤实现 bucket 分片：
    1.  在 bucket 创建之前进行分片。
    2.  对于已经存在的 bucket，可以将其转换为新的分片 bucket。

**八、行动计划**

*   等待 Guang 回来后，进一步讨论 bucket 可扩展性功能的细节。
*   实现无序 list 命令。
*   完成radi Gateway agent 的开发工作。
*   实现bucket 分片功能。

**九、会议总结**

本次会议讨论了 Ceph 分布式存储项目的多个议题，包括 bucket 可扩展性、list 命令、multi-object 上传、blind buckets、object engine 分支、radi Gateway agent 和 bucket 分片等。会议明确了下一步的行动计划，并希望新加入的成员能够为项目贡献力量。