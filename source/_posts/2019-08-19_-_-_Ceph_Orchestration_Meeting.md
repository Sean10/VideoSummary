---
categories:
- 视频总结
date: 2019-08-19
subtitle: 2019-08-19_-_-_Ceph_Orchestration_Meeting
tags:
- Ceph
- 分布式存储
- 编排
- CephFS
- Rook
title: "'2019-08-19 :: Ceph Orchestration Meeting'"
updated: 2019-08-20
---




本次会议主要围绕Ceph分布式存储项目的讨论展开，包括OSD替换、功能冻结、Rook与Orchestrator的兼容性等关键议题。

**关键细节与讨论议题**：

1. **OSD替换**：Petrus指出，当前替换OSD的流程存在困难，因为orchestrator API缺少必要的代码支持。讨论了通过orchestrator API调用set_volume创建新OSD并指定现有OSD ID的需求，以及通过UI界面简化OSD替换流程的可能性。

2. **功能冻结**：Petrus提到，Ceph 1.1版本的特性冻结将在本周五进行，预计9月初发布。讨论了可能影响Orchestrator的功能，如disruption budgets、bucket object bucket claims等。

3. **Rook与Orchestrator兼容性**：Petrus表示，Orchestrator团队将专注于确保最新master分支的Rook与最新Rook版本兼容，并讨论了兼容性问题及未来版本的规划。

4. **其他议题**：讨论了Ceph集群的启动过程，以及是否需要使用safethought conf等配置文件。还讨论了将override config代码从CRD中移除的PR。

**决定事项**：

1. Petrus将与Chief讨论如何改进Orchestrator的UI，以简化OSD替换流程。
2. Petrus将关注Ceph 1.1版本的发布，确保Orchestrator的兼容性。
3. Joey将关注将override config代码从CRD中移除的PR。

**后续行动计划**：

1. Petrus将与Chief讨论并改进Orchestrator的UI。
2. Petrus将关注Ceph 1.1版本的发布，并与Rook团队沟通兼容性问题。
3. Joey将关注PR的进展，并确保override config代码从CRD中移除。