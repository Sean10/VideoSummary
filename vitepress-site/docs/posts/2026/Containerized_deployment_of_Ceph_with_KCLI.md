---
title: "Containerized deployment of Ceph with KCLI"
date: 2026-05-12
updated: 2026-05-12
tags:
  - "Ceph"
  - "容器化"
  - "编排"
categories:
  - "视频总结"
outline: deep
---
## 概述

本次分享由 Crimson 团队成员 Shraddha 主讲，介绍了如何使用 KCLI 工具在容器化环境中部署 Ceph 集群。内容涵盖了 KCLI 的基本概念、配置方式、Classic OSD 与 Crimson OSD 的部署流程，以及实际演示中遇到的常见问题与解决方案。

## 为什么需要容器化部署

在使用 KCLI 之前，Shraddha 的开发方式是在本地开发机上进行裸机（bare metal）安装。这种方式存在以下几个明显局限：

- **OS 版本锁定**：只能使用开发机上已安装的特定 OS 版本，难以复现在其他环境下出现的问题。
- **镜像 tag 难以对齐**：当用户使用特定 tag 时，裸机环境下很难精确匹配，排查问题效率低。
- **cephadm 与 dashboard 部署困难**：涉及 cephadm 或 dashboard 的开发调试在裸机环境下操作繁琐。
- **Rocky 10 推广受阻**：团队正在推进 Rocky 10 在Ceph 中的全面支持，容器化部署可以大幅加速这一进程。

使用 KCLI 的容器化部署方案可以消除上述约束，让开发者专注于实际问题本身，而不是环境差异带来的干扰。

## KCLI 简介

KCLI 是一个为不同虚拟化提供商提供统一用户体验的工具。它可以：

- 按需 provision 虚拟机（VM），自由指定 OS 镜像、内存、CPU 数量
- 配置磁盘类型（NVMe、SSD、HDD）和磁盘大小
- 自动安装指定软件包
- 将本地源码目录挂载到 VM，实现代码修改实时生效，无需重复构建和部署

## KCLI 配置文件结构

KCLI 的核心是一个 YAML 格式的配置文件（`ceph-cluster.yaml`），主要包含以下部分：

- **parameters段**：定义节点数量、IP offset、磁盘大小、CPU 数量、使用的 OS 镜像等全局参数。
- **节点定义段**：为每个节点单独配置镜像、SSH 密钥、网络、存储池（pool）等。
- **源码挂载**：可将本地 Ceph 源码目录挂载到 VM，修改立即同步到运行中的集群。
- **文件与脚本复制**：支持将特定脚本或配置文件复制到 VM 节点。
- **bootstrap 脚本**：定义 Ceph 特定的初始化逻辑，包括 Classic 和 Crimson 两种模式。

## Classic OSD 部署流程

Classic 模式的 bootstrap 脚本流程相对简单：

1. 指定 Ceph 镜像（可以是 release 镜像、CI 构建的开发镜像或自定义镜像）
2. 下载并赋予 cephadm 二进制可执行权限
3. 执行 `cephadm bootstrap` 命令，可配置 dashboard 初始密码、是否跳过 monitoring 等选项
4. 从配置中获取 FSID
5. 为每个节点复制 SSH 密钥并加入集群
6. 通过 `ceph orch apply OSD` 命令批量部署 OSD

## Crimson OSD 部署流程

Crimson 模式在 Classic 基础上增加了若干配置步骤：

1. 同样定义镜像、部署 cephadm、执行 bootstrap
2. 启用 Crimson feature flag
3. 设置默认 pool 类型为 Crimson
4. 配置 `crimson_cpu_num` 等 Crimson 专属参数
5. 添加调试相关配置（便于开发调试）
6. 部署 Crimson OSD：在 `ceph orch apply OSD` 命令中添加 `--osd-type crimson` 参数，或使用 `ceph orch add OSD` 单独添加指定 OSD

## 实际演示要点

演示分为 Classic 和 Crimson 两个集群的完整部署过程，关键步骤如下：

**环境准备：**
- 更新包管理器
- 安装 libvirt（虚拟化引擎）
- 将当前用户加入 libvirt 组
- 配置 SSH，开启 `PermitRootLogin yes` 并重启 SSH 服务
- 生成 SSH 密钥（若不存在）

**KCLI 初始化：**
- 安装 KCLI（官方提供一键安装脚本）
- 创建默认 pool 和默认网络
- 下载所需 OS 镜像（演示使用 Fedora 43；也支持自定义镜像，通过 `-H` 参数指定 URL）

**集群部署：**
- 使用 `kcli create plan` 命令基于 YAML 配置文件创建集群
- VM 启动后自动执行 bootstrap 脚本
- 通过 `cloud-init` 输出日志（`/var/log/cloud-init-output.log`）跟踪部署进度
- 使用 `podman ps` 查看容器启动状态
- 使用 `cephadm shell` 进入 Ceph 管理环境执行 `ceph health`、`ceph pg dump` 等命令验证集群状态

**Crimson 集群特别注意事项：**
- 部署新集群前必须删除旧的 plan 并重建网络，否则会出现难以排查的网络错误
- 多人共用同一台机器时，每人应使用不同的 network 和 pool
- 若使用 OSD spec 文件，需确保该文件已在 `ceph-cluster.yaml` 中配置为复制到 VM
- 镜像 tag 必须明确指定，否则无法拉取镜像

**验证 Crimson OSD：**
- 查看 OSD 日志，确认 Crimson 进程已启动，即可确认为 Crimson OSD

## 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 找不到 OSD spec 文件 | YAML 中引用了未复制的文件 | 在 `ceph-cluster.yaml` 中添加文件复制配置 |
| 无法拉取镜像 | 未指定镜像 tag | 在配置中明确指定完整 tag |
| MON 无法获取 IP | 缺少网络工具包 | 在 bootstrap 脚本中预装所需网络工具 |
| SSH 连接失败 | 未开启 root 登录或密钥缺失 | 配置 `PermitRootLogin yes`，确保密钥存在 |
| 磁盘空间不足 | 配置的磁盘大小过小 | 调整 YAML 中的磁盘大小参数 |

## Q&A 摘要

**KCLI 的系统要求？**
KCLI 本身安装要求不高，但 VM 的资源需求取决于配置文件中的定义。已验证可用的系统包括 Ubuntu、Fedora 和 RHEL。

**旧镜像的磁盘空间清理？**
需要手动清理，KCLI 不会自动回收未使用镜像占用的空间。

**能否对 KCLI 集群执行升级？**
可以，使用 cephadm 在 KCLI 集群上执行升级完全可行。

**集群使用完毕后如何销毁？**
建议及时销毁，避免占用系统资源（尤其是日志会持续增长）。销毁命令为 `kcli delete plan <plan-name>`，操作非常简单。

## 参考资源

- Classic 部署配置：GitHub 仓库（以该仓库为配置的 source of truth）
- Crimson 部署配置：Ceph Wiki 页面（包含 Crimson 专属配置说明）
- 问题反馈：可通过 Slack 或邮件列表联系 Shraddha，团队也在考虑为 KCLI 相关讨论创建专属 Slack 频道
