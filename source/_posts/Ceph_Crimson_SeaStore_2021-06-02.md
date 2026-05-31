---
title: " Ceph Crimson/SeaStore 2021-06-02 "
date: 2021-06-02
updated: 2021-06-03
tags:
- Ceph
- 分布式存储
categories:
- "视频总结"
subtitle: Ceph_Crimson_SeaStore_2021-06-02
---

在Ceph Crimson/SeaStore的2021年6月2日会议中，研发人员和专家讨论了一系列与Ceph分布式存储系统相关的问题和进展。

### 会议要点：

1. **Crimson OSD启动失败问题**：会议重点讨论了Crimson OSD在Rook中运行失败的复现和解决方法。上周尝试使用经典设备启动Crimson失败，本周将重点解决启动时的错误报告问题。

2. **异常处理与错误报告**：提出使用与Ceph数据库相同的清理函数钩子方法作为修复方案，并解决了ASAN报告的越界访问问题，这是ASAN自身的bug。

3. **ZFS学习与研究**：研究ZFS在垃圾收集和分配器问题上的处理方式。

4. **事务管理器读取交换断言问题**：修复了因分段状态跟踪器混乱导致的事务管理器读取交换断言问题。

5. **OSD停止异常**：发现Crimson OSD在启动后立即停止，正在调试LBA析构函数中的断言问题。

6. **新实习生介绍**：介绍了Red Hat的新实习生Joseph，他将在Crimson项目中工作。

7. **Scrubbing PR讨论**：讨论了关于Scrubbing的PR，建议重新创建PR以包含最新的基础提交。

8. **Clang编译问题修复**：Sam修复了Clang编译问题，计划提交到Clang上游。

9. **可中断分配器开发**：继续开发可中断分配器，以便在Ceph存储中使用。

10. **扩展放置管理器调试**：正在调试扩展放置管理器，希望本周能提交PR。

11. **键值大小限制实现**：实现了键值大小的限制，相关PR已合并。

### 决定事项：

- 继续调试Crimson OSD启动和停止的异常问题。
- 重新创建Scrubbing PR以包含最新的基础提交。
- 提交Clang编译问题的reproducer到上游。

### 后续行动计划：

- 继续调试和修复Crimson OSD相关问题。
- 完成Scrubbing PR的重新创建和测试。
- 提交Clang编译问题的reproducer。
- 继续开发和测试可中断分配器。
- 完成扩展放置管理器的调试并提交PR。

会议在无其他议题的情况下结束，感谢大家的参与。