---
categories:
- 视频总结
date: 2022-11-15
subtitle: Data_Security_and_Storage_Hardening_In_Rook_and_Ceph
tags:
- Ceph
- Red Hat
- Storage Security
- Rook
- Data Encryption
title: "Data Security and Storage Hardening In Rook and Ceph"
updated: 2022-11-16
---


### 会议纪要

本次会议主要讨论了Red Hat在存储安全方面的实践和未来方向，重点涉及Rook和Ceph存储系统的安全加固措施。

#### 参会人员介绍

- **Federico Lucifredi**: Red Hat产品管理总监，负责Obsession平台，曾在Red Hat和Canonical担任产品经理。
- **Anna Hacker**: Red Hat安全团队成员，负责应急响应和存储产品安全。
- **Mike Hackett**: Red Hat支持团队重要贡献者。

#### 会议主要议题

1. **网络安全分区**：讨论了四个网络安全分区：公共安全区、存储访问区、SAS客户端区和集群区，强调了根据威胁模型选择合适的加密和安全实践的重要性。
2. **产品安全实践**：介绍Red Hat采用的安全开发生命周期，包括渗透测试、依赖项清单、漏洞审查等。
3. **加密和密钥管理**：讨论了数据在静态和传输中的加密方法，以及密钥管理的重要性。
4. **身份和访问管理**：讨论了Ceph和RGW的身份验证和授权机制，支持多种身份验证方法。
5. **审计和数据保留**：强调审计日志的重要性，建议将日志集中管理并定期清理。
6. **二进制文件加固**：讨论了通过操作系统环境和内核提供的加固选项，以增强二进制文件的安全性。

#### 决定事项

- 确认Red Hat在产品安全和加密方面的当前实践和未来方向。
- 强调根据具体威胁模型选择合适的安全措施的重要性。

#### 后续行动计划

- 优化和加强Red Hat存储产品的安全特性。
- 探索和实施更全面的应用层日志记录，以更好地跟踪和审计高层次的操作。

#### 资源链接

- Kubernetes秘密管理
- 数据安全和加固文档

#### 问答环节

会议还回答了关于拒绝服务攻击、加密对性能的影响以及审计日志的详细问题。