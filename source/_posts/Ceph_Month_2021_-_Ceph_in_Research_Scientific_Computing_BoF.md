---
title: "Ceph Month 2021: Ceph in Research & Scientific Computing BoF"
date: 2021-06-10
updated: 2021-06-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
本次会议是关于Ceph分布式存储系统和科学计算的“鸟类聚会”，由Kevin主持。会议每两个月举行一次，旨在讨论Ceph和科学计算相关的话题，包括有趣的用例、实验和技术挑战。

#### 主要讨论议题
1. **Ceph RBD Mirroring**: 下一周将有一位新成员进行关于RBD镜像的演示。
2. **CephFS Snapshots**: CERN团队正在测试CephFS的快照功能，发现了一些限制，特别是在Nautilus和Octopus版本中，快照删除操作非常慢。建议升级到Pacific版本以解决这些问题。
3. **Ceph Adm的使用**: 讨论了Ceph Adm在管理Ceph集群中的应用，特别是与Puppet的集成问题和容器镜像的管理。
4. **Ceph升级经验分享**: 分享了从Luminous升级到Octopus的经验，强调了升级过程中的一些关键步骤和注意事项，如确保所有虚拟机重启以避免安全问题。
5. **CephFS性能问题**: 讨论了CephFS在处理大量文件时的性能问题，特别是MDS日志段的管理和清理。
6. **Ceph版本和包管理**: 讨论了Ceph版本的升级策略和包管理的最佳实践，包括从FileStore迁移到BlueStore的计划。

#### 决定事项
- 建议升级到Ceph Pacific版本以解决快照管理的性能问题。
- 需要进一步测试和验证Ceph Adm在不同环境下的兼容性和功能。
- 强调了在升级Ceph集群时，特别是涉及安全特性的升级时，需要特别注意文档中的警告和建议操作。

#### 后续行动计划
- 继续测试Ceph Adm的功能和性能，特别是在集成Puppet和容器镜像管理方面。
- 计划在下一个会议周期（可能是8月或9月）再次举行“鸟类聚会”，以继续讨论Ceph和科学计算的相关话题。
- 对于CephFS的性能问题，将继续进行压力测试和优化，以确保在大规模文件系统中的稳定性和性能。

#### 其他注意事项
- 会议中提到的关于Ceph Adm和Podman的特定问题，需要进一步的技术验证和社区反馈。
- 对于Ceph版本的升级，特别是从FileStore到BlueStore的迁移，需要详细的计划和测试，以确保数据的安全和服务的连续性。

本次会议为Ceph社区成员提供了一个交流和分享经验的平台，有助于推动Ceph在科学计算领域的应用和发展。