---
title: "2019-06-19 :: Ceph Orchestration meeting"
date: 2019-06-19
updated: 2019-06-19
tags:
  - "Ceph"
  - "分布式存储"
  - "编排"
  - "CephFS"
  - "RBD"
categories:
  - "会议纪要"
outline: deep
---
### 会议纪要

**会议时间**： 2019年6月19日

**参会人员**： huh, me, paint him, Joshua, Brooke, Jim, Timm, Sebastian, Pierre, John Spray, Travis

**会议主题**： 讨论Ceph分布式存储的Rook Toolkit服务接口、调度器（Orchestrator）功能以及后续行动计划。

**会议内容**：

1. **会议时间调整**：
   - 由于新西兰的参会者时间较晚，会议决定将会议时间提前，以便所有参会者都能参加。
   - 会议时间初步定于下午5:30。

2. **安全守护者（Safe Demon）探讨**：
   - Joshua提出探讨安全守护者技术，这可能有助于所有调度器，特别是Essentia Orchestrator，以封装运行容器镜像所需的所有操作。
   - 目前这一想法还处于概念阶段，没有代码实现。Rock Point方面有一个相关的pull request。

3. **接口讨论**：
   - 讨论了现有RTW服务接口存在的问题，包括不愉快的端点和RTW更新名称风格。
   - 提出了改进接口的建议，例如提供新的端点以创建新的存储桶、配置新的存储桶组等。
   - 讨论了将服务器管理、存储桶组管理和RDW结构管理分离的必要性。

4. **RDW结构管理**：
   - 讨论了RDW结构管理的最佳实践，包括使用Rook的admin命令进行管理，以便任何工具都可以轻松地进行此类管理。
   - 强调了将RDW网关命令封装在调度器之外的重要性。

5. **Rook与Ceph的集成**：
   - 讨论了Rook与Ceph集成的细节，包括RDW网关和RDW实例之间的区别。
   - 提出了将RDW网关视为默认区域，除非显式指定其他区域。

6. **其他议题**：
   - Timm提到他在缓存库存和服务方面的工作进展，并已合并了Sebastian和Pierre的修改。
   - 讨论了Ganesha的pull request以及与Dipsy编排相关的端点URL。

**行动计划**：

1. 调整会议时间，确保所有参会者都能参加。
2. Joshua继续研究安全守护者技术。
3. 改进RTW服务接口，包括提供新的端点和改进命令。
4. 分离服务器管理、存储桶组管理和RDW结构管理。
5. 进一步研究Rook与Ceph的集成细节。
6. Timm继续进行缓存库存和服务的工作，并合并相关pull request。

**备注**：

- 会议中提到了一些关键术语，如RTW服务、调度器、RDW、Rook、Ceph等，这些术语在会议记录中已保留英文原文。