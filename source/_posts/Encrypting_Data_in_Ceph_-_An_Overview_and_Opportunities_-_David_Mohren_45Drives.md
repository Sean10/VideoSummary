---
title: Encrypting Data in Ceph- An Overview and Opportunities - David Mohren, 45Drives
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 安全性
categories: 
- "视频总结"
subtitle: Encrypting_Data_in_Ceph_-_An_Overview_and_Opportunities_-_David_Mohren_45Drives
---

会议纪要：Ceph 数据加密与 SEF 概述及改进机会

**会议主题**: Ceph 数据加密与 SEF 概述及改进机会  
**主讲人**: David Mohren  
**日期**: 2025年1月23日



#### 1. **会议概述**
   - David Mohren 介绍了 Ceph 中的数据加密技术，重点讨论了服务器端加密（Server-Side Encryption）和客户端加密（Client-Side Encryption）的实现方式。
   - 目标是消除加密技术的神秘感，提供代码片段和实现细节，帮助与会者更好地理解加密过程。
   - 讨论了当前加密方案的优缺点，并提出了改进建议。

#### 2. **主要议题**
   - **服务器端加密（Server-Side Encryption）**：
     - **OSD 加密**：Ceph 使用 Bluestore 和 Linux 内核的加密功能，通过配置硬盘驱动器实现数据加密。
     - **RGW 加密**：RGW 支持对象存储加密，使用外部密钥存储管理密钥，加密模式为 AES-256-CBC。
     - **常见问题**：密钥存储在外部组件中可能导致单点故障，密钥在 Monitor 中以明文存储存在安全隐患。
   - **客户端加密（Client-Side Encryption）**：
     - **RBD 加密**：RBD 支持客户端加密，使用 LUKS 标准。用户可以在用户空间库中格式化并加载加密密钥，但存在密钥管理问题。
     - **CephFS 加密**：CephFS 支持 FSCRYPT，文件系统级别的加密工具，使用 AES-56-XTS 加密文件内容。
   - **加密方案的改进**：
     - **完整性问题**：当前的加密方案在数据完整性方面存在缺陷，修改加密数据后系统不会报错，可能导致数据损坏。
     - **提议改进**：引入 AEAD（Authenticated Encryption with Associated Data）加密模式，如 AES-GCM，以确保数据的完整性和真实性。
     - **RADOS 级别的加密**：建议在 RADOS 层实现加密，统一加密逻辑，减少重复开发工作，提高系统安全性。

#### 3. **决定事项**
   - **加密方案的改进**：
     - 引入 AEAD 加密模式（如 AES-GCM）以增强数据完整性。
     - 在 RADOS 层统一加密逻辑，减少不同组件之间的重复开发。
   - **密钥管理改进**：
     - 解决密钥在外部存储中的单点故障问题。
     - 加强密钥在 Monitor 中的安全性，避免明文存储。

#### 4. **后续行动计划**
   - **开发团队**：
     - 评估 AEAD 加密模式的可行性，并在 RADOS 层实现统一加密逻辑。
     - 改进密钥管理方案，确保密钥存储的安全性和高可用性。
   - **测试与验证**：
     - 进行性能测试，评估 AEAD 加密模式对系统性能的影响。
     - 验证 RADOS 层加密的可行性和安全性。

#### 5. **会议总结**
   - 本次会议详细讨论了 Ceph 中的数据加密技术，分析了现有方案的优缺点，并提出了改进建议。
   - 重点在于引入 AEAD 加密模式以增强数据完整性，并在 RADOS 层统一加密逻辑，减少重复开发工作。
   - 后续将由开发团队负责具体实现，并进行相关测试与验证。



**会议结束**