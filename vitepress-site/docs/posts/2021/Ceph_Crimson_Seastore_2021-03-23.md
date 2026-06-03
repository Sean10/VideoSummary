---
title: "Ceph Crimson/Seastore 2021-03-23"
date: 2021-03-26
updated: 2021-03-26
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
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

#### 会议内容

本次会议主要讨论了Ceph存储系统的开发进展和相关技术问题。以下为会议关键点：

1. **Ceph Crimson/Seastore项目进展**：
   - 项目成员分享了各自的工作进展，包括代码重构、邮件同步和文档编写等。
   - 讨论了映射和外部指针的问题，需要与工程师进行进一步沟通。

2. **代码审查与PR处理**：
   - 评审了Crimson项目的pull请求（PR），包括文档清理、代码审查和问题修复。
   - 部分成员遇到了配置错误，需要进一步解决。

3. **垃圾回收器（GC）改进**：
   - 实施了垃圾回收器的改进，将GC从每个事务的内置操作改为并发任务，简化了GC状态。
   - 希望改进能够解决之前观察到的崩溃问题。

4. **系统状态机修改**：
   - 修改了经典Scrub状态机，以匹配在Queensland系统中的实现。
   - 允许在经典OSD中使用fmt-based logo格式，以简化代码共享。

5. **其他讨论**：
   - 讨论了如何使用watch notified在OSD中进行通信，以及如何为Reaper Executor添加抽象层。
   - 计划更新相关代码，并继续进行测试。

#### 后续行动计划

- 完成系统状态机的修改和垃圾回收器的改进。
- 解决配置错误，并继续审查和合并PR。
- 完成缺失的Systole接口方法实现。
- 继续测试并更新相关代码。