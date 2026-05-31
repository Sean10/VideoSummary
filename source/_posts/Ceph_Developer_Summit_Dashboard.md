---
title: Ceph Developer Summit   Dashboard
date: 2025-09-11
updated: 2025-09-12
tags:
- Ceph
- Dashboard
- RGW
categories: 
- "视频总结"
subtitle: Ceph_Developer_Summit_Dashboard
---

本次Ceph开发者峰会Dashboard会议主要讨论了Ceph Dashboard在Tentacle版本中的关键改进以及Umbrella版本的未来规划。以下是会议的主要内容和决定事项：

### Tentacle Release 主要亮点

1. **NVMe over TCP (NVMe-oF) 支持**：升级支持最新规范的NVMe-oF Gateway Groups，并允许用户一次性创建多个Namespace。
2. **多集群支持（Multi-Cluster Support）**：新增Multi-Cluster标签页，支持连接Hub Cluster并查看跨集群的Metrics。
3. **RGW (RADOS Gateway) 功能增强**：包括Multi-Site自动化、Tiering Storage Classes支持、RGW Topics和S3 Bucket通知管理，以及Granular Bucket Replication改进。
4. **SMB 协议支持**：新增SMB协议的完整管理及监控功能。
5. **监控与 Grafana 集成**：新增NVMe、CephFS、SMB协议的监控面板，支持按协议查看存储使用情况。
6. **Carbon 设计系统引入**：采用Carbon Design System，对Dashboard UI进行全面现代化改造，提升用户体验。
7. **测试与基础设施改进**：提升Testing Coverage和CI/CD流程，升级Grafana & Angular版本。

### Umbrella Release 未来规划

1. **文档优化**：补齐Tentacle新增功能的文档，确保与代码同步。
2. **100% Carbon 化**：继续推进NVMe-oF UI优化，改进Notification系统，优化大规模集群下的告警展示。
3. **弃用旧版 Dashboard**：移除旧版Dashboard（v2），仅保留v3，不再支持回退。
4. **性能优化**：提升Dashboard在大型集群（10,000+ OSDs）下的性能，降低CPU/Memory开销。
5. **新功能探索**：计划实现Multi-Tenancy & S3 Browser，优化REST API设计，引入AI辅助Troubleshooting功能。
6. **其他改进**：更新Tools & Packages，优化Troubleshooting，提升Dashboard在异常场景下的可用性。

会议还展示了Tentacle版本中Dashboard UI的改进，包括Multi-Cluster管理界面、NVMe-oF Gateway配置、RGW Multi-Site Wizard、SMB管理界面、Grafana监控面板等。

后续行动计划包括继续推进Umbrella Release功能开发、完善文档、实验性开发AI辅助Troubleshooting功能，以及移除旧版Dashboard。



以上是对Ceph Developer Summit Dashboard会议的改进总结，涵盖了会议的关键细节、主要议题、决定事项以及后续行动计划，并保留了相关领域的英文原文关键词。