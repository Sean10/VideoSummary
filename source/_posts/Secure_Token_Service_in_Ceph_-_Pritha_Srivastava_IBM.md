---
title: "Secure Token Service in Ceph - Pritha Srivastava, IBM"
date: 2023-05-15
updated: 2023-05-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** STS在Surf RGW中的应用

**主讲人：** Pritha

**职位：** IBM的Safe RGW团队开发人员

**会议内容概述：**
Pritha介绍了STS（Security Token Service）在Surf RGW中的应用，涵盖了STS的基本概念、构建块、支持的API、自定义凭证提供者、ABAC授权策略以及在多站点环境中的实现。

**关键细节：**
1. **STS简介：** STS是一组API，返回具有临时性和有限权限的凭证，基于AWS STS。SDS（Security Domain Service）用于跨账户访问和集成外部应用，这些应用拥有大量用户且不希望拥有永久S3凭证。
2. **当前支持：** RGW支持STS API的子集，包括AssumeRole、AssumeRoleWithWebIdentity和GetSessionToken。还实现了AWS IAM API的子集，用于对角色、策略和OpenID Connect提供者的CRUD操作。
3. **临时凭证：** 临时凭证包括访问密钥ID、秘密访问密钥和会话令牌。会话令牌加密，包含认证和授权信息。
4. **角色与策略：** 角色是一个实体，类似于用户但没有永久S3凭证。角色关联两个IAM策略：信任策略（决定谁可以假设角色）和权限策略（决定角色可以做什么）。
5. **支持的API：**
   - **AssumeRole：** 提供跨账户或跨租户访问。
   - **AssumeRoleWithWebIdentity：** 提供Web身份联合，用户通过OpenID Connect兼容提供者认证后，可以访问S3资源。
6. **ABAC授权策略：** 基于属性的访问控制（ABAC）使用标签（键值对）来定义权限，简化权限集的定义。
7. **STS Lite：** 基于GetSessionToken API，主要用于外部认证如Keystone和LDAP，减少对Keystone服务器的延迟和负载。
8. **自定义凭证提供者：** 一个Java模块，改进AWS SDK中的Web身份令牌凭证提供者，支持会话持续时间和会话策略，并提供刷新令牌功能。
9. **多站点实现：** 角色和策略元数据复制已实现，OpenID Connect提供者元数据复制仍在进行中。

**决定事项：**
- STS在RGW中的实现和功能已基本明确，多站点元数据复制功能已部分实现。

**后续行动计划：**
- 继续完善OpenID Connect提供者元数据复制功能。
- 探索和优化从桶策略到使用角色的性能改进。

**参考资料：**
- STS及其相关主题的文档和GitHub仓库链接。

**会议结束：**
Pritha感谢大家的参与，并邀请提问。会议中讨论了多站点配置、性能改进和与其他IDP的兼容性问题。

[Applause]