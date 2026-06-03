---
title: "CDS Infernalis (Day 1) -- Ceph && Containers"
date: 2015-03-06
updated: 2015-03-07
tags:
  - "Ceph"
  - "Docker"
  - "Kubernetes"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： [请填写会议时间]

**参会人员**： Sebastian、[其他参会人员]

**会议主题**： Ceph 分布式存储 Docker 集成工作及 Ceph 作为容器存储提供商的讨论

**会议内容**：

**一、Ceph Docker 集成工作**

* Sebastian 介绍了 Ceph Docker 集成工作的最新进展，包括：
    * 基于 GitHub 上的 soccer SF 项目进行了改进，并将其移至 get-up-st 环境中。
    * 提供了官方的 Ceph Docker 镜像，包括监控器、OSD、MDS、Rgw 等组件。
    * 支持 Ceph Web 界面（CIT）在 Rgw 上的集成，并已合并。
    * 使用 etcd 进行分布式配置，方便快速部署 Ceph 集群。
    * 考虑使用 comd 生成模板，以便在 console 和 etcd 中重用。
    * 目前已有一些基于 Firefly 的镜像，计划创建更多分支以支持不同版本。
    * 已解决 Docker 镜像中的 bug，并有人提出了自己的解决方案。
* 讨论了 Ceph Docker 镜像的版本问题，以及如何支持不同版本。
* 讨论了 Ceph 与其他存储解决方案（如 Coros）的兼容性问题。

**二、Ceph 作为容器存储提供商**

* 讨论了如何将 Ceph 作为存储提供商集成到 Docker 和 Kubernetes 中。
* 讨论了 Docker 中的存储抽象（volume）模型，以及如何使用 Ceph 作为后端存储。
* 讨论了 Ceph 在 Kubernetes 中的集成方案，包括使用 csi 驱动程序。
* 讨论了在 Atomic 操作系统上集成 Ceph 的挑战，以及如何解决命名空间问题。
* 讨论了 Ceph 与其他存储解决方案（如 Coros）的兼容性问题。

**三、行动计划**

* Sebastian 将继续推进 Ceph Docker 集成工作，并创建更多分支以支持不同版本。
* 讨论了 Ceph 与其他存储解决方案的兼容性问题，并计划进一步研究。
* 讨论了 Ceph 作为容器存储提供商的集成方案，并计划进一步研究。

**四、其他**

* 讨论了 Fedora 21 的发布计划，以及 Ceph 在 Fedora 21 上的支持。
* 讨论了 Ceph 在 Kubernetes 中的集成方案，并计划进一步研究。

**五、总结**

本次会议讨论了 Ceph 分布式存储 Docker 集成工作和 Ceph 作为容器存储提供商的讨论，并制定了后续行动计划。会议重点涉及了 Ceph 的 Docker 集成、Ceph 作为容器存储提供商的集成方案、Ceph 与其他存储解决方案的兼容性以及 Fedora 和 Kubernetes 中的 Ceph 集成。

**改进说明**：

* 保留了会议的关键细节，包括 Ceph Docker 集成工作的进展、Ceph 作为容器存储提供商的讨论以及后续行动计划。
* 确保了计算机科学/ceph相关领域的英文原文关键词被保留。
* 简化了一些描述，以避免重复并提高可读性。