---
title: Cephadm at Scale for Detractors- Why its time to reconsider containerized Ceph deployments
date: 2025-05-08
updated: 2025-05-09
tags:
- Ceph
- Cephadm
- 容器化
- 分布式存储
- 可扩展性
categories: 
- "视频总结"
subtitle: Cephadm_at_Scale_for_Detractors_-_Why_it_s_time_to_reconsider_containerized_Ceph_deployments
---

Cephadm at Scale for Detractors- Why its time to reconsider containerized Ceph deployments 这次会议纪要深入探讨了Ceph部署的历史、容器化趋势以及Ceph在大规模集群中的表现。

1. **会议背景与目标**：主讲人分享了与Ceph的渊源，回顾了11年前在Acme公司使用Ceph的经历，并讨论了Ceph部署的历史、容器化趋势以及Ceph在大规模集群中的表现。

2. **Ceph部署的历史**：从早期的自定义Ansible脚本部署到Cephadm的出现，Ceph的部署工具经历了演变。容器化趋势简化了Ceph的部署和管理，Cephadm成为主流。

3. **容器化的优势与挑战**：容器化提供了可重复的环境、隔离性、移植性和性能优势，但也增加了管理和故障排查的复杂性，以及安全性的持续关注。

4. **Ceph在大规模集群中的表现**：Ceph在2021年进行的规模测试中表现出色，但性能问题主要集中在监控和管理模块上。Cephadm agent的引入有助于减轻集中式管理的压力。

5. **未来挑战与目标**：Ceph社区致力于实现10,000个OSD的集群，并对生产环境中的Ceph集群规模提出了建议。

6. **社区贡献与反馈**：鼓励用户通过提交问题、反馈和文档贡献来帮助Ceph社区的发展，并呼吁运行大规模Ceph集群的用户参与到社区中。

7. **后续行动计划**：计划在未来的社区活动中组织大规模集群用户的讨论，并探讨如何鼓励更多的大规模集群用户参与到Telemetry中，以便更好地了解Ceph在全球的实际使用情况。

本次会议强调了Cephadm在容器化部署中的重要性，并讨论了Ceph在大规模集群中面临的挑战和未来发展方向。