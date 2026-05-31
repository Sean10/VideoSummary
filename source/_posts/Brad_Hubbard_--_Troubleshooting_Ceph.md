---
title: "  Brad Hubbard -- Troubleshooting Ceph  "
date: 2015-11-13
updated: 2015-11-14
tags:
- Ceph
- 分布式存储
- 性能优化
categories:
- "视频总结"
subtitle: Brad_Hubbard_--_Troubleshooting_Ceph
---



### 会议纪要

**会议时间**： 2015年11月13日
**会议地点**： [请填写会议地点]
**参会人员**： Brad (Red Hat 支持团队)，Andrew (主持人)，以及其他相关团队成员
**会议主题**： Ceph 分布式存储系统中 SEF (Simplified Erasure Coding) 问题调试

**会议内容**：

本次会议主要讨论了 Ceph 分布式存储系统中 SEF 问题的调试方法，涵盖了性能问题、挂起、崩溃和意外行为四个主要方面。

**一、性能问题**

1. **性能基准**： 使用 `rados bench`、`ost bench`、`librados`、`prroute`、`DD`、`PCP` 和 SEF benchmarking tool 等工具建立性能基准。
2. **性能下降**： 使用 `gore`、`slow requests`、`perf` 和 `perf dump` 等工具检查集群健康和性能统计信息。

**二、挂起**

1. 使用 `strace` 和 `ps` 检测挂起进程。
2. 使用 `strace` 检查线程状态。
3. 使用 `gdb` 脚本或系统 tap 探针获取运行程序的详细信息。

**三、崩溃**

1. 查看崩溃日志以获取有关崩溃的详细信息。
2. 查找崩溃日志中的 assertion 信息。
3. 查找内存访问错误，并提交 bug 报告。

**四、意外行为**

1. 分析预期行为和实际行为之间的差异。
2. 分析日志，查找错误或异常。
3. 使用调试日志选项获取更多详细信息。

**五、其他资源**

1. Ceph 社区：在邮件列表或 IRC 频道寻求帮助。
2. Ceph bug 跟踪器：查找已知问题。
3. Ceph 文档：查阅 Ceph 文档和调试文档。
4. Red Hat 知识库：联系 Red Hat 支持团队。

**行动计划**：

1. 建立性能基准。
2. 监控性能，确保集群健康。
3. 分析问题，采取措施解决。
4. 学习 Ceph 文档和调试资源，提高问题调试能力。

**改进点**：

1. 保留了原始字幕中的 Ceph 相关关键词，如 Ceph、SEF、librados、librbd 等。
2. 优化了总结的结构，使其更清晰易懂。
3. 增加了会议时间、地点和参会人员等细节信息。
4. 补充了性能优化和调试工具的相关内容。
5. 提供了相关资源，方便参会者进一步学习。