---
title: "Ceph RGW Refactoring Meeting 2026-01-21"
date: 2026-01-21
updated: 2026-01-26
tags:
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 RGW 重构会议主要围绕两个议题展开：S3 Vectors API 中vector bucket 的实现方案，以及 multisite 测试套件从 boto2 迁移到 boto3 的工作进展。

## 议题一：S3 Vectors API — Vector Bucket 实现方案

### 背景与目标

发言人介绍了正在进行的 S3 Vectors API 实现工作。S3 Vectors API 的顶层实体是 **vector bucket**，它与普通 S3 bucket 有诸多相似之处，但也存在关键差异：

- vector bucket 不包含 objects
- vector bucket 没有 bucket index
- 其余特性如 bucket policy、ownership校验、authentication/authorization、multisite 支持、bucket 创建/删除、bucket 列表等与普通 bucket 类似

实现目标是在尽量减少代码重复的同时，也尽量减少对现有代码的侵入性改动，在两者之间寻求平衡。

### 架构设计

**Cell 层（RGW Cell）**

在 driver 层新增两个函数：
- `load_vector_bucket`：对应现有的 `load_bucket`
- `list_vector_buckets`：对应现有的 `list_buckets`

新增抽象类 `vector_bucket`，作为 bucket cell 类的子集，提供 `create、`remove`、`get_attrs`、`set_attrs` 等接口。

关键设计决策：复用现有的 `bucket_info` 对象，不引入继承或多态。虽然 `bucket_info` 中部分字段对 vector bucket 无意义（如 resharding、layout 等），但复用它极大地减少了其他模块的改动量。未来可能会为 vector bucket 添加 stats/usage 等 admin 功能。

**RADOS 实现层**

- 为 vector bucket 新增独立的 pool，以便存储特性可以独立配置
- 新增 `create_vector_bucket` 和 `delete_vector_bucket` 函数，代码基本从对应的普通 bucket 函数 copy-paste 而来，主要差异在于操作的是 `control.vector_bucket` 而非 `control.bucket`
- bucket controller 同时持有 `bucket` 和 `vector_bucket` 两个对象，避免引入新的多态层级（原 controller 本身无多态行为）

**SVC Bucket 层（`svc_bucket_sobj`）**

该层已有多态设计，因此顺势扩展：

- 新增 `RGWSI_VectorBucket_SObj` 继承自 `RGWSI_Bucket_SObj`
- 主要差异通过 virtual 函数实现：
  - **oid prefix**：vector bucket 使用不同的对象名前缀（如 `vectorbucket.meta`），确保同名的普通 bucket 与 vector bucket 不冲突
  - **cache key**：使用不同前缀（如 `VBI/` 替代 `BI/`）避免缓存混淆
  - **pool**：使用 vector bucket 专属 pool
  - **metadata sync section**：新增独立的 `vector_bucket` section，与 `bucket` section 分开同步

**Metadata Sync 层**

- 复用现有的多态结构，新增 `VectorBucketInstanceMetadataHandler` 继承自现有 handler
- 将两个原本非 virtual 的函数改为 virtual，在派生类中 override 为空操作，因为 vector bucket 没有 bucket index，无需同步 index

**服务初始化**

在 `RGWServices` 的 service definition 中同时注册 `bucket_sobj` 和 `vector_bucket_sobj`，`control.bucket` 返回前者，`control.vector_bucket` 返回后者。

### 集成测试

当前 PR 的集成测试覆盖：
- vector bucket 的创建与删除
- 同名 vector bucket 与普通 bucket 并存
- 各种顺序的删除操作

确保新增功能不干扰现有行为。

### 与LanceDB PR 的关系

vector bucket 是顶层实体，实际的向量存储、索引创建、向量写入、查询搜索等功能由另一个互补 PR 实现（集成 LanceDB）。两个 PR 相对正交，LanceDB PR 不依赖 vector bucket 的内部机制，与 RGW 内部耦合较低。

### 代码注释问题

与会者 Igor 指出新增类缺乏注释，导致需要阅读代码才能理解类之间的差异。发言人认可这一反馈，承诺为新增的类和公共方法补充文档注释。

## 议题二：Multisite 测试 — boto2 迁移至 boto3

### 问题背景

Shelpa 介绍了 multisite 测试套件的现状：Moto 2（boto2）已损坏，相关测试无法正常运行。

### 当前进展

已提交 draft PR，开始将测试从 boto2 迁移至 boto3：
- 对于需要比较 objects 和 buckets 的 zone 文件，改用 S3 resource API
- 测试本身计划改用 S3 client API

欢迎社区成员参与贡献或协助测试。

### 关于迁移至 pytest的讨论

与会者提出是否可以同步将测试框架从 nose 迁移至 pytest（nose 已是停止维护的框架）。

发言人解释了之前尝试 pytest 的障碍：multisite 测试的执行方式较为特殊，测试需要在 teuthology task 内部运行，以便访问 teuthology 的远程 API，从而在不同主机上发出命令。在该环境下无法让 pytest 正常工作，因此目前仍保留 nose。如有兴趣，可以提供相关文件和历史 PR 作为参考。

## 后续行动

- **vector bucket PR**：请感兴趣的开发者审阅 PR 并提交反馈；发言人将为新增类补充代码注释
- **boto3 迁移 PR**：欢迎社区参与，Shelpa 将持续推进迁移工作
- **pytest 迁移**：作为潜在后续工作，需要解决 teuthology 环境下的调用问题
