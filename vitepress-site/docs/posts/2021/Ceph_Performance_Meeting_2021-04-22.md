---
title: "Ceph Performance Meeting 2021-04-22"
date: 2021-04-22
updated: 2021-04-24
tags:
  - "Ceph"
  - "分布式存储"
  - "CRUSH算法"
  - "高可用性"
  - "可扩展性"
  - "对象存储"
  - "块存储"
  - "文件系统存储"
  - "性能"
  - "BlueStore"
  - "BlueFS"
  - "RocksDB"
  - "OSD"
  - "MON"
  - "MDS"
  - "PG"
  - "RADOS"
  - "librados"
  - "libcephfs"
  - "RBD"
  - "RGW"
  - "RESTful API"
  - "认证"
  - "授权"
  - "加密"
  - "复制"
  - "快照"
  - "克隆"
  - "iSCSI"
  - "NFS"
  - "CIFS"
  - "POSIX"
  - "监控"
  - "Dashboard"
  - "编排"
  - "自动化"
  - "容器化"
  - "Kubernetes"
  - "Docker"
  - "虚拟化"
  - "云计算"
  - "AWS"
  - "Azure"
  - "Google Cloud"
  - "混合云"
  - "多云"
  - "存储集群"
  - "SSD"
  - "HDD"
  - "SAN"
  - "NAS"
  - "网络"
  - "恢复"
  - "弹性"
  - "负载均衡"
  - "缓存"
  - "压缩"
  - "去重"
  - "分层"
  - "测试"
categories:
  - "视频总结"
outline: deep
---
本次会议是 Ceph 开发团队的定期会议，主要讨论了近期的工作进展、待处理的 Pull Requests（PRs）以及一些技术细节。

#### 主要议题

1. **Pull Requests（PRs）讨论**

   - 讨论了两个新的 PR，均与 o-node pinning 和 trimming 相关。一个是 Igor 提交的，另一个是 Adam 提交的，但 Adam 本周不在，因此未能深入讨论。Igor 建议对两个方案进行独立审查。
   - 更新了关于 RGW 压缩和 roxdb 内存分配的 PR，Gabriel 的 PR 需要进一步的审查和测试。

2. **技术细节讨论**

   - Gabriel 讨论了在 roxdb 中进行对象计数的挑战，提出了使用估计大小和节点遍历的方法来改进进度显示。
   - 讨论了如何从 PG map 中获取对象计数信息，以及如何改进 osd 的启动过程显示。

3. **Crimson 存储优化**

   - 介绍了 Crimson 存储的最新进展，包括与 IBM 的合作和性能优化。目前 Crimson 在处理小随机读写方面更高效，但仍需解决多核利用率的问题。

#### 决定事项

- 对 Igor 和 Adam 的 PR 进行独立审查，计划在下一次性能会议上进一步讨论。
- Gabriel 将继续测试和改进 roldb 中的对象计数和进度显示方法。
- 继续推进 Crimson 存储的多核优化工作。

#### 后续行动计划

- 对 Gabriel 的 PR 进行详细审查和性能测试。
- 继续研究和优化 Crimson 存储的多核利用率。
- 下一次会议将讨论 PR 的进一步审查结果和 Crimson 存储的进展。

#### 其他事项

- 确认了关于 backfill 和 recovery reservations 的邮件列表讨论的澄清。
- 会议结束时，主持人提醒大家下周再见，并祝大家一周愉快。

本次会议有效地总结了近期的工作进展，并为接下来的工作指明了方向。