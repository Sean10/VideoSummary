---
title: Barriers between Ceph Development and Ceph Support
date: 2026-04-02
updated: 2026-04-03
tags:
- Ceph
- 容器化
- 分布式存储
categories: 
- 视频总结
subtitle: Barriers_between_Ceph_Development_and_Ceph_Support
---

## 演讲背景

本次演讲由来自 Croyd 公司的 L2 Ceph 支持工程师 K. Gopalakrishnan 主讲。Croyd 成立于 2017 年，专注于简化 Ceph 的部署与管理，提供 Ceph 管理 UI，并向用户提供技术支持服务（support@croyd.io）。

## 核心议题：从用户到开发者的 Bug 修复流程

### 理想流程

演讲者以"故事"的形式逐层拆解了 Ceph 生态中各角色的工作流程：

**用户视角**：用户在 Ceph 集群上发现 bug → 联系支持团队 → 支持团队联系开发者 → 修复被开发、测试、打包 → 用户收到修复。

**开发者视角**：
1. `git clone` Ceph 仓库，在新分支上 checkout
2. 编写修复代码，经过 review 和迭代
3. 通过 `vstart.sh` 进行构建测试
4. 提交最终 commit，生成 patch set或 PR
5. 将修复 backport 到 release/stable 分支
6. 通过独立的打包和发布渠道完成部署

**Maintainer 视角**（以 Proxmox、SUSE、Ubuntu 等下游发行商为例）：
- 获取 bug 通知和 patch
- 在自有基础设施中重新构建软件包
- 通过自有渠道推送给用户

在基于软件包（package-based）的部署模式下，上述流程运转良好：用户无需自建基础设施，无需等待新版本发布，修复交付快速高效。

## 核心问题：容器化部署带来的新挑战

### 背景转变

Ceph 正在从 package-based 部署向 container-based 部署迁移，cephadm 已成为官方推荐的标准部署方式，容器镜像来源于 quay.io。

### 官方容器构建流程

官方流程为：源代码 → RPM 包 → 上传至 yum repo → 构建容器镜像 → 交付至用户集群。

构建工具链：
- `build_with_container.py`：Python 脚本，负责整体构建流程
- `container file` + `build.sh`：实际调用 podman 构建容器
- 环境变量控制构建行为，其中关键变量为 `CUSTOM_CEPH_REPO_URL`

### 问题一：无法从本地 RPM 构建运行时镜像

`build_with_container.py` 在 RPM 构建步骤完成后即停止，不会继续生成容器镜像，且不报错，导致支持团队无法将本地 patch 打入容器。

一年前，`CUSTOM_CEPH_REPO_URL` 环境变量根本不存在，支持团队完全没有办法从自定义 repo 拉取 RPM 来构建容器。感谢 John Mulligan 贡献了该变量，但目前该 patch 仅存在于 main 分支，尚未 backport 到 squid 和 tentacle 分支。

### 问题二：无法将容器镜像导出为本地 tarball

在 air-gapped（离线隔离）环境中，无法从外部 registry 拉取镜像，必须能够将镜像导出为 tarball 并分发到所有 cephadm 节点。目前官方构建流程不支持此功能。

### 问题三：cephadm 的 registry 校验阻碍本地镜像使用

即使完成了本地镜像构建并推送到本地 registry，cephadm 的 orchestrator 也会因 validation 检查而阻止升级：
- 本地镜像没有 repo digest
- 需要手动设置 `ceph_use_repo_digest = false`
- 若使用 HTTP（无 TLS），还需设置 `registry_insecure = true`

### 当前支持团队的临时工作流（步骤繁琐）

1. 修复 curl 问题，确保所有包来自本地而非 shaman.ceph.com 或 download.ceph.com
2. Backport John Mulligan 的 `CUSTOM_CEPH_REPO_URL` patch
3. 使用 `build_with_container.py` 构建 RPM
4. 将 RPM 放入自定义 repo 并配置 repo URL
5. 提供一个空的 dummy credentials文件（构建系统要求）
6. 使用 `build.sh` 构建容器镜像
7. 搭建自定义基础设施并推送镜像
8. 向客户解释如何从自定义地址拉取镜像

这一流程步骤过多，对支持团队造成了极大负担。

## 解决方向与进展

### 正在推进的工作

演讲者的同事已提交一系列 patch，目标是实现**一条命令完成完整的本地容器镜像构建**（包含所有 patch）。目前该方案仍处于 draft 阶段，需要进一步完善，但演讲者已验证其可行性。

### 期望目标

1. 将完整的构建流程文档化，发布至 docs.ceph.com
2. 支持在不执行大量额外步骤的情况下，对旧版本 Ceph release 同样适用
3. 部分支持厂商已有内部维护的自定义 container registry（预置关键 bug fix），希望这些经验能够上游化并形成文档

## 总结与展望

- 容器化部署中 hotfix 交付困难的问题并非 Ceph 独有，是整个容器生态面临的共性挑战
- 从本地源码自动化构建容器镜像只是第一步
- 社区应共同努力，让用户能够在不等待正式 release 的情况下及时获得 bug 修复
- 减少支持团队与开发团队之间的流程壁垒，是提升 Ceph 生态整体健康度的关键
