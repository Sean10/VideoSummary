---
title: "2020-01-30 -- Ceph Performance Meeting"
date: 2020-01-30
updated: 2020-04-01
tags:
  - "Ceph"
  - "性能优化"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
在 2020 年 1 月 30 日的 Ceph 性能会议上，研发人员和内容审核专家讨论了多个关键议题，包括性能优化、代码逻辑简化、CI 系统改进以及具体的 Pull Requests (PRs)。

### 关键细节

- **新 PR 介绍**：会议开始时，介绍了包括 Casey 和 Braddock 的优化 buffer lists 的 PR。
- **Igor 的 PR**：Igor 提交了一个简化 Onoda pin 和 unpin 逻辑的 PR，解决了之前修复时引入的复杂性和潜在的竞态条件问题。
- **Zone Commodity 配置**：讨论了允许 zone commodity 配置 index charts 的 PR，包括增加 bucket shards 数量的简单更改。
- **PG autoscaler 更新**：一个将默认 PG 数量增加到 32 的 PR 已合并，旨在提高 OSD 对更多 PG 的响应性。
- **Bufferless 和 Buffer List 优化**：Radek 和 Corel 讨论了优化 buffer list 大小的旧努力，包括使用迭代器和减少内存占用。

### 讨论的主要议题

- **性能优化**：重点讨论了通过优化 buffer lists 和调整 PG 数量来提高性能。
- **简化逻辑**：强调了简化代码逻辑的重要性，如 Igor 的 PR 所示。
- **CI 和测试**：讨论了 CI 系统的改进，包括增加对 master 分支的 CI 支持和对不同基准测试的性能比较。

### 决定的事项

- **合并 PR**：多个 PR 被合并或准备合并，包括优化 PG 数量和 bufferless 使用的 PR。
- **CI 改进**：决定继续改进 CI 系统，增加对更多基准测试的支持。

### 后续行动计划

- **继续优化**：继续关注和优化 buffer lists 和 PG autoscaler。
- **CI 系统升级**：继续升级 CI 系统，确保所有测试环境的一致性和最新性。
- **性能测试**：进行更多的性能测试，特别是在不同硬件和配置下的测试。

### 其他讨论点

- **SSD 性能问题**：讨论了 SSD 性能问题，特别是关于队列大小和服务时间的优化。
- **环境升级**：讨论了测试环境的升级，包括从 CentOS 7 升级到更高版本。

会议最后，主持人宣布将休息两周，期间可能不会有会议。整体上，会议聚焦于性能优化和 CI 系统的改进，同时讨论了具体的 PR 和未来的工作方向。