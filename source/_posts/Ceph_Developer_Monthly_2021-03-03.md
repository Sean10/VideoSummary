---
title: "Ceph Developer Monthly 2021-03-03"
date: 2021-04-20
updated: 2021-04-21
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议主题：Ceph分布式存储系统优化与测试改进

#### 日期：2021年3月

#### 参会人员：Kyle Vigor, 以及其他Ceph研发和测试团队成员

#### 主要议题：

1. **Ceph RGW性能优化与配置简化**
   - **讨论内容**：
     - 讨论了通过预设的Erasure Coded（EC）配置文件来简化用户配置，以提高性能和易用性。
     - 探讨了如何在集群启动时自动加载这些预设配置文件，并让用户可以直接使用，无需手动设置。
     - 讨论了如何通过RGW客户端根据不同的EC配置文件动态调整参数，以优化性能。
     - 提出了在BlueStore中为特定池设置提示或属性，以便优化存储分配和管理。
   - **决定事项**：
     - 需要进一步讨论和定义具体的EC配置文件参数。
     - 需要研究如何在RGW和BlueStore中实现这些优化策略。
   - **后续行动计划**：
     - 创建跟踪问题（tracker issues）和任务分解，以便具体实施这些优化策略。
     - 与开发团队合作，确保这些优化策略的技术可行性和实施细节。

2. **构建与测试优化**
   - **讨论内容**：
     - 讨论了如何优化测试执行和提高测试覆盖率，包括改进测试的并行执行和减少测试间的重复。
     - 探讨了如何减少测试环境的设置和重置时间，以及如何减少日志收集的开销。
     - 讨论了使用Ninja作为构建工具的可能性，以提高构建速度。
   - **决定事项**：
     - 需要进一步分析和优化测试执行流程。
     - 需要评估Ninja作为构建工具的效果和可行性。
   - **后续行动计划**：
     - 开展暑期项目，专注于测试优化和构建效率提升。
     - 探索使用Ninja和其他构建工具的可能性，并进行实际测试。

3. **Telemetry意识提升**
   - **讨论内容**：
     - 讨论了如何在用户界面和命令行接口中提高Telemetry的可见性和用户参与度。
     - 探讨了如何通过教育和宣传来减少用户对Telemetry的疑虑。
   - **决定事项**：
     - 需要在主要升级时提醒用户启用Telemetry。
     - 需要通过CLI和文档宣传Telemetry的好处和实际应用案例。
   - **后续行动计划**：
     - 在主要升级时通过CLI提醒用户启用Telemetry。
     - 制作宣传材料，展示Telemetry的实际应用和好处。

4. **Windows支持**
   - **讨论内容**：
     - 讨论了Windows支持的进展，包括构建和测试流程的自动化。
     - 探讨了如何通过CI集成来确保Windows支持的稳定性和可靠性。
   - **决定事项**：
     - 需要进一步完善Windows支持的CI流程。
     - 需要确保Windows支持的测试覆盖率和质量。
   - **后续行动计划**：
     - 与CI团队合作，完善Windows支持的CI流程。
     - 增加Windows支持的测试用例，确保质量。

#### 总结：
本次会议主要聚焦于Ceph RGW的性能优化、构建与测试流程的改进、Telemetry的推广以及Windows支持的进展。通过讨论，明确了具体的优化方向和实施步骤，并制定了相应的后续行动计划。