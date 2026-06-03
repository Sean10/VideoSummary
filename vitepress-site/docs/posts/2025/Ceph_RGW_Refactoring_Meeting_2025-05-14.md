---
title: "Ceph RGW Refactoring Meeting 2025-05-14"
date: 2025-05-14
updated: 2025-05-24
tags:
  - "Ceph"
  - "RGW"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### Ceph RGW 重构会议纪要

**会议日期**: 2025-05-14  
**参会人员**: 待补充  
**讨论主题**: RGW (RADOS Gateway) 相关功能设计与实现

#### 1. Bucket Logging API 实现位置讨论
- **问题背景**: 需要为 `bucket logging` 添加一个返回规范化操作名称的 API，以匹配 AWS 日志中的命名格式。
- **关键讨论点**: RGW 操作类存在三层抽象，包括 S3/Swift 协议层、Object Store 层和基础操作类。
- **决策**: 将实现放在 `RGWOp_ObjectStore` 层，以记录 S3/Swift 操作；对于非 REST 操作，放在基类 `RGWOp` 中；默认实现返回操作名称，子类可覆盖以匹配 AWS 格式。
- **后续行动**: 在 `RGWOp_ObjectStore` 中实现 API。

#### 2. 持久化通知（Persistent Notifications）的存储池选择问题
- **问题背景**: 当前的持久化通知队列对象默认存储在 `log pool`，但可能导致性能问题。
- **解决方案讨论**: 允许通过 `zone params` 指定自定义池（如 `notif_pool`），但需处理迁移问题。
- **后续行动**: 默认使用 `log pool`，但提供配置选项；补充文档说明性能建议和迁移步骤。

#### 3. CORS 全局规则支持（Dashboard 团队需求）
- **问题背景**: Dashboard 团队在测试 S3 浏览器应用时，因 CORS 限制导致交互失败。
- **需求**: 扩展 RGW 的 CORS 支持，添加全局规则以简化 S3 浏览器集成。
- **后续行动**: 跟踪相关 Issue，协调开发资源。

#### 4. 快照（Snapshot）统计数据的处理逻辑
- **问题背景**: `head bucket` 返回的统计信息是否应包含快照中的隐藏对象。
- **决策**: 对外 API 返回当前视图，内部接口返回全量数据（含快照）。
- **后续行动**: 明确快照统计逻辑并更新相关接口。

#### 5. 其他事项
- **Tentacle 版本状态**: 仍处于代码冻结阶段，等待 RC 发布。
- **文档改进**: 需补充各存储池的性能特性说明。

**下一步行动**
1. 实现 `bucket logging` API 并提交代码审核。
2. 完善 `notif_pool` 配置及迁移文档。
3. 推进 CORS 全局规则开发。
4. 明确快照统计逻辑并更新相关接口。