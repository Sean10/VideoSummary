---
title: "Ceph CI and Developer Tooling- Past, Present, and Futur"
date: 2026-04-20
updated: 2026-04-21
tags:
  - "Teuthology"
categories:
  - "视频总结"
outline: deep
---
## 演讲者介绍

本次演讲由 David Galloway 主讲。他于 2010 年加入 Red Hat 内部帮助台，2012 年转入工程部门。随着 InkTank 被 Red Hat 收购，他成为 Ceph 实验室的专职资源，负责机架安装、布线及初期硬件投资的落地工作，并参与了实验室从 Irvine 迁移至 Morisville 的全过程。

团队成员（按入职时间排序）：
- **Dan Mick**：随 InkTank 收购一同加入
- **Adam Kreitman**：2019 年加入，带来 Ansible、Jenkins 及云计算经验
- **Evelyn**：项目经理，2024 年加入
- **Fernando**：安全方向，2024 年加入
- **Jitendra**：最新成员，近期贡献突出

## Ceph 实验室的历史沿革

**2014 年**：InkTank 被 Red Hat 收购，实验室主体位于加利福尼亚州 Irvine 的托管数据中心。

**2015 年初**：Red Hat 完成初期硬件投资，David 完成机架安装与布线，并将 Irvine 的大部分设备迁移至北卡罗来纳州 Morrisville 的 Red Hat 托管空间。收购后实验室分为两个独立部分：
- **上游开发与测试实验室**：位于 Red Hat 社区机柜，对社区成员开放
- **下游实验室（Octo Lab）**：主要面向 QE，位于 Red Hat 防火墙之后

**2022 年**：Ceph 项目完全并入 IBM，实验室再次迁移：
- 下游 Octo Lab 迁至亚利桑那州 Tucson
- 上游实验室迁至纽约州 Poughkeepsie（约四分之三的设备仍处于网络接入待完成状态）

## 为什么 Ceph CI 如此复杂

**多发行版支持**：目前需在以下平台上构建和支持 Ceph：
- CentOS 8、9，Rocky 10
- Ubuntu 20、22、24
- 若干 Debian 版本
- Windows 驱动

近期重大改进：已实现在容器内构建 Ceph，Ubuntu 宿主机可构建 RPM，反之亦然。

**多架构支持**：上游支持 x86 和 arm64，下游还支持 Power 和 s390x。

**硬件维护挑战**：各硬件厂商提供工程样机用于测试，维护这些样机极为繁琐。演讲者展示了为早期 arm 原型手工制作串口转接头的电路图，以及用于固件刷写的工具。

**规模化集成测试**：每天运行约 2,000 至 3,000 个集成测试任务，每个任务会锁定 1 至 4 台裸金属服务器，完整流程包括：安装操作系统、运行配置管理、安装 Ceph、执行集成测试（部分测试会对磁盘和网络设备进行压力测试）。

**自定义 Python 微服务依赖**：团队重度依赖若干自研 Python 微服务，调试难度较高。

## CI 历史回顾

### GitBuilders 时代

GitBuilders 是早期的构建系统，每台裸金属或虚拟机专门负责构建特定发行版和架构组合（例如：CentOS 6 x86 TCMalloc）。每次只能构建一个版本，构建耗时约 4 小时，每天最多只能构建约 6 个分支，开发者常需要等待数天才能获得二进制包。构建产物也由同一台 GitBuilder 提供服务，一旦宕机影响极大。

### VPS 测试阶段

在拥有大量裸金属测试节点之前，集成测试主要在虚拟机（VPS）上运行：
- 约 100 台2U 服务器，每台配备单四核处理器、32GB 内存、8 块 1TB 机械硬盘
- 每台 VPS 宿主机运行 8 个虚拟机（单 vCPU、4GB 内存、1块硬盘）
- 使用 cloud-init 和自研工具 **downburst**（基于 libvirt）快速部署实例
- 曾短暂使用 OVH 公有云运行 Teuthology 任务，但因稳定性问题放弃

### 监控与资产管理

- 直到 InkTank 并入 Red Hat 后才开始使用数据中心资产管理工具
- 2015 年引入 Nagios 实现集中监控告警，现已迁移至 Grafana
- 曾有一个手动维护的状态门户，Nagios 下线后随之废弃

### Jenkins 演进

Ceph 项目在 Jenkins 方面长期落后于业界：
- 2015 年才开始运行 make check
- 直到去年才开始使用 Jenkins Pipeline 功能
- Pipeline 之前，同一分支的 8 种发行版/架构组合需要分别构建同一份源码 tarball

## 当前 CI 架构（Present）

### 完整流程概述

