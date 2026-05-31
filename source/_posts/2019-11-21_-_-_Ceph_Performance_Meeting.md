---
categories:
- 视频总结
date: 2019-11-25
subtitle: 2019-11-21_-_-_Ceph_Performance_Meeting
tags:
- 性能优化
- CRUSH算法
- 分布式存储
title: 2019-11-21 -- Ceph Performance Meeting
updated: 2019-11-26
---




### 会议纪要

#### 关键细节
- **新提交的PR**:
  - David Zetland的PR针对upnot balancer逻辑改进，以提升速度和优化性能。
  - MDS PR涉及CPU亲和性设置。
  - Adam的PR针对字符串优化，使用string_view或其他方法。
  
- **已关闭或更新的PR**:
  - Neha的快速修复，禁用arm range合并。
  - 调整默认的max MF条目每请求的合并。
  - 用户空间拉取事件的PR因内核实验性内容被关闭。
  - 避免OSD消耗map的PR被关闭，无具体解释。
  - PG autoscaler默认PG数216已批准。
  - Eric的OSD中GW CLS代码的过滤改进已更新。

- **其他讨论**:
  - 4K min_alloc_size的讨论，涉及SSD和NVMe驱动器的性能和空间放大问题。
  - 混合工作负载处理，特别是对RGW工作负载的影响。
  - 新Intel节点的测试，包括读写性能和I/O操作。

#### 主要议题
- **性能优化**: 重点讨论了upnot balancer逻辑改进和字符串优化方法。
- **硬件兼容性**: 讨论了4K min_alloc_size在不同类型存储设备上的表现和优化策略。
- **系统配置**: 涉及MDS的CPU亲和性设置和OSD的过滤改进。

#### 决定事项
- 继续进行4K min_alloc_size测试，特别是对RGW工作负载的影响。
- 对新的Intel节点进行优化配置，以提高性能。

#### 后续行动计划
- 对4K min_alloc_size进行更多测试，包括RGW工作负载的性能评估。
- 继续优化新的Intel节点的配置，以达到更好的读写性能和I/O操作。
- 下周会议将继续讨论相关PR和配置优化。

#### 其他备注
- 会议中提到一些技术细节和测试结果，需要进一步分析和验证。
- 对于混合工作负载的处理，需要找到更通用的解决方案。