---
categories:
- 视频总结
date: 2020-08-25
subtitle: Ceph_Day_CERN_2019_-_Ceph_storage_for_openstack_in_a_security_-_Etienne_Chabrerie
tags:
- Ceph
- OpenStack
- 分布式存储
- 安全性
title: Ceph Day CERN 2019- Ceph storage for openstack in a security - Etienne Chabrerie
updated: 2020-08-26
---




### 会议纪要

**会议主题：** 法国内政部IT部门关于在OpenStack中使用Ceph存储的安全性和部署讨论

**参会人员：** 法国内政部IT部门的DevOps团队

**会议时间：** 下午

**会议地点：** 线上视频会议

**会议内容总结：**

1. **背景介绍：**
   - 法国内政部IT部门负责国家内部安全、警察、身份文件发放等。
   - 该部门采用基于OpenStack的安全云服务，并寻求可扩展的存储解决方案。

2. **云服务概述：**
   - 目前使用OpenStack和VSA存储平台，但存在性能和配置复杂性问题。
   - 客户需要私有云环境，无法使用公共云服务。

3. **技术挑战与解决方案：**
   - 计划部署Ceph存储，包括块存储（RBD）和对象存储（S3和Swift）。
   - 使用SSD和NVMe存储以提高性能。
   - 开发Ansible和SaltStack playbooks以集成外部存储。

4. **实施细节：**
   - 提供S3服务，支持双向复制，确保数据的高可用性和灾难恢复。
   - 使用Cobbler服务器进行节点部署，通过Ansible进行集成。
   - 使用DeepSea进行集群发现和配置。

5. **自动化与部署：**
   - 采用CI/CD策略，提高部署的可靠性和效率。
   - 使用Cobbler服务器和Ansible进行自动化部署。

6. **性能评估：**
   - 基准测试表明新系统的性能优于现有系统。

**后续行动计划：**
- 继续推进Ceph存储系统的部署。
- 优化CI/CD流程，提高自动化水平。
- 定期进行性能评估和系统更新。

**备注：**
- 会议中提到的技术术语包括Ceph、OpenStack、VSA、SSD、NVMe、Ansible、SaltStack、DeepSea、RBD、S3、Swift、CI/CD等，体现了会议内容的专业性和技术深度。

**会议结束时间：** 未明确记录

**记录人：** [您的姓名]

**审核人：** [审核人姓名]