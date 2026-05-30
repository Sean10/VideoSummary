---
categories:
- 视频总结
date: 2023-11-29
subtitle: Ceph_RGW_Refactoring_Meeting_2023-11-29
tags:
- Ceph
- RGW
- HTTP通信优化
- Lua集成
- LDAP弃用
title: Ceph RGW Refactoring Meeting 2023-11-29
updated: 2023-11-30
---




本次会议重点讨论了Ceph分布式存储系统中RGW（Rados Gateway）的优化与重构，包括以下议题：

1. **HTTP通信优化**：会议讨论了如何优化HTTP通信以使其更加健壮，并强调了需要更全面的审查和测试覆盖。讨论了多站点功能测试的不稳定性，并提出了通过改进测试基础设施来解决。决定在本地和toothylogy环境中运行测试，以验证PR的功能。

2. **Lua集成**：讨论了如何更好地集成Lua脚本与HTTP头信息的暴露问题。提出了重新组织Lua API的建议，以提供更清晰和安全的访问方式。

3. **LDAP的弃用**：讨论了弃用LDAP作为独立认证机制的可能性，建议使用STS（Security Token Service）来替代。

会议决定事项包括：

- Jane将添加评论到PR中，指导测试文件的位置和一般策略。
- 对现有的Lua绑定进行清理和优化，以提供更稳定的API。
- 计划在下一个主要版本中宣布LDAP的弃用，并提供详细的迁移指南。

后续行动计划：

- HTTP通信优化：在本地测试环境中使用Mstart进行初步测试，并在toothylogy环境中进行后续验证。
- Lua集成：对现有的Lua绑定进行清理和优化，确保API的稳定性和安全性。
- LDAP弃用：创建跟踪问题以准备LDAP弃用的文档和迁移指南。

会议总结了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划，以确保所有参与者对项目的进展有清晰的认识。