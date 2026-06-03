---
title: "Ceph RGW Refactoring Meeting 2026-02-11"
date: 2026-02-11
updated: 2026-02-19
tags:
  - "RGW"
  - "去重"
  - "加密"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 RGW Refactoring Meeting 主要围绕两个核心议题展开：一是 Gaby 提出的 DDUP（数据去重）与 server-side encryption 结合的设计问题；二是 Matthew 介绍的 AES-256-GCM 加密模式支持 PR。

## 议题一：DDUP 与 Server-Side Encryption 的结合

### 背景与问题

Gabby 正在实现 DDUP 功能，并希望支持对 server-side encryption 对象进行去重。核心问题有两个：

1. 是否应该允许加密对象与未加密对象之间进行 DDUP？
2. 是否可以在已有 E tag（MD5 of clear data）的基础上，额外添加一个更强的 hash（如 SHA 或 BLAKE）用于去重判断？

### 加密模式分析

会议讨论了 RGW 支持的几种 server-side encryption 模式：

- **SSE-S3（AES-256 模式）**：服务端管理密钥，E tag 为明文数据的 MD5，Amazon 已将此模式设为所有 bucket 的默认行为。
- **SSE-KMS**：客户端可指定 KMS key ID，E tag 同样为明文数据的 MD5。
- **客户端提供密钥（SSE-C）**：密钥由客户端提供，E tag 为加密数据的 hash，无法直接用于去重。

关键结论：SSE-S3 和 SSE-KMS 的 E tag 均为明文数据的 MD5，因此服务端可以通过 E tag 判断两个对象是否极有可能相同，这为 DDUP 提供了基础。

### 安全性讨论

与会者讨论了 DDUP 是否会引入额外的安全风险：

- SSE-S3 的 E tag 本身就是明文 MD5，任何有 bucket 读权限的用户已经可以通过 E tag 推断两个对象是否相同。
- DDUP 操作本身不会暴露更多信息，因为 E tag 已经提供了等价的信息。
- SSE-S3 的设计目标是保护静态数据（data at rest），防止物理磁盘被盗后数据泄露，而非端到端加密（end-to-end encryption）。

### 跨 bucket DDUP 的限制

讨论中发现跨 bucket 进行加密对象 DDUP 存在关键问题：

- SSE-S3 使用 per-bucket key（每个 bucket 独立的加密密钥）。
- 如果将 tail object 链接到另一个 bucket 的对象，当原始 bucket 被删除时，对应的加密密钥也会被删除，导致数据无法解密。
- 虽然理论上可以通过引用计数（ref count）来 pin 住加密密钥，但这会给非 DDUP 代码路径增加额外开销，不值得。

**结论**：当前阶段，加密对象的 DDUP 只在同一 bucket 内进行，跨 bucket 的加密 DDUP 暂不支持。

### 强hash 的必要性

Gabby 提出需要在 E tag（MD5）之外额外存储一个强 hash（SHA 或 BLAKE）：

- MD5 不具备密码学安全性，理论上可以构造碰撞。
- 强 hash 可以作为长期属性保留，未来可用于 multi-site sync 优化：在同步时通过比对强 hash 跳过已有数据的传输。
- 该 hash 不会暴露给 S3 客户端，仅作为内部属性存储。

与会者对此基本认可，认为不会带来显著安全风险。

### 实现路径

- 当前优先实现 SSE-S3 模式下同 bucket 内的 DDUP。
- DDUP 依赖 split head 功能完成后才能完整实现（split head 使head object 不再包含嵌入数据）。
- SSE-KMS 模式的 DDUP 支持留待后续，需要进一步确认 E tag 是否为明文 hash。
- 跨 bucket 加密 DDUP 的 key pining 方案留待 per-bucket DDUP 验证可行后再评估。

## 议题二：AES-256-GCM 加密模式支持

### PR 概述

Matthew 介绍了为 RGW server-side encryption 添加 AES-256-GCM 支持的 PR，主要特点：

- GCM 是一种 **size-changing cipher**（认证加密后数据大小会变化），因此需要修复大量假设加密前后数据大小不变的代码，包括 content length计算、offset 追踪等。
- 新增三个 head object 属性，用于记录明文大小（plain text size）和原始大小。
- GCM 的核心优势：任何数据损坏或密钥错误都会立即触发 authorization denied，提供完整性保护。

### 测试情况

- 通过了 Teuthology workload 测试。
- 通过了 RGW verify suite、crypt suite 和 multi-site suite。
- multi-site suite 中发现一个问题，确认为 main分支已有问题，与本 PR 无关。

### PR 规模与设计

- PR 约新增 3600 行代码，主要为单元测试和新的 GCM crypto 类。
- 采用通抽象设计，未来添加其他 size-changing cipher（如 ChaCha20）只需新增对应加密类，现有的 size handling、range request 和 multipart 机制均可复用。
- QAT 硬件加速的 stub 已添加，但完整实现尚未完成，不影响代码审查。
- 新模式标识为 `AES-256-GCM`，与现有 `AES-256`（CBC）模式并列。

### 与 DDUP 的关系

- 当前 DUP 实现应先聚焦 CBC 模式，GCM 模式的 DDUP 支持留待后续。
- 需要 Marcus 和 Matt 进行深度代码审查，建议在 Slack 频道发起 review 请求。

## 后续行动

| 负责人 | 行动项 |
|--|--|
| Gabby | 确认 SSE-KMS 模式下 E tag 是否为明文 MD5 |
| Gabby | 先实现同 bucket 内 SSE-S3 对象的 DDUP，验证可行性 |
| Gaby | 与 Marcus 讨论跨 bucket 加密 DDUP 的 key pinning 设计 |
| Matthew | 在 Slack 频道发起 GCM PR 的 review 请求 |
| Matthew | 后续完成 QAT 硬件加速支持 |
