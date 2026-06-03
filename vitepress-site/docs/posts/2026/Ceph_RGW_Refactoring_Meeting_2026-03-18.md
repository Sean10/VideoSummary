---
title: "Ceph RGW Refactoring Meeting 2026-03-18"
date: 2026-05-13
updated: 2026-05-14
tags:
  - "RGW"
  - "加密"
  - "认证"
categories:
  - "视频总结"
outline: deep
---
## 概述

本次会议围绕 Ceph RGW 的多个重构议题展开，主要涵盖 lifecycle 压缩/encryption 支持、GCM 加密安全审查、Keystone 用户 ID 条件扩展、S3 vector 存储隔离方案，以及后台进程与 RADOS 驱动解耦等技术讨论。

## 议题一：lifecycle 过渡中的 encryption 支持

**背景**

Matthew 提出了一个已提交的 PR，目标是在 lifecycle transition 过程中支持对象的压缩与解压缩。其团队正在推进全集群范围的 encryption 部署，希望在此 PR 基础上进一步添加加解密支持。

**核心问题**

当前 Ceph 中没有原生的对象重加密机制，唯一的方式是客户端手动下载再上传。团队希望通过 lifecycle transition 实现自动化的重加密流程，具体思路是：客户端配置 lifecycle policy，将对象迁移到一个启用了 compression 和 encryption 的 storage class，从而触发重加密。

**讨论结果**

与会者 Daniel 提出了更优方案：引入一种新的 lifecycle transition 类型，专门用于 encryption key 的轮换（key rotation）。该 transition 的语义为：
- 若对象已加密，则用旧 key 解密后用新 key 重新加密；
- 若对象未加密，则直接用新 key 加密。

此方案与现有 lifecycle transition 逻辑解耦，更加清晰。与会者普遍认可这一方向，Matthew 表示将跟进调研。

## 议题二：lifecycle 版本对象批量删除优化 PR

Matthew 介绍了另一个已提交的 PR，该 PR 对 lifecycle 代码进行了重构：将相同 object key 下的多个版本对象归组，使用 multi-delete 批量删除，最后统一更新 OLH（Object Logical Head）。

**性能提升**

实测显示，版本化 bucket 的 lifecycle 处理速度提升约 50%~60%，主要收益来自 multi-delete 的批量操作减少了与 OSD 的交互次数。

**并发问题讨论**

有与会者询问 lifecycle 自身的并发控制与 multi-delete 内部并发是否会叠加。Matthew 解释：实现上将 multi-delete 的核心逻辑提取为 helper function，lifecycle 调用该 helper 时将并发度设为 1，逐个版本对象串行删除，避免了并发放大问题。

## 议题三：GCM 加密安全审查

**背景**

团队此前推进 AES-GCM 模式替换 CBC 的工作，但因安全顾虑暂缓，目前仍以 CBC 模式推进。

**核心关切**

GCM 模式下 nonce 的使用方式存在潜在风险。与会者指出，nonce 复用在 GCM 中是不可接受的高危行为，当前实现中针对 multipart 上传场景使用了 high bits / low bits 的分段策略，但该方案的安全性尚未经过充分的外部审查。

**后续行动**

- 需要引入具备密码学实现经验的外部专家进行审查；
- Casey 提议邀请 Cloudflare 团队参与，因其在早期设计阶段曾对 nonce 使用提供过意见；
- Matthew 表示可以主导与 Cloudflare 的沟通，推动安全审查落地。

## 议题四：Keystone 用户 ID 条件扩展

**提案内容**

与会者提出在现有 Keystone role 条件基础上，新增 Keystone user ID 作为 policy 条件，支持基于用户 ID 的细粒度访问控制（例如实现用户级别的 home directory 隔离）。

**技术说明**

Keystone token 中已包含 user ID 字段，实现上只需复用现有函数，将 user ID 注入 policy 环境变量，并通过 `StringEquals` 条件进行匹配。这是一个 RGW 针对 Keystone authentication 的扩展，不影响标准 S3 语义。

**决定**

与会者认为该提案合理，建议将 user ID 条件作为新 commit 追加到当前已开放的 Keystone role PR 中，而非单独开 PR。

## 议题五：S3 vector 内部存储桶的隔离方案

**背景**

S3 vector API 在底层使用普通 S3 bucket 存储向量数据，这些 bucket 属于实现细节，不应对用户可见，包括 vector bucket 的所属用户。

**方案讨论**

讨论了两种主要方案：

1. **独立账户方案**：创建专用账户或用户持有这些内部 bucket，但会导致 quota 统计与实际用户脱节。

2. **子用户 + bucket policy 方案**：在用户账户内创建专用子用户，并通过 bucket policy 阻止包括 root 在内的其他用户访问。但 root 可以修改 policy 绕过限制，存在数据一致性风险。

**最终方向**

Casey 提出利用 tenant namespace隔离：为 S3 vector 保留一个全局专用 tenant，内部 bucket 归属于该 tenant 下，但 quota 和 ownership仍关联到原始用户账户。用户在 `list all my buckets` 时不会看到这些隐藏 bucket，管理员仍可通过 tenant 维度进行管理。

Yuval 认为这一方向更清晰，表示将深入调研，重点关注如何在 `list all my buckets` 响应中过滤掉 vector 相关 bucket，以及如何正确处理 quota 归属。

**内部 S3 操作的身份问题**

讨论明确：向内部 bucket 写入数据时，应以 bucket owner 的身份执行操作，而非发起 S3 vector API 请求的用户身份，以确保 quota 正确归账。后续计划通过 cell 层直接调用（绕过 HTTP 签名），由 Somi 负责推进该实现。

## 议题六：后台进程与 RADOS 驱动解耦

**背景**

S3 vector 引入了一个后台进程用于 re-indexing 和 table optimization，该进程本身与 RADOS 无关，但需要持有 driver 指针。当前 RGW 中的后台进程大多与 RADOS 强绑定，或通过 pause/resume API 订阅 realm reload 通知。

**问题**

若将后台进程放入 `app_main`，realm reload 时driver 指针会被销毁重建，导致后台进程持有悬空指针而崩溃。

**讨论结**

Casey 建议：引入一个包装类，在 realm reload 的 pause/resume 回调中负责销毁并重建后台进程实例，使后台进程本身保持对 RADOS 的无感知。该包装类可以放在 `app_main` 中，不必是 RADOS 专属实现。

Casey 还提到近期有一个 PR 已将 realm reload 逻辑拆分为具体实现与通用接口两层，将分享给 Yuval 参考。Yuval 表示将研究 RGW 前端的 pause/resume 实现，确认是否可以在不引入 RADOS 依赖的前提下完成集。

## 后续行动计划

| 负责人 | 行动项 |
|--------|--------|
| Matthew | 调研基于 lifecycle 的新型 encryption key rotation transition方案 |
| Matthew | 联系 Cloudflare 团队，推动 GCM nonce 使用的安全审查 |
| Matthew | 推进 lifecycle 版本对象批量删除 PR 的社区 review |
| 提案者 | 将 Keystone user ID 条件追加到现有 PR 中 |
| Yuval | 调研 tenant namespace 隔离方案在 S3 vector 中的可行性，重点关注 bucket list 过滤与 quota 归属 |
| Yuval | 研究 RGW 前端 pause/resume 机制，设计后台进程与 realm reload 的解耦方案 |
| Casey | 分享 realm reload 接口拆分 PR 给 Yuval 参考 |
