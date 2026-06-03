---
title: "Closer than you think- Cephs journey to nearest neighbor search"
date: 2026-04-21
updated: 2026-04-21
tags:
  - "Ceph"
  - "对象存储"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
## 概述

本次演讲由 IBM 架构师 Kyle Bader 主讲，介绍了 Ceph 在 object storage 中引入 nearest neighbor search（近邻搜索）能力的工作进展。核心目标是让 Ceph RGW 兼容 Amazon S3 Vectors API，使用户无需额外部署独立的向量数据库系统，即可在 Ceph 集群中存储和检索 vector embedings。

## 背景：什么是 Vector Search

演讲者以 Google Images 为例说明 vector search 的日常应用——用户输入关键词并附加颜色、尺寸等过滤条件，系统返回相似图片，这本质上是一种 hybrid approximate nearest neighbor search。

另一个典型场景是 LM 中的 **Retrieval Augmented Generation（RAG）**：在用户输入 prompt 后，系统通过 vector search 检索相关上下文并注入 prompt，以增强模型推理质量。

**Vector 的基本概念：**
- Vector 是多维空间中的点，每个维度代表某种特征属性（如身高、体重、眼睛颜色等）
- 常见维度数量可达 1024 维（float32 类型）
- Vector 通常由 embedding 模型生成，例如 OpenAI 文本模型或医学影像特征提取模型
- Approximate nearest neighbor search 即在向量空间中找到与查询向量最相似的 top-K 结果

## Amazon S3 Vectors API

2025 年 12 月，AWS 发布了 S3 Vectors，对 S3 进行了扩展：

- 新增 **vector bucket** 类型（区别于普通 bucket）
- 在 vector bucket 内可创建多个 **index**（子容器）
- 支持批量写入 vectors 到指定 index
- 支持 vector query，返回 top-K 相似结果
- 底层存储结构包含 vector 数据、自动构建的索引文件及版本指针

这一设计的优势在于：unstructured data 与对应的 embedings 可以存储在同一系统中，无需额外维护独立的向量数据库。

## Ceph 实现目标

在 Ceph 中实现 S3 Vectors 兼容能力的核心目标：

1. **低成本存储**：无需额外部署 PGVector、Milvus、OpenSearch 等独立系统，利用 Ceph 现有的 replication、erasure coding、high availability 能力
2. **低空间放大率**：index 数据与原始 embedding 数据的空间比不超过 3:1，因此选用 **IVFPQ**（Inverted File Index + Product Quantization）索引格式
3. **零额外基础设施**：作为 RGW 的内置能力，不需要单独运维
4. **低延迟目标**：sub-millisecond 级别的查询响应

## 设计参数

| 参数 | 限制 |
|------|------|
| 每个 vector bucket最大 index 数 | 10,000 |
| 单个 index 最大 embedding 数量 | 十亿级别 |
| Vector 类型 | Dense，float32 |
| 最大 top-K 返回数 | 30 |
| 批量写入限制 | 500 vectors或 20MB，取较小值 |

## 技术选型：向量库评估

团队评估了三个主要的 approximate nearest neighbor 库：

**1. FAISS（Facebook AI Similarity Search）**
- 最成熟、知名度最高
- 缺点：设计上要求将整个 index 加载到内存，在多租户 RGW 场景下内存开销不可接受，被排除

**2. DiskANN**
- 支持 cosine 和 L2（Euclidean）距离度量
- C++ 实现，接口友好
- 缺点：仅提供索引构建能力，hybrid query（含 metadata 过滤）需要自行实现，工作量过大

**3. LanceDB（最终选择）**
- 同时支持 cosine 和 Euclidean 距离
- 使用 IVFPQ 索引，磁盘效率高
- 内置 hybrid search 能力，无需自行实现查询层
- 使用 Rust 编写，通过 Rust FFI（Foreign Function Interface）提供 C bindings，可被 C++ 的 RGW 调用
- 支持 merge-insert（upsert 语义），写入逻辑简洁
- 未来可通过 NVIDIA CUVS 库实现 GPU 加速索引构建

