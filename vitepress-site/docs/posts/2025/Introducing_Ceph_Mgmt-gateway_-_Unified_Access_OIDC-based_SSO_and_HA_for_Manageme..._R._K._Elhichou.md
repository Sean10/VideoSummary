---
title: "Introducing Ceph Mgmt-gateway- Unified Access, OIDC-based SSO, and HA for Manageme... R. K. Elhichou"
date: 2025-11-19
updated: 2025-11-19
tags:
  - "高可用性"
categories:
  - "视频总结"
outline: deep
---
### Ceph 管理网关功能介绍会议纪要

#### **会议基本信息**
- **主题**: 介绍 Ceph 新功能“安全管理网关”
- **主讲人**: Redwan（IBM 软件架构师，Ceph 编排团队核心贡献者）
- **会议目标**: 讲解 Ceph 下一个版本（Tentacle）中的安全管理网关功能，旨在简化管理和监控系统架构，提高安全性和可用性。



#### **关键讨论内容**

1. **现有架构痛点**  
   - Ceph 监控和管理服务（如 Prometheus、Grafana、Dashboard 等）分散，访问复杂，用户体验割裂。
   - 认证机制不统一，各服务独立认证，缺乏统一身份管理。
   - 高可用性不足，监控栈（如 Prometheus）无原生 HA 支持，存在单点故障风险。
   - 安全性缺陷，TLS 配置分散，内部服务通信未强制 mTLS，存在安全风险。

2. **新架构设计**  
   - **Management Gateway**: 统一入口，提供 HTTPS 终结点和负载均衡，简化访问。
   - **OAuth2 Proxy**: 集成外部身份提供商（IDP），支持 SSO（如 Keycloak、Red Hat SSO、Azure AD），提供统一认证。
   - **内部 CA**: 基于 `cephadm` 签发证书，强制服务间 mTLS 认证，提高安全性。
   - **高可用性实现**: 多实例部署 + Keepalived（VRRP 协议）提供虚拟 IP（VIP）故障转移，后端服务多活冗余。

3. **功能优势**  
   - **统一访问**: 单端点访问所有服务，如 `/grafana`、`/prometheus`。
   - **企业级 SSO**: 支持 OIDC 协议，兼容主流 IDP。
   - **安全性提升**: 前端 TLS 终止 + 后端 mTLS 加密，集中式证书生命周期管理。
   - **运维简化**: 通过 `cephadm` 自动化配置。

4. **Demo 演示**  
   - SSO 登录演示，用户通过 VIP 访问 Dashboard，重定向至 Keycloak 完成认证后无缝访问所有服务。
   - 故障恢复测试，展示 Manager 切换、Grafana 实例故障转移、Gateway 节点故障转移。

5. **当前限制与未来计划**  
   - **局限性**: Prometheus 多实例数据可能存在间隙，OAuth2 Proxy 不支持机器间认证，部分服务 SSO 集成需手动配置。
   - **Roadmap**: 扩展 mTLS 覆盖所有服务，审计日志与监控增强，支持自定义根证书。



#### **Q&A 重点摘要**
- 混合认证模式：不支持同时启用 SSO 和本地用户。
- RGW 集成：理论可行，需测试验证。
- 证书管理：未来通过 `cephadm` 的 Cert Manager 实现自动轮换。
- DNS 支持：当前使用短名称，FQDN 需额外配置。
- 网络定制化：VIP 目前绑定公共网络，未来可能支持多网卡选择。



#### **后续行动计划**
- **功能完善**: 补全 Prometheus 数据冗余方案，实现 OAuth2 Proxy 的机器认证支持。
- **用户文档**: 编写详细配置指南。
- **社区反馈**: 收集企业用户场景需求。



#### **参会人员反馈**
- 普遍认可新架构的简洁性和安全性提升，关注企业环境落地可行性。

**会议结束时间**: [需补充]  
**资料链接**: [需补充演示文稿或代码库地址]  

（注：部分术语保留英文原词如 `cephadm`、`mTLS`、`OIDC` 以保持技术准确性。）