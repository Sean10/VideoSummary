---
title: "Ceph RGW Refactoring Meeting 2025-08-13"
date: 2025-08-13
updated: 2025-09-08
tags:
  - "Ceph"
  - "RGW"
  - "性能优化"
  - "Erasure Coding"
categories:
  - "视频总结"
outline: deep
---
在2025年8月13日的Ceph RGW重构会议中，讨论了以下关键议题：

### 1. Bucket Logging在EC Pool中的问题及解决方案
- **问题背景**：EC Pool不支持对RADOS对象的原地追加日志记录，这影响了性能。
- **现有方案**：将数据写入额外的数据池（replicated pool），但需要用户手动创建`storage class`。
- **讨论要点**：
  - **临时方案 vs. 最终方案**：一致同意采用异步复制日志记录到EC Pool，并在提交时创建`head object`。
  - **性能优化**：若在replicated pool中，则直接写入；若在EC Pool，则临时写入extra data pool，异步复制到目标池。
- **后续行动**：Nithia & Yuval将继续实现异步复制逻辑，确保`head object`正确指向`tail objects`。

### 2. Bucket Listing性能优化
- **问题背景**：当`bucket index`包含大量连续的`delete markers`时，列表操作会显著变慢。
- **讨论要点**：
  - **优化方向**：保持长连接，发送`whitespace`防止客户端超时，优化长列表性能。
- **后续行动**：Jane & Eric将重新评估设计，优先考虑保持标记连续性的方案。

### 关键结论
- **Bucket Logging**：采用异步复制到EC Pool的最终方案。
- **Bucket Listing**：优化列表逻辑，减少`delete markers`的影响。

### 下一步计划
| 任务 | 负责人 | 时间节点 |
||--|-|
| 实现异步复制逻辑 | Nithia & Yuval | 后续迭代 |
| 优化Bucket Listing性能 | Jane & Eric | 待优先级确认 |
| 修复GC误删问题 | Nithia (需与Eric协作) | 短期跟进 |

该会议讨论了Ceph RGW在Bucket Logging和Bucket Listing方面的性能优化和改进方案，并确定了后续的行动计划。