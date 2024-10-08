---
title: "Ceph Performance Meeting 2020-08-13"
date: 2020-08-13
updated: 2020-08-14
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **日期**: [具体日期]
- **参会人员**: [参会人员名单]
- **会议主持**: [主持人姓名]

#### 主要议题
1. **PR讨论**:
   - **Bufferless Depends优化**: Radek和主持人共同完成的工作，旨在提高bufferless depends的速度。提出了两个互补的更改，第一个较小更改已在本周的PR中提交。该更改动态调整append buffer的长度，类似于C++中vector的增长方式，但有边界限制。尽管在某些情况下tc_malik会变慢，但总体上仍优于master版本，尤其是在pen_hole和ring buffer的情况下。
   - **Ephemeral Pinning改进**: Yan提交的PR，加强了最近引入的ephemeral pinning功能。目的是通过分发franks来减少子树的数量。

2. **CRUSH算法扩展**:
   - 介绍了一篇在FAST会议上发表的论文，该论文提出了一种CRUSH算法的扩展，旨在改善集群扩展时的数据迁移问题。新算法引入了一个集中式的权威来管理数据迁移，通过添加一个虚拟层来减少数据迁移量，特别是在集群扩展时。
   - 论文展示了在Ceph FS和RBD上的测试结果，显示新算法在IOPS和延迟方面有显著改进。会议讨论了该算法的潜在影响和是否需要在SSD上进行进一步测试。

#### 决定事项
- 主持人将联系论文作者，探讨他们是否愿意在未来的会议中进行详细介绍。
- 参会人员将在接下来的两周内详细阅读论文，并在下次会议中进一步讨论。

#### 后续行动计划
- 主持人将联系论文作者，安排一个会议时间。
- 所有参会人员需阅读论文，准备下次会议的讨论。
- 考虑在不同硬件上测试新算法，特别是SSD，以评估其在现代存储设备上的表现。

#### 其他讨论
- 讨论了D3M缓存和Majin Peng的PR更新，以及Radic对减少buffer list重建的工作。

#### 结论
- 会议结束时，所有参会人员同意在下次会议前详细阅读论文，并期待进一步的讨论和可能的实施测试。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。