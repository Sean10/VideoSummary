---
title: Per-Subvolume IO Metrics in CephFS - Igor Golikov & Alex Markuze, IBM
date: 2025-11-19
updated: 2025-11-20
tags:
- CephFS
- 分布式存储
- Ceph
categories: 
- "视频总结"
subtitle: Per-Subvolume_IO_Metrics_in_CephFS_-_Igor_Golikov_Alex_Markuze_IBM
---

### 改进后的中文总结

CephFS Subvolume Metrics 设计与未来观测性增强会议纪要

本次会议主要讨论了Ceph文件系统（CephFS）中Subvolume级别IO指标的引入及其未来观测性增强方案。以下是会议的关键点：

**会议概述**

- **主持人**: Eager Goov (IBM CephFS团队) 与 Alex Marcus (IBM CephFS团队)
- **核心主题**: CephFS subvolume metrics 新特性及其未来观测性增强方案
- **技术领域**: 分布式存储，CephFS，指标收集，异常检测

**关键讨论点**

1. **Subvolume Metrics 特性介绍**
   - **背景动机**: 针对大规模Ceph集群中数千甚至数万个subvolumes，传统per-client监控无法定位热点路径性能瓶颈，需细粒度观测特定路径的IO活动状态。
   - **核心需求**: Subvolume级别指标收集，高可扩展性，最小性能影响，MDS ranks间一致性，复用现有metrics基础设施，自动修剪非活跃metrics。
   - **指标设计**: 数据类型包括IOPS/throughput/latency，采用30秒滑动窗口，平滑短期IO峰值，限制内存使用，自动清理非活跃路径指标。

2. **系统架构**
   - **数据流**: Client记录单次IO操作，定期发送统计到关联MDS，MDS汇总数据到rank0 MDS，rank0 MDS维护全局滑动窗口聚合。
   - **关键技术点**: Client通过MDS元数据响应识别subvolume路径，避免client端持久化存储，加权平均计算。

3. **指标暴露**
   - 通过标准接口输出：Admin socket (`ceph daemon mds.<id> perf dump`), Prometheus exporter，未来将集成到`cephfs-top`工具。
   - JSON格式示例包含：Filesystem名称，Subvolume标识，读写IOPS/吞吐量/延迟。

4. **未来工作计划**
   - **短期增强**: 增加metadata操作指标，支持自定义路径监控，用histogram替代平均值，Kernel client支持。
   - **长期方向**: 异常检测系统，日志向量化分析，预测性洞察能力建设。

**Q&A重点摘要**

- **客户端支持范围**: 当前仅FUSE实现，NFS Ganesha理论上应兼容，Kernel client支持正在开发中。
- **滑动窗口配置**: 30秒为默认值，可通过配置参数调整。
- **K8s集成**: 目前缺乏PVC/PV与subvolume的直接关联，建议通过subvolume group命名实现间接关联。
- **Prometheus输出**: 当前设计采用服务端计算，讨论是否改为原生counter供客户端灵活计算。
- **细粒度分析**: 当前为subvolume聚合指标，未来可能增加per-client细分。

**行动计划**

- **短期交付**: 完成kernel client支持，增加subvolume监控配置灵活性，评估histogram实现方案。
- **长期研究**: 建立异常检测POC，开发日志-指标关联分析能力，优化时间序列预测模型。
- **社区协作**: 邀请用户提供生产环境指标数据，异常场景日志记录，使用场景反馈。

本次会议在技术讨论和社区协作倡议中结束，与会者对新特性的实用价值和未来方向表示积极认可。