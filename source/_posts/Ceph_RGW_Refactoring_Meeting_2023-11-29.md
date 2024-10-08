---
title: "Ceph RGW Refactoring Meeting 2023-11-29"
date: 2023-11-29
updated: 2023-11-30
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph分布式存储系统中的HTTP通信优化与Lua集成

#### 参会人员：Matt, Casey, Jane, 以及其他相关研发人员

#### 会议日期：[具体日期]

#### 会议地点：视频会议

#### 会议内容总结：

1. **HTTP通信优化讨论**
   - **议题介绍**：Matt介绍了如何优化HTTP通信以使其更加健壮的议题。讨论了Mark的测试工作，但强调了需要更全面的审查和测试覆盖。
   - **主要讨论点**：
     - Casey提出了对Mark的PR（Pull Request）进行重试的测试覆盖不足的担忧。
     - 讨论了多站点功能测试的不稳定性，建议通过改进测试基础设施来解决。
     - 提出了在本地和toothylogy环境中运行测试的策略，以验证PR的功能。
   - **决定事项**：
     - Jane将添加评论到PR中，指导测试文件的位置和一般策略。
     - 计划在本地测试环境中使用Mstart进行初步测试，并在toothylogy环境中进行后续验证。

2. **Lua集成讨论**
   - **议题介绍**：讨论了如何更好地集成Lua脚本与HTTP头信息的暴露问题。
   - **主要讨论点**：
     - 讨论了当前Lua绑定中HTTP头信息的暴露方式存在的问题，如命名混乱和安全性问题。
     - 提出了重新组织Lua API的建议，以提供更清晰和安全的访问方式。
   - **决定事项**：
     - 决定采用统一的接口来访问所有HTTP头信息，同时考虑安全性和稳定性。
     - 计划对现有的Lua绑定进行清理和优化，以提供更稳定的API。

3. **LDAP的弃用讨论**
   - **议题介绍**：讨论了弃用LDAP作为独立认证机制的可能性，建议使用STS（Security Token Service）来替代。
   - **主要讨论点**：
     - 讨论了如何通知用户并提供迁移指南。
   - **决定事项**：
     - 计划在下一个主要版本（如Squid）中宣布LDAP的弃用，并提供详细的迁移指南。

#### 后续行动计划：
- **HTTP通信优化**：
  - Jane将添加测试指导到PR中，并开始在本地环境中进行测试。
  - 继续改进多站点测试基础设施，以提高测试的稳定性和可靠性。
- **Lua集成**：
  - 对现有的Lua绑定进行清理和优化，确保API的稳定性和安全性。
  - 提供统一的接口来访问HTTP头信息。
- **LDAP弃用**：
  - 创建跟踪问题以准备LDAP弃用的文档和迁移指南。
  - 在下一次主要版本发布时宣布LDAP的弃用。

#### 会议结束：
- 会议在讨论完所有议题后结束，感谢所有参与者的贡献和讨论。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。