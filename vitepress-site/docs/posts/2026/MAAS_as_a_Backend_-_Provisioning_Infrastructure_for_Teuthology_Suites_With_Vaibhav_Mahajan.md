---
title: "MAAS as a Backend- Provisioning Infrastructure for Teuthology Suites With Vaibhav Mahajan"
date: 2026-04-22
updated: 2026-04-23
tags:
  - "Teuthology"
categories:
  - "视频总结"
outline: deep
---
## 概述

本次演讲由来自 IBM India 的 DevOps 工程师 Vaibhav Mahajan 主讲，介绍了为 Teuthology（Ceph 的集成测试框架）新增的 MAAS（Metal as a Service）裸金属 provisioning 后端支持。演讲涵盖了架构设计、节点生命周期管理、配置要求以及实际演示。

## 背景：为什么选择 MAAS

Teuthology 目前支持三种 provisioning 平台：

- **Fog**：专用于裸金属的镜像与 provisioning 工具，需要预先配置
- **OpenStack**：虚拟化平台，支持部署 VM 并执行测试
- **MAAS（新增）**：提供类云体验的裸金属管理工具

选择 MAAS 的主要原因：

1. **丰富的 REST API**：MAAS 提供的 API 集合与 Teuthology 现有的 Fog 集成模式高度契合，支持机器的创建、删除等标准操作
2. **Cloud-init 支持**：可像云平台一样通过 cloud-init 文件完成节点初始化配置
3. **动态服务管理**：支持根据用户请求动态进行服务定位和服务器分配，提供真正的类云体验

## 系统架构与节点生命周期

### 整体工作流

Teuthology 负责主要的 inventory 管理，完整的节点生命周期如下：

1. **节点选择**：Teuthology 根据 suite 中指定的机器类型，或用户显式请求的特定机器名称，向 Padles（后端数据库）发送分配请求
2. **Provisioning**：请求推送至 MAAS 后，MAAS 负责处理 PXE 启动、OS 部署以及 cloud-init 配置
3. **测试执行**：Provisioning 完成后，Teuthology 通过 SSH 连接到机器，执行部署步骤和测试用例
4. **清理回收**：测试完成后，Teuthology 向 MAAS 发送删除请求，将机器恢复至 ready 状态

**重要约定**：Teuthology 中的机器名称必须与 MAAS 中的机器名称保持一致，需在配置 Padles 或 Pulpito 时统一管理。

## 部署要求

### MAAS 侧要求

- 已部署 MAAS controller，并完成机架（rack）配置
- 待管理的机器已添加至 MAAS 并处于 **ready 状态**（即空闲理想状态）
- 网络配置正确，Teuthology 控制节点可访问 MAAS 管理的子网
- 机器已完成 commissioning
- 已生成 API key（包含 consumer key、consumer token 和 secret）

### Teuthology 控制节点要求

- 运行 dispatcher 和 supervisor 进程
- 控制节点的 SSH 公钥需添加至 MAAS，以便 MAAS 在部署机器时将其注入为 authorized key
- 配置 Python 虚拟环境（与 Fog 后端要求相同）

### teuthology.yaml 配置

需在配置文件中新增以下字段：

```yaml
mas:
  api_url: http:/<maas-server>:5240/MAAS/api/2.0/
  api_key: <consumerkey>:<consumer_token>:<secret>
  machine_type: <类型标签>
  timeout: <超时时间（秒）>
  user_data: |
    # cloud-init 配置
    # 可配置用户、软件源等初始化内容
```

## 核心操作详解

### Lock（锁定）操作

锁定操作存在双重锁定机制：

- **Teuthology 侧锁定**：防止其他用户访问或操作该机器
- **MAAS 侧锁定**：防止对机器执行删除或更新等操作

操作流程：
1. Teuthology 向Paddles 查询可用机器
2. Paddles 分配机器并通知 supervisor
3. Teuthology 向 MAAS 发起REST API 部署请求

存在两种场景：
- **场景一**：机器处于 ready 或 new 状态 → 移至 allocated 状态 → 按指定 OS 类型和版本部署 → 锁定
- **场景二**：机器已处于 deployed 状态但在 Teuthology 中显示为未锁定 → 先解锁并释放 → 回到 allocated 状态 → 重新部署 → 锁定

如需覆盖锁定，可使用 Teuthology 的 `owner` 标签进行匹配。

### Unlock（解锁）操作

1. Teuthology 验证 Paddles 中的 inventory owner与请求发送者匹配
2. 向 MAAS 发送 release 请求

三种处理情形：
- 机器已处于 ready 或 allocated 状态（因状态不一致）→ 仅在 Teuthology 中标记为已释放，不做其他操作
- 机器处于 deploying 状态 → 中止部署，恢复至 ready 状态
- 机器处于 deployed 状态 → 释放并解锁，回归资源池

### Suite 执行流程

1. Dispatcher 获取所需测试 suite 列表
2. 将任务调度至 BeanStalkd 队列
3. Supervisor 读取任务，根据机器类型从资源池选取节点
4. 执行与 lock 操作相同的 MAAS 交互序列
5. 测试完成后，Teuthology 删除机器并将其恢复至 ready 状态

## 监控与故障排查

两套系统协同工作，提供完整的可观测性：

| 系统 | 用途 |
|------|------|
| **MAAS Dashboard** | 查看机器部署和清理的详细步骤日志 |
| **Pulpito Dashboard** | 监控 Teuthology 的执行、锁定等操作日志 |
| **Supervisor 日志**（控制节点） | 获取最详细的操作日志，也可通过 Pulpito 访问 |

PXE 启动等底层问题需直接依赖 MAAS 日志进行排查。

## 演示环节

演讲者使用 LXD（Linux Containers）环境进行了演示，展示了 MAAS 管理虚拟机的能力（MAAS 同样支持真实裸金属）：

- 搭建了一台 LXD 宿主机，添加了多台不同配置的 VM（如 burndup、prana 等），统一归类为 `lxd` 机器类型
- 在 Pulpito 中可见这些机器以 `lxd` 类型注册，部分处于 ready 状态，部分处于 deployed 状态
- 演示了单机锁定（`lock` 命令）、单机解锁（`unlock` 命令）以及多机批量锁定（`lock many）操作
- 演示了完整的 smoke test suite 执行流程，包括 dispatcher 调度和 supervisor 节点选择

LXD 机器的 commissioning 流程：在 MAAS 中创建机器后，需配置 power 类型为 LXD，提供宿主机地址、实例名称和证书，完成 commissioning 后机器进入 allocated 状态，分配给用户后变为 ready 状态。

## 总结

MAAS 作为 Teuthology 的新 provisioning 后端，配置简单，只需：

1. 在 `teuthology.yaml` 中添加 MAAS 相关配置
2. 将 Teuthology 控制节点的 SSH 公钥添加至 MAAS

在网络配置正确的前提下，即可实现与 Fog 后端同等的裸金属自动化测试能力，同时获得更好的类云管理体验和更丰富的 API 支持。
