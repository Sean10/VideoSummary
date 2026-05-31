---
title: From ISCSI to NVMe-of- A Comparative Look on Storage Protocol Advantages & Challenges - A. Muthmann
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- iSCSI
categories: 
- "视频总结"
subtitle: From_ISCSI_to_NVMe-of_-_A_Comparative_Look_on_Storage_Protocol_Advantages_Challenges_-_A._Muthmann
---

### 会议纪要

**会议主题**: Ceph中的块存储协议比较：从iSCSI到NVMe-oF

**主讲人**: Andy Muthmann，CRO公司管理总监

**会议内容**:

1. **公司介绍**:
   - CRO公司成立于2017年，总部位于德国，专注于Ceph的部署和管理软件，提供咨询、专业服务、支持和培训等服务。
   - CRO公司是Ceph基金会的创始成员之一，积极参与Ceph的开发。

2. **会议主题**:
   - 讨论Ceph中的块存储协议，主要比较RBD、iSCSI和NVMe-oF的优缺点。
   - 介绍这些协议的历史、性能、可靠性、可扩展性等方面的比较。

3. **协议介绍**:
   - **RBD**: Ceph原生的块存储协议，支持精简配置、快照、克隆和复制，广泛用于虚拟化、容器和私有云环境。
   - **iSCSI**: 行业标准的块存储协议，已进入维护模式。
   - **NVMe-oF**: 最新的协议，支持高性能网络，如RDMA、InfiniBand，集成到Ceph中。

4. **协议比较**:
   - **部署复杂性**: RBD最简单，iSCSI和NVMe-oF需要额外的网关和配置。
   - **网络设置**: RBD使用标准TCP/IP，iSCSI支持多路径，NVMe-oF支持RDMA和多路径。
   - **性能**: RBD性能最佳，NVMe-oF次之，iSCSI最差。
   - **可靠性**: RBD依赖Ceph的高可靠性，iSCSI和NVMe-oF需要集群网关来实现高可用性。
   - **成本**: RBD成本最低，iSCSI和NVMe-oF可能需要额外的硬件和网络支持。
   - **安全性**: iSCSI缺乏传输加密，需要额外的安全机制。

5. **客户反馈**:
   - 一些客户已从iSCSI迁移到NVMe-oF，整体满意度较高，性能有所提升。
   - 迁移速度较慢，部分客户受限于vSphere版本，无法及时升级。
   - 部分客户考虑迁移到其他虚拟化环境，而非继续使用VMware。

6. **结论**:
   - 没有一种协议适合所有场景，选择取决于具体环境、预算和需求。
   - 通常推荐RBD，因其简单、可靠且性能良好。
   - 尽量避免使用iSCSI，因其已进入维护模式。
   - NVMe-oF是一个现代化的选择，但目前采用率较低。

**后续行动计划**:
- 继续关注Ceph的新版本，特别是与高可用性和部署相关的改进。
- 与客户合作，帮助他们根据具体需求选择合适的块存储协议。

**会议结束**:
- 主讲人感谢大家的参与，并鼓励大家继续关注Ceph的发展。

**会议时间**: 未知

**会议地点**: 线上会议

**参会人员**: CRO公司成员及Ceph社区相关人员