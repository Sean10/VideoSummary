---
title: "Using Rook in Production on National Research Platform - Dmitry Mishin, UCSD SDSC"
date: 2025-11-19
updated: 2025-11-20
tags:
  - "Rook"
  - "Ceph"
  - "Kubernetes"
  - "分布式存储"
  - "云计算"
categories:
  - "视频总结"
outline: deep
---
在本次会议中，Dmitry Mishin（San Diego Supercomputer Center, UCSD）分享了National Research Platform（NRP）项目中使用Rook管理Ceph分布式存储的经验。以下是会议内容的总结：

### 会议概述
- 主讲人：Dmitry Mishin
- 主题：NRP项目中使用Rook管理Ceph分布式存储的经验分享
- 背景：NRP是一个由70多个教育机构组成的科研计算平台，提供免费的计算资源和网络实验环境。

### NRP项目简介
- NRP最初用于测量高校间科学网络链路性能，后发展为基于Kubernetes的大规模集群。
- 资源规模：1500+ GPUs，30000 CPU核心，177TB RAM，存储集群总容量13PB（800+ OSDs）。
- 网络架构：全美节点通过Science DMZ互联，支持跨地域存储访问。

### Ceph与Rook的集成模式
- NRP中Ceph主要通过Rook管理，讨论了四种集成方式：
  1. Rook全托管模式：Rook自动部署Ceph（包括CSI Driver），简化管理。
  2. Rook外部集群模式：手动部署Ceph，Rook仅管理Kubernetes端接入。
  3. 手动安装CSI Driver：直接对接已有Ceph集群，NRP未使用此模式。
  4. Host Path直连模式：节点直接挂载CephFS/RBD，适用于Slurm/Lustre环境。

### NRP中的Ceph存储池现状
- 多集群部署：8个Ceph集群，部分区域/本地专用。
- 数据规模：12000+ Persistent Volumes (PVs)，800+ OSDs。

### Rook的优势与挑战
**优势**：
- 快速部署：自动配置Ceph和CSI Driver，适合中小规模集群。
- Kubernetes原生管理：通过Pod/Logs监控组件，无需SSH。
- 资源调度：Kubernetes自动分配MDS/OSD等资源。

**挑战**（多集群大规模场景）：
- 集群管理耦合：单个集群故障可能阻塞其他集群的操作（如升级）。
- NVMe限制：单NVMe盘用于BlueStore/RocksDB，故障需整节点替换。
- 性能与扩展性问题：过去Rook Operator因并发读取ConfigMap导致API过载（已修复），配置变更耗时。

### 结论与建议
- 推荐场景：中小规模Kubernetes集群（如云环境快速部署）。
- 注意事项：
  - 多大型集群需预先评估管理耦合风险。
  - 优先使用Host Network（避免Overlay性能损耗）。

### Q&A环节
- 讨论聚焦于多集群运维经验和NVMe优化方案。

Dmitry Mishin在会议中分享了NRP项目使用Rook管理Ceph的经验，并讨论了Rook在多集群大规模场景下的优势与挑战。这对希望了解Rook在实际生产环境中应用情况的技术人员具有重要的参考价值。