---
title: Dont Get Confd Making Ceph Configuration Changes Obvious
date: 2026-04-02
updated: 2026-04-03
tags:
- Ceph
- OSD
categories: 
- 视频总结
subtitle: Don_t_Get_Conf_d_Making_Ceph_Configuration_Changes_Obvious
---

## 概述

本次演讲由 Red Hat Ceph 团队的 Naveen 主讲，核心议题是如何让 Ceph 的配置变更加透明可追踪，避免运维人员在版本升级过程中因配置默认值悄然改变而导致工作流中断。

## Ceph 配置机制简介

Ceph 作为一个由众多大型服务组成的分布式存储系统，包含 MON、MDS、MGR、RBD、RGW 等组件，每个组件都有各自的配置项。这些配置的"唯一真相来源"存储在源码目录 `src/common/options` 下的 YAML 文件中，按服务类型（Crimson、MDS、MGR、MON 等）分别归档。

构建时，一个名为 **y2c**（YAML to C）的脚本会读取这些 YAML 文件，将其转换为 C++ 文件，最终生成一个 options vector注入到 Ceph context 中。当用户执行 `ceph config set XYZ` 时，实际上是在更新 Ceph binary 内部的 config proxy 变量。

## 问题背景

Ceph 目前拥有多达 **2,061 个配置项**，管理难度极高。2024 年 Ceph 用户峰会上，大量客户反映了同一个痛点：**跨版本升级时，无法清晰了解某个配置项从版本 A 到版本 B 发生了哪些变化。**

这一问题带来三方面影响：

1. **默认值变更风险**：大多数服务运维人员依赖配置的默认值运行集群，一旦默认值悄然改变，极易破坏现有工作流。
2. **Release notes遗漏**：发布团队虽然努力记录变更，但由于缺乏每个 PR 改动了哪些配置的上下文信息，仅靠 `git diff` 难以全面覆盖。
3. **运维人员缺乏追踪手段**：目前没有系统化的方式让运维人员主动追踪配置变更，只能逐一翻阅 PR 和 release notes。

## 解决方案

团队采取了**双管齐下**的策略：

### 1. CI 强制提示：ceph-config-diff

在 GitHub CI 中新增了一个名为 **ceph-config-diff** 的检查，该检查在每个 PR 提交时自动运行。若检测到配置项发生变更，会：

- 在 PR 下方自动添加评论，提示开发者"你修改了配置，如果认为重要，请更新 release notes"
- 在 PR 页面添加 annotation，将注意力引导至具体变更位置

**实际案例演示**：某 PR 作者将 OSD scrubing 过程中的默认数据读取步长（`osd_deep_scrub_stride`）从 512 KB 调整为 4 MiB，修改了 `osd.yaml.in` 文件。作者最初忘记更新 release notes，ceph-config-diff 工具自动输出了变更提示，审查者也据此要求作者补充说明。这类细微改动对开发者影响不大，但对不知情的用户可能造成困扰。

目前该检查为**非强制性**（non-blocking），团队认为在将其设为强制检查之前还需要更多完善工作，但相关脚本已合入上游仓库，可直接使用。

### 2. 手动追踪与自助工具

ceph-config-diff 的输出格式经过特别设计，**便于在 GitHub 搜索栏中直接检索**。例如，运维人员发现某配置值发生变化，可直接将旧值或新值粘贴到 PR 搜索框，快速定位到引入该变更的具体 PR，从而了解变更背后的讨论和决策过程。

**命令行演示**：演讲者现场演示了如何用脚本对比 Squid 和 Tentacle 两个版本之间的配置差异，输出为结构化的 JSON 格式，清晰展示每个服务下新增、删除和修改的配置项。例如，BlueStore 中某配置的默认值从 64 MB 增大到 2 GB。

演讲者还基于该脚本构建了一个简单的 Web 界面（坦言前端能力有限，借助 AI 完成），用户可通过扫描现场 QR 码访问，选择两个版本后即可直观查看配置差异。

## 后续行动

- 脚本和 README 已合入上游仓库，运维人员可直接集成到自己的工具链中
- 欢迎社区反馈：该工具是否有用、希望增加哪些功能、有哪些改进建议
- 演讲者表示将在会场全程驻留，欢迎当面交流

## 总结

通过在 CI 流程中引入 ceph-config-diff 检查，并提供结构化的配置差异脚本，Ceph 社区正在逐步建立一套让配置变更"显而易见"的机制，帮助开发者养成更新 release notes 的习惯，同时赋予运维人员自主追踪配置演变的能力，降低版本升级带来的不确定性风险。
