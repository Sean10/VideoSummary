---
title: Enhancing Ceph for Infinite Scalability at LINE - Jinmyeong Lee & Sungjoon Koh, LINE Plus
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 可扩展性
- 分布式存储
- 对象存储
- 存储优化
categories: 
- "视频总结"
subtitle: Enhancing_Ceph_for_Infinite_Scalability_at_LINE_-_Jinmyeong_Lee_Sungjoon_Koh_LINE_Plus
---

## 会议概览
在Sephalocon 2025技术分享会上，LINE公司的存储架构师Lee和Sunjun分享了如何通过构建多层架构解决Ceph RGW的单集群扩展限制。

## 关键技术背景
LINE公司在运营中遇到了Ceph RGW的单集群容量限制、缺乏高级监控/认证功能以及与Yahoo Japan合并后引入的Dragon存储系统（高性能S3兼容）等挑战。

## 架构创新
- **路由层(Router)**：通过bucket location map实现请求路由，支持多子集群统一端点暴露，扩展Create Bucket API支持存储类标识。
- **迁移系统**：候选选择器(Candidate Selector)基于时间局部性特征选择迁移目标，迁移API设计保留所有属性，Arclone定制化实现迁移。

## 加密增强方案
建议增加AES-CTR支持，AES-GCM主密钥加密，HMAC-based SSE-C密钥验证，处理Dragon(AES-CTR)与Ceph(AES-CBC)的差异。

## 生产部署
迁移工作流包括MongoDB状态更新、FaaS触发迁移、Arclone执行和验证+源端清理。性能保障方面，迁移流量与生产流量隔离，异步迁移不影响CRUD操作。

## 后续行动计划
- 社区贡献：提交加密增强方案，开发分层存储框架提案。
- 优化方向：Fast List机制深度优化，存储类与AWS标准的兼容性改进。
- 协作计划：参与上游Ceph社区会议，探讨存储类transition机制的协同方案。

## 会议结论
LINE通过构建router抽象层和智能迁移系统，实现了Ceph与Dragon存储的优势互补，在保持S3兼容性的同时突破单集群限制，提高了性能与成本优化效益。