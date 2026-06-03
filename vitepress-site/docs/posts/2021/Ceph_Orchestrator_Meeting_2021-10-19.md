---
title: "Ceph Orchestrator Meeting 2021-10-19"
date: 2021-10-19
updated: 2021-10-20
tags:
  - "Ceph"
  - "分布式存储"
  - "编排"
  - "NFS"
  - "Rook"
categories:
  - "视频总结"
outline: deep
---
Ceph Orchestrator 会议于2021年10月19日举行，主要讨论了以下议题：

1. **NFS功能缺失**：
   - 讨论了在Ceph中NFS LGW导出功能在self-ansible支持中的缺失，特别是导出单个桶和与单个用户关联的一组桶的能力。
   - 确认当前Ceph的NFS模块仅支持在桶级别导出，且用户总是桶的所有者。
   - 提议通过增加功能，允许通过用户名创建导出，以便用户可以导出其所有的桶。

2. **CLI命令调整**：
   - 讨论了NFS导出创建命令的参数顺序问题，建议调整以提高直观性。
   - 决定即使可能破坏向后兼容性，也要改进CLI命令，确保用户使用命名参数而非依赖顺序。

3. **Rook支持讨论**：
   - 询问了Rook是否支持类似NFS LGW用户的导出功能，确认Rook支持定义NFS服务器，但导出管理不涉及。

4. **ELSO项目进展**：
   - 讨论了ELSO项目的进展，特别是与Topol VM和Top LVM Operator的集成。
   - 确认Top LVM项目社区活跃，但Topol VM Operator社区不理想，可能需要重新设计或创建新的Operator。
   - 计划与Topol VM Operator团队进行会议，讨论可能的贡献和必要的更改。

会议决定：
- 改进NFS导出功能的CLI命令，增加通过用户名导出的能力。
- 确保用户在使用CLI时使用命名参数，以适应可能的命令调整。
- 安排与Topol VM Operator团队的会议，讨论项目贡献和设计更改。

后续行动计划：
- 实施 NFS 导出功能的改进，包括 CLI 命令的调整。
- 跟进与 Topol VM Operator 团队的会议，确定项目贡献和设计更改的可行性。
- 监控 Rook 对 NFS 导出功能的支持情况，确保与 Ceph 的集成顺畅。