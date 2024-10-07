---
title: "Ceph Orchestrator Meeting 2022-03-29"
date: 2022-03-30
updated: 2022-03-31
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 主要议题：
1. **Ceph vstart 依赖性问题**
   - **问题描述**：当前vstart在启用self adm时失败，原因是无法加载self adm的依赖项。这些依赖项是运行时依赖，因此在从源代码构建Ceph并尝试启动vstart时会失败。
   - **讨论内容**：讨论了是否应将这些依赖项作为构建请求的一部分添加，但Kifu Chai指出这些依赖项并非严格意义上的构建依赖，因此不能直接添加。
   - **解决方案**：提出了一个短期解决方案，即在导入时处理异常，如果导入失败则使用模拟（mock）代替。长期解决方案需要进一步研究vstart如何处理运行时依赖。

2. **Ceph开发工具的使用**
   - **讨论内容**：讨论了开发人员通常使用的工具，如kcli和容器化方法，以及vstart的使用频率较低，导致一些问题未被及时发现。

3. **Ceph NFS相关问题**
   - **问题描述**：讨论了NFS服务的部署问题，特别是多个NFS守护进程在同一主机上的部署问题，以及NFS服务的高可用性配置。
   - **解决方案**：提出了一些改进措施，如改进端口冲突解决机制，以及考虑在Ceph的构建过程中使用Python虚拟环境。

#### 决定事项：
- **vstart依赖性问题**：短期内将采用异常处理和模拟方法解决，长期需要找到合适的运行时依赖管理机制。
- **NFS部署问题**：需要进一步研究和测试NFS服务的部署和运行机制，特别是高可用性和端口冲突问题。

#### 后续行动计划：
- **vstart依赖性问题**：继续研究vstart的依赖管理，寻找更合适的解决方案。
- **NFS部署问题**：创建跟踪票，进一步研究NFS服务的部署和运行机制，特别是高可用性和端口冲突问题。
- **开发工具使用**：鼓励团队成员更多地使用vstart等开发工具，以便及时发现和解决问题。

#### 其他讨论：
- **Ceph开发工具的使用**：讨论了开发人员通常使用的工具，如kcli和容器化方法，以及vstart的使用频率较低，导致一些问题未被及时发现。
- **Ceph NFS相关问题**：讨论了NFS服务的部署问题，特别是多个NFS守护进程在同一主机上的部署问题，以及NFS服务的高可用性配置。

#### 结论：
会议主要解决了Ceph vstart的依赖性问题和NFS服务的部署问题，并提出了相应的短期和长期解决方案。后续将继续研究和测试相关问题，确保Ceph的稳定性和可靠性。