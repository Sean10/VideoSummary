---
title: "Ceph Day CERN 2019: Ceph storage for openstack in a security - Etienne Chabrerie"
date: 2020-08-25
updated: 2020-08-26
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

**会议主题：** 法国内政部IT部门关于云服务部署的讨论

**参会人员：** 法国内政部IT部门的DevOps团队成员

**会议时间：** 下午

**会议地点：** 线上视频会议

**会议内容总结：**

1. **背景介绍：**
   - 发言人目前在法国内政部IT部门工作，负责开发面向公众的云服务。
   - 该部门负责国家内部安全、法国国家警察、身份文件发放（如护照、身份证）、选举物流组织等。

2. **云服务概述：**
   - 提供基于OpenStack的安全云服务，已获得安全认证，适用于敏感应用。
   - 客户需要存储的数据和应用需要私有云环境，无法使用Amazon Cloud或Google Cloud Platform。

3. **技术挑战与解决方案：**
   - 客户需要更多的存储空间，因此需要可扩展的存储解决方案。
   - 目前使用的技术包括OpenStack和VSA存储平台，但存在性能和配置复杂性问题。
   - 计划部署新的存储系统，包括两个集群：一个用于块存储（RBD），另一个用于对象存储（S3和Swift）。

4. **实施细节：**
   - 使用SSD存储以提高性能，特别是对于小IO操作。
   - 开发Ansible和SaltStack playbooks以集成外部存储。
   - 提供S3服务，支持双向复制，确保数据的高可用性和灾难恢复。

5. **自动化与部署：**
   - 采用CI/CD策略，减少手动操作，提高部署的可靠性和效率。
   - 使用Cobbler服务器进行节点部署，通过Ansible进行集成。
   - 部署过程中使用DeepSea进行集群发现和配置。

6. **性能评估：**
   - 进行了一些基准测试，结果显示新系统的性能优于现有系统。

**后续行动计划：**
- 继续推进新存储系统的部署，确保其稳定性和性能。
- 优化CI/CD流程，提高自动化水平，减少人为错误。
- 定期进行性能评估和系统更新，确保满足客户需求。

**备注：**
- 会议中提到的技术术语包括OpenStack、VSA、SSD、NVMe、Ansible、SaltStack、DeepSea、Ceph等，这些关键词体现了会议内容的专业性和技术深度。

**会议结束时间：** 未明确记录

**记录人：** [您的姓名]

**审核人：** [审核人姓名]