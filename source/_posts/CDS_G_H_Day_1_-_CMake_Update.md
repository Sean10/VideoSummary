---
title: "CDS G/H (Day 1) - CMake Update"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： Ceph 项目中 CMake 更新及 CI 技术讨论

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： Matt Benjamin, Ilya Dryomov, Adam Emerson, Luis, Luke, Dan（可能还有其他未提及的人员）

**会议内容**：

**一、CMake 更新**

*   **项目背景**： 为了提高构建速度，特别是多核机器上的构建速度，项目组开始将构建系统从 Autoconf/Makefile 转换为 CMake。
*   **进展情况**：
    *   Ali（实习生）完成了初步的转换工作，但后续人员在不同分支上进行了修改。
    *   第一版 CMake 构建系统与 Autoconf/Makefile 基本一致，但缺少了测试等部分。
    *   项目组通过减少重复构建的对象数量和简化文件结构，提高了构建速度。
    *   目前，CMake 版本已合并到 Firefly 分支，并添加了测试。
*   **下一步计划**：
    *   将 CMake 版本合并到 master 分支。
    *   检查是否存在遗漏的目标或其他问题。
    *   确保所有边缘情况都能正常工作，例如库检测、构建脚本等。
    *   移植 CMake 到 Civic Web 等其他子模块。

**二、CI 技术讨论**

*   **议题**： 讨论 CI 技术的选择和优先级。
*   **讨论内容**：
    *   评估了 Jenkins、GitLab CI/CD 等不同的 CI 工具。
    *   讨论了 CI 工具的集成、测试覆盖范围、性能等问题。
    *   讨论了不同分支的测试策略。
*   **结论**：
    *   项目组对 CMake 的未来持乐观态度。
    *   将 CMake 合并到 master 分支。
    *   继续讨论 CI 技术的选择和实施计划。

**三、其他事项**

*   Ilya Dryomov 正在研究构建目标在源树外部的情况。
*   项目组将继续关注 Civic Web 等其他子模块的 CMake 移植工作。

**后续行动计划**：

*   Matt Benjamin 将在当天晚些时候推送 CMake 的 master 分支原型。
*   项目组将检查 CMake 版本中是否存在遗漏的目标或其他问题。
*   项目组将讨论 CI 技术的选择和实施计划。

**备注**：

*   会议中提到了一些计算机科学/ceph 领域的英文关键词，例如：CMake, Autoconf, Makefile, Jenkins, GitLab CI/CD, Civic Web, RocksDB, BlueStore, RBD, CRC, Autoconf, Makefile, Jenkins, GitLab CI/CD 等。