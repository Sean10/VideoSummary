---
title: Ceph RGW Refactoring Meeting 2026-04-15
date: 2026-05-13
updated: 2026-05-14
tags:
- RGW
- 加密
categories: 
- 视频总结
subtitle: Ceph_RGW_Refactoring_Meeting_2026-04-15
---

## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2026 年 4 月 15 日举行，主要议题涵盖 GCM 加密 PR 审查、生命周期转换中的 recompression 支持、压缩对象的 deduplication 设计讨论、版本化 bucket 中的 lifecycle 一致性问题，以及全局 OIDC 提供者方案探讨。

## 议题一：GCM 加密 PR 与生命周期 Recompression（Matthew）

### GCM 加密 PR

Matthew 汇报了两个待审查的 PR。第一个是 GCM 加密相关 PR，Marcus 已提出若干评论，Matthew 已回应并提交了新的 commit。

主要争议点在于 Marcus 希望支持更大的 block cipher尺寸（如 512 或 1024 位），而非仅支持 128/256 位。Matthew 对此持保留意见，原因是 NIST 标准目前并不认可 AES-512 等更大的 block size，偏离 NIST 标准意味着使用非官方实现，存在合规风险。Matthew 表示需要更多社区成员参与 review。

### 生命周期转换中的 Recompression PR

第二个 PR 针对通过 lifecycle 在 storage classes 之间进行对象转换时的 recompression 支持。该 PR 同时支持 encryption 和 compression，复用了 copy object 的现有逻辑，通过一个小的 shim 层使 transition 和 copy object 均可调用。

当前该 PR 被若干依赖 PR 阻塞，这些依赖 PR 涉及 encrypted 与 compressed 对象的处理问题，需等待其合并后方可推进。

Casey 表示会跟进 lifecycle transition 部分的 review，并指出 compression base class 与 encryption 关注点混杂的问题值得改进。

## 议题二：压缩对象的 Deduplication 设计（Gabriel）

Gabriel 就压缩对象的 deduplication 方案提出了若干设计问题：

**跨压缩/非压缩对象的 dedupe**

- 是否应允许在 compressed 与 uncompressed 对象之间进行 dedupe？
- 若允许，应保留哪个副本（compressed 还是 uncompressed）？
- 讨论结论：以 storage class 当前配置的压缩策略为准，若 storage class 配置了压缩则保留 compressed 版本，否则保留 uncompressed 版本。

**跨压缩算法的 dedupe**

- 同一 storage class 可能先后使用不同的压缩算法，历史对象与新对象的算法可能不同。
- 讨论结论：增量 dedupe 场景下，允许 best-effort 处理，不强制保证所有对象都使用最新算法，以降低实现复杂度。

**加密与 dedupe 的交互**

- 跨 bucket 的 dedupe 在不同 bucket 使用不同 encryption key 时存在困难，因为 bucket 删除后 key 也随之消失，dedupe 引用可能失效。
- 讨论认为跨 bucket 的加密 dedupe 问题复杂，暂不在当前范围内解决。

Gabriel 总结：采用 best-effort 策略，以 storage class 当前策略为准，增量 dedupe 不做强制保证，社区表示认可。

## 议题三：Tentacle 版本 Backport 状态（Boris）

Boris 询问两个 bug fix 何时会进入 Tentacle 版本：

1. **SSE 对象 copy 时需要 re-encryption 的问题**
2. **lifecycle policy 未被删除的问题**

关于第二个问题，backport 已完成并合并，tracker 显示 fixed in 20.0.0，应已包含在初始 Tentacle 发布中，Boris 需重新验证。

关于第一个问题（server-side copy with encryption），该 feature 已合并到 main，但存在若干后续修复尚未完成。由于项目缺乏密码学专家（整个项目只有两人具备相关能力），所有涉及 cryptography 的工作都需经过这两人审查，进展较慢。

结论：需等待 compressed 与 encrypted 对象的 copy 相关 PR 全部合并并通过 QA 测试后，才能考虑 backport 到 Tentacle。Matthew 承诺当天更新 tracker，标注阻塞依赖关系。若无法赶上 Tentacle，则需等待下一个大版本 Umbrella。

## 议题四：Lifecycle 与版本化 Bucket 一致性问题（Igor）

Igor 汇报了对内部集群进行 bucket index scan 后发现的三类数据一致性问题：

1. **对象最新版本不是 current version**（latest 标记指向非当前版本）
2. **同一对象存在多个 current version**
3. **对象没有任何 current version**（所有版本均为 non-current）

这些不一致状态可能导致 lifecycle 执行错误操作，例如误删所有版本或对无 current version 的对象执行错误的清理逻辑，存在数据丢失风险。

**解决方案**

