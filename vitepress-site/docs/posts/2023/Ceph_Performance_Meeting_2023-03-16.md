---
title: "Ceph Performance Meeting 2023-03-16"
date: 2023-03-16
updated: 2023-03-17
tags:
  - "Ceph"
  - "性能优化"
  - "分布式存储"
  - "RocksDB"
categories:
  - "视频总结"
outline: deep
---
在 2023 年 3 月 16 日的 Ceph 性能会议上，参会人员包括 Casey, Igor, Mark, Joshua 等相关人员。会议主要讨论了以下议题：

### 关键细节

- **参会人员**: Casey, Igor, Mark, Joshua 及其他相关人员。
- **会议时间**: 具体时间未提及，但有人迟到。
- **会议平台**: 讨论了从 Blue Jeans 迁移到 Jitsu 的计划。

### 讨论的主要议题

1. **Zero Back End**: Casey 介绍了 Zero Back End，这是一个优化 Beast 前端和 HTTP 3 前端性能的工具。团队对此表示兴奋，并讨论了其在 Ceph RGW 的应用潜力。
2. **HTTP 3 Front End**: 讨论了 HTTP 3 前端的性能工作，以及如何通过 Zero Back End 进行苹果对苹果的比较。
3. **HS Bench**: 提到了 HS Bench 工具的使用，询问是否有改进测试的方法。
4. **Mini IO Work**: 讨论了 Mini IO 工作的进展，确认其对团队有用，并考虑将其集成到 CBT 中。
5. **Writable File Allocate PR**: Igor 介绍了他的 PR，该 PR 旨在减少 SSD 文件的碎片化，提高性能。讨论了其对 RocksDB 接口的影响和潜在的性能提升。
6. **RocksDB Store**: 讨论了 RocksDB Store 的多个 PR，包括优化删除范围阈值和使用边界迭代器。
7. **D4N Work for RGW**: 讨论了一个大型 PR，涉及 RGW 的 D4N 工作，目前正在进行中。
8. **TC Malek in C-Star**: 讨论了在 C-Star 中启用 TC Malek 的 PR，以解决内存泄漏问题，提高性能和内存使用效率。

### 决定的事项

- 确认 Zero Back End 的潜力，并计划进一步探索其在 Ceph 中的应用。
- 确认 Mini IO 工作的有用性，并考虑将其集成到 CBT 中。
- 确认 Igor 的 Writable File Allocate PR 的潜在性能提升，并计划进行进一步测试。
- 确认 RocksDB Store 的多个 PR 的进展，并计划进行 QA 测试。
- 确认 D4N Work for RGW 的 PR 的进展，并计划进行进一步的工作。
- 确认 TC Malek in C-Star 的 PR 的进展，并计划进行进一步的测试和集成。
- 迁移会议平台从 Blue Jeans 到 Jitsu。

### 后续行动计划

- 继续探索 Zero Back End 在 Ceph 中的应用。
- 继续测试和集成 Mini IO 工作到 CBT 中。
- 继续测试和集成 Igor 的 Writable File Allocate PR。
- 继续测试和集成 RocksDB Store 的多个 PR。
- 继续测试和集成 D4N Work for RGW 的 PR。
- 继续测试和集成 TC Malek in C-Star 的 PR。
- 迁移会议平台从 Blue Jeans 到 Jitsu。

### 其他讨论

- 讨论了 Ceph 的性能改进，特别是在 Reef 版本中，提到了随机写入性能的提升。
- 讨论了 SSD 驱动器的固件升级对性能的影响，以及如何处理驱动器碎片化问题。

会议涵盖多个技术议题，包括性能优化、工具集成和平台迁移。团队对未来的工作充满期待，并计划继续推进各项议题的进展。