## 架构实现

整体实现分为以下几个层次：

1. **RGW 前端扩展**：新增 S3 Vectors 相关的 API actions、请求解析、条件判断，并与现有 access control 机制集成
2. **请求处理层**：policy 执行、rate limiting、请求路由
3. **向量库集成**：LanceDB 作为嵌入式库加载到 RGW 进程中，负责序列化、索引构建和查询
4. **存储抽象层（zipper）**：通过 RGW 的 zipper 存储抽象层对接 RADOS 后端，同时支持 standalone 文件系统模式；使用 RADOS 时自动获得 replication 和 erasure coding 保护

## Metadata 过滤方案

S3 Vectors API 支持在 query 时附带 metadata 过滤条件（每个 vector 最多 10 个 filterable key）。由于 filterable key 不固定，动态创建列会导致列数无界，团队最终采用 **post-filtering** 方案：

- 查询时将 top-K 扩大若干倍，获取更多候选结果
- 在结果集上进行 metadata 过滤，返回符合条件的 top-K

此外，团队还计划提供扩展能力：在 create index 时可预先声明 scalar schema，若提供了 schema，则为 filterable metadata 创建独立列，从而支持更高效的预过滤查询，同时保持与标准 S3 Vectors SDK 和 AWS CLI 的完全兼容。

## 与 OpenSearch 的定位对比

演讲者明确指出两者是互补关系，而非替代：

| 场景 | 推荐方案 |
|------|------|
| 大规模 embedding 存储 + 偶发查询 + 亚秒级响应可接受 | S3 Vectors（Ceph 实现） |
| 超低延迟（单位毫秒）+ 全文搜索 + 复杂 query DSL | OpenSearch |

## 当前进展与 Demo

演讲现场展示了基于 Rook 部署的 Ceph 集群（minikube 环境）的功能 Demo，通过 AWS CLI 完整演示了以下操作流程：

1. 创建 vector bucket（`movies`）
2. 创建 vector index，指定 float32 数据类型、距离度量和维度数
3. 批量写入 vectors（Star Wars、Aliens、Blade Runner 等电影数据）
4. 列出 index 中的 vectors
5. 执行 get vectors 操作
6. 执行 query vectors，返回 top-3 相似结果
7. 依次删除 vectors、index、vector bucket

**当前实现状态：**
- 前端请求处理已完成
- IAM policy actions 已添加到语法，enforcement 部分仍在实现中
- 认证（authentication）已就绪，基于 bucket/identity policy 的授权（authorization）仍在开发
- 存储抽象层的最终对接工作进行中
- 已提供开发版容器镜像供实验使用

## 配置与资源管理

- S3 Vectors 功能需在 RGW 配置中显式启用（类似 IAM、STS 的启用方式），默认不开启
- 建议为运行 S3 Vectors 的 RGW 配置更多 CPU 和内存
- 可将 S3 Vectors 部署在独立的 RGW 实例集合上，与常规 S3 流量隔离
- 索引更新为异步后台操作，不阻塞 put vector 写入路径；新写入的 vectors 在索引合并前通过 brute-force 方式参与查询

## Q&A 要点

- **GPU 加速**：当前索引构建基于 CPU（x86 SIMD 指令），未来可探索通过 CUVS 支持 CUDA GPU 加速，类似 RGW 的 GC/lifecycle 后台任务模式
- **兼容性动机**：Ceph object storage 的一贯目标是跟进 S3 新特性，保证用户可以将 AWS应用直接迁移到 Ceph
- **数据持久性讨论**：会后 Q&A 中讨论了 Ceph 的 durability 与 availability 的区别，Ceph 在 CAP 定理中优先保证 consistency，被描述为"悲观型"集群（pessimistic），会积极触发数据修复
