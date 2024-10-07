---
title: "Ceph Crimson/SeaStore 2021-11-10"
date: 2021-11-10
updated: 2021-11-11
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 关键细节：
1. **Journal PRs 合并**：本周团队成功合并了两个 Journal PRs。
2. **PRT 结构泛化**：Myeongwon 正在努力泛化 PRT 结构，以便只有段管理器内部关心段管理器部分，从而能够在 Ceph 存储和事务管理器中无缝使用随机访问设备地址。
3. **ZNS 段管理器**：Joseph 正在开发 ZNS 段管理器，并已实现大部分功能。实验室中已有几个实际的 ZNS 设备，进展顺利。
4. **Crimson 配置简化**：Radik 上周主要在 Crimson 项目中工作，发送了一个 PR 以移除 Rook 中 Crimson 的特定配置需求，简化了 Kubernetes 集群中的客户端配置。
5. **中断条件问题**：Barth 发现了一个与中断条件相关的问题，即在可中断未来中，全局中断条件未被清除，导致后续事件无法正确启动。该问题已在测试环境中发现，将在离线讨论中解决。
6. **C-Store 测试**：Soonel 尝试在上游主分支中测试 C-Store，但发现部署工具尚未支持 C-Store，建议继续关注 Blue Store 的测试。
7. **段故障问题**：上周在测试中遇到了严重的段故障问题，原因是 GC 未启动导致空间未回收。已提交 PR 修复 32 位类型溢出问题，但仍在寻找根本原因。
8. **中断条件状态**：在处理 PG 事件时遇到了嵌套中断条件的问题，建议通过实现某种中断条件状态来解决。

#### 讨论的主要议题：
- PRT 结构的泛化和其在 Ceph 中的应用。
- ZNS 段管理器的开发进展和实际设备测试。
- Crimson 配置的简化及其在 Kubernetes 集群中的应用。
- 中断条件问题的诊断和解决方案。
- C-Store 的测试现状和未来方向。

#### 决定的事项：
- 继续推进 PRT 结构的泛化工作。
- 继续 ZNS 段管理器的开发和测试。
- 简化 Crimson 配置，移除不必要的特定配置。
- 解决中断条件问题，确保事件处理的正确性。
- 关注 Blue Store 的测试，同时探索 C-Store 的部署可能性。

#### 后续的行动计划：
- Myeongwon 继续泛化 PRT 结构，确保其在 Ceph 中的无缝应用。
- Joseph 继续 ZNS 段管理器的开发，并进行实际设备测试。
- Radik 继续简化 Crimson 配置，确保其在 Kubernetes 集群中的顺利应用。
- Barth 与 Jihad 离线讨论中断条件问题的解决方案。
- Soonel 继续关注 Blue Store 的测试，同时探索 C-Store 的部署可能性。
- 解决段故障问题的根本原因，并确保 GC 的正常运行。

### 会议结束
- 会议结束，祝大家本周工作顺利。

---

以上是本次会议的纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。