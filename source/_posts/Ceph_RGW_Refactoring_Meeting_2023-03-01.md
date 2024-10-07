---
title: "Ceph RGW Refactoring Meeting 2023-03-01"
date: 2023-03-06
updated: 2023-03-07
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节
- **Reef 分支决策**: 今天的上游领导会议决定分叉 Reef 发布分支，预计今天完成。任何需要进入 Reef 的改动现在必须合并到 Main 并通过 backboards。
- **同步策略问题**: Katie 报告了在禁用 bucket sink 的情况下测试同步策略时遇到的问题。发现即使只有两个区域配置为同步，第三个区域仍在拉取数据，这似乎是一个回归问题。
- **日志修剪问题**: 与同步策略相关的另一个问题是日志修剪和归档区域的问题，即使某些区域不从其他区域同步数据，同步策略仍指示查询这些区域，这阻止了日志被修剪。
- **rgwhttp 客户端**: 讨论了新的 rgwhttp 客户端类，该类可能在多站点配置中非常有用，尤其是在使用 HTTP/3 前端时。讨论了如何处理 OpenSSL 和 BoringSSL 的链接问题。

#### 主要议题
- **同步策略的实现和问题**: 讨论了同步策略在多区域配置中的具体实现问题，包括数据同步的逻辑和日志修剪的策略。
- **rgwhttp 客户端的使用和挑战**: 探讨了在多站点环境中使用新 HTTP 客户端的潜在好处和面临的挑战，特别是与 SSL 库的兼容性问题。

#### 决定事项
- **Reef 分支分叉**: 决定分叉 Reef 发布分支，所有后续的合并请求需要通过 Main 和 backboards。
- **同步策略问题**: 需要进一步审查和测试同步策略的实现，特别是关于数据同步和日志修剪的逻辑。
- **rgwhttp 客户端**: 虽然新的 rgwhttp 客户端在多站点环境中可能非常有用，但需要解决与 SSL 库的兼容性问题。

#### 后续行动计划
- **同步策略审查**: Yehuda 将审查同步策略的实现，并测试更多案例以确认和解决存在的问题。
- **rgwhttp 客户端开发**: 继续开发和测试 rgwhttp 客户端，特别是在处理 SSL 库兼容性方面的工作。
- **跟踪问题**: 所有相关问题和讨论将被记录在 Tracker 和 Theta pad 中，以便后续跟踪和解决。

### 结论
会议讨论了关于 Reef 分支分叉、同步策略的实现问题以及 rgwhttp 客户端在多站点环境中的应用。决定分叉 Reef 分支并继续审查和改进同步策略和 rgwhttp 客户端的实现。所有相关问题和讨论将被记录并跟踪，以便后续的开发和改进。感谢所有参与者的贡献和讨论。