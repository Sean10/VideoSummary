---
title: "Rook: Why Would You Ever Deploy Ceph Inside Kubernetes? - Travis Nielsen, IBM"
date: 2023-05-05
updated: 2023-05-05
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概述
会议由Travis Nielsen主持，他作为Ceph项目的主要维护者和IBM存储团队的一员，分享了关于在Kubernetes环境中部署Ceph的重要性和方法。Travis强调了Ceph在Kubernetes中的部署优势，并介绍了Rook作为管理层的角色。

#### 讨论的主要议题
1. **Kubernetes与存储的需求**：
   - Kubernetes本身并非为存储设计，但部署应用时需要存储支持。
   - 传统上，存储通常是外部的，但在私有数据中心中使用云提供商存储存在限制。

2. **Ceph在Kubernetes中的部署**：
   - Ceph提供了企业级的存储解决方案，包括三种类型的存储。
   - Rook作为管理层，专门用于在Kubernetes中部署和管理Ceph。

3. **Rook的功能与优势**：
   - Rook使用Operator模式，通过自定义资源定义（CRDs）来实现Ceph的自动化部署和管理。
   - Rook自2018年12月宣布稳定，并已在多个生产环境中得到验证。

4. **生产环境中的应用案例**：
   - Dimitri Mission的案例展示了Rook和Ceph在多个大学系统中的成功应用，管理着数百个节点和多PB级的数据。

5. **Rook的社区与支持**：
   - Rook是CNCF毕业项目，拥有近11,000个GitHub星标和2.8亿次Docker Hub下载。
   - 项目遵循社区优先的哲学，定期发布更新，并与Kubernetes的发布周期同步。

#### 决定的事项
- Rook和Ceph的结合为Kubernetes提供了强大的存储解决方案，特别适合需要高可配置性和灵活性的企业环境。
- 社区将继续支持和发展Rook项目，鼓励更多的用户和贡献者参与。

#### 后续行动计划
- 继续推动Rook和Ceph的集成，优化在Kubernetes中的部署和管理。
- 加强社区建设，通过Slack、GitHub等平台收集用户反馈，持续改进项目。
- 在即将到来的KubeCon活动中，将会有更多关于Rook和Ceph的讨论和展示。

#### 其他信息
- Travis Nielsen将在KubeCon上有进一步的分享，并欢迎社区成员参与讨论和交流。

### 结束语
感谢Travis Nielsen的精彩分享，期待社区成员的积极参与和反馈，共同推动Rook和Ceph项目的发展。