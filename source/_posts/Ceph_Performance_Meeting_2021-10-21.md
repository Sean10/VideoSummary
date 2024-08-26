---
title: "Ceph Performance Meeting 2021-10-21"
date: 2021-10-21
updated: 2021-10-22
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **新PR讨论**：本周有一个关于backfill和recovery性能的新PR，由用户“gun”提交。该PR针对特定情况，即新OSD需要从主OSD进行完整复制，且主OSD的PG日志条目数小于OSD最小PG日志条目数时，新OSD可以通过PG日志进行恢复。该方法通过backfill处理比recovery更快，因为recovery涉及更多额外工作。Mia将审查该PR。
- **已关闭的PR**：四个PR已关闭，包括TTL缓存、async messenger帧消息头优化、OSD压缩绕过和Adam的BlueFist fine green locking PR。其中，BlueFist PR在测试中导致锁定失败，但Adam正在处理。
- **更新的PR**：三个PR已更新，包括MDS的树移除PR和两个库D优化PR。这些PR需要重新审查。
- **性能优化**：Jeff Layton提交了内核客户端的修复，可能解决之前观察到的3GB/s瓶颈问题。使用自旋锁替代不必要的互斥锁，Ilia将审查并进行测试，目标是达到8GB/s的性能。
- **GDB PMP问题**：GDB PMP在多线程环境下导致经典OSD崩溃，Adam开发了一个使用live unwind的新版本，速度更快但代码复杂。目前正在尝试结合lib unwind和lib dw进行优化。

#### 讨论的主要议题
- **Backfill与Recovery性能优化**：讨论了新PR中提出的backfill与recovery性能优化方法。
- **PR状态更新**：回顾了已关闭和更新的PR，特别是涉及性能优化和锁定的PR。
- **内核客户端性能瓶颈**：讨论了Jeff Layton提交的修复，旨在解决内核客户端的性能瓶颈。
- **GDB PMP的替代方案**：讨论了GDB PMP的问题及其替代方案，包括Adam的新版本和结合lib unwind与lib dw的尝试。

#### 决定的事项
- **审查新PR**：Mia将审查关于backfill和recovery性能的新PR。
- **测试性能优化**：Ilia将审查并测试Jeff Layton提交的内核客户端修复。
- **继续优化GDB PMP替代方案**：继续探索和优化GDB PMP的替代方案，结合lib unwind和lib dw。

#### 后续行动计划
- **审查和测试PR**：继续审查和测试所有相关的PR，确保代码质量和性能。
- **性能测试**：进行详细的性能测试，特别是内核客户端的修复和GDB PMP的替代方案。
- **代码优化**：持续优化代码，特别是涉及锁定的部分和性能瓶颈的解决。

### 结束语
会议在讨论了各项PR的状态和性能优化措施后结束，团队成员将继续跟进相关工作，确保项目的稳定性和性能提升。