---
title: "SMB Keeping - Clients, Clusters & Clouds - John Mulligan, IBM"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
Ceph 会议纪要：SMB on Ceph 技术分享与讨论

## 会议概览
- **主题**：SMB on Ceph 的技术进展、新特性及未来规划
- **主讲人**：John Mulligan（IBM 软件开发者，Samba 团队成员）
- **核心内容**：介绍了 SMB 协议在 Ceph 分布式存储生态中的集成，功能演示，2025年新特性，及社区合作展望。

## 背景与现状
### SMB on Ceph 的核心功能
- **Ceph Manager Module**：全局管理 SMB 相关配置，通过 `cephadm` 部署容器化组件。
- **Active Directory (AD) 集成**：基于 Windows 生态的身份管理与认证。
- **CTDB 集群支持**：通过 Samba 的 CTDB 工具实现高可用（HA）和容错性。
- **VFS 模块优化**：重构为 `VFS_new`，开发 `cephfs-proxy` 工具，提供 Samba 性能数据。
- **监控与指标**：通过 Prometheus 兼容的指标导出器提供 Samba 性能数据。

### 部署简易性
- **两步创建集群**：支持 AD 和 CTDB 的快速部署。
- **分层架构**：命令式 CLI 与声明式接口，Sidecar 容器模型。

## 2025年新特性
### Collocation（多租户资源优化）
- **需求**：同一 Ceph 节点上运行多个独立 SMB 实例。
- **实现方式**：端口隔离和 IP 隔离。

### Remote Control（精细化控制）
- **功能**：基于 gRPC 的 API，支持查询客户端连接状态，强制断开指定客户端。

### QoS 与速率限制
- **目标**：防止单一客户端占用过多带宽或 IOPS。
- **配置项**：带宽/IOPS 阈值，异步操作延迟调控。

### FS-Crypt 与 Keybridge（多租户安全）
- **FS-Crypt**：基于内核加密的 CephFS 用户空间 API。
- **Keybridge**：通用 KMS 连接器，通过 varlink RPC 与 SMBD 交互。

## 演示环节
- **快速搭建集群**：通过 `ceph smb cluster create` 和 `ceph smb share create` 命令。
- **跨节点共享验证**：Windows 客户端通过不同节点 IP 访问同一共享目录。
- **Remote Control 演示**：通过 gRPC API 动态断开指定客户端连接。

## 未来规划（2026）
- **社区协作**：鼓励用户反馈需求，如多协议支持、ID 映射模式扩展。
- **潜在方向**：网络命名空间隔离，NFS/SMB 多协议并行访问。

## Q&A 重点摘要
- **多租户网络隔离**：当前仅通过子网绑定隔离，未来可能支持网络命名空间。
- **Windows ACL 支持**：支持完整 ACL，当前默认 ID 映射模式为 `auto_rid`。
- **NFS/SMB 同时访问**：暂不支持，需解决子卷“earmarking”限制。
- **Ceph CSI 集成**：声明式 API 已通过 GObject 暴露，便于云编排工具调用。

## 后续行动项
- **功能完善**：推进 FS-Crypt 和 QoS 的补丁合并，评估网络命名空间对多租户的增强价值。
- **社区参与**：收集用户对 ID 映射模式的需求，开放议题讨论 NFS/SMB 多协议共存方案。