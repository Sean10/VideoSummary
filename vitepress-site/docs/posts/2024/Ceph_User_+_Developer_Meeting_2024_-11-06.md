---
title: "Ceph (User +) Developer Meeting 2024-11-06"
date: 2024-11-06
updated: 2024-11-19
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 改进后的中文总结内容

**会议时间**: 2024年11月  
**会议主题**: Ceph开发月度会议 (CDM)  
**参会人员**: Ken, Yehuda, Laura, 以及其他Ceph开发者



**会议议题**

1. **Ken: 关于EL10和SELinux的集成**
   - **背景**: 讨论了在CentOS Stream 10 (EL10) 上启用SELinux的挑战和需求。
   - **目标**: 了解EL10的特性，探讨在EL10上启用SELinux，并讨论如何实现这一目标。
   - **工作流程**: 
     - 通过Fedora Rawhide获取缺失的包，进行本地构建和测试。
     - 使用Copr系统共享RPM包，并逐步将这些包集成到EL10的AppStream中。
   - **挑战**: 需要解决Senta Storage SIG中的NFS Ganesha集成问题，并将EL10集成到Ceph的CI/CD系统中。
   - **后续行动**: 继续推进EL10的集成工作，特别是与NFS Ganesha的集成，并更新Ceph的容器文件以支持EL10。

2. **Yehuda: RGW Bucket Level Snapshots**
   - **背景**: 讨论了在RGW中实现Bucket级别的快照功能的需求。
   - **目标**: 提出一种基于RGW版本控制系统的Bucket快照方案，避免使用RADOS快照。
   - **方案**: 在Bucket元数据中维护一个快照ID，每次创建快照时递增该ID，并记录每个对象版本所属的快照ID。
   - **挑战**: 需要处理非版本化Bucket的快照问题，并优化Bucket索引的扫描性能。
   - **后续行动**: 继续设计Bucket快照的实现细节，特别是如何处理快照删除时的对象版本管理，并考虑引入生命周期策略。



**决定事项**

1. 继续推进EL10的集成工作，特别是与NFS Ganesha的集成。
2. 设计Bucket快照的实现细节，并考虑引入生命周期策略。



**后续行动计划**

1. 更新Ceph的容器文件，支持EL10作为基础镜像。
2. 继续设计Bucket快照的实现细节，并考虑引入生命周期策略。
3. 讨论如何将EL10的包构建和测试集成到Ceph的容器化工作流中。



**其他讨论**

- 讨论了如何将EL10的包构建和测试集成到Ceph的容器化工作流中。
- 讨论了是否可以使用Alma Linux作为上游CI的基础镜像。



**会议结束时间**: 未知
**下次会议时间**: 2024年12月