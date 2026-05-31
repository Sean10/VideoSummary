---
title: "  CDS Infernalis (Day 2.2) -- RBD: Kernel RBD client supports copy-on-read  "
date: 2015-03-06
updated: 2015-03-07
tags:
- RBD
- Ceph
- 存储优化
- 分布式存储
categories:
- "视频总结"
subtitle: CDS_Infernalis_Day_2.2_--_RBD_-_Kernel_RBD_client_supports_copy-on-read
---



### 会议纪要

**会议时间**： 2015年3月6日

**参会人员**： Lee, Yin Chen, [其他参会人员]

**会议主题**： RBD（Rados Block Device）相关功能改进讨论

**会议内容**：

1. **RBD差异导出功能**：
   - Lee提出了导出RBD克隆和父块差异的功能。
   - 讨论了使用协作列表（collab list）提高性能的方案，并计划添加回调请求到类中。
   - 目前该功能尚未实现，需要进一步开发。

2. **性能改进**：
   - 提出使用状态机技术优化RBD复制和写入操作。
   - 讨论了在内核中使用与用户空间相同的状态机技术。
   - 计划分两步进行：首先重构现有复制和写入代码，其次优化查找和跟踪操作。

3. **对象映射**：
   - 讨论了使用哈希表（hash table）和查找列表（lookup list）优化对象映射的性能。
   - 认为使用哈希表可能比查找列表性能更好。
   - 计划在实现复制和写入操作后，再进行优化。

4. **异步操作**：
   - 讨论了使用异步操作（AIO）提高性能。
   - 认为AIO操作在内核中比用户空间更灵活。
   - 计划进一步研究AIO操作在RBD中的应用。

5. **用户空间工具**：
   - 讨论了将通用选项传递给rdmap的方案。
   - 认为无需修改用户空间工具，只需在RBD模块中添加复制和还原功能即可。

**后续行动计划**：

1. Lee和Yin Chen负责实现RBD差异导出功能。
2. 进一步研究使用状态机技术优化RBD复制和写入操作。
3. 优化对象映射性能。
4. 研究AIO操作在RBD中的应用。
5. 将通用选项传递给rdmap。

**备注**：

- 讨论中涉及到的计算机科学/ceph相关领域英文关键词：RBD, clone, parent, diff, collab list, callback, state machine, object map, AIO, kernel, user space, hash table, lookup list。