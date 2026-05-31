---
categories:
- 视频总结
date: 2022-02-22
subtitle: Ceph_Orchestrator_Meeting_2022-02-22
tags:
- Ceph
- 监控
- 存储优化
- 高可用性
title: "Ceph Orchestrator Meeting 2022-02-22"
updated: 2022-02-23
---


本次Ceph Orchestrator会议主要讨论了以下议题：

1. **主机缓存对象问题**：当前主机缓存对象过大，影响了Monkey Store的性能。会议提出了增加Monkey Store大小限制、分割主机缓存对象、使用数据压缩等解决方案。

2. **配置和密钥环存储位置**：讨论了将配置和密钥环从Etsy Stuff迁移到var/lib/fsid的可能性，以提高管理和推理的便利性。决定支持在两个位置同时存储的方案。

3. **Prometheus版本升级**：讨论了升级Prometheus版本的需求，特别是为了支持外部Prometheus实例的功能。建议升级到2.28版本。

4. **支持外部Prometheus实例**：讨论了如何支持用户使用外部的Prometheus实例来监控Ceph集群。决定在Ceph中创建一个端点供外部Prometheus实例获取配置信息。

5. **Prometheus高可用性（HA）配置**：讨论了使用RBD图像存储Prometheus的配置和数据以实现高可用性。会议对此方案提出了多个问题，包括依赖集群本身的可用性、数据写入的复杂性以及存储需求等。

会议决定事项包括：探索分割缓存对象和数据压缩的解决方案、支持在两个位置同时存储配置和密钥环、进一步研究和测试Prometheus版本升级的可行性、开发外部Prometheus实例的端点支持、讨论和评估Prometheus HA配置的可行性。

后续行动计划包括：实施主机缓存对象分割和数据压缩的方案、实现配置和密钥环在两个位置同时存储的功能、进行Prometheus版本升级的测试和验证、开发并测试外部Prometheus实例的端点支持、进一步讨论和评估Prometheus HA配置的可行性。