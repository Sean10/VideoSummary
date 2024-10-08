---
title: "Ceph RGW Refactoring Meeting 2023-07-05"
date: 2023-07-05
updated: 2023-07-06
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：扩展用户存储桶数量的讨论

**主要议题：**
- 当前用户存储桶列表存储在单个RADOS对象的omap中，随着存储桶数量的增加，可能会导致RADOS的omap过大，影响性能。
- 讨论了omap的最大键数限制（200,000），以及其对RADOS复制和恢复设计的影响。
- 提出了通过分片（sharding）策略来解决存储桶数量增长的问题，但需要考虑排序和分页的需求。
- 讨论了是否需要为存储桶列表API增加排序和分页功能。

**决定事项：**
- 需要进一步研究和实现分片策略，以支持更大数量的存储桶。
- 需要评估和优化存储桶列表API的性能，考虑是否增加排序和分页功能。

**后续行动计划：**
- 继续研究和测试分片策略，确保其能够有效支持大量存储桶。
- 评估存储桶列表API的需求，考虑是否需要增加排序和分页功能。
- 增加文档说明，明确用户存储桶数量的限制和相关性能影响。

#### 会议主题：Lua包重载机制的改进

**主要议题：**
- 当前Lua包重载需要重启RADOS网关（rgw），希望避免这种情况。
- 讨论了使用watch notify机制来实现无需重启的重载。
- 讨论了是否需要抽象出通知机制，以便未来支持其他存储后端。

**决定事项：**
- 需要进一步研究和实现watch notify机制，以支持Lua包的动态重载。
- 需要考虑抽象出通知机制，以便未来支持其他存储后端。

**后续行动计划：**
- 继续研究和测试watch notify机制，确保其能够有效支持Lua包的动态重载。
- 考虑抽象出通知机制，以便未来支持其他存储后端。

#### 其他议题：
- 讨论了Bloom过滤器的最新进展，但没有新的更新。

**会议总结：**
- 本次会议主要讨论了如何扩展用户存储桶数量和改进Lua包重载机制，确定了后续的研究和开发方向。
- 需要继续关注和研究相关技术细节，确保解决方案的有效性和性能。

**下次会议预告：**
- 下次会议将继续讨论和评估本次会议确定的方案，并根据进展调整后续行动计划。