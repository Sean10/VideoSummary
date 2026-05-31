---
categories:
- 视频总结
date: 2018-02-13
subtitle: 2018年2月7日 Ceph开发者月度会议
tags:
- Ceph
- Dashboard
title: "2018-FEB-07 -- Ceph Developer Monthly"
updated: 2018-02-13
---


2018年2月7日，Ceph开发者月度会议在德国举行，会议主要讨论了以下几个关键议题：

1. **Dashboard v2**：
   - 自动化团队正在开发新的Dashboard v2，旨在替代现有版本。
   - 使用Angular 2作为前端框架，后端采用CherryPy，集成到Manager中。
   - 目前后端开发已完成，前端页面开发正在进行中，包括健康页面等。
   - 计划下周结束前提交可审查的代码，并计划与监控等功能集成。

2. **OpenStack Swift与Ceph的集成**：
   - 自动化团队正在开发OpenStack Swift与Ceph的集成。
   - 使用Ansible进行部署，不使用SaltStack或其他工具。
   - 计划集成自动化监控功能，但需要手动设置图表和配置Dashboard。

3. **Ceph Messenger v2**：
   - Messenger v2正在进行开发，包括身份验证和传输加密。
   - 计划使用GSSAPI进行身份验证和加密，支持Kerberos和其他认证协议。
   - 目前正在进行Kerberos的集成工作。

4. **Ceph集群级别复制**：
   - 讨论了集群级别复制的架构和实现细节。
   - 使用日志条目和操作缓存来管理复制操作。
   - 引入了新的模块来处理复制工作，讨论了复制暂停和恢复机制。

会议行动计划包括：
- 自动化团队继续开发Dashboard v2和OpenStack Swift与Ceph的集成。
- Ceph社区成员继续讨论和改进集群级别复制的实现。
- Messenger v2团队继续进行身份验证和加密的集成工作。

会议还讨论了Ceph社区的最新动态和未来发展方向。

[改进后的总结中可能遗漏或需要更正的信息]
- 原始字幕内容中提到OpenStack Swift与Ceph的集成使用Ansible进行部署，但未提及是否集成自动监控功能。
- 原始字幕中提到Ceph Messenger v2使用GSSAPI进行身份验证和加密，但未提及支持的具体认证协议。
- 原始字幕中提到Ceph集群级别复制的实现细节，但未提及如何处理复制暂停和恢复机制。

[改进后的总结内容结束]
