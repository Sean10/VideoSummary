---
title: CBS- A Containerized, Declarative, Flexible Build System Enhanced for Ceph Builds- Joao Eduardo Luis
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 自动化
- 容器化
categories: 
- "视频总结"
subtitle: CBS_-_A_Containerized_Declarative_Flexible_Build_System_Enhanced_for_Ceph_Builds-_Joao_Eduardo_Luis
---

### 改进后的中文总结

在这次Ceph构建系统（CBS）技术分享会议中，Joel（Ceph项目10年贡献者，现任Clyo企业存储产品开发负责人）详细介绍了Clyo Build System（CBS）——一个面向Ceph及其他软件的自动化构建发布系统。

**会议关键点**：

- **系统设计原则**：CBS采用全容器化工作流，确保环境清洁；通过YAML进行声明式配置，支持构建任意软件包；采用元数据驱动管理patch sets和release生命周期。
- **关键技术组件**：
  - **Release Tool**：管理从分支创建到最终发布的完整生命周期，支持迭代开发，自动生成release notes。
  - **Build System**：基于components概念，分阶段容器构建，支持RPM签名并存储到S3，最终生成签名容器镜像。
  - **Build Service**：基于Celery+Redis的任务队列，支持分布式构建节点，通过CBS Client提交任务，集成Google SSO认证。
- **当前技术栈**：
  - **基础架构依赖**：HashiCorp Vault (密钥管理)，S3兼容存储 (RPM/镜像存储)，Redis (任务队列broker)。
  - **构建环境**：默认基于Rocky Linux，支持多EL版本(EL8/EL9)构建，理论上兼容CentOS/AlmaLinux。
- **现存挑战**：
  - 尚未完全实现声明式配置。
  - 部分依赖Clyo内部基础设施。
  - 补丁冲突需人工解决。
  - 缺乏自动化的依赖补丁追踪。
- **后续计划**：
  - 自动化测试集成。
  - 权限与工作流增强。
  - 供应链安全。
  - 补丁管理。

**会议讨论**：

- 构建服务架构：使用Celery+Redis实现任务队列，可扩展多个worker节点并行构建。
- 补丁冲突处理：主要依赖人工解决，支持创建custom patch sets应对复杂情况。
- 发行版兼容性：实际基于Rocky Linux构建，通过指定基础镜像支持多发行版。
- 补丁依赖管理：当前需人工维护补丁关系，未来计划增强metadata支持。

**行动项**：

- 社区可试用GitHub公开的CBS项目。
- 开发者可贡献对更多发行版的支持。
- 需要完善补丁依赖管理功能。
- 计划增强自动化测试流水线。

这次会议为Ceph社区提供了一个深入了解CBS的宝贵机会，并展示了如何利用自动化和容器化技术提高Ceph项目的开发和发布效率。