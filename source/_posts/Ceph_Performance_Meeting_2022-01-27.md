---
title: "Ceph Performance Meeting 2022-01-27"
date: 2022-02-02
updated: 2022-02-03
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **Ceph性能前线**：本周相较于前几周较为平静，PR（Pull Request）活动在性能方面有所减少。
- **Ronin的PR**：涉及scrub功能的PR，主要改变了一些chunking操作，以优化scrub过程中的chunk大小。
- **Scrub Chunk Size**：讨论了scrub过程中chunk大小的配置参数，建议区分deep scrub和regular scrub的chunk大小，以减少对常规客户端请求的延迟影响。
- **Tracing功能**：讨论了将tracing功能默认编译进Ceph的PR，尽管有轻微的性能开销，但可以方便用户在遇到问题时启用tracing。
- **RocksDB的TTL和Compaction**：讨论了RocksDB中的TTL（Time to Live）和compaction设置，特别是在大量插入和删除操作下的性能问题，建议通过调整TTL来定期清理tombstones，以避免性能退化。

#### 讨论的主要议题
- **Scrub性能优化**：如何通过调整scrub的chunk大小来优化性能，同时不影响客户端请求。
- **Tracing功能的集成**：讨论了将tracing功能默认编译进Ceph的利弊，以及如何平衡性能开销和调试便利性。
- **RocksDB的性能问题**：深入讨论了RocksDB在处理大量数据插入和删除时的性能问题，特别是tombstones导致的性能退化，提出了通过TTL来定期清理tombstones的解决方案。

#### 决定的事项
- **Scrub Chunk Size调整**：决定区分deep scrub和regular scrub的chunk大小，并进行进一步测试以确保不会引入新的延迟问题。
- **Tracing功能默认编译**：尽管存在轻微性能开销，但决定将tracing功能默认编译进Ceph，以便用户在需要时启用。
- **RocksDB的TTL设置**：决定尝试通过调整TTL来定期清理tombstones，以解决性能退化问题，并进行进一步的测试和验证。

#### 后续的行动计划
- **Scrub Chunk Size测试**：进行进一步的测试，确保调整后的chunk大小不会影响客户端请求的性能。
- **Tracing功能评估**：评估tracing功能默认编译后的性能影响，并考虑是否需要进一步优化。
- **RocksDB的TTL和Compaction测试**：在实际生产环境中测试调整TTL后的性能表现，并监控其对系统的影响。
- **与Spdb合作**：考虑与Spdb合作，评估其RocksDB替代方案在Ceph中的性能表现，特别是在处理大量数据插入和删除时的性能优化。

#### 其他事项
- **性能测试和优化**：继续关注和优化Ceph在不同硬件配置下的性能表现，特别是在AMD和Intel节点上的性能对比。
- **生产环境验证**：在实际生产环境中验证各项优化措施的效果，并根据反馈进行调整。

本次会议涵盖了Ceph性能优化的多个方面，从scrub性能到tracing功能的集成，再到RocksDB的性能问题，都进行了深入的讨论和决策。后续将通过一系列的测试和验证，确保各项优化措施能够有效提升Ceph的性能和稳定性。