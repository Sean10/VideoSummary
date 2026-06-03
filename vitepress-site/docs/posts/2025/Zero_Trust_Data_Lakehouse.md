---
title: "Zero Trust Data Lakehouse"
date: 2025-06-24
updated: 2025-06-24
tags:
  - "分布式存储"
  - "Ceph"
categories:
  - "视频总结"
outline: deep
---
会议纪要中提到了Ceph分布式存储在零信任Lakehouse架构中的应用，以下是会议的关键点：

1. **Ceph对象存储的优势**：
   - 高扩展性与高可用性；
   - 支持结构化/非结构化数据，如Parquet、多模态嵌入数据；
   - 企业级特性，包括加密、Kafka/Knative集成、对象日志等。

2. **Lakehouse架构挑战**：
   - 数据治理问题，特别是多引擎访问同一数据集时的权限管理；
   - 零信任需求，包括防止数据泄露、存储层统一认证；
   - 性能与扩展性，避免代理成为瓶颈。

3. **Polaris Catalog解决方案**：
   - Catalog凭证分发，使用临时STS Token，基于最小权限；
   - 细粒度访问控制，包括表级权限和命名空间隔离。

4. **演示环节**：
   - Terraform自动化部署，创建S3 Bucket、IAM策略、Polaris Catalog；
   - Spark与Trino测试，展示用户权限管理。

5. **决策与行动计划**：
   - 技术方向，推动Ceph RGW与Polaris Catalog深度集成，优化STS Token审计日志；
   - 发布Ceph Lakehouse红皮书，提供实际用例与部署指南；
   - 社区合作，增强RGW对分析负载的支持。

6. **用户建议**：
   - 迁移HDFS到Ceph对象存储（通过S3A连接器）；
   - 使用Polaris Catalog实现跨团队数据共享。

会议强调了Ceph在构建高可用、高扩展性的Lakehouse架构中的关键作用，并讨论了如何通过Polaris Catalog实现零信任安全模型下的数据治理和访问控制。会议还展示了如何使用Terraform自动化部署和测试不同的数据查询引擎，以确保系统的性能和安全性。