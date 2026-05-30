---
categories:
- 视频总结
date: 2021-05-11
subtitle: Ceph_Orchestrator_Meeting_2021-05-11
tags:
- Ceph
- OpenStack集成
- NFS模块
- 存储解决方案
- 分布式存储
title: "Ceph Orchestrator Meeting 2021-05-11"
updated: 2021-05-12
---




本次会议主要讨论了OpenStack与Ceph集成中的NFS模块问题，与会人员包括OpenStack与Ceph开发团队成员。会议主要议题包括：

1. **NFS模块现状与挑战**：目前NFS模块存在多个模块和限制，需要找到解决方案以推动OpenStack的发展。仪表盘模块功能良好，但需要与新的NFS模块集成，该模块目前尚未完全功能完善。

2. **OpenStack与Ceph集成中的NFS模块问题**：需要部署Ganesha和Pacemaker，但存在配置和部署的复杂性。现有的NFS模块不支持NFSv3，仅支持NFSv4.1及以上版本。

3. **短期与长期解决方案讨论**：
   - **短期解决方案**：使用TripleO Ansible部署Ganesha和Pacemaker，类似于Stephansible的方式；确保部署的Ganesha能够与Ceph集群通信，并正确配置。
   - **长期解决方案**：使用Cephadm管理NFS守护进程和入口服务；Manila直接与Cephadm交互，动态部署和管理Ganesha集群。

4. **后续行动计划**：
   - **短期行动**：完成TripleO Ansible部署Ganesha和Pacemaker的脚本；确保迁移过程中现有客户的平稳过渡。
   - **长期行动**：完善Cephadm的NFS模块，确保其支持所有必要的功能；简化Manila代码，使其能够利用新的NFS模块接口；开发迁移工具，帮助客户从旧系统迁移到新系统。

会议明确了OpenStack与Ceph集成中NFS模块的问题，并制定了短期和长期的解决方案。开发团队将按照会议确定的行动计划，逐步推进项目的进展。