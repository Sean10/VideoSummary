---
title: "Modernizing Ceph Deployments at CERN- CephFS and Object Storage Across Data Centres - Enrico Bocchi"
date: 2025-11-19
updated: 2025-11-19
tags:
  - "CephFS"
  - "分布式存储"
  - "CERN"
categories:
  - "存储技术"
  - "Ceph"
  - "数据中心"
  - "会议总结"
  - "存储架构"
outline: deep
---
## 会议基本信息

- **演讲者**：Enrico（CERN SEF 技术负责人）
- **会议主题**：CERN 中 Ceph 存储部署的现代化升级方案
- **主要内容**：聚焦 CephFS 优化、多文件系统部署、跨数据中心存储方案

## 核心讨论内容

### 1. Ceph 在 CERN 的现状

- **部署规模**：20个生产集群，约100PB容量，分布在3个不同位置
- **主要用例**：
  - Kubernetes/OpenShift PVC 后端存储
  - HPC 暂存和临时空间
  - 软件编译和分发（RPM）
  - 替代 Windows DFS（CephFS+SMB 原型）
  - 新型 home 目录服务（CephFS over NFS）

### 2. CephFS 运营挑战

- **关键问题**：
  - 缺乏客户端 metadata 请求限流机制
  - 高并发目录操作导致的性能问题
  - MDS 崩溃风险（特别是驱逐客户端时）
  - 备份方案不足（未使用 snapshots）

### 3. 现代化部署方案

- **架构优化方向**：
  - 从大型单一文件系统转向专用文件系统
  - 通过 OpenStack Manila share types 实现隔离
  - 构建 availability zones 实现跨数据中心冗余

- **技术实现**：
  - 同集群部署多个文件系统
  - 每个文件系统配置独立 MDS
  - 与 Kubernetes CSI 深度集成

### 4. 多文件系统运营经验

- **优势**：
  - 更好的隔离性和可控性
  - 独立配置调优
  - 滚动升级可能性

- **灾备注意事项**：
  - 默认文件系统恢复顺序问题
  - 推荐客户端明确指定文件系统名挂载

### 5. Metadata 负载均衡测试

- **测试方法**：
  - 基于 IO500 MDtest 基准
  - 对比不同策略：自动平衡、手动 pinning、ephemeral pinning

- **主要发现**：
  - 自动平衡器在高负载时性能下降
  - 手动 pinning 提供最佳控制但需管理员介入
  - Ephemeral pinning 策略效果因工作负载而异

### 6. 跨数据中心方案

- **CephFS 跨 DC**：
  - 通过 CRUSH rule 确保每个 DC 有数据副本
  - 利用 MDS join FS tag 实现"偏好"数据中心
  - 客户端本地读优化待完善

- **对象存储跨 DC**：
  - 传统多站点配置（primary+secondary）
  - 通过前端负载均衡器实现透明访问
  - 利用新增 HTTP headers 检查复制状态

## 未来工作计划

1. **对象存储整合**：
   - 统一管理三个对象存储集群
   - 开发自动化数据迁移工作流

2. **备份增强**：
   - 与磁带存储系统集成
   - 评估 RGW zipper 提供 S3-to-POSIX 接口

3. **客户端优化**：
   - 完善跨 DC 读取本地性
   - 改进 metadata 限流机制

## 问答环节重点

1. **灾备故障转移**：
   - 当前采用手动切换模式，secondary 集群保持 read-only
   - 确保强一致性，避免数据丢失

2. **备份方案**：
   - 当前备份目标为专用 HDD 集群或磁带系统
   - 未来计划实现更统一的备份接口

## 行动项

1. 评估 S3 到磁带的工作流自动化方案
2. 完善跨数据中心读取的客户端配置
3. 推进多文件系统在生产环境的进一步部署

[改进后的中文总结内容结束]