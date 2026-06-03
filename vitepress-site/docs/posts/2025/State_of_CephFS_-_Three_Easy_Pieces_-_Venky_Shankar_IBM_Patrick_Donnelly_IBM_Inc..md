---
title: "State of CephFS- Three Easy Pieces - Venky Shankar, IBM & Patrick Donnelly, IBM, Inc."
date: 2025-01-23
updated: 2025-01-24
tags:
  - "CephFS"
  - "存储优化"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要：CephFS 三部曲

**会议主题**: CephFS (CephFS) 三部曲
**主讲人**: Venki、Patrick、RI
**会议时间**: 未知
**会议地点**: 线上/线下



#### 会议概述
本次会议主要讨论了 CephFS（CephFS）的最新进展、历史回顾以及未来发展方向。会议分为三个部分：CephFS 概述、CephFS 的最新功能和改进、以及未来的工作计划。



#### 主要议题

1. **CephFS 概述**
   - **CephFS 简介**: CephFS 是一个 POSIX 兼容的分布式文件系统，旨在提供与本地文件系统相同的用户体验。CephFS 通过分离元数据和数据处理，元数据由 MDS (Metadata Server) 处理，而客户端直接与数据池交互进行读写操作。
   - **历史回顾**: CephFS 自 2006 年首次提出以来，经历了多个重要阶段，包括 2014 年被 Red Hat 收购，2016 年宣布稳定，2017 年引入多 MDS 支持等。

2. **CephFS 的最新功能和改进**
   - **Qui 功能**: 该功能支持崩溃一致性快照，允许在多个目录上进行一致性快照操作，特别适用于分布式数据库等场景。
   - **MDS Journal 修剪改进**: 优化了 MDS 日志修剪机制，减少了线程锁争用问题，提升了性能。
   - **自动平衡器**: 默认禁用了自动平衡器，以避免在多 MDS 集群中出现子树分裂过多导致的性能问题。
   - **Case-insensitive 目录树**: 为支持 Samba 环境，引入了大小写不敏感的目录树功能，提升了性能。
   - **高效硬链接管理**: 通过引入 Referent Inode，解决了全局快照域（Global Snap Realm）在硬链接管理中的性能和稳定性问题。
   - **FS Crypt 支持**: 在 Linux 6.6 内核中，CephFS 支持了 FS Crypt 加密功能，用户可以通过 fs-crypt 工具加密 CephFS 目录树。
   - **异步 I/O 支持**: 用户空间客户端和 NFS Ganesha 的异步 I/O 支持，提升了 I/O 吞吐量。

3. **未来的工作计划**
   - **Referent Inode 的进一步优化**: 该功能预计在 Tentacle 版本中发布，旨在彻底解决硬链接管理中的性能问题。
   - **快速克隆 (Fast Cloning)**: 基于 Referent Inode 的工作，未来将实现类似 RBD 的快速克隆功能，避免全量复制。
   - **QoS (Quality of Service)**: 计划在未来的版本中引入 QoS 支持，以更好地管理存储资源。
   - **用户空间 FS Crypt 支持**: 正在开发用户空间 FS Crypt 支持，预计在 Tentacle 版本中发布。



#### 决定事项
- **Qui 功能**：已实现并将在 Squid 版本中发布，支持崩溃一致性快照。
- **自动平衡器**：默认禁用，以避免性能问题。
- **Case-insensitive 目录树**：预计在 Tentacle 版本中发布，支持 Samba 环境。
- **Referent Inode**：预计在 Tentacle 版本中发布，解决硬链接管理中的性能问题。



#### 后续行动计划
- **继续优化 MDS 性能**：进一步改进 MDS 的日志修剪和子树管理。
- **开发快速克隆功能**：基于 Referent Inode 的工作，实现快速克隆。
- **引入 QoS 支持**：计划在未来的版本中引入 QoS，以更好地管理存储资源。
- **用户空间 FS Crypt 支持**：继续开发用户空间 FS Crypt 功能，确保与内核版本的兼容性。



#### 问答环节
- **FS Crypt 与 Case-insensitive 目录树的兼容性**：FS Crypt 的加密名称将作为 Alternate Name，确保大小写不敏感的目录树功能正常工作。
- **客户端是否会被通知 Qui 操作**：客户端不会被直接通知 Qui 操作，但会收到 caps 召回通知。
- **CephFS Mirror 是否支持同步扩展属性**：目前不支持，但有计划在未来版本中解决。



**会议总结**: 本次会议详细介绍了 CephFS 的最新进展和未来计划，特别是在性能优化、硬链接管理、加密支持等方面。未来将继续优化 MDS 性能，并引入快速克隆和 QoS 支持，以满足更多用户需求。