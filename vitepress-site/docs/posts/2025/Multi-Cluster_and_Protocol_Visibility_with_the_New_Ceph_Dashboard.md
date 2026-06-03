---
title: "Multi-Cluster and Protocol Visibility with the New Ceph Dashboard"
date: 2025-06-24
updated: 2025-06-24
tags:
  - "对象存储"
categories:
  - "存储技术"
outline: deep
---
### 会议主题

IBM工程师Ankosh分享了Ceph Dashboard的最新功能，重点讨论了多集群管理、对象存储增强、管理网关、文件系统改进和监控面板优化等主题。

### 核心讨论内容

#### 1. Ceph Dashboard的重要性
- 提供统一管理界面，支持block、file和object storage。
- 支持大规模集群的健康状态、性能指标和容量管理。
- 简化复杂操作，如CRUSH算法配置和PG管理。

#### 2. Tentacle版本新功能

1. **多集群管理（Multicluster Management）**
   - 集中监控多集群指标，在Grafana中统一展示。
   - 管理多个集群的资源，如OSD和MON。
   - 跨集群告警统一展示。
   - 支持跨集群数据复制，如RGW bucket复制。

2. **对象存储增强（Object Enhancements）**
   - 跨集群复制，支持自动化token交换。
   - 云分层，支持AWS S3等作为后端存储。
   - S3账户管理，实现多租户自服务。

3. **管理网关（Management Gateway）**
   - 通过OAuth2/OIDC协议实现统一认证，支持SSO登录。
   - 简化访问，通过单一入口访问所有管理服务。

4. **文件系统改进（File Improvements）**
   - 支持SMB协议，管理SMB集群、用户和共享目录。
   - 优化NFS UX，统一cluster和shares视图。

5. **监控面板优化（Monitoring Dashboards）**
   - 跨集群监控，展示跨集群容量、告警和资源状态。
   - 应用概览，按block、file、object分类统计存储使用情况。
   - NVMe监控，新增NVMe网关性能和容量指标面板。
   - 增强文件系统详情，可视化metadata、IOPS等指标。

#### 3. 未来计划（Roadmap）
- 提升易用性，优化NVMe配置流程。
- 改进故障排查，在告警中增加修复建议。
- 支持超大规模OSD集群。
- 完善监控面板，覆盖更多存储类型。

#### 4. 行动项（Action Items）
- 测试多集群功能，验证跨集群复制和Prometheus Federation的稳定性。
- 收集用户对S3账户管理和云分层的使用体验反馈。
- 推动从SAML迁移至OAuth2/OIDC。

#### 5. 关键词保留（Ceph 术语）
- CRUSH algorithm | RADOS | PG | Bluestore | RocksDB
- Erasure Coding | Thin Provisioning | iSCSI | CIFS/POSIX
- Kubernetes Integration | Hybrid Cloud | JBOD/NAS

#### 6. 参与贡献
- 通过Ceph Dashboard Slack或邮件列表联系开发团队。

**会议结束**