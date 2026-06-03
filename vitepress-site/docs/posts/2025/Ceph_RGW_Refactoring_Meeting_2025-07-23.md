---
title: "Ceph RGW Refactoring Meeting 2025-07-23"
date: 2025-07-23
updated: 2025-07-24
tags:
  - "Ceph"
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
### **Ceph 社区会议纪要 - SS3/KMS 集成与加密对象拷贝问题**

#### **日期**: 2025-07-23 | **参会人员**: Boris, Marcus, Cena 等



### **1. 主要议题与讨论**

#### **(1) SS3 与 KMS（密钥管理系统）集成问题**

- **问题背景**: 由于当前使用的 OVH KMS 系统不支持 transit engine，需通过 KMIP 或 key-value engine 实现与 SS3 的集成。
- **技术可行性**: Ceph 代码库不支持非 Vault 的 KMS 后端，需开发新功能。KMIP 支持需升级以支持类似 Vault transit 的加密模式。
- **替代方案讨论**: 探索 IBM/OVH 提供的 KMS API 或开源 KMIP 实现，如 `open-pkcs11`。
- **后续行动**: Boris 将尝试联系 OVH 获取 KMS 实例，社区将创建 Feature Tracker 标记此需求。

#### **(2) 加密对象拷贝（Copy Encrypted Object）问题**

- **问题描述**: 当前 Ceph 中，加密对象的拷贝和移动操作失败，原因是拷贝响应中缺少必要的加密元数据。
- **技术细节**: AWS S3 规范要求拷贝操作需返回与源对象相同的加密头。
- **下一步计划**: Marcus 将修复 multipart upload 的加密属性传递问题，并重新测试。



### **2. 关键结论与行动计划**

| **事项**               | **负责人** | **下一步行动**                                                                 |  
|||--|  
| SS3 支持非 Vault KMS   | Boris      | 联系 OVH 获取 KMS 实例；评估 OpenBao 代理方案的可行性。                         |  
| 改进 Ceph KMIP 支持    | 社区       | 创建 Feature Tracker；评估代码修改范围，优先支持 transit-like 模式。            |  
| 加密对象拷贝修复       | Marcus     | 修复 multipart upload 的加密属性传递问题，重新提交 PR 并通过测试。              |  



### **3. 其他备注**

- 关键术语保留英文（如 KMIP、transit engine、multipart upload、SSE-S3/KMS）。
- 下次会议将跟进 KMS 集成进展和加密拷贝问题的修复状态。

**会议结束时间**: [需补充] | **下次会议时间**- [需补充]