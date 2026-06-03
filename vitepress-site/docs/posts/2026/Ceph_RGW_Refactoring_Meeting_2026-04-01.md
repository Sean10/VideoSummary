---
title: "Ceph RGW Refactoring Meeting 2026-04-01"
date: 2026-04-01
updated: 2026-05-14
tags:
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
## 会议概述

本次 RGW Refactoring 例会主要围绕 RGW 测试套件的修复进展、多站点（multi-site）测试问题、Java S3 测试的维护挑战，以及一个将 RGW 中URL 端点从字符串重构为结构体的 PR 展开讨论。

## 主要议题

### 1. RGW verify 测试套件阻塞问题

当前 RGW verify 子套件的推进被 Java S3 测试阻塞。Casey 提到已提交相关 tracker 和 PR，Eric 也在自己的 PR 中更新了进展。两人计划线下协作，尝试合并一个可行方案以解除阻塞。

Casey 的PR 提供了一个更通用化的解决方案，而 Eric 的方案则较为针对 Rocky Linux 特定版本。核心问题在于 teuthology 中的 Java S3 task 使用了某个特定的 `alternatives` 命令（GP）来查找 Java 版本，但该命令无法识别最新安装的 Java 版本。

讨论方向：
- 将 Java安装逻辑从 bootstrap 脚本迁移到 Python QA task 文件中，使其能够感知当前 distro 并自动选择正确的 `alternatives` 配置。
- 这样可以更好地支持 Rocky 10、CentOS 10 等不同 distro。

### 2. 多站点（multi-site）测试中的 shutdown hang 问题

一位参会者报告在调试 multi-site realm reload崩溃时，发现了 RGW coroutines manager 在 shutdown 过程中进入死循环的问题：在收到 `e-cancelled` 错误时，代码没有跳出循环，而是持续尝试重新获取锁，导致某个线程 CPU 占用率飙升，RGW 变得无响应。

该问题在 realm reload 或 shutdown 中间阶段触发，表现为 replication lag 持续累积，类似"replication 腿瘸"的现象。目前已有下游修复，正在尝试构造可靠的复现用例以便提交上游 PR。

### 3. Valgrind 问题

Casey 提到在修复 Java 测试问题后，可能会暴露出之前被掩盖的 Valgrind 错误，尤其是 Rocky 特有的新 Valgrind 问题。计划在调试当前问题的同时一并排查。

### 4. Java S3 测试的价值与维护成本讨论

讨论了 Java S3 测试套件的意义：
- Java SDK 对请求签名的处理方式与 Python boto3 不同，尤其是 streaming SIGv4 的支持，能覆盖不同的代码路径。
- 历史上曾出现 false positive，部分测试被禁用。
- 维护成本较高，每次切换 distro 都需要处理 Java 版本兼容问题。

与会者还提出了对 Go SDK 和 C++ SDK 测试的需求：
- 内部团队大量使用 C++ SDK，但目前没有对应的测试用例。
- Go SDK 测试也被提及（之前有过 "chase check" 相关工作）。

Casey 表达了对测试策略的看法：S3 测试（Python）应作为功能测试的主体，其他语言 SDK 的测试应聚焦于"已知行为差异"的场景，避免为每个新 S3 feature 重复编写四套测试。

### 5. RGW URL 端点重构 PR（Oazison 提交）

Oazison 介绍了两个 PR：

**PR 1**：涉及对象名称中列分隔符的处理，原本认为列分隔符不会出现在对象名中，但实际上是允许的，会引发一些复杂情况。

**PR 2（重点）**：将 RGW 中 URL 端点的表示方式从裸字符串（如 `http://example.com`）重构为结构体，将相关数据和方法封装在一起。

- PR 体积较大，主要原因是需要对所有使用 URL 字符串的文件进行级联修改。
- 核心逻辑相对简单：将字符串转为结构体，并新增从 DNS 端点解析 IP 的能力，以便在发送 curl 请求时可以指定 `connect-to` 参数。
- 该功能默认关闭，计划通过 teuthology 分别测试启用和禁用两种配置，对比是否引入 regression。

Casey 表示高层次上认可该方向，已有若干 pending comments 待提交，并建议最终应默认启用该功能（若 endpoint 只解析为单个 IP，开销可忽略不计）。

### 6. RGW multi-site 测试套件现状

目前约 53 个测试用例，95% 稳定通过。已知问题：
- 1 个测试持续失败（Shai 正在跟进）。
- 2-3 个 flaky 测试，初步判断与 zone group 配置差异有关（单 zone group + 双 zone vs 双 zone group + 各双 zone），已在 tracker 中记录。

结论：multi-site 套件整体状态良好，Oazison 可以不必等待 RGW verify 套件修复完成，直接针对 multi-site 套件运行 URL 重构 PR 的测试。

## 决定事项

- Casey 和 Eric 线下协作解决 Java S3 测试的 `alternatives` 问题，优先尝试使用最新 Java 版本的通用方案。
- 考虑将 Java 安装逻辑从 bootstrap 脚本迁移至 Python QA task，以更好地支持多 distro。
- Oazison 在获取 teuthology 测试结果后，将 URL 重构 PR 提交给团队深入 review。
- 下周例会取消，改为参加 Ceph Developer Monthly（已重新安排至同一时间）。

## 后续行动

| 负责人 | 行动项 |
|--------|--------|
| Casey | 调查 Rocky 特有的 Valgrind 问题 |
| Casey & Eric | 线下协作修复 Java S3 teuthology task |
| 多站点调试者 | 构造 realm reload crash 的可靠复现，提交上游 PR |
| Oazison | 重新运行 multi-site teuthology 测试（启用/禁用两种配置），更新 URL 重构 PR |
| Casey | 提交 URL 重构 PR 的pending review comments |
