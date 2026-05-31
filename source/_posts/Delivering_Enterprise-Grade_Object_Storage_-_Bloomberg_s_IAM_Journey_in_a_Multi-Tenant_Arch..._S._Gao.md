---
title: Delivering Enterprise-Grade Object Storage- Bloomberg’s IAM Journey in a Multi-Tenant Arch... S. Gao
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 对象存储
categories: 
- "视频总结"
subtitle: Delivering_Enterprise-Grade_Object_Storage_-_Bloomberg_s_IAM_Journey_in_a_Multi-Tenant_Arch..._S._Gao
---

### **Ceph 会议纪要 - Bloomberg 企业级对象存储实践**

#### **会议基本信息**
- **演讲人**：Asan（Bloomberg）
- **主题**：Bloomberg 基于 Ceph 构建的企业级多租户对象存储实践
- **关键词**：Ceph, RGW, multi-tenancy, IAM, Squid, QoS, S3 compatibility

#### **Bloomberg 背景与 Ceph 规模**
- Bloomberg 作为全球金融科技公司，每日处理海量金融数据。
- 使用 Ceph 构建 10 个集群，覆盖多个数据中心，最大单集群拥有 4500 个 OSDs，存储容量达 77PB。
- 提供统一 S3 兼容对象存储（RGW）和块存储（RBD）服务。

#### **多租户模型设计与挑战**
- **核心需求**：资源隔离、策略管控、透明性、权限管理。
- **实现方案**：租户映射、自研 UI 管理系统、预定义角色。
- **IAM 集成**：过渡到 Account 模型、控制平面与数据平面分离。

#### **Squid 版本迁移与 IAM 集成**
- **迁移目标**：临时凭证、身份联邦。
- **迁移挑战**：兼容性问题、无缝迁移。
- **IAM 功能落地**：临时凭证优势、控制限制。

#### **性能与安全优化**
- **QoS 层**：自研全局流量控制。
- **监控**：租户级实时指标、自动化测试集群。
- **安全**：全链路 HTTPS、静态加密、跨数据中心容灾。

#### **问答环节重点**
- **容器化部署**：当前为裸金属集群，但控制平面与 Ceph 解耦。
- **延迟影响**：STS 凭证性能与长期凭证相当，部分场景更优。
- **元数据库**：使用 PostgreSQL + Airflow 自动化，未出现瓶颈。
- **权限检查**：IAM 策略通过标准 S3 协议处理，无额外延迟层。

#### **后续行动计划**
- **IAM 完善**：逐步开放 `Condition` 和 `Deny` 策略支持。
- **身份联邦**：集成 Bloomberg SSO（OIDC）。
- **工具链**：发布内部认证的 S3 客户端库。
- **问题修复**：跟踪 Squid 社区 PR。

#### **总结**
Bloomberg 通过 Ceph RGW 构建了金融级对象存储服务，实现了多租户隔离、IAM 精细化管控和自动化运维，满足了海量高安全性需求。