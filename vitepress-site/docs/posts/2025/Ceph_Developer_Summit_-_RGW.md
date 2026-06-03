---
title: "Ceph Developer Summit - RGW"
date: 2025-09-11
updated: 2025-09-12
tags:
  - "Ceph"
  - "分布式存储"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
在本次Ceph开发者峰会中，与会者讨论了即将发布的Umbrella版本的规划与功能进展。以下为会议的关键点：

### 关键讨论与决议

#### 1. D4N性能优化
- **当前状态**：Pria正在完成性能优化代码，预计将包含在Umbrella版本中。
- **下一步计划**：实现分布式缓存功能，作为下一个重要里程碑。
- **关键词**：D4N, distributed cache, performance tuning

#### 2. DDUP（数据去重）
- **进展**：Full DDUP PR已提交测试，Rate Limiting for DDUP的PR待文档修正后合并，Small Object DDUP逻辑开发中。
- **功能增强**：估算工具将显示常规对象和小对象的去重节省空间，帮助用户权衡性能开销。
- **关键词**：DDUP, erasure coding, deduplication, small object optimization

#### 3. 快照（Snapshots）
- **现状**：Yehuda的原实现需rebase并修复单元测试，解决QE报告的版本兼容性问题。
- **争议**：快照与bucket logging的备份方案优劣讨论，但快照仍被视为独立高价值功能。
- **行动计划**：寻找开发者接手，目标纳入Umbrella。
- **关键词**：snapshots, versioning, backup, bucket logging

#### 4. Ordered Bucket Listing
- **状态**：Eric未参会，但据传开发进展较快，可能瞄准Umbrella。
- **疑问**：设计文档和代码未公开，需进一步确认优先级。
- **关键词**：Ordered Bucket Listing

#### 5. 其他功能更新
- **Customer Managed Policies**：Pritha和Raja的PR进展顺利，预计无合并障碍。
- **Account-wide Public Access Block**：已有PR，待测试和审查。
- **AWS Organization APIs**：初期设计阶段，目标支持账户层级管理和配额控制，但Umbrella版本可能来不及纳入。
- **S3 Vectors**：处于设计阶段，明确排除在Umbrella外。
- **Log Offload**：确定延迟至V版本合并。
- **关键词**：Customer Managed Policies, Account-wide Public Access Block, AWS Organization APIs, S3 Vectors, Log Offload

#### 6. 技术债务与弃用
- **OMAP Data Logs**：计划在Umbrella版本中标记为deprecated，但实际移除推迟至后续版本。
- **关键词**：deprecation, OMAP, migration

#### 7. Bucket Logging 增强
- **EC Pool 支持**：NIT正在开发异步刷新临时日志的功能，设计改动较大，但预计纳入Umbrella。
- **关键词**：bucket logging, EC pools, asynchronous flush

### 后续行动计划
1. 合并D4N性能优化代码，启动分布式缓存开发。
2. 加速DDUP PR合并，完成Small Object DDUP。
3. 分配开发者解决快照测试和版本兼容性问题。
4. 通过邮件公开功能列表，收集社区反馈。
5. 继续使用EtherPad记录进展。

本次会议还讨论了Tentacle RC1的发布情况，以及社区成员对于即将到来的版本的兴趣和需求。