---
categories:
- 视频总结
date: 2022-02-02
subtitle: Ceph_Performance_Meeting_2022-01-27
tags:
- RocksDB
- 测试
- RBD
title: Ceph Performance Meeting 2022-01-27
updated: 2022-02-03
---


### 会议纪要

#### 关键细节
- **Ceph 性能动态**：本周性能相关 Pull Request 活动相对平静。
- **Ronin 的 PR**：涉及 scrub 功能的优化，主要是调整 chunk 大小以优化 scrub 过程。
- **Scrub Chunk Size**：讨论了 scrub 过程中 chunk 大小的配置，建议根据 scrub 类型（深度或常规）调整 chunk 大小。
- **Tracing 功能**：讨论了将 tracing 功能默认编译进 Ceph 的 PR，尽管有轻微性能开销，但便于用户调试。
- **RocksDB 的 TTL 和 Compaction**：讨论了 RocksDB 中的 TTL 和 compaction 设置，特别是在大量插入和删除操作下的性能问题，建议通过调整 TTL 清理 tombstones。

#### 讨论的主要议题
- **Scrub 性能优化**：通过调整 scrub chunk 大小优化性能，同时减少对客户端请求的影响。
- **Tracing 功能集成**：讨论了将 tracing 功能默认编译进 Ceph 的利弊，以及如何平衡性能开销和调试便利性。
- **RocksDB 性能问题**：深入讨论了 RocksDB 在处理大量数据插入和删除时的性能问题，特别是 tombstones 导致的性能退化，提出了通过 TTL 定期清理 tombstones 的解决方案。

#### 决定的事项
- **Scrub Chunk Size 调整**：决定区分 deep scrub 和 regular scrub 的 chunk 大小，并进行进一步测试以确保不会引入新的延迟问题。
- **Tracing 功能默认编译**：尽管存在轻微性能开销，但决定将 tracing 功能默认编译进 Ceph，以便用户在需要时启用。
- **RocksDB 的 TTL 设置**：决定尝试通过调整 TTL 定期清理 tombstones，以解决性能退化问题，并进行进一步的测试和验证。

#### 后续行动计划
- **Scrub Chunk Size 测试**：进行进一步的测试，确保调整后的 chunk 大小不会影响客户端请求的性能。
- **Tracing 功能评估**：评估 tracing 功能默认编译后的性能影响，并考虑是否需要进一步优化。
- **RocksDB 的 TTL 和 Compaction 测试**：在实际生产环境中测试调整 TTL 后的性能表现，并监控其对系统的影响。
- **与 Spdb 合作**：考虑与 Spdb 合作，评估其 RocksDB 替代方案在 Ceph 中的性能表现，特别是在处理大量数据插入和删除时的性能优化。

#### 其他事项
- **性能测试和优化**：继续关注和优化 Ceph 在不同硬件配置下的性能表现，特别是在 AMD 和 Intel 节点上的性能对比。
- **生产环境验证**：在实际生产环境中验证各项优化措施的效果，并根据反馈进行调整。