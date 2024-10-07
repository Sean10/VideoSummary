---
title: "Ceph Performance Meeting 2023-03-02"
date: 2023-03-06
updated: 2023-03-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是在两周后再次召开的，原因是会议主持人之前在纽约度假。会议主要回顾了最近两周的PR（Pull Request）列表，讨论了几个关键的议题，并决定了一些后续行动计划。

#### 主要讨论议题
1. **PR审查进度**
   - 主持人接近完成了PR列表的审查，但尚未完全完成。
   - 提到了一个来自Casey的新PR，关于在rgw中切换回多态执行器的问题，Mark Hogan进行了测试，未发现明显的性能提升，但仍计划在Reef之后进行切换。

2. **已关闭的PR**
   - 讨论了几个已关闭的PR，包括Igor的一个csq更改，使用更大的读取块在cue列表条目中，预计会有小的性能改进。
   - 另一个重要的PR是关于更新Facebook的RocksDB，将在稍后讨论。

3. **新的和更新的PR**
   - 讨论了几个新的和更新的PR，包括替换RBD配置的PR，加密添加qat批处理的PR等。

4. **RocksDB更新**
   - 讨论了RocksDB的更新，该更新在现有的Valgrind测试中失败，但通过添加大量新的Valgrind抑制规则使其通过。计划在接下来的几个月中进行大量测试，如果出现问题，可能会回滚。

5. **新的基准测试工具**
   - 讨论了一个新的基准测试工具，该工具使用了许多底层库，如librbd等，并自动填充Google表格与基准测试结果。但需要更多的测试和与现有工具如fio的比较。

6. **读取平衡器**
   - 讨论了读取平衡器的性能改进，计划在一个小集群上进行测试，以证明性能的实际改进。

7. **QAT加密问题**
   - 讨论了QAT加密的性能问题，特别是关于是否需要在插件中进行等待的设计问题。

#### 决定事项
- 计划在Reef之后切换回多态执行器。
- RocksDB的更新将在接下来的几个月中进行大量测试，如果出现问题，可能会回滚。
- 将进行一个小集群的测试，以证明读取平衡器的性能改进。
- 将进行QAT加密的性能测试，以评估是否需要进行等待。

#### 后续行动计划
- 继续完成PR列表的审查。
- 进行RocksDB的更新测试，并监控内存泄漏和其他问题。
- 进行新的基准测试工具的测试，并与现有工具进行比较。
- 在小集群上进行读取平衡器的性能测试。
- 进行QAT加密的性能测试，以评估是否需要进行等待。

#### 其他讨论
- 讨论了关于Spinner设置的首次写入问题，建议尝试禁用首次写入以减少开销。
- 讨论了Blue Store的日志问题，建议尝试使用新的日志实现来减少对RocksDB的依赖。

#### 会议结束
会议在讨论了所有议题后结束，感谢所有参与者的贡献，并期待下一次会议。