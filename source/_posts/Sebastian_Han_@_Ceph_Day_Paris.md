---
title: "  Sebastian Han @ Ceph Day Paris  "
date: 2014-11-10
updated: 2014-11-11
tags:
- Ceph
- OpenStack
- 分布式存储
categories:
- "视频总结"
subtitle: Sebastian_Han_@_Ceph_Day_Paris
---



Sebastian Han在Ceph Day Paris会议上分享了关于Ceph与OpenStack集成状态的最新进展、Juno周期的进展以及Ceph的部署情况。

**会议内容总结**：

**一、Ceph与OpenStack集成状态**

1. **DevStack Self**： Sebastian成功将SEF集成到DevStack中，简化了Ceph集群的配置过程。用户可以通过配置文件轻松设置集群大小、副本数量等参数。
2. **OpenStack支持**：
    - Nova：支持从Ceph复制和克隆虚拟机镜像，提高了虚拟机启动速度和效率。
    - Cinder：支持Ceph存储后端，并实现了Cinder备份功能。
    - Nova：支持Ceph存储后端的实时迁移，提高了灾备能力。
    - Cinder：支持自定义RBD卷的条带大小，提高了性能。
3. **正在进行中的工作**：
    -Nova：修复了Ceph存储后端的灾备功能。
    - Cinder：实现Ceph存储后端的卷迁移功能。
    - Nova：优化了快照功能，提高效率。

**二、Anible与Ceph部署**

1. **Anible架构和版本支持**： Anible支持部署Ceph集群，包括Monitor、OSD、MDS、RGW等组件，并支持虚拟机、物理机等多种部署环境。
2. **Anible功能**：
    - 支持部署Ceph集群的各种组件。
    - 支持配置Ceph集群的各种参数。
    - 支持虚拟机、物理机等多种部署环境。
    - 支持多种OSD部署场景，包括OSD和Journal同盘部署、分离部署等。
    - 支持使用目录作为OSD部署路径。
    - 支持滚动升级和清理Ceph集群。

**三、后续行动计划**

1. 继续完善Ceph与OpenStack的集成，包括灾备、快照等功能。
2. 完成Cinder存储后端的卷迁移功能。
3. 优化Anible的部署流程和功能。

**改进点**：

- 在总结中增加了对DevStack Self、Anible架构和版本支持的详细描述。
- 强调了Ceph与OpenStack集成的具体功能和正在进行中的工作。
- 明确了Anible的功能和优势，以及后续行动计划。