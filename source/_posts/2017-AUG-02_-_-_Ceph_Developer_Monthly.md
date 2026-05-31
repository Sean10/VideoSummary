---
categories:
- 视频总结
date: 2017-08-29
subtitle: 2017-AUG-02_-_-_Ceph_Developer_Monthly
tags:
- Ceph
- 分布式存储
- CRUSH算法
- 可扩展性
- 对象存储
- 块存储
- 文件系统存储
- 高可用性
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
- 容器化
- Kubernetes
- Docker
- 云计算
- AWS
- Azure
- Google Cloud
- 混合云
- 存储集群
- 存储
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
- 去重
- 分层
- 性能优化
- 测试
title: "'2017-AUG-02 :: Ceph Developer Monthly'"
updated: 2017-08-29
---




在本次Ceph开发者月度会议上，与会人员讨论了Ceph Luminous版本发布准备情况、Ceph功能更新与改进、Ceph性能优化以及Ceph与其他技术的集成。

**主要议题**：

* **Ceph Luminous版本发布准备**： Leo表示Ceph Luminous版本即将发布，目前正在进行最后的bug修复工作。
* **Ceph功能更新与改进**：
    * 新Web仪表板，提供简单直观的界面用于监控和管理Ceph集群。
    * 服务映射功能，允许用户从命令行或模块中访问服务信息。
    * 应用程序标签功能，允许用户将标签应用于存储池。
    * 日志改进，包括新的日志消息和JSON格式。
    * 状态模块，提供友好的界面查看Ceph集群状态。
    * 配置选项改进，包括新的帮助命令和diff命令。
    * 平衡器模块，允许用户轻松进行数据平衡操作。
    * 自动调整P基因组功能。
    * 速率限制功能，允许用户限制特定账户的I/O操作。
    * 快速失败请求功能。
    * 跨集群复制功能。
    * 共享读取缓存功能。
    * 阵列代码改进。
    * 与Prometheus集成。
* **Ceph性能优化**： 讨论了Ceph的性能优化，包括数据分布、I/O操作等方面的改进。
* **Ceph与其他技术的集成**： 讨论了Ceph与其他技术的集成，包括Prometheus、Kubernetes等。

**行动计划**：

* 继续进行Ceph Luminous版本的bug修复工作。
* 开发Ceph的新功能。
* 改进Ceph的速率限制功能和跨集群复制功能。
* 开发Ceph的共享读取缓存功能和阵列代码。
* 改进Ceph与Prometheus的集成。

本次会议为Ceph的发展做出了重要贡献，讨论了Ceph的最新进展和未来的发展方向。