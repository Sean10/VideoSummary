---
title: "Ceph Performance Meeting 2021-06-17"
date: 2021-06-23
updated: 2021-06-23
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **MDS改进提案**：本周有一个有趣的pull request针对MDS（元数据服务器），旨在改进在并发客户端访问同一文件时的锁定机制。理论上，这可能减少长时间等待获取读锁的情况，但需要进一步测试验证。
- **B树分配器提交**：ifu提交了一个新的B树分配器，可能在内存使用和某些情况下的性能上有所优势，尽管会增加CPU使用。初步测试显示，与AVL分配器相比，空间改进接近两倍，CPU消耗增加不大。
- **内存管理讨论**：讨论了新的分配器在长时间运行测试中的潜在问题，特别是关于碎片化和内存使用的增长。建议进行更长时间的测试以验证其稳定性。
- **TC malloc缓存大小调整**：Adam提交了一个新的pull request，允许在运行时修改TC malloc缓存的大小，这被认为是改进内存管理的一个正确方向。

#### 讨论的主要议题
- **性能优化**：讨论了多个pull request，旨在优化Ceph的性能，特别是在高并发和高负载情况下的表现。
- **内存管理**：深入讨论了新的B树分配器在实际应用中的表现，包括其对内存使用和CPU消耗的影响。
- **配置管理**：讨论了如何更好地管理Ceph组件的配置，特别是在运行时调整缓存大小的能力。

#### 决定的事项
- **测试新分配器**：决定对新的B树分配器进行更深入的测试，包括长时间运行和高负载条件下的表现。
- **配置管理改进**：支持Adam的pull request，认为这是改进Ceph配置管理的正确方向。

#### 后续行动计划
- **深入测试**：对新的B树分配器进行包括长时间运行和高负载条件下的测试。
- **性能分析**：继续分析和优化Ceph在不同配置下的性能表现，特别是在高并发和高负载情况下的稳定性。
- **配置管理优化**：进一步讨论和实施运行时配置调整的方案，以提高Ceph的灵活性和性能。

本次会议涵盖了Ceph存储系统的多个关键技术领域，包括性能优化、内存管理和配置管理，旨在通过技术改进提升系统的整体稳定性和效率。