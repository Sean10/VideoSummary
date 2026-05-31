---
title: From Chaos To Clarity- Systematic Ceph Cluster Analysis for Rapid Troublesho... S. Zhang & J. Blanch
date: 2025-11-19
updated: 2025-11-20
tags:
- 分布式存储
categories: 
- "视频总结"
subtitle: From_Chaos_To_Clarity_-_Systematic_Ceph_Cluster_Analysis_for_Rapid_Troublesho..._S._Zhang_J._Blanch
---

## 会议纪要

在Clyo公司的Josh和Stephen的主持下，本次会议重点介绍了Ceph集群分析方法和他们开发的工具集。会议内容分为两部分：第一部分讲解了如何分析Ceph集群的健康状况和潜在问题；第二部分则介绍了他们开发的CLI工具“auto”（Dr. Octopus）以及相关的Web分析工具。

### 主要议题

**1. Ceph集群分析流程**

- **初始检查**：使用`ceph health`和`ceph status`命令进行初步检查，但“health OK”状态并不能完全保证集群健康。
- **数据收集**：通过`ceph-diagnostic`脚本收集CephFS、Ceph df、PG dump等基础数据。
- **分析管道**：
  - 检查Ceph版本及已知关键bug。
  - 数据平衡分析（检查PG分布不均问题）。
  - CRUSH规则分析（检查规则重叠和跨域问题）。
  - OSD性能分析（延迟、命中率等问题）。
  - CephFS特定分析（MDS的create/unlink延迟，“noisy neighbor”问题）。
  - RGW分析（检查bucket的autosharding配置和多站点设置）。

**2. 分析工具介绍**

- **auto (Dr. Octopus)**：
  - 单一二进制CLI工具，整合了日常运维脚本（如主机下线、PG重映射等）。
  - 支持对收集的数据进行深度分析。
  - 包含文档化的标准操作流程（如主机下线步骤）。
- **Web分析工具**：
  - 提供集群健康评分（基于约30-40项检查）。
  - 版本采用统计（显示18.2.7正在成为主流稳定版本）。
  - 配置对比工具（可比较不同Ceph版本的2100+配置项）。

### 关键发现

1. **版本趋势**：
   - 18.2.7逐渐取代17.2.7成为最稳定版本。
   - 新版本集群中出现更多"C"评分（需关注原因）。
2. **常见问题**：
   - PG分布不均导致的性能热点。
   - CRUSH规则配置不当影响autoscaling。
   - RGW中autosharding未启用导致的性能问题。
   - 硬件配置不当（如rocksdb放在旋转磁盘上）。

### 行动计划

1. **工具推广**：
   - 将auto CLI工具开源（GitHub可用）。
   - 考虑将配置对比工具整合到ceph.io网站。
2. **功能增强**：
   - 开发改进版balancer（基于OSD利用率）。
   - 开发类似k9s的TUI界面。
   - 增加更多配置检查项。
3. **社区协作**：
   - 收集更多用户反馈改进工具。
   - 持续更新已知bug数据库（通过YAML文件维护）。

### Q&A重点

1. **版本bug跟踪**：通过硬编码notorious bugs（如Pacific的PG merge/split bug）。
2. **配置错误模式**：无法直接从ceph report获取配置（因安全考虑），但可通过CLI工具检查。
3. **数据展示**：所有分析基于原生Ceph数据，工具仅重组和可视化。

### 资源链接

- GitHub仓库：包含auto CLI工具源码。
- 分析网站：analyzer.claso.com

会议以讨论如何进一步改进工具和增强社区协作为结束。