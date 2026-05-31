---
title: SWITCH- Operations, Data Management and Automation - Theophilos Mouratidis, SWITCH
date: 2025-01-23
updated: 2025-01-24
tags:
- Ceph
- 分布式存储
- 自动化
categories: 
- "视频总结"
subtitle: SWITCH_-_Operations_Data_Management_and_Automation_-_Theophilos_Mouratidis_SWITCH
---

### 会议纪要：Switch团队在Ceph存储系统中的实践与创新

**会议主题**：Switch团队在Ceph存储系统中的应用与自动化部署实践

**主讲人**：Theos Moris，Switch团队的Ceph工程师

**会议内容总结**：

#### 1. **Switch团队背景**
   - Switch是瑞士的国家研究与教育网络（NREN），负责提供IT服务，包括云计算、网络安全和法律服务等。
   - Switch团队专注于存储解决方案，主要使用Ceph。

#### 2. **存储解决方案**
   - **传统系统**：基于Ceph的对象存储版本1和基于Claudian Hyperstore的对象存储版本2。
   - **新系统**：
     - **Object Store v3**：基于Ceph，为Switch Cloud平台提供S3服务。
     - **Switch Cloud Portal**：提供计算、S3和Kubernetes等服务。

#### 3. **Ceph集群的规模与升级**
   - 现有多个Ceph集群，总容量约20PB。
   - 最近从Ceph Octopus升级到Ceph 17版本，支持全IPv6。
   - 新集群Albinia和BN已部署，正在进行实验和优化。

#### 4. **Ceph与Claudian的对比**
   - Ceph更灵活、可扩展，能够进行复杂的升级和替换。
   - Claudian容量有限，扩展和替换困难，升级过程复杂且耗时。
   - 团队正在将数据从Claudian迁移回Ceph。

#### 5. **DevOps与GitOps实践**
   - 传统DevOps使用脚本进行配置管理，存在配置不一致的问题。
   - GitOps通过Git作为单一的事实来源，确保配置的一致性和持续交付。
   - 使用Ansible、Terraform和Makefile进行自动化部署。

#### 6. **Ceph自动化部署工具**
   - **OSv3 Ansible Collection**：基于Red Hat的Ceph Ansible Collection，Switch团队进行了大量定制。
   - 每个角色只负责单一任务，确保代码的模块化和可维护性。
   - 配置管理仓库包含集群特定的信息，支持多种操作。

#### 7. **多站点部署**
   - 支持多站点集群的自动化部署，确保数据在不同站点之间的复制和同步。
   - 使用GitLab CI/CD进行自动化部署。

#### 8. **Switch Cloud Portal**
   - 提供多租户支持，用户可以通过UI管理计算、S3和Kubernetes服务。
   - 集成Ceph的RGW Admin API，支持S3服务的创建和管理。

#### 9. **未来计划**
   - 计划将OSv3 Ansible Collection开源。
   - 继续优化自动化部署流程，增加更多功能。

#### 10. **问答环节**
   - 使用标签而非组，因为标签可以在同一组中灵活添加和删除，避免代码维护的复杂性。

**会议总结**：
Switch团队在Ceph存储系统的应用中，通过GitOps和自动化工具实现了高效的集群管理和部署。未来，团队计划将这些工具开源，以帮助更多Ceph用户简化部署流程。