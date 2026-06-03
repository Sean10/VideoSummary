---
title: "2017-JAN-26 -- Ceph Tech Talk: Getting Started with Ceph Development"
date: 2017-01-27
updated: 2017-01-27
tags:
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2017年1月26日

**会议主题**： Ceph 开发入门

**参会人员**： Ceph 社区成员

**会议内容**：

* **会议背景**： 这是 Ceph 社区 2017 年的首场技术研讨会，旨在帮助新成员了解 Ceph 的开发流程。
* **主要议题**：
    * 如何获取 Ceph 源代码
    * 如何编译和构建 Ceph
    * 如何修复 Ceph 中的 bug
    * 如何进行单元测试和集成测试
    * 如何提交 pull request
    * Ceph 的 QA 测试流程
* **关键细节**：
    * Ceph 源代码托管在 GitHub 上，可以通过 fork 和 clone 方式获取。
    * 使用 `install-deps` 脚本安装编译依赖。
    * 使用 `make-tree` 脚本设置构建环境。
    * 使用 `make` 命令编译 Ceph。
    * 使用 `vstart` 脚本启动测试集群。
    * 使用 `blue store` 作为存储后端。
    * 使用 `git` 进行版本控制。
    * 使用 `git gui` 进行提交操作。
    * 使用 `hub` 工具创建 pull request。
    * 使用 `pathology` 工具进行 QA 测试。
* **决定事项**：
    * 新成员应熟悉 Ceph 的开发流程。
    * 新成员应积极参与 Ceph 的开发。
    * 新成员应使用 `git gui` 和 `hub` 工具进行开发。
* **后续行动计划**：
    * 新成员应阅读 Ceph 的官方文档。
    * 新成员应参加 Ceph 社区的邮件列表和聊天室。
    * 新成员应积极向 Ceph 社区提交代码和反馈。

**计算机科学/ Ceph 相关领域英文关键词**：

* Ceph
* GitHub
* Git
* Blue Store
* CRUSH algorithm
* High Availability
* Scalability
* Object Storage
* Block Storage
* File System Storage
* Consistency
* Decentralization
* Performance
* OSD
* MON
* MDS
* PG
* RADOS
* librados
* libcephfs
* CephFS
* RBD
* RadosGW
* RESTful API
* Authentication
* Authorization
* Encryption
* Erasure Coding
* Replication
* Snapshots
* Clones
* Thin Provisioning
* iSCSI
* Fibre Channel
* NFS
* CIFS
* POSIX
* Monitoring
* Dashboard
* Management
* Orchestration
* Automation
* Integration
* Containerization
* Kubernetes
* Docker
* Virtualization
* Cloud Computing
* AWS
* Azure
* Google Cloud
* Hybrid Cloud
* Multi-cloud
* Storage Cluster
* Node
* Disk
* SSD
* HDD
* JBOD
* SAN
* NAS
* Network
* Topology
* Failure Domain
* Recovery
* Resilience
* Load Balancing
* Caching
* Compression
* Deduplication
* Tiering
* Performance Tuning
* Benchmarking
* Testing
* Validation