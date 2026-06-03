---
title: "Running Teuthology Outside of the Sepia lab With Deepshikha Singh"
date: 2026-01-15
updated: 2026-01-16
tags:
  - "Teuthology"
  - "OpenStack"
  - "CI/CD"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
## 概述

本次分享由 Deepshikha Singh 主讲，介绍了如何在 Sepia 实验室之外的自有 OpenStack 环境中运行 Teuthology 测试框架。核心目标不是引入新的工作流，而是让各团队能够使用自己的基础设施执行与 Sepia 实验室（CPI）相同的测试套件。

## 执行流程

Teuthology 从一个专用的控制 VM 运行，该 VM 承载 dispatcher 和编排逻辑。Supervisor 节点在基础设施 VM 上动态 provision，用于触发测试套件（suite）和任务（job）。

从测试角度来看，测试套件的执行方式与在 CPI 中完全一致，区别仅在于运行在虚拟机而非真实硬件上。任务完成后，结果和日志会归档到 archive 目录，并通过 Pulpito 对外提供访问，保持与上游一致的可见性体验。

**当前已知限制：**
- Power cycle 相关测试不支持（需要 IPMI 硬件支持）
- Ceph store（BlueStore）基于真实磁盘的测试不支持（需要物理磁盘）
- 上述限制在近期内预计不会解除，因为这些测试本质上依赖真实硬件

## 基础设施前提条件

启动前需满足以下条件：

- 拥有可用的 OpenStack 项目及有效凭据
- Teuthology 依赖以下标准 OpenStack 服务：
  - **Keystone**：认证（authentication）
  - **Nova**：计算资源
  - **Neutron**：网络
  - **Cinder**：存储卷
- 一台控制 VM 用于托管服务
- 网络需正确配置，包括 security group 和 floating IP（实例需要外部访问权限以拉取代码仓库）
- 需创建 SSH 密钥对并上传至 OpenStack（Teuthology 用于节点访问）

**基础套件推荐资源配置（最低）：**
- 24 vCPU
- 48 GB RAM
- 240磁盘（跨所有 provision 资源合计）

## 控制节点配置

控制节点为轻量级 VM，推荐配置如下：
- 操作系统：Ubuntu 22.04
- 4 vCPU、8 GB RAM、50 GB 磁盘
- 随着运行规模扩大，日志存储需求增加，磁盘空间需相应扩展

**配置步骤：**
1. 克隆 Teuthology 代码仓库
2. 运行 bootstrap 脚本安装依赖
3. Teuthology 在 Python 虚拟环境中运行，需激活该环境
4. 在 `clouds.yaml` 文件中配置 OpenStack 凭据
5. 通过 `openstack server list` 等命令验证访问是否正常
6. 在 `teuthology.yaml` 中定义 OpenStack 专属配置，包括 cloud 设置、镜像（image）、规格（flavor）和网络详情

## 实际执行流程

```
1. 使用 SSH 密钥和 --setup 参数初始化 Teuthology
   （--setup 会自动配置 Pulpito、Padles、PostgreSQL、Beanstalkd 等支撑服务）

2. 以 OpenStack 模式启动 dispatcher，启用动态 provisioning

3. 指定 machine type 为 openstack、Ceph 代码仓库及 job数量上限，触发测试套件
   （后续触发时可跳过 --setup 步骤）
```

smoke 套件是验证基础功能的推荐起点，至少包含一个 job、最多使用三个节点。

## 监控与结果查看

- **Dispatcher 日志**：用于诊断 provisioning 或调度问题
- **Archive 目录**：存储每次运行的详细日志，供深度调试
- **Verbose 模式**：执行时加 `--verbose` 参数可获得更多运行时信息
- **Pulpito**：提供高层次的 job 状态、结果和历史运行记录，与上游工作流保持一致

关于 Pulpito 实例：当前使用的是下游（downstream）自建实例，通过 `--setup` 参数会在控制节点上自动完成部署。Shaman 目前仍使用上游实例，是否可以覆盖为自建实例尚不确定。

## 当前进展与后续计划

- 正在积极扩大 Teuthology 在 OpenStack 上的测试覆盖范围，增加 job 数量并提升稳定性
- 持续改进可复现性（reproducibility），减少测试抖动（flakiness）
- **Mass 模式执行**已合并（昨日刚合并），现已支持基于 Mass 的执行模型
- **OpenShift 模式执行**已在 PoC 层面完成验证
- 正在评估本地和实验室工作流，以改善开发者体验
- 探索 PR 触发和分布式 CI 模型，面向更广泛的社区使用
