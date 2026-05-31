---
title: Ceph User + Dev Monthly - July 2025
date: 2025-07-16
updated: 2025-07-17
tags:
- Ceph
categories: 
- "视频总结"
subtitle: Ceph_User_+_Dev_Monthly_-_July_2025
---

### Ceph 用户 + 开发者月度会议 - 七月 2025

本次会议主要讨论了 Ceph 社区活动、用户参与策略以及一些技术议题。

**社区活动（CephCon）**:
- **CephCon 2023 注册**：会议将于温哥华举办，Laura 提供了注册链接，鼓励社区成员参与。
- **提案征集（CFP）截止**：CFP 提交截止时间为当天 23:59（太平洋时间），Anthony 强调需要更多用户故事，包括 Ceph 在实际场景中的应用案例、解决技术问题的经验分享、改进建议或痛点反馈等。

**Ceph 用户参与策略**:
- Anthony 分享了三步计划：
  1. **“Ceph 在您组织的状态”调查**：收集用户反馈，用于改进社区策略。
  2. **Ceph 愿景板**：整理 Ceph 的发展历程、现状和未来方向，需社区成员贡献案例。
  3. **CephCon 用户互动**：计划通过博客/视频形式分享用户故事，并现场采访参会者。
- 行动项：填写调查表并积极参与 CephCon 的内容贡献和讨论。

**技术议题**:
- **容器化 Ceph 的补丁构建问题**：当前 `build-container` 脚本仅支持从官方仓库拉取包，无法使用本地构建的补丁包。讨论建议提交 Tracker Ticket，评估通过 Shaman 构建临时包的可行性。
- **RGW 的 S3 API 兼容性回归问题**：测试发现 Reef/Squid 版本的 RGW 在部分 S3 API 行为上比 Quincy 版本更不符合 AWS S3 规范。后续行动为提交 Tracker Ticket，附详细测试对比，RGW 团队跟进 Issue。

**决议与行动计划**:
- 所有成员尽快提交 CephCon 提案。
- 参与用户调查，推动故事分享计划。
- 提交 Tracker Ticket，跟进技术问题。
- 下月例会将继续讨论进展。

**关键词保留**:
- `OSD`, `MON`, `MDS`, `PG`, `RADOS`, `librados`, `CephFS`, `RBD`, `RGW`
- `Object Storage`, `Block Storage`, `File System Storage`
- `CRUSH Algorithm`, `Erasure Coding`, `Replication`, `BlueStore`, `RocksDB`
- `Kubernetes`, `AWS S3 API`, `iSCSI`, `NFS`, `CIFS`