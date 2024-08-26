---
title: "Introducing Sibench: A New Open Source Benchmarking Tool Optimized for Ceph"
date: 2023-05-19
updated: 2023-05-20
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph 性能基准测试工具 Sidebench 的介绍与讨论

#### 参会人员：Ceph 社区成员及研发人员

#### 会议时间：[具体日期]

#### 会议地点：[具体地点]

#### 主要议题：
1. **基准测试的挑战与痛点**
   - 基准测试过程中的复杂性和变量控制问题。
   - Ceph 的多接口和多工作负载特性增加了基准测试的难度。
   - 工作负载对操作员的不透明性，以及 Ceph 后台任务对性能的影响。

2. **Cosbench 的问题与替代方案**
   - Cosbench 的使用历史和存在的问题，如 Java Native Interface (JNI) 的高开销、维护不足、架构脆弱等。
   - 介绍 Sidebench 作为 Cosbench 的替代方案，强调其简单、轻量、易于调试和线性可扩展性。

3. **Sidebench 的设计目标与功能**
   - 设计目标包括低开销、直接调用 C 库、多线程支持、数据格式灵活性等。
   - 功能包括多协议支持（RADOS, RBD, CephFS, S3）、带宽限制、数据切片生成、读写混合测试等。

4. **Sidebench 的架构与使用示例**
   - Sidebench 包含一个守护进程和命令行工具，支持多节点分布式测试。
   - 演示了如何使用 Sidebench 进行 RADOS 和 RBD 的基准测试，以及如何通过 Benchmaster 进行多变量测试。

5. **未来发展方向与社区反馈**
   - 讨论了 Sidebench 的未来发展方向，如工作负载生成器、OSD 数量扫描、元操作支持等。
   - 强调社区参与和反馈的重要性，鼓励用户使用并贡献代码。

#### 决定事项：
- 继续开发和完善 Sidebench，特别是在工作负载生成和多变量测试方面。
- 鼓励社区成员参与 Sidebench 的测试和开发，提供反馈和建议。

#### 后续行动计划：
- 发布 Sidebench 的最新版本，并提供详细的安装和使用文档。
- 组织线上研讨会或工作坊，进一步介绍 Sidebench 的功能和最佳实践。
- 收集和分析社区反馈，根据需求调整开发计划。

#### 备注：
- Sidebench 的代码和文档可在 [sidebench.io](http://sidebench.io) 和 GitHub 上获取。
- 会议中提到的 Benchmaster 是一个用于管理多基准测试的 Python 工具，支持输出结果到 Google Sheets。

---

本次会议详细讨论了 Ceph 基准测试工具的发展和优化，特别是 Sidebench 的引入和未来规划，旨在提高 Ceph 性能测试的效率和准确性。