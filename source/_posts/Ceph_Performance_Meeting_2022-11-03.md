---
title: "Ceph Performance Meeting 2022-11-03"
date: 2022-11-09
updated: 2022-11-10
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议主要讨论了Ceph分布式存储系统的性能问题，特别是关于librbd与qemu-kvm的性能差距、RBD镜像的性能问题以及Blue Store的优化方向。会议中涉及了多个技术议题，包括性能调优、加密对性能的影响、快照和快照修剪的性能问题，以及Blue Store的未来发展方向。

#### 主要议题
1. **librbd与qemu-kvm性能差距**
   - 讨论了一篇关于librbd与qemu-kvm性能差距的博客文章。
   - 实验结果显示，在启用加密的情况下，16K随机读取的IOPS可以达到123,000，而随机写入的IOPS约为65,000。
   - 加密导致性能下降约30%，主要原因是加密处理占用了messenger线程的大量时间。

2. **RBD镜像性能问题**
   - 讨论了RBD镜像性能下降的问题，主要原因是快照和快照修剪导致的OSD使用率上升。
   - 分析了对象碎片化和共享blob的问题，提出了两种解决方案：一种是减少共享blob，另一种是对象去碎片化。
   - 目前这两种方案都有各自的优缺点，正在进行进一步的测试和优化。

3. **Blue Store的优化方向**
   - 讨论了Blue Store的未来发展方向，包括可能的Blue Store 2版本。
   - 提出了一些大的改变，如改进写路径、处理分层存储等。
   - 讨论了是否值得进行这些大的架构改变，以及如何平衡性能和稳定性。

#### 决定事项
- 将继续测试和优化RBD镜像的性能问题，特别是快照和快照修剪的影响。
- 对于Blue Store的优化，将考虑是否需要进行大的架构改变，以及如何实现这些改变。
- 将进行更多的实验和测试，以确定最佳的性能调优方案。

#### 后续行动计划
- 继续跟踪和优化RBD镜像的性能问题，特别是快照和快照修剪的影响。
- 对于Blue Store的优化，将进行更多的讨论和实验，以确定最佳的发展方向。
- 将进行更多的性能测试，以确定最佳的性能调优方案。

#### 其他事项
- 讨论了关于Blue Store的写路径优化，特别是如何处理小写入和大写入的问题。
- 讨论了如何更好地利用不同的存储设备，如NVMe和HDD。

#### 会议总结
本次会议深入讨论了Ceph存储系统的多个性能问题，并提出了相应的解决方案和优化方向。后续将继续进行更多的测试和优化工作，以提高系统的性能和稳定性。