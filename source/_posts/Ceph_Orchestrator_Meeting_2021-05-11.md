---
title: "Ceph Orchestrator Meeting 2021-05-11"
date: 2021-05-11
updated: 2021-05-12
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：OpenStack与Ceph集成中的NFS模块问题讨论

#### 与会人员：OpenStack与Ceph开发团队成员

#### 会议时间：[具体时间]

#### 会议地点：在线会议

#### 主要议题：
1. **NFS模块现状与挑战**
2. **OpenStack与Ceph集成中的NFS模块问题**
3. **短期与长期解决方案讨论**
4. **后续行动计划**

#### 讨论内容：

1. **NFS模块现状与挑战**
   - 目前存在多个模块和限制，需要找到解决方案以推动OpenStack的发展。
   - 仪表盘模块功能良好，但需要与新的NFS模块集成，该模块目前尚未完全功能完善。

2. **OpenStack与Ceph集成中的NFS模块问题**
   - 需要部署Ganesha和Pacemaker，但存在配置和部署的复杂性。
   - 现有的NFS模块不支持NFSv3，仅支持NFSv4.1及以上版本。

3. **短期与长期解决方案讨论**
   - **短期解决方案**：
     - 使用TripleO Ansible部署Ganesha和Pacemaker，类似于Stephansible的方式。
     - 确保部署的Ganesha能够与Ceph集群通信，并正确配置。
   - **长期解决方案**：
     - 使用Cephadm管理NFS守护进程和入口服务。
     - Manila直接与Cephadm交互，动态部署和管理Ganesha集群。

4. **后续行动计划**
   - **短期行动**：
     - 完成TripleO Ansible部署Ganesha和Pacemaker的脚本。
     - 确保迁移过程中现有客户的平稳过渡。
   - **长期行动**：
     - 完善Cephadm的NFS模块，确保其支持所有必要的功能。
     - 简化Manila代码，使其能够利用新的NFS模块接口。
     - 开发迁移工具，帮助客户从旧系统迁移到新系统。

#### 决定事项：
- 确认了短期和长期的解决方案方向。
- 确定了短期内的具体行动步骤，包括TripleO Ansible的部署脚本编写。
- 明确了长期目标，包括Cephadm的NFS模块完善和Manila代码的简化。

#### 后续行动：
- 开发团队将开始编写TripleO Ansible的部署脚本。
- Cephadm团队将继续完善NFS模块，确保其满足所有需求。
- Manila团队将开始简化代码，以便能够利用新的NFS模块接口。
- 开发迁移工具，确保客户能够平稳过渡到新系统。

#### 会议总结：
会议明确了OpenStack与Ceph集成中NFS模块的问题，并制定了短期和长期的解决方案。开发团队将按照会议确定的行动计划，逐步推进项目的进展。