---
categories:
- 视频总结
date: 2019-07-22
subtitle: 2019-07-18_-_-_Ceph_Performance_Meeting
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 高可用性
- 可扩展性
- 对象存储
- 块存储
- 文件系统存储
- 性能
- BlueStore
- BlueFS
- RocksDB
- OSD
- MON
- MDS
- PG
- RADOS
- librados
- libcephfs
- RBD
- RGW
- RESTful API
- 认证
- 授权
- 加密
- 复制
- 快照
- 克隆
- iSCSI
- NFS
- CIFS
- POSIX
- 监控
- Dashboard
- 编排
- 自动化
- 容器化
- Kubernetes
- Docker
- 虚拟化
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 多云
- 存储集群
- SSD
- HDD
- SAN
- NAS
- 网络
- 弹性
- 恢复
- 负载均衡
- 缓存
- 压缩
- 分层
- 性能优化
- 测试
title: "'2019-07-18 :: Ceph Performance Meeting'"
updated: 2019-07-22
---


**会议纪要**

**会议时间**： 2019年7月18日

**会议地点**： 线上会议

**参会人员**： Adam, Sage, Igor, Patrick, Lucas, Marcus, Bella, Alex, David 等

**会议主题**： Ceph 项目进展、技术讨论、行动计划

**会议内容**：

**一、Ceph 项目进展**

*   Adam 近期提交了三个新的 Pull Request (PR) 用于图表工作，令人兴奋。
*   Sage 正在审查 Adam 的 PR，并希望尽快将其集成到自己的工作中。
*   Igor 的 PR 是一个很好的发展方向，团队将尝试使其更明确。
*   Patrick 和 Sage 就 AppTracker 的 PR 进行了讨论，讨论了字符串视图和动态事件的接口问题。
*   Sage 认为应该将字符串视图和动态事件分开，以避免复制和优化性能。
*   团队将进行更大范围的审查，以确定动态事件的接口应该是什么样子，并避免在一般情况下进行复制。
*   Sage 认为应该去掉动态事件，只传递信息。
*   Sage 和 Adam 正在合作解决 RocksDB 的复制问题。
*   团队正在讨论将 RocksDB 的 delete range 功能集成到 Nautilus 中。
*   Sage 认为应该将 RocksDB 5.18.12 版本的 delete range 功能集成到 Nautilus 中。
*   团队正在讨论如何测试 RocksDB 的 delete range 功能。

**二、技术讨论**

*   Sage 讨论了 RocksDB 的 OpTracker 性能问题，认为当前 OpTracker 对随机写入的性能影响很大。
*   团队讨论了 OpTracker 的改进方案，包括使用采样和优化 OpTracker 代码。
*   Sage 认为应该修复 OpTracker 中的明显问题，例如字符串复制，而不是完全重写代码。
*   团队讨论了将 OpTracker 的快速锁应用于其他地方的可能性。

**三、行动计划**

*   Sage 和 Adam 将继续合作解决 RocksDB 的复制问题。
*   团队将进行更大范围的审查，以确定动态事件的接口应该是什么样子，并避免在一般情况下进行复制。
*   Sage 将与团队讨论 OpTracker 的改进方案。
*   团队将测试 RocksDB 的 delete range 功能，并决定是否将其集成到 Nautilus 中。
*   团队将讨论如何将 RocksDB 的 OpTracker 的快速锁应用于其他地方。

**四、其他事项**

*   Sage 和 Bella 将讨论 Jenkins 集成事宜。
*   Marcus 将分享关于 Tableau 存储的跟踪信息。

**五、会议总结**

本次会议讨论了 Ceph 项目的进展、技术讨论和行动计划。团队将继续努力解决各种问题，并推动 Ceph 项目的进展。