---
categories:
- 视频总结
date: 2020-08-25
subtitle: Ceph_Day_CERN_2019_-_Utilising_Ceph_for_large_scale_to_support_the_LHC_experiments_-_Tom_Byrne
tags:
- Ceph
- LHC实验
- 分布式存储
- 高吞吐量
- 数据处理
title: Ceph Day CERN 2019- Utilising Ceph for large scale to support the LHC experiments - Tom Byrne
updated: 2020-08-26
---


会议纪要：

### 会议主题

利用Ceph支持大型高吞吐量存储以支持LHC实验

### 会议参与者

Tom Byrne等

### 会议内容总结

1. **Ceph集群介绍**：
   - Tom Byrne介绍了名为ECHO的Ceph集群，该集群位于英国的Rutherford Appleton实验室，服务于LHC实验。
   - ECHO集群拥有180个存储节点，5000个OSDs，并准备扩展。
   - 数据池采用EC 8+3配置，使用librados striker，对象大小为64MB。
   - 集群运行在Luminous版本，并开始测试Mimic版本。

2. **LHC实验背景**：
   - LHC实验在全球LHC计算网格中有大量计算和存储需求，Tier 1站点提供约40%的计算和存储资源。
   - ECHO集群为LHC实验提供所有磁盘存储，支持大规模数据处理。

3. **数据处理流程**：
   - 实验数据从Tier 0转移到Tier 1存储，如ECHO集群，并模拟大量碰撞数据。
   - 数据需要重建，从探测器读数到粒子的动量和轨迹，通常在Tier 1进行。

4. **数据访问架构**：
   - 主要使用GridFTP进行广域网传输，XRootD用于作业输入输出文件传输。
   - 集群通过7个网关机器提供服务，XRootD服务器基础设施被容器化。

5. **监控和性能问题**：
   - 集群运行稳定，但偶尔会出现性能问题，影响外部传输。
   - 缺乏监控使得定位和解决这些问题变得困难。
   - 通过脚本收集慢请求的详细信息，并将其导入Elasticsearch进行分析。

### 决定事项

- 继续监控和优化ECHO集群的性能，特别是解决已知的性能瓶颈。
- 等待Ceph新版本的发布，以解决当前已知的问题。

### 后续行动计划

- 加强集群的监控系统，确保能够及时发现和解决性能问题。
- 继续测试和部署Ceph的新版本，以利用新功能和修复。
- 优化数据处理流程，提高数据传输和处理的效率。

### 关键词

- Ceph
- ECHO集群
- LHC实验
- Tier 1站点
- GridFTP
- XRootD
- Elasticsearch
- OSDs
- librados striker