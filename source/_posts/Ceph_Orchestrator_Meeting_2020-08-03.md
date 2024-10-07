---
title: "Ceph Orchestrator Meeting 2020-08-03"
date: 2020-08-03
updated: 2020-08-04
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要：Ceph Orchestrator 周会

#### 会议时间：[具体日期]
#### 参会人员：[参会人员名单]

#### 会议议程：
1. **显示警告消息**
2. **OSD 移除设计命令**
3. **改进 Ceph Orchestrator 的开发者体验**
4. **使用单一容器镜像**

#### 讨论内容：

1. **显示警告消息**
   - **议题概述**：讨论如何通过 Ceph 健康检查（Ceph Health）向用户传播警告消息。
   - **讨论要点**：
     - 当前已有多个拉取请求（pull requests）涉及此话题。
     - 需要改进警告消息的显示方式，使其在仪表盘或健康输出中可见。
     - 讨论了自动解决警告消息的机制，当前每六分钟自动解决一次。
     - 提出了是否应允许用户手动触发健康检查循环（surf loop）的讨论。
   - **决定事项**：
     - 需要提供一种自动解决警告消息的方法。
     - 讨论了是否应允许用户手动触发健康检查循环，最终认为不应中断或排队循环。

2. **OSD 移除设计命令**
   - **议题概述**：讨论 Rook 和 Ceph 在 OSD 移除方面的设计。
   - **讨论要点**：
     - Rook 不自动移除 OSD，而是提供一个一次性操作的 Kubernetes 作业。
     - 讨论了与 Ceph 的相似性和差异，包括安全措施和强制标志。
   - **决定事项**：
     - Rook 和 Ceph 应采用相似的 OSD 移除算法。
     - 需要更新设计文档以反映新的 OSD 移除方法。

3. **改进 Ceph Orchestrator 的开发者体验**
   - **议题概述**：讨论如何改进 Ceph Orchestrator 的开发者体验。
   - **讨论要点**：
     - 当前 Ceph Orchestrator 的开发者体验不佳，需要进行重构。
     - 提出了将 Ceph Orchestrator 变为一个适当的 Python 包的建议。
   - **决定事项**：
     - 需要进行基础工作，包括移除注入的代码并使其成为一个适当的 Python 包。
     - 需要发布 Ceph Orchestrator，以便用户可以从下载平台获取而不是直接从 GitHub 下载。

4. **使用单一容器镜像**
   - **议题概述**：讨论在集群中使用单一容器镜像的需求。
   - **讨论要点**：
     - 提出了在 Ceph Orchestrator 中使用单一容器镜像的建议。
     - 讨论了如何将标签转换为摘要（digest）以确保一致性。
   - **决定事项**：
     - 需要实现与 Ansible 类似的方法，将标签转换为摘要。

#### 后续行动计划：
- **显示警告消息**：
  - 实现自动解决警告消息的机制。
  - 讨论并决定是否允许用户手动触发健康检查循环。
- **OSD 移除设计命令**：
  - 更新设计文档以反映新的 OSD 移除方法。
  - 确保 Rook 和 Ceph 采用相似的 OSD 移除算法。
- **改进 Ceph Orchestrator 的开发者体验**：
  - 进行基础工作，将 Ceph Orchestrator 变为一个适当的 Python 包。
  - 发布 Ceph Orchestrator，使其可以从下载平台获取。
- **使用单一容器镜像**：
  - 实现将标签转换为摘要的方法，确保集群中使用单一容器镜像的一致性。

#### 会议结束：
- 会议于[具体时间]结束，下次会议定于下周同一时间进行。

#### 备注：
- 会议中提到的具体拉取请求和设计文档链接已记录在会议笔记中，供后续参考。