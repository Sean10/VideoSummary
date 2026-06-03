---
title: "Ceph Developer Monthly Meetup EMEA - April 2026"
date: 2026-04-08
updated: 2026-04-09
tags:
  - "Ceph"
  - "OSD"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 Ceph Developer Monthly Meetup EMEA（2026 年 4 月）为临时性会议，议程中原本没有预设议题。主持人开放自由讨论，最终围绕 Umbrella 升级工作的测试状态展开了一次有价值的技术交流。

## 主要议题：Umbrella 升级测试失败问题

### 背景

Umbrella 升级的 kickoff PR 已经合并，但合并时升级测试（upgrade tests）大量失败。团队在明知测试未通过的情况下仍选择合并，计划后续跟进修复。

### 失败原因分析

与会者 Alex 分享了当天早上触发的测试运行结果，界面呈现"一片红色"。经过讨论，失败原因主要分为以下几类：

**1. Health Warning 导致的失败（主要原因）**

大多数测试失败源于集群日志中出现的 health warning。测试框架在每个测试结束前会执行一次集群健康检查（cluster badness check），即便 health warning 是瞬时出现的，也会导致测试标记为失败。

重要说明：这类失败并不意味着升级本身未完成，只是测试在升级完成后检测到了 health warning。这属于"令人烦恼"而非"令人恐慌"的问题。

具体出现的 health warning 包括：
- 集群日志中出现 quota 耗尽（running out of quota）
- pool full 警告

**2. Umbrella 特有问题（已基本修复）**

- cephos 软件包的 RBM 重命名导致的若干问题
- 某命令新增参数导致 cephadm 解析失败

上述问题均已开 tracker 并修复。

**3. 残留问题**

- 仍有少量测试在尝试安装 cephos-d Classic时失败，需进一步排查
- 存在少量 stuck PG 现象

### 应对策略

**短期行动：**
- Alex 将在 Ceph core team 内部频道发起协作，招募有带宽的成员共同 review 本次测试运行结果
- 对所有失败项进行 triage，确保每类问题都有对应 tracker
- 参考此前 Rocky 10 工作中建立 baseline 的经验，建立升级测试的稳定 baseline

**中期目标：**
- 自实验室迁移以来，升级测试缺乏持续的 baseline 调度，需要恢复定期运行机制
- 针对 cephadm failed daemon 问题，需联系 cephadm 团队跟进，该问题目前尚未有人认领解决

**已知修复可用：**
- cephos-d Classic 安装失败问题此前在 encoder 测试中已有修复方案，可直接应用到升级测试中

## 工具分享

Alex 提到，他在使用 IBM watsonx Code Assistant（基于 Claude Code）辅助分析大量测试日志，取得了较好的效果，在定位有效调试信息方面命中率较高，显著提升了日志分析效率。

- IBM内部用户可直接使用 IBM watsonx Code Assistant（需有许可证）
- 外部用户可考虑使用 Claude Code 等类似代码助手产品
- 有兴趣了解具体 prompt 策略的人员可直接联系 Alex

## 后续行动计划

| 行动项 | 负责人 | 状态 |
|-----|--------|------|
| 在 core team 频道发起升级测试 review 协作 | Alex | 待执行 |
| Review 本次测试运行，确保所有失败项有 tracker | Core team 志愿者 | 待认领 |
| 跟进 cephadm failed daemon 问题 | Alex / cephadm 团队 | 待联系 |
| 排查残留的 cephos-d Classic 安装失败 | Alex | 进行中 |
| 恢复升级测试定期 baseline 调度 | Core team | 待规划 |

## 总结

本次会议虽为临时召开，但围绕 Umbrella 升级测试的讨论颇具实质性价值。核心结论是：当前大量测试失败主要由 health warning 机制触发，并非升级流程本身存在根本性问题。团队将通过协作 triage、建立 baseline 和跟进专项问题等方式逐步稳定测试结果。
