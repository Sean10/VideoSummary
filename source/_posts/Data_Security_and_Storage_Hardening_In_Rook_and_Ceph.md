---
title: "Data Security and Storage Hardening In Rook and Ceph"
date: 2022-11-15
updated: 2022-11-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员介绍
- **Federico Lucifredi**: 产品管理总监，负责Obsession平台，曾在Red Hat和即将加入IBM。之前在Canonical担任Ubuntu Server产品经理，参与过14.04版本的开发。曾维护Mount，著有O'Reilly出版的书籍。
- **Anna Hacker**: 使用they/them代词，Red Hat安全团队成员，即将加入IBM。目前负责Red Hat的应急响应，未来将负责存储产品如Ceph ODF和SAP的安全。曾在UCSC攻读形式方法和存储安全，本科毕业于UMass Amherst。
- **Mike Hackett**: 因工作繁忙未能参加，但对本次工作有重要贡献。

#### 会议主要议题
1. **网络安全分区**
   - 讨论了四个网络安全分区：公共安全区、存储访问区、SAS客户端区和集群区。强调了根据威胁模型选择合适的加密和安全实践的重要性。

2. **产品安全实践**
   - Red Hat采用安全开发生命周期，包括渗透测试、依赖项清单、漏洞审查等。介绍了Red Hat在安全架构和应急响应方面的具体做法。

3. **加密和密钥管理**
   - 讨论了数据在静态和传输中的加密方法，以及密钥管理的重要性。提到了使用LUKS进行数据加密，以及RGW的额外加密能力。

4. **身份和访问管理**
   - 讨论了Ceph和RGW的身份验证和授权机制，支持多种身份验证方法如LDAP、Active Directory和OpenStack Keystone。

5. **审计和数据保留**
   - 强调了审计日志的重要性，建议将日志集中管理并定期清理。讨论了数据保留策略和安全删除方法。

6. **二进制文件加固**
   - 讨论了通过操作系统环境和内核提供的加固选项，如ASLR、限制系统调用等，以增强二进制文件的安全性。

#### 决定事项
- 确认了Red Hat在产品安全和加密方面的当前实践和未来方向。
- 强调了根据具体威胁模型选择合适的安全措施的重要性。

#### 后续行动计划
- 继续优化和加强Red Hat存储产品的安全特性。
- 探索和实施更全面的应用层日志记录，以更好地跟踪和审计高层次的操作。

#### 资源链接
- 提供了多个与安全相关的资源链接，包括Kubernetes秘密管理、数据安全和加固文档等。

#### 问答环节
- 回答了关于拒绝服务攻击、加密对性能的影响以及审计日志的详细问题。

本次会议详细讨论了Red Hat在存储安全方面的实践和未来方向，强调了安全措施的实施需要根据具体的威胁模型进行定制。