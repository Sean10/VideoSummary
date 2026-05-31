---
title: Ceph RGW Refactoring Meeting 2025-12-10
date: 2025-12-10
updated: 2025-12-10
tags:
- RGW
categories: 
- 视频总结
subtitle: Ceph_RGW_Refactoring_Meeting_2025-12-10
---

## 会议概述

本次 Ceph RGW Refactoring Meeting 于 2025 年 12 月 10 日举行，主要围绕 RGW 账户迁移过程中的对象所有权（object ownership）变更、ACL 处理逻辑以及相关测试覆盖展开讨论。

## 主要议题

### 1. 账户迁移测试覆盖（Put Object测试）

Casey 正在编写一个 shell 脚本，用于自动化执行已文档化的用户到账户（user-to-account）迁移流程。该脚本计划集成到 Teuthology 测试框架中，以提供回归测试能力，并为后续新增测试用例奠定基础。

Kronel 表示此前在查阅相关脚本时未能找到账户迁移相关内容，Casey 的工作正好填补了这一空白。

### 2. 节假日会议安排

Casey 建议在节假日期间取消部分例会，下周的会议照常进行，之后两周暂停。

### 3. Bucket Chown 与对象所有权变更（核心议题）

讨论围绕 Casey 提交的第二个 PR 展开，该 PR 涉及在 bucket chown 操作时同步变更 bucket 下所有对象的所有权。

**背景说明：**

- `radosgw-admin bucket chown` 命令原本已支持变更 bucket 的所有权，新 PR 进一步将变更范围扩展到 bucket 下的所有对象（包括对象的 ACL）。
- 在最初设计账户迁移方案时，出于对生产系统中可能存在数百万对象的性能考量，迁移流程刻意只修改 bucket 所有权，而不修改对象所有权。

**两个 PR 的定位区别：**

- `radosgw-admin bucket chown`：面向集群管理员（cluster admin/operator），由管理员主动触发所有权变更。
- Casey 的新 PR：允许 S3 客户端自行修复其 bucket 的所有权问题。

两者服务于不同的使用场景，均有其价值。

### 4. 跨账户访问与 ACL 兼容性问题（重要发现）

讨论中揭示了一个此前未充分考虑的问题：

**问题描述：**

在账户迁移完成后，bucket 的所有权已变更为 account，但 bucket 下的对象所有权仍归属于原始的旧 UID（user ID）。当账户下新增其他用户（如 STS 用户、临时用户或普通用户）时，这些用户尝试访问带有旧 UID 所有权的对象时，RGW 的 authorization逻辑会将此类请求判定为跨账户（cross-account）请求，从而导致访问被拒绝。

**根本原因：**

RGW 使用旧式 canonical UID 命名规范标记对象所有者，迁移后 bucket 归属于 account，但对象的 owner 字段仍为旧 UID，两者不匹配，触发跨账户策略评估逻辑。

**可能的解决方案：**

1. 使用 `bucket chown` 命令批量修改所有对象的所有权（但对大规模生产系统代价较高）。
2. 为相关用户配置显式的 bucket policy，授予访问权限（但目前不确定是否存在适用的 policy配置）。
3. 利用 main 分支已有的 **S3 Object Ownership** 特性，在迁移前先禁用对象 ACL（object ACLs），再执行迁移——但此方案对 Squid 和 Tentacle 版本无效，且对已有 ACL 的对象行为需进一步验证。

**代码层面的补充说明：**

当前 RGW 代码实现中，即使对象没有显式 ACL，代码也会自动创建一个默认 ACL，将当前用户设为 owner 并进行验证。因此，当 requester 与 owner 一致时，访问始终被允许；问题出现在 requester 与 owner 不一致的跨用户场景。

### 5. AWS 行为对比验证

与会者建议通过对比 AWS 的实际行为来验证上述逻辑：

- AWS 本身不存在 UID 与 account ID 分离的概念，bucket 默认归属于创建者的账户。
- 需要验证的场景：当 bucket 属于某账户，而 bucket 内的对象由另一个账户上传时，bucket owner 发起的对象访问请求，AWS 是否会将其判定为跨账户请求。
- 该场景是 RGW 账户迁移特有的问题，AWS 原生不存在此类迁移需求。

## 决定事项

1. Casey 的账户迁移 shell 脚本将集成到 Teuthology，作为回归测试基础。
2. Kronel 将验证账户内新增用户访问旧 UID 所有权对象的实际行为，并与 AWS 行为进行对比测试。
3. 上述测试用例将纳入账户迁移的 QA 测试矩阵中。

## 后续行动计划

| 负责人 | 行动项 |
|--|--|
| Casey | 完成账户迁移 shell 脚本并提交至 Teuthology |
| Kronel | 验证账户内多用户访问旧 UID 对象的行为，对比 AWS 实际表现 |
| 全体 | 评估 S3 Object Ownership 特性在迁移流程中的适用性 |

## 小结

本次会议深入探讨了 RGW 账户迁移中对象所有权变更的必要性与复杂性。核心结论是：在多用户账户场景下，仅迁移 bucket 所有权而不迁移对象所有权，可能导致账户内其他用户无法访问已有对象，这一问题需要通过 `bucket chown`、显式 policy 或禁用 ACL 等方式加以解决，具体方案有待进一步测试验证。
