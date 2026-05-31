---
title: Enhancing Ceph Monitoring at CERN- Our Approach and Solutions - R. Valverde Cameselle & E. Bocchi
date: 2025-11-19
updated: 2025-11-19
tags:
- Ceph
- 监控
- 高可用性
- 可扩展性
- OpenStack
categories: 
- "视频总结"
subtitle: Enhancing_Ceph_Monitoring_at_CERN_-_Our_Approach_and_Solutions_-_R._Valverde_Cameselle_E._Bocchi
---

### CERN Ceph监控方案会议纪要

#### 会议基本信息
- **时间**：未明确（上午会议）
- **主讲人**：
  - Enrico（CERN SEF技术负责人）
  - Roberto（CERN SEF运维及监控负责人）
- **主题**：CERN如何通过增强监控方案优化Ceph存储系统的运维。

#### CERN及Ceph背景介绍
- CERN是全球最大的粒子物理实验室，位于法国-瑞士边境，运营着大型强子对撞机（LHC），产生海量数据。
- Ceph部署在CERN的存储环境中，规模约100 PB，包括object存储（RADOSGW）、block存储（RBD）和file存储（CephFS），用于IT服务、实验数据存储、备份和虚拟化存储。

#### 监控架构演进
- CERN早期使用Graphite进行监控，但面临数据查询和降采样问题。
- 2018年转型至Prometheus + Thanos，实现统一查询接口和自动降采样。
- 监控架构包括Prometheus、Thanos、Node Exporter、自定义脚本等，支持多数据中心双活部署。

#### 关键监控场景与故障排查
- 监控CephFS问题，如客户端会话和MDS内存泄漏。
- 监控多站点S3同步，通过自定义脚本解析同步状态。
- 联动基础设施监控，如网络问题、OpenStack OVN和Kubernetes。

#### 告警与自动化
- 分级告警，低优先级通过邮件/ServiceNow工单，高优先级通过Mattermost/Telegram即时通知。
- 硬件退役时，利用标签快速定位受影响节点。

#### 后续计划与社区协作
- 改进MDS慢请求监控，推动上游修复误导性日志。
- 加入Ceph科学用户组，分享HPC/研究场景经验。

#### Q&A重点
- 监控高可用：Thanos支持多实例读写，但CERN选择简单双活。
- 部署工具：主要用原生包，少数集群试用Cephadm。
- 硬件故障响应：依赖基础架构监控，按影响范围分级处理。

#### 行动项
- 短期：优化MDS慢请求监控标签。
- 长期：评估Thanos多活自动化。