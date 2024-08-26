---
title: "2019-11-21 :: Ceph Performance Meeting"
date: 2019-11-25
updated: 2019-11-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **新PR概览**: 本周有三个新的PR。
  - **David Zetland**的PR涉及改进upnot balancer的逻辑，以解决优化不佳导致的速度过慢问题。
  - **MDS**的PR关于设置CPU亲和性。
  - **Adam**的PR标题为“Got the World on a String”，涉及字符串优化，使用string_view或其他方法。

- **已关闭或更新的PR**:
  - Neha的快速修复，禁用arm range合并。
  - 调整默认的max MF条目每请求的合并。
  - 一个关于从用户空间拉取事件的PR被stale bot关闭，因需要内核中的实验性内容。
  - 一个旧的PR避免OSD消耗map被关闭，无具体解释。
  - PG autoscaler默认PG数216已批准。
  - Eric的OSD中GW CLS代码的过滤改进已更新。

- **其他讨论**:
  - 关于4K min_alloc_size的讨论，涉及SSD和NVMe驱动器的性能和空间放大问题。
  - 讨论了如何处理混合工作负载，特别是对于RGW工作负载的影响。
  - 提到了新的Intel节点的测试，包括读写性能和I/O操作。

#### 主要议题
- **性能优化**: 重点讨论了如何改进upnot balancer的逻辑，以及字符串优化的方法。
- **硬件兼容性**: 讨论了4K min_alloc_size在不同类型存储设备上的表现和优化策略。
- **系统配置**: 涉及MDS的CPU亲和性设置和OSD的过滤改进。

#### 决定事项
- 继续对4K min_alloc_size进行更多测试和研究，特别是对于RGW工作负载的影响。
- 对于新的Intel节点，将继续优化配置以提高性能。

#### 后续行动计划
- 对4K min_alloc_size进行更多测试，包括RGW工作负载的性能评估。
- 继续优化新的Intel节点的配置，以达到更好的读写性能和I/O操作。
- 下周会议将继续讨论相关PR和配置优化。

#### 其他备注
- 会议中提到了一些技术细节和测试结果，需要进一步分析和验证。
- 对于混合工作负载的处理，需要找到更通用的解决方案。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。