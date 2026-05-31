---
categories:
- 视频总结
date: 2019-05-24
subtitle: Messenger_V2_-_The_New_Ceph_Wire_Protocol_-_Ricardo_Dias_SUSE_Linux
tags:
- Ceph
- 分布式存储
title: "'Messenger V2: The New Ceph Wire Protocol - Ricardo Dias, SUSE Linux'"
updated: 2019-05-24
---



### 会议纪要

**会议主题**： 新SEF信使协议（Messenger v2）介绍及配置

**参会人员**： Ricardo Dias（SUSE Linux高级软件工程师）

**会议内容**：

**1. SEF信使组件简介**

- SEF信使是Ceph集群内部组件间通信的通信库。
- 该组件存在于服务器守护进程（如Mon、OSD等）和客户端库（如librgw、libcephfs等）中。
- 信使抽象了物理通信技术，工作在传输层之上，确保消息可靠交付，并处理连接故障。

**2. 新协议的需求**

- Messenger v1协议存在扩展性差、安全性不足等问题。
- 新协议（Messenger v2）旨在解决这些问题，并支持以下特性：
  - 可扩展性：允许在不破坏现有版本的情况下扩展协议。
  - 多种认证方案：支持多种认证方式，包括无认证、suffix认证等。
  - 加密：支持端到端加密，保证数据安全。
  - 结构化消息：消息结构清晰，易于维护。

**3. Messenger v2协议工作原理**

- 协议分为四个阶段：交换信息、认证、会话建立和消息交换。
- 交换信息阶段，客户端和服务器交换支持的特性和所需功能。
- 认证阶段，客户端和服务器协商认证方式和连接模式。
- 会话建立阶段，客户端和服务器交换身份信息，并生成会话cookie。
- 消息交换阶段，客户端和服务器可以发送和接收消息。

**4. 加密模式**

- 如果协议协商使用安全模式，则所有消息将进行加密和签名。
- 使用AES 128 GCM算法进行加密，保证数据的机密性和完整性。

**5. 配置和管理**

- 需要配置地址向量，指定每个守护进程监听的端口号。
- 新增配置选项，包括messenger1和messenger2，用于控制监听协议版本。
- 默认启用messenger v2，可以通过配置文件禁用。

**6. 升级**

- 从Luminous或Mimic版本升级到Nautilus版本时，需要启用messenger v2。
- 使用`safe mon messenger2`命令启用messenger v2。

**7. 问题解答**

- 使用CRC32进行完整性检查。
- 加密模式对性能有一定影响，具体影响待测试。

**后续行动计划**：

- 完成性能测试，评估加密模式对性能的影响。
- 撰写文档，详细介绍新协议的配置和管理方法。