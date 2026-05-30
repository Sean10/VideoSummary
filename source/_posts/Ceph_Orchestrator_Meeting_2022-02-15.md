---
categories:
- 视频总结
date: 2022-02-15
subtitle: Ceph_Orchestrator_Meeting_2022-02-15
tags:
- Ceph
- Kubernetes
- Rook
- Cephadm
- Orchestration
title: "Ceph Orchestrator Meeting 2022-02-15"
updated: 2022-02-16
---




本次会议主要讨论了Ceph在Kubernetes环境下的Rook管理模块（manager rook）与Ceph管理模块（cephadm）的差异，以及未来的发展方向。会议内容如下：

1. **Rook管理模块的历史和设计初衷**：Rook管理模块旨在提供一个通用的接口来与不同的编排器协同工作，但目前主要支持fadm和Rook，在Kubernetes环境下的操作方式与其他平台（如cephadm）存在显著差异。

2. **面临的挑战**：
   - Rook在Kubernetes中的操作与其他平台不同，导致一些编排器API对Rook不适用。
   - 仪表盘（dashboard）可能需要为Kubernetes集群提供不同的用户体验。

3. **Rook管理模块的未来**：
   - 讨论了是否应该继续投入资源到Rook管理模块，以及是否有其他更合适的方法。
   - 特别关注仪表盘集成的问题，以及是否应该正式支持Rook管理模块。

4. **文档和API的调整**：
   - 建议修改Ceph文档，不再将Rook与cephadm进行直接比较，或者明确指出哪些功能对Rook不适用。
   - 讨论了是否应该在Ceph文档中记录Rook的方法，或者直接引导用户到Rook文档。

5. **决定事项**：
   - 需要进一步讨论和明确Rook用户的需求，特别是在Kubernetes环境下的需求。
   - 需要与仪表盘团队进行深入讨论，以确定仪表盘在Kubernetes环境下的功能和体验。
   - 可能需要为Rook设计一个不同于编排器API的新API，以更好地适应Kubernetes环境。

6. **后续行动计划**：
   - 安排一个专门的会议，邀请仪表盘团队和Rook团队成员，以及相关的产品经理，深入讨论Rook管理模块的未来方向。
   - 继续评估和调整文档，确保信息的准确性和实用性。
   - 考虑长期的产品规划和用户需求，以决定Rook管理模块的最终定位和功能。