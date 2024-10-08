---
title: "CDS Tentacle - Cephadm"
date: 2024-08-22
updated: 2024-08-23
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议时间**： 2023年11月X日

**会议地点**： 线上会议

**参会人员**： 项目团队成员

**会议主题**： 讨论Ceph项目T版本的关键功能改进和开发计划

**会议内容**：

**一、已进行中的工作**

1. **标签IDE折扣**： 允许为服务分配多个标签，实现更灵活的资源分配和故障域管理。
2. **OSD替换改进**：
    * **无替换标记**： 允许标记即将替换的磁盘，避免其被误选为OSD。
    * **一次性规格**： 提供一次性OSD部署机制，方便用户进行手动部署。
3. **容器镜像管理**：
    * **列出默认镜像**： 列出默认的Ceph容器镜像，方便用户了解和使用。
    * **生成Cephadm规格**： 根据用户配置生成Cephadm规格文件，方便用户进行集群部署。
    * **支持断开连接安装**： 支持用户在本地仓库中部署容器镜像，无需连接互联网。
    * **多架构镜像**： 解决不同架构主机在升级过程中使用不同镜像的问题。
4. **Cephadm兼容性测试**： 测试Cephadm在基于oci容器镜像的操作系统上的兼容性。
5. **Ceph Dashboard安全改进**：
    * **管理网关**： 引入管理网关，提供单点登录和反向代理功能，提高安全性。
    * **联合MLS**： 实现组件间通信的联合MLS，提高安全性。
    * **高可用性**： 为监控服务提供高可用性，确保监控服务的稳定性。

**二、讨论的主要议题**

1. **标签IDE折扣的文档**： 需要编写详细的文档，解释如何使用标签IDE折扣功能。
2. **一次性规格的自动化**： 考虑将一次性规格功能与Cephadm集成，实现自动化部署。
3. **断开连接安装的镜像镜像**： 考虑使用Scopio等工具自动化镜像镜像过程。
4. **多架构镜像的跟踪**： 需要跟踪每个主机的架构和镜像摘要，以确保使用正确的镜像。
5. **Cephadm兼容性测试的覆盖范围**： 需要扩大Cephadm兼容性测试的覆盖范围，包括更多操作系统和容器镜像。
6. **Ceph Dashboard安全改进的测试**： 需要进行充分的测试，确保管理网关和联合MLS功能的安全性。

**三、决定的事项**

1. 继续推进已进行中的工作，并确保按时完成。
2. 完善相关文档，帮助用户了解和使用新功能。
3. 扩大Cephadm兼容性测试的覆盖范围。
4. 加强Ceph Dashboard安全改进的测试。

**四、后续行动计划**

1. 项目团队成员负责完成各自负责的工作。
2. 定期召开会议，跟踪项目进度。
3. 及时解决项目开发过程中遇到的问题。

**五、其他事项**

1. 讨论了SMB功能的开发计划，计划在T版本中提供SMB功能，并在后续版本中提供更稳定的支持。
2. 讨论了Ceph项目的其他改进方向，例如性能优化、故障恢复等。