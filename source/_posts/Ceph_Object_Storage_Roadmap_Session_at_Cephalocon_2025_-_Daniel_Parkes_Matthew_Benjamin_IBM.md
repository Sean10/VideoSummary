---
title: Ceph Object Storage Roadmap Session at Cephalocon 2025 - Daniel Parkes & Matthew Benjamin, IBM
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 对象存储
- 分布式存储
- 云计算
categories: 
- "视频总结"
subtitle: Ceph_Object_Storage_Roadmap_Session_at_Cephalocon_2025_-_Daniel_Parkes_Matthew_Benjamin_IBM
---

Ceph 社区在 Cephalocon 2025 会议中讨论了 Ceph 对象存储的最新发展。以下是会议的主要内容和讨论要点：

### Squid 版本亮点

Squid 版本引入了多项改进，包括：

1. **多站点相关改进**：
   - 对象头部复制状态查询：支持通过 HTTP Header 检查对象在多集群间的复制状态。
   - 异步数据恢复支持：支持从外部存储（如 AWS S3、IBM Cloud）拉取数据回 Ceph 集群。

2. **S3 Bucket Logging**：
   - 自助式日志配置：终端用户可通过 S3 API 自行配置 Bucket 访问日志。
   - 应用场景：流量监控、增量备份。

3. **RGW Accounts (多租户增强)**：
   - IAM API 兼容性：通过 AWS IAM 兼容接口实现租户资源自治。
   - 工作流程示例：Ceph 管理员创建租户账户并分配配额，租户管理员自主管理子用户、OIDC 单点登录等。

4. **混合云分层存储（Cloud Tiers）**：
   - 支持生命周期规则将数据自动迁移至云存储（如 S3 Glacier）。
   - 透明读取：客户端可直接请求归档对象，RGW 自动从云端拉取数据。

### Tentacle 版本规划

Tentacle 版本将引入以下新特性：

1. **核心优化方向**：
   - Bucket 索引扩展性：重构 Bucket 索引结构以支持 10 亿级对象的规模。
   - IAM/STS 增强：客户托管策略、S3 Public Access Block。

2. **性能与可观测性**：
   - D4N 缓存（下一代）：读写加速、智能预取。
   - Prometheus 集成：按用户/存储类的配额与用量指标导出。

3. **数据分析与 AI 集成**：
   - S3 Vector API：支持向量数据库的索引与查询。
   - Lakehouse 支持：强化与 Iceberg 等开放表格式的集成。

4. **其他关键特性**：
   - 去重（Deduplication）：基于对象哈希的轻量级去重。
   - NFS over RDMA：实验性支持高性能存储访问。

### 用户讨论与反馈

- 大规模 Bucket 挑战：讨论了 5 亿对象 Bucket 在复制时的性能问题。
- 协议网关需求：NFS over RDMA 已支持，SMB 网关需社区贡献。

### 后续行动计划

- Bucket 索引重构：Ceph RGW 核心开发组负责，预计在 Tentacle 版本实现。
- D4N 缓存 MVP 发布：波士顿大学合作团队负责，预计在 2024 年 Q3 完成。
- S3 Vector API 集成：IBM/Red Hat 负责，预计在 2024 年下半年完成。
- 用户级配额 Prometheus 指标：社区贡献者负责，预计在 Tentacle 版本实现。

此次会议展示了 Ceph 对象存储在多租户支持、性能优化、数据分析和 AI 集成等方面的持续进步。随着 Tentacle 版本的发布，Ceph 对象存储将更好地满足用户对大规模存储、高性能和灵活性的需求。