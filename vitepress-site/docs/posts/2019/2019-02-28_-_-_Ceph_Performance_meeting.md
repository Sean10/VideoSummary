---
title: "2019-02-28 :: Ceph Performance meeting"
date: 2019-04-15
updated: 2019-04-16
tags:
  - "Ceph"
  - "分布式存储"
  - "性能优化"
  - "存储集群"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Sage, Radix, Adams, Igor 等

**会议主题**： Ceph 项目进展讨论

**会议内容**：

* **项目进展**：
    * Sage 报告了 Nautilus 项目的进展顺利，团队目前主要集中在此项目上。
    * 会议讨论了本周的两个合并的 PR：Radix 提交的从缓冲区列表中移除 radix 缓冲区的 PR 已合并；sea-star charred lru 相关的 PR 已关闭，转向其他方向。
    * 一些 PR 更新了 macing messenger 代码，Adams 对其中一些 PR 提出异议。
    * goan 发现了 boost CEO 的问题，该问题不支持具有多个参数的函数，可能影响 GW。
    * batch handle send message 的 PR 需要进行更多测试，以验证性能改进。
    * 降低 blue space 分配数量的 PR，关于是否在新位图分配器中实现 discard 特性存在讨论。
    * VLA 相关的 PR 正在测试和调试中。
    * Igor 的自动调优 PR 尚未完成，计划在 Nautilus 之后进行。
    * Igor 的 cash bidding 代码分支实现了更智能的 cash binning 和改进的 blue store trim 策略。
* **讨论议题**：
    * Sage 提出了关于 blue story cash 大小的疑问，认为对于 SSD，默认应为 3GB，而不是 HDD。
    * 经过讨论，Sage 解释了当时设置 SSD 缓存大小为 HDD 的原因，但认为这是一个不好的设计。
    * 目前 Ceph 存在双重缓存的问题，需要进一步改进。
* **行动计划**：
    * 继续推进 Nautilus 项目的开发。
    * 完成未完成的 PR，并解决相关性能问题。
    * 研究并解决双重缓存问题。

**备注**：

* 会议中提到了一些 Ceph 相关的关键词，如 Nautilus, radix, macing messenger, VLA, auto-tuning, cash bidding 等。
* 会议还讨论了 Ceph 的性能优化和缓存策略，以及对 blue store 和 SSD 缓存大小的调整。