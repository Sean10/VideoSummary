---
title: Ceph Dashboard Roadmap
date: 2026-04-02
updated: 2026-04-03
tags:
- 分布式存储
- 监控
- RGW
categories: 
- 视频总结
subtitle: Ceph_Dashboard_Roadmap
---

## 演讲背景

本次演讲来自 Ceph India 社区活动，由 IBM 的 Ceph dashboard 团队成员 Naman 和 Nisam 共同主讲。Nisam 是 IBM 高级软件工程师，在 Ceph dashboard 领域有六年经验，曾担任 dashboard 团队的 component leader。本次分享围绕 Ceph dashboard 的现状、Tentacle 版本新特性、未来规划以及现场 demo 展开。

## 当前 Dashboard 能力概览

Ceph dashboard 目前已是一个功能完整的管理与 monitoring UI，主要能力包括：

- 多用户与角色管理（multi-user and role management）
- Single Sign-On（SSO）支持
- SSL/TLS 加密
- 审计（auditing）与国际化（internationalization）
- 统一 authentication 与 authorization
- 集中式日志（centralized logging）
- 集中式通知页面（centralized notification page，新引入）

首页 overview 面板涵盖 inventory 状态、capacity、cluster 利用率及集群详情等核心信息。

## Tentacle 版本新特性

### Multicluster Dashboard

新增独立的 multicluster 管理视图，支持跨集群的添加、删除、编辑操作，可在下拉菜单中快速切换集群，并统一查看 capacity、throughput、IOPS 及 alerts。

### 安全增强：OAuth2 SSO

集成 management gateway，基于 OIDC 协议实现现代化 SSO，支持 MFA（多因素认证），提供统一的集群服务入口，安全性显著提升。

### SMB 管理

新引入 SMB 管理功能，提供便捷的 SMB cluster 创建与管理界面，支持：
- 创建 standalone 用户或 Active Directory 接入
- 创建、修改、删除 SMB cluster 及 shares
- 集成 Grafana overview dashboard

### RGW 对象存储增强

**Multi-site 自动化**：利用 multicluster 配置实现跨集群数据 replication，提供向导式（wizard）UI 流程，支持从零创建新的 multi-site 配置，也支持将现有配置转换为对象 replication。对于未配置 multicluster 的 standalone 场景，提供 token 导入机制。

**Notification Destination**：支持对接 Kafka 或AMQP 等外部服务，可针对 bucket 事件（对象创建、删除等）配置通知规则。

**Storage Class 管理**：支持 cloud S3、cloud S3 Glacier、local 三种 storage class 类型，可通过 dashboard 创建 storage class 配置，并结合 bucket tiering（生命周期策略）实现对象在不同 storage tier 之间的自动 transition。

**用户账户管理（Accounts）**：新增 RGW account 管理，支持创建 account、将用户关联至 account（root 用户或普通用户）、将 bucket 关联至 account，bucket 所有权自动转移至 account。

### NVMe-oF TCP 管理

按照最新 Carbon Design System 规范完整重构 NVMe TCP 管理界面，UI 更加规范美观，并引入新的 NVMe 向导式配置流程。

### Scalability 与 performance 优化

这是本版本的重要改进方向：
- 优化 API 与网络效率，按需加载前端资源
- 减少脚本执行时间（scripting time）与渲染时间
- **LCP（Largest Contentful Paint）从 9.82 秒降至 2.11 秒**，达到 2.5 秒以内的 performance 基准，是 dashboard 团队的重要里程碑

### Carbon Design System 迁移

持续将 dashboard 组件从 Bootstrap 迁移至 Carbon Design System，遵循统一的 UX 规范，提升界面一致性与可用性。

### Grafana 监控集成

新增多个 Grafana 监控 dashboard：
- Multicluster monitoring
- SMB overview
- CephFS overview
- NVMe overview 及 NVMe performance
- Multi-site（应用层）overview
- S3 analytics dashboard

## 未来规划

### 持续进行中

- Carbon Design System 迁移：继续将现有 Bootstrap 组件迁移至 Carbon
- REST API 文档完善：补充响应格式说明等缺失文档
- OAuth2 management gateway推广：逐步废弃旧的 SSL配置方式，提供迁移指引

### 新 Overview 页面

基于用户调研反馈，UX 设计师重新设计了 overview 页面，将包含：
- 数据弹性（data resiliency）展示，即 PG 状态与数据健康度
- 容量消耗趋势（consumption trends）及预测
- 性能统计（performance stats）
- 系统 alerts 增强展示
- PG 活动专属区域

### CephFS Mirroring

引入 CephFS mirroring 功能，补齐 block（RBD）和 RGW multi-site 已有 mirroring 能力的空白，利用 CephFS mirroring 模块实现文件系统级别的数据镜像。

### 对象管理视图

提供 RGW bucket 内对象的浏览、上传、删除功能，实现对象级别的管理视图。

### RGW 用户管理增强

- 改进 IAM policies 管理
- 计划将 dashboard 用户与 RGW 用户打通，实现登录后仅查看对应 RGW 用户的 bucket，而非全局 admin 视图

### Archive Zone配置

支持将 zone 标记为 archive zone 的配置功能。

### NVMe 向导流程持续优化

根据用户反馈持续改进 NVMe 配置向导，提升端到端配置体验。

## Demo 要点回顾

现场 demo 覆盖以下流程：

1. **SMB 管理**：创建 Active Directory 模式和 standalone 用户模式的 SMB cluster，创建 share 并关联 CephFS volume，演示 subvolume 配置
2. **RGW Accounts管理**：创建 account，创建 root 用户与普通用户，演示 IAM policy（S3 read-only vs S3 full access）对 bucket 操作的权限控制，演示 bucket 与 account 的关联
3. **Bucket Notification**：配置 Kafka notification destination，创建 bucket notification 配置，上传对象后在 Kafka UI 中验证通知消息接收
4. **Storage Class 与 Tiering**：创建 cloud S3 storage class，配置生命周期规则（lifecycle rule），观察对象从源集群 transition 至目标集群的完整流程

## 联系与参与

团队通过 Ceph 上游社区渠道（IRC、邮件列表等）接受问题反馈，欢迎社区成员参与 Ceph dashboard 的贡献与讨论。
