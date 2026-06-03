---
title: "2019-08-01 :: Ceph Performance Meeting"
date: 2019-08-02
updated: 2019-08-03
tags:
  - "Ceph"
  - "BlueStore"
  - "RocksDB"
  - "性能"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Neha, Josh, Adam, Eric, Igor, Aaron, Mark, Sam 等

**会议主题**：

1. **本周 PR 回顾**：
   - 合并了支持 RocksDB 新版本的 master，增加了 proxy cache 和 range 功能。
   - Moshing 和 Peng 提交的 PR 减少了 BlueStore 的唤醒次数，可能带来性能提升。
   - May 提交的 PR 通过测试，为 BlueStore 带来了 25-30% 的随机小写性能提升。
   - Trim cache on ad PR 已合并到 P 上。
   - Eric 提交的 RGW 效率提升 PR 已进入测试阶段。
   - Adams 提交的 PR 正在测试中，希望尽快合并。

2. **RFC：将 BlueFS Alexeyes 默认值设置为与 BlueStore 相同，并设置为 16K**：
   - 背景和目的：为了解决 BlueFS 和 BlueStore 在碎片化方面的差异，提出将两者分配大小设置为相同的 RFC。
   - 讨论：Neha 介绍了 RFC 的背景和目的，Josh 解释了 PR 的具体实现方式，Mark 提出性能影响的担忧，并希望进行更多测试，Adam 认为将分配大小设置为 16K 是一个合理的折衷方案，决定将 PR 作为高优先级任务进行测试和评估。

3. **其他议题**：
   - Igor 的 RocksDB 提示文件 PR 仍在进行中。
   - 6.1.2 版本已合并到 master，并计划将其回滚到 Nautilus。
   - MDS 和 Demon 内存限制调整 PR 正在开发中。
   - OpTracker 事件优化 PR 已与 Patrick 达成共识。
   - Igor 的自动调整 PR 需要重构和重置。

4. **行动计划**：
   - 对 BlueFS Alexeyes 默认值设置为 16K 的 PR 进行测试和评估。
   - 继续开发其他 PR。
   - 讨论将 RocksDB 6.1.2 版本回滚到 Nautilus 的可行性。
   - 关注 Igor 的 RocksDB 提示文件 PR 的进展。

**后续会议**：

- 下周会议可能讨论 Sam 关于 LoRan 内部延迟的分享。

**改进点**：
- 更详细地描述了 RFC 的背景和目的，以及相关的讨论内容。
- 补充了 Igor 的 RocksDB 提示文件 PR 和自动调整 PR 的进展情况。
- 确保了所有 Ceph 相关的关键字得到保留。