1. **需求跟踪**：开发者从 tracker.ceph.com（Redmine）获取任务
2. **代码开发**：从 GitHub fork/clone Ceph 仓库，可使用 **VStart cluster** 在本地部署轻量级单节点 Ceph 集群进行验证
3. **触发构建**：推送分支至 Ceph CI Git 仓库，GitHub webhook 触发 Jenkins 构建任务
4. **Jenkins 构建**：
   - 所有 Jenkins 任务以YAML 定义，通过 OpenStack 的 Jenkins Job Builder 工具推送至 Jenkins
   - 构建在 Poughkeepsie 实验室的裸金属 Jenkins builder 上运行
   - 每台 builder 使用 4-5 个 Ansible role 初始化，当前每台只有 1 个 executor
5. **源码 tarball 构建**：Ceph dev pipeline 启动 source dist 任务，构建源码 tarball 并上传至 Jenkins，随后为每种发行版和架构创建 builder 容器
6. **包存储与分发**：
   - 构建完成的包推送至 **Chakra**（自研 Python 微服务，提供 API、二进制存储和 repo 托管，保存 14 天）
   - Chakra 通知 **Shaman**（另一自研 Python 微服务，含数据库、API 和 Web UI）repo 已就绪
7. **容器镜像构建**：基于 Rocky Linux 10（本周刚切换为默认基础镜像），安装运行时依赖和 Ceph 包，发布开发容器镜像至 quay.ceph.io
8. **集成测试（Teuthology）**：
   - Teuthology 通过 Padles（API +数据库）管理测试节点和任务结果，Pulpito 提供 Web 展示
   - dispatcher 守护进程通过 beanstalkd 调度任务
   - 测试节点通过 **FOG**（Fully Open Ghost）项目进行系统重装：IPMI 上电 → DHCP → PXE boot → FOG OS →流式写入 gold OS镜像（预装 Ceph 测试依赖）→ 重启 → Ansible 配置（zap NVMe 用于 OSD 等）→ 安装 Ceph → 运行 QA 测试
   - 每个任务结束后，内核日志、syslog、core dump 及任务日志写入 **CephFS** 挂载点，存储于长期运行集群（LRC，同时作为 dogfood 集群验证预发布版本）
9. **PR 检查**：每个 PR 触发 17 项检查：
   - Jenkins（9 项）：make check、API 测试、Windows 测试等，每项耗时 1-2 小时
   - GitHub Actions（7 项）：PR 标签分配、rebase 检查等
   - Read the Docs（1 项）：文档构建与语法检查

### 正式发布流程

1. 变更合并至主分支后，视情况向各 release 分支（如 Tentacle）提交 backport PR
2. QE 流程：批量合并 PR 至独立 CephCI 分支，构建并跑完所有 Teuthology 测试套件
3. 组负责人审批测试结果后，手动触发 **Ceph release pipeline** Jenkins 任务
4. 构建产物推送至独立 Chakra 实例（仅存储待签名的预发布包）
5. 手动 rsync 至实验室 VM **Signer**（通过 Nitrokey USB 设备安全存储 GPG 签名密钥）
6. 签名后推送至 download.ceph.com 的密码保护暂存目录
7. 手动触发容器构建，x86 和 arm64 容器合并后推送至 quay.io
8. 发布公告与 Release Notes 发布

## 当前痛点

- **重复构建**：每个 PR 的二进制包被构建 3 次（make check、API 测试、Windows 任务各一次），正在推进容器化以实现一次构建多处复用
- **跨发行版测试差异**：单元测试在 Jamy 上通过但在 Noble 上失败的情况时有发生
- **构建状态可见性差**：Shaman 只有在构建实际开始后才感知到任务，Jenkins 队列积压时开发者可能重复 force push 反而延误自己的构建
- **基础设施故障影响 CI**：近期发生测试节点磁盘故障导致数十个 Teuthology 任务失败，此类问题本应在影响 CI 前被提前发现
- **Shaman/Chakra 技术债**：十年前因缺乏跨发行版工具而自研，现已有 **Pulp** 等现代开源替代方案，团队正在评估迁移
- **Jenkins 任务效率低下**：部分任务仅需运行几秒钟的脚本，却要花费大量时间从 GitHub clone 整个 Ceph 仓库，应迁移至 GitHub Actions；团队在 GitHub Actions 方面经验不足，正在学习中
- **单 executor 资源浪费**：96 核 builder 运行单线程任务时，95 个核心处于闲置状态

## 未来规划（Future）

当前年度实验室优先事项：

**开发者与管理层友好的指标和 Dashboard**：
- 团队成员 Evelyn 已发出调查问卷，收集开发者最关心的指标
- 已上线示例 Dashboard，展示 Jenkins 队列中的等待任务数、PR 任务等待启动时长等关键指标
- 随着 Red Hat 设备迁入 IBM 并完成布线，队列积压情况已明显改善（此前高峰期等待时间达 4-5 小时）

**持续推进容器化**：将更多构建和测试任务迁移至容器，提升资源利用率和跨平台一致性。

**GitHub Actions 能力建设**：将适合的轻量级任务（如 commit 签名检查）迁移至 GitHub Actions，减少对 Jenkins builder 的不必要占用。
