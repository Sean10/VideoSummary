---
title: Efficient Ceph Performance Troubleshooting in Production Using eBPF - Dongdong Tao, Canonical
date: 2025-11-19
updated: 2025-11-20
tags:
- Ceph
- 存储优化
- 分布式存储
categories: 
- "视频总结"
subtitle: Efficient_Ceph_Performance_Troubleshooting_in_Production_Using_eBPF_-_Dongdong_Tao_Canonical
---

### Ceph性能生产故障排除研讨会纪要

## 会议概述
本次研讨会由Dongdong Tao主持，介绍了其开发的Ceph Safe Trace项目，这是一个基于eBPF的强大性能追踪工具集，用于高效诊断Ceph集群性能问题。研讨会通过实际生产案例展示了这些工具如何显著提升性能故障排查效率。

## 关键讨论点

### 1. Ceph性能问题现状
- 性能问题可能表现为：慢请求、IOPS下降和延迟增加。
- 传统排查方法（如`perf dump`和调试日志）效率低下，缺乏对操作全生命周期(`life cycle latency`)的测量能力。

### 2. Safe Trace项目核心
- 设计目标：测量OSD操作的`life cycle latency`，准确定位IO路径中的瓶颈。
- 技术实现：通过eBPF程序在关键函数（如`inq_op`/`dq_op`）注入时间戳，结合`client ID`和`request ID`关联同一IO操作。

### 3. 主要工具介绍
#### OSD Trace
- 功能：追踪任意Ceph OSD进程，输出每个IO操作的详细生命周期延迟。
- 延迟分解：包括Messenger层、OSD层、BlueStore层和关键指标。

#### Rados Trace
- 特点：可追踪任意librados-based客户端（如VM、Cinder、RGW等）。
- 输出信息：进程ID、客户端ID、PG ID、参与的OSD、端到端延迟等。

### 4. 生产案例分享
- 案例1：高尾延迟问题，通过OSD Trace发现网络路径问题。
- 案例2：EC镜像克隆性能问题，通过优化`extent_cmp`操作，性能提升显著。

### 5. 容器化支持
- 已支持通过`cephadm`部署的容器化进程追踪。
- 无需安装调试符号，最低内核版本要求：5.8。

## 演示环节
- 问题复现：通过fio测试显示SSD集群出现高尾延迟。
- 诊断流程：使用Rados Trace定位问题OSD，再用OSD Trace确认瓶颈。
- 修复验证：修复网络问题后，高尾延迟消失。

## 未来计划
- 开发`MDS Trace`：追踪MDS请求的生命周期延迟。
- 实现`kernel FS trace`：追踪CephFS内核客户端的元数据IO。
- 扩展平台支持：已验证Ubuntu/CentOS Stream，计划支持更多Linux发行版。

## 问答环节
- 依赖项：极简（主要用C/C++实现，无需BCC）。
- RocksDB设备监控：理论上可通过eBPF注入实现（待开发）。
- 性能影响：单OSD追踪对IOPS影响可忽略。

## 后续行动
- 推广工具使用：项目已开源（GitHub仓库提供）。
- 欢迎社区贡献：包括测试框架开发和多平台适配。
- 参考资源：Ceph AC 2023演讲材料、项目README中的操作指南。

研讨会以掌声结束，与会者对工具的实际价值表示高度认可。