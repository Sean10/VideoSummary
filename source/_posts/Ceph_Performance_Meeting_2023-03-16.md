---
title: "Ceph Performance Meeting 2023-03-16"
date: 2023-03-16
updated: 2023-03-17
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **参会人员**: Casey, Igor, Mark, Joshua, 及其他相关人员。
- **会议时间**: 具体时间未提及，但提到会议开始时有人迟到。
- **会议平台**: 讨论了从Blue Jeans迁移到Jitsu的计划，因为Blue Jeans即将停止服务。

#### 讨论的主要议题
1. **Zero Back End**: Casey介绍了Zero Back End的概念，这是一个优化Beast前端和HTTP 3前端性能的工具。团队对此表示兴奋，并讨论了其在Ceph RGW（RADOS Gateway）中的应用潜力。
2. **HTTP 3 Front End**: 讨论了HTTP 3前端的性能工作，以及如何通过Zero Back End进行苹果对苹果的比较。
3. **HS Bench**: 提到了HS Bench工具的使用，询问是否有改进测试的方法。
4. **Mini IO Work**: 讨论了Mini IO工作的进展，确认其对团队有用，并考虑将其集成到CBT（Ceph Build Test）中。
5. **Writable File Allocate PR**: Igor介绍了他的PR，该PR旨在减少SSD文件的碎片化，提高性能。讨论了其对RocksDB接口的影响和潜在的性能提升。
6. **RocksDB Store**: 讨论了RocksDB Store的多个PR，包括优化删除范围阈值和使用边界迭代器。
7. **D4N Work for RGW**: 讨论了一个大型PR，涉及RGW的D4N工作，目前正在进行中。
8. **TC Malek in C-Star**: 讨论了在C-Star中启用TC Malek的PR，以解决内存泄漏问题，提高性能和内存使用效率。

#### 决定的事项
- 确认Zero Back End的潜力，并计划进一步探索其在Ceph中的应用。
- 确认Mini IO工作的有用性，并考虑将其集成到CBT中。
- 确认Igor的Writable File Allocate PR的潜在性能提升，并计划进行进一步测试。
- 确认RocksDB Store的多个PR的进展，并计划进行QA测试。
- 确认D4N Work for RGW的PR的进展，并计划进行进一步的工作。
- 确认TC Malek in C-Star的PR的进展，并计划进行进一步的测试和集成。

#### 后续的行动计划
- 继续探索Zero Back End在Ceph中的应用。
- 继续测试和集成Mini IO工作到CBT中。
- 继续测试和集成Igor的Writable File Allocate PR。
- 继续测试和集成RocksDB Store的多个PR。
- 继续测试和集成D4N Work for RGW的PR。
- 继续测试和集成TC Malek in C-Star的PR。
- 迁移会议平台从Blue Jeans到Jitsu。

#### 其他讨论
- 讨论了Ceph的性能改进，特别是在Reef版本中，提到了随机写入性能的提升。
- 讨论了SSD驱动器的固件升级对性能的影响，以及如何处理驱动器碎片化问题。

#### 结论
会议涵盖了多个技术议题，包括性能优化、工具集成和平台迁移。团队对未来的工作充满期待，并计划继续推进各项议题的进展。