Igor 提出在 LC RBJ list 类中注入检测逻辑，当发现上述不一致状态时，跳过该对象并记录日志，不执行任何 lifecycle 规则，以防止数据丢失。同时允许 lifecycle 继续处理状态正常的对象，避免 bucket 无限膨胀。

PR 正在从内部分支向上游 main 分支移植，预计当天或次日发布，届时会在 Slack 频道通知。

**根因调查**

Matthew 提到 tracker #73539 中 Cornell 提交的 PR 涉及 delete marker 早期过期问题，可能与部分不一致现象相关，但无法解释全部情况。

Igor 指出，部分 bucket 的数据已存在多年，某些 latest 版本比 current 版本新出数年，无法单纯用 RGW 竞态条件解释，multi-site 环境可能是重要因素。

Casey 建议可通过 unit test 构造竞态场景并手动传入 epoch 来建立 reproducer，Igor 表示会跟进。

**现有工具**

讨论中提到 object re-index、check-olh 等工具可能有助于修复部分不一致状态，但目前没有统一的修复工具。建议后续考虑开发管理员可用的修复命令。

## 议题五：全局 OIDC 提供者方案（Krunal）

Krunal 提出在 RGW 中支持全局 OIDC 提供者的需求，背景来自 Bloomberg 作为企业用户管理大量账户的实际场景。

**当前问题**

OIDC 目前绑定到具体账户，每个账户需单独调用 create OIDC 接口。企业场景下，管理员希望配置一个全局 OIDC，所有账户均可直接使用，无需重复创建。

**参考 AWS 实现**

AWS 内置了 Google、Amazon、Facebook 等 OIDC 提供者，用户无需调用 create OIDC 即可直接使用这些 URL 进行 Assume Role with Web Identity。

**设计思路**

Krunal 提出在存储 OIDC 时，将 account字段设置为特殊值（如 "global"）来标识全局 OIDC。在 Assume Role 流程中，RGW 先查找账户级别的 OIDC，若未找到则 fallback 到全局 OIDC。这样无需修改 STS/S3 API 接口，对调用方透明。

全局 OIDC 的创建权限仅限管理员，可通过 RadosGW admin API 或 ceph-dashboard 进行配置。

Casey 提到 ceph-users 邮件列表中有用户希望将 ceph-dashboard 的 OIDC 配置与 RadosGW 打通，全局 OIDC 方案可以支持这一场景。

**后续行动**

Krunal 将把设计提案发布到 RGW dev Slack 频道并tag Preetha（该领域专家）征求反馈。

### 附：持久化通知队列计数器 Bug

Krunal 还提到 ceph-users 邮件列表中有用户反馈持久化通知在 Reef 升级到 Tentacle 后出现问题。

根因分析：持久化通知中的 reservation 计数器从未被重置，持续累加。CLS queue 的上限为 128MB，当计数器值超过 1.28 亿时，系统会误判队列已满，导致无法发送通知。

但 Casey 指出，用户报告的错误是 EINVAL（解码异常），而非 ENOSPC（空间不足），更可能是 Reef 到 Tentacle 升级过程中的数据结构兼容性问题（包含 Squid 的重大变更）。Casey 将尝试复现该升级路径下的问题并跟进。

## Teuthology 测试套件状态更新

Casey 汇报了 RGW teuthology 测试套件的最新状态：

- Valgrind 问题修复 PR 已获批准，等待合并，合并后 RGW verify suite 将恢复绿色
- multi-site 和部分 notification 测试仍存在失败
- 另有一个修复 pubsub topic 创建时未初始化字段的 Valgrind PR 正在测试中，Yuri 已运行完整 RGW regression，发现约 4 次重跑，请求社区协助确认是否为已知问题

建议将测试结果和问题讨论发布到 RGW QA 或 RGW devel Slack 频道。

## 后续行动计划

| 负责人 | 行动项 |
|-----|--------|
| Matthew | 更新 Tentacle backport tracker，标注 server-side copy 的阻塞依赖关系 |
| Matthew | 跟进 GCM 加密 PR 和 lifecycle recompression PR 的 review |
| Casey | 跟进 lifecycle transition PR 的 review，关注 compression/encryption 关注点分离 |
| Igor | 完成 lifecycle 一致性保护 PR 的冲突解决并发布，在 Slack 通知社区 |
| Igor | 与 Casey 合作，通过 unit test 构建OLH 竞态 reproducer |
| Krunal | 将全局 OIDC 设计提案发布到 RGW dev Slack 并 tag Preetha |
| Casey | 复现 Reef 到 Tentacle 升级后持久化通知 EINVAL 问题 |
| Yuri | 将 RGW regression 测试结果发布到 RGW QA 频道 |
