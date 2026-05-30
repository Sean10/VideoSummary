---
categories:
- 视频总结
date: 2021-10-07
subtitle: Ceph_Tech_Talk_-_Ceph_at_DigitalOcean
tags:
- Ceph
- Distributed Storage
- DigitalOcean
- Cloud Computing
- Storage Systems
title: "'Ceph Tech Talk: Ceph at DigitalOcean'"
updated: 2021-10-08
---




### 会议纪要

#### 会议主题：DigitalOcean 的 Ceph 使用案例介绍

#### 会议时间：[具体日期]

#### 会议地点：[线上/线下]

#### 主讲人：Alex Merrigan
- **职位**：Senior Engineer at DigitalOcean
- **团队**：Storage Systems Team

#### 会议内容概述：

Alex Merrigan 介绍了 DigitalOcean 在存储系统中使用 Ceph 的情况，包括公司简介、Ceph 的部署与运维、自动化工具的使用以及遇到的问题和挑战。

#### 关键细节：

1. **DigitalOcean 简介**：
   - 成立于 [具体年份]，以简化云资源配置为核心理念。
   - 产品包括 Droplets（虚拟机）、Block Storage、Spaces（对象存储平台）等。
   - 全球八个区域的数据中心，最近完成 IPO。

2. **Ceph 使用情况**：
   - 用于 Block 和 Object 存储产品，总计 38 个生产集群，37 个在 Nautilus，1 个在 Luminous。
   - 总存储量超过 54 PB，包括全闪存和混合存储（HDD 和 QRC Flash）。

3. **选择 Ceph 的原因**：
   - 水平扩展、自愈能力、强一致性、性能可接受、支持多种存储产品。

4. **Ceph 操作流程**：
   - 高度自动化，使用 Ansible Playbooks 和 AWX。
   - 容器化部署，监控使用 Ceph Exporter 和 Node Exporter。
   - 自动化工具如 Archimedes 和 PgRemapper。

5. **遇到的问题**：
   - Ceph 升级过程中文档不足，动态重新分片可能导致 RGW 线程耗尽，Beast 后端默认线程设置可能不足。

#### 后续行动计划：
- 优化 Ceph 的自动化和监控工具。
- 加强 Ceph 升级和测试流程的改进。
- 考虑将更多产品迁移到 Ceph。

#### 其他信息：
- DigitalOcean 正在招聘，感兴趣的候选人可以查看招聘页面。
- 如有关于会议内容的疑问，可以联系 Alex Merrigan。

#### 会议结束：
感谢所有参与者的参与，祝大家有一个愉快的一天。