---
title: "Scaling RGW D4N Caches With Experimental Offloading - Jesse Williamson & Matthew Benjamin, IBM"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
本次会议聚焦于Ceph RGW（RADOS Gateway）的性能优化，特别是针对D4N（Directory-based Data Center Delivery Network）缓存架构的改进，以及探索使用FoundationDB作为替代后端数据库的潜力，以提升S3桶索引的可扩展性和事务支持。

#### 关键讨论点

1. **D4N缓存架构的演进**
   - D4N旨在实现分布式读写缓存，支持跨节点数据共享和弹性扩展。
   - 当前状态：单节点原型已实现，使用Redis作为后端，正在开发分布式块缓存和测试套件。
   - 目标：支持事务、多租户策略和动态缓存管理。

2. **FoundationDB的引入**
   - 使用FoundationDB作为替代后端数据库，以解决现有OMAP在分布式事务和一致性上的限制。
   - 优势：原生支持原子事务和全局有序键空间，适合大规模桶索引。
   - 实现进展：开发了libfdb客户端库，支持STL容器和Ceph的`bufferlist`。

3. **未来方向**
   - 探索将全部桶索引元数据迁移到FoundationDB。
   - 研究跨地域低延迟缓存的可能性。
   - 设计智能缓存策略，如Spark工作负载感知的预取。

#### 决策事项

1. 推进FoundationDB作为D4N的备选后端，验证其在大规模桶索引场景下的性能。
2. 重构D4N后端接口，支持多数据库插件化。
3. 完善libfdb的Ceph生态集成，联合社区测试FoundationDB在超大规模桶枚举中的表现。

#### 后续行动计划

| 任务 | 负责人 | 时间线 |
||--|--|
| 完成 D4N 分布式缓存原型 | RGW 团队 | Q3 2023 |
| 提交 FoundationDB 驱动 PR | Casey/Jesse | 当前进行中 |
| 性能基准测试（vs OMAP） | 社区协作 | Q4 2023 |
| 多租户缓存策略设计 | Matt | 长期规划 |

#### 遗留问题

- FoundationDB在跨地域高延迟环境中的可行性需进一步验证。
- 是否支持可变数据缓存以加速读写混合负载？

#### 相关资源

- [FoundationDB 论文](https://www.foundationdb.org/files/fdb-paper.pdf)
- D4N 原型代码库（搜索 `PR #foundationdb` 或 `libfdb`）
- Ceph 社区关于 OMAP 替代方案的讨论（邮件列表存档）