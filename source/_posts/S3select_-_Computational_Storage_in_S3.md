---
title: "  S3select: Computational Storage in S3  "
date: 2022-11-14
updated: 2022-11-15
tags:
- [S3 Select]
- [数据存储]
- [SQL查询]
- [性能优化]
- [AWS服务]
categories:
- "视频总结"
subtitle: S3select_-_Computational_Storage_in_S3
---
Gar Salomon 在会议上介绍了 S3 Select 的概念、工作原理、优势以及未来的发展方向。S3 Select 是 AWS S3 的一种新能力，允许客户端将 SQL 语句推送到存储层，从而只提取所需的数据，提高性能并降低成本。

### 会议内容概述

1. **S3 Select 简介**
   - 引入时间：2020年7月
   - 功能：允许客户端推送 SQL 语句到存储层
   - 优势：提高性能，减少成本

2. **为什么需要 S3 Select**
   - 传统方法：数据移动到操作地点
   - S3 Select 方法：操作推送到数据附近
   - 优势：减少内存消耗，优化大数据生态系统

3. **S3 Select 的工作原理**
   - 集成到 GET 对象模型中
   - 对象被获取并由 S3 Select 模型处理每个片段
   - 支持格式：CSV, JSON, Parquet

4. **SQL 在机器学习中的作用**
   - SQL 是处理数据的主要语言
   - 数据必须格式化以供机器学习算法使用

5. **S3 Select 的软件设计特点**
   - 引擎设计：头文件代码，单文件函数，内存高效使用
   - 数据类型处理：不同数据类型的读取器与 SQL 引擎解耦

6. **数据类型处理流程**
   - CSV：简单格式，不支持数据类型
   - JSON：支持数据类型和模式
   - Parquet：高级对象，包含元数据，支持直接访问特定数据

7. **并行处理和优化**
   - 通过分割数据范围并行处理查询
   - 未来可能集成到 Spark, Presto 等分析应用中

8. **验证和测试**
   - 表达式生成器：生成复杂表达式以验证引擎
   - SQL 生成器：生成复杂 SQL 语句以测试系统

9. **未来工作**
   - 集成 S3 Select 到 Spark, Presto 等分析应用中
   - 优化方向：作为优化器，提高查询性能

10. **开发和测试**
    - 继续开发和测试 S3 Select 的功能
    - 探索与现有分析应用的集成可能性

### 关键词保留

- [S3 Select]
- [数据存储]
- [SQL查询]
- [性能优化]
- [AWS服务]
- [Parquet]
- [CSV]
- [JSON]
- [Spark]
- [Presto]

### 改进点

- 原总结中缺少了对数据类型处理流程的详细描述，如 CSV、JSON 和 Parquet。
- 原总结中未提及 S3 Select 的软件设计特点，如头文件代码和单文件函数。
- 原总结中未提及 S3 Select 的验证和测试方法，如表达式生成器和 SQL 生成器。
- 原总结中未提及 S3 Select 的未来工作，如集成到 Spark 和 Presto。