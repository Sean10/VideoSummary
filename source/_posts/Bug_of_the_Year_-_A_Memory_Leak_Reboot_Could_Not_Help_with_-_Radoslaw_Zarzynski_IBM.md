---
title: "  Bug of the Year: A Memory Leak Reboot Could Not Help with - Radoslaw Zarzynski, IBM  "
date: 2023-05-05
updated: 2023-05-05
tags:
- Ceph
- Memory Leak
- Storage Systems
- Bug Fixes
- Open Source
categories:
- "视频总结"
subtitle: Bug_of_the_Year_-_A_Memory_Leak_Reboot_Could"Not_Help_with_-_Radoslaw_Zarzynski_IBM
---



在Radoslaw Zarzynski的IBM会议中，详细讨论了Ceph存储系统中一个长期存在的内存泄漏问题。以下是会议的关键要点：

1. **问题背景**：Radek自2015年起从事Ceph存储系统开发，讨论了一个特殊的内存泄漏问题，该问题对重启等常规处理手段具有免疫力。

2. **问题描述**：内存泄漏存在于OSD（Object Storage Daemon）启动时从磁盘加载的内存结构中，自2017年起存在于代码中，并在Octopus版本中因自动缩放器（auto scalar）的默认设置更改而加剧。

3. **技术细节**：问题根源在于C++标准库（STDC++）中的`std::list`容器的`size`方法在某些版本中不是常数时间复杂度，导致PG锁（PG lock）中的dupes结构在处理重复操作时出现问题。

4. **问题影响与症状**：内存泄漏导致OSD在处理恢复和peering过程时消耗更多内存和CPU资源，症状包括增加的延迟、内存使用量上升、TC malloc警告、以及OSD间歇性闪烁。

5. **诊断方法**：传统方法包括使用`objectstore_tool`工具导出PG锁，但具有侵入性。非侵入性方法包括使用admin socket命令观察mempools统计信息。

6. **解决方案与修复**：修复工作分为多个阶段，解决离线工具（CLT）对dupes结构的无知问题，并在OSD启动时逐步清理膨胀的dupes条目。

7. **后续行动计划**：继续监控和优化修复措施，开发更多的诊断工具，加强代码审查和测试流程。

会议强调了内存泄漏问题的复杂性和难以诊断的特点，但通过团队的努力，已经找到了有效的修复方法。未来将加强代码审查和测试，以防止类似问题再次发生。