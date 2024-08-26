---
title: "Ceph Tech Talk: Ceph at DigitalOcean"
date: 2021-10-07
updated: 2021-10-08
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：DigitalOcean 的 Ceph 使用案例介绍

#### 会议时间：[具体日期]

#### 会议地点：[线上/线下]

#### 主讲人：Alex Merrigan
- **职位**：Senior Engineer at DigitalOcean
- **团队**：Storage Systems Team

#### 会议内容概述：
Alex Merrigan 介绍了 DigitalOcean 在存储系统中使用 Ceph 的情况，包括公司的基本信息、Ceph 的使用案例、操作流程、自动化工具以及遇到的一些问题。

#### 关键细节：
1. **DigitalOcean 简介**：
   - 成立于 [具体年份]，核心理念是简化云资源的配置。
   - 提供多种产品，包括 Droplets（虚拟机）、Block Storage、Spaces（对象存储平台）等。
   - 全球有八个区域的数据中心，最近的重要事件是六个月前的 IPO。

2. **Ceph 使用情况**：
   - 用于 Block 和 Object 存储产品，总计 38 个生产集群，其中 37 个在 Nautilus，1 个在 Luminous。
   - 计划将 Image Backups 产品也迁移到 Ceph。
   - 总存储量超过 54 PB，硬件配置包括全闪存和混合存储（HDD 和 QRC Flash）。

3. **选择 Ceph 的原因**：
   - 水平扩展能力、自愈能力、强一致性。
   - 性能可接受，且具有可预测性。
   - 支持多种存储产品，简化运维。

4. **Ceph 操作流程**：
   - 高度自动化，使用 Ansible Playbooks 和 AWX。
   - 部署 Ceph 使用自定义的 Playbook，支持容器化部署。
   - 监控使用 Ceph Exporter 和 Node Exporter，开发了 Canary 进程进行性能和可用性检查。

5. **自动化工具**：
   - Archimedes：自动处理 CRUSH 权重调整。
   - PgRemapper：用于管理 PG 映射，支持取消回填、优先恢复权重等。
   - 开发了 OSD 生命周期管理工具，包括诊断、部署、升级、移除等功能。

6. **遇到的问题**：
   - Ceph 升级过程中的文档不足和一些未预见的问题。
   - 动态重新分片可能导致 RGW 线程耗尽。
   - Beast 后端的默认线程设置可能不足。

#### 后续行动计划：
- 继续优化 Ceph 的自动化和监控工具。
- 加强对 Ceph 升级和测试流程的改进，计划与社区合作。
- 考虑将更多产品迁移到 Ceph，并优化现有配置。

#### 其他信息：
- DigitalOcean 正在招聘，感兴趣的候选人可以查看 [DigitalOcean 招聘页面](https://www.digitalocean.com/jobs)。
- 如有关于会议内容的疑问，可以联系 Alex Merrigan (amerrigan@digitalocean.com)。

#### 会议结束：
感谢所有参与者的参与，祝大家有一个愉快的一天。

---

以上是根据会议内容整理的会议纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。