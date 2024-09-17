---
title: "CDS G/H (Day 1) - Calamari Development"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



### 会议纪要

**会议主题**： Calamari 开发讨论

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： John Gregor, Sage, Patrick等

**会议内容**：

**一、Calamari 开发计划**

1. **Crush 管理功能**：
   - 高优先级功能，即将加入 Calamari REST API。
   - 目的：支持 Erasure Code 池和 Cache Tiering 等特性。
   - 主要工作：
     - 实现 Crush Map 的 CRUD 操作。
     - 将 OSD 和主机映射到 Crush 节点。
     - 处理 Ceph 配置文件中的 Crush Location 问题。

2. **其他工作**：
   - 清理使用 Salt 私有接口的代码。
   - 将 Diamond 和 Graphite 的分支合并到上游。
   - 改进打包方式，简化前端构建过程。
   - 移除 DoSulu 插件管理器。

**二、社区合作**

1. **Dashing Ceph 和 Sef-Dash**：
   - 讨论了将社区项目代码整合到 Calamari 的可能性。
   - 目前 UI 开发资源有限，优先考虑将社区贡献的 UI 设计理念整合到 Calamari。

2. **Ink Scope**：
   - 讨论了 Ink Scope 项目与 Calamari 的合作可能性。
   - 鼓励社区成员参与 UI 开发。

**三、其他事项**

1. **文档聚合**：
   - 讨论了将文档聚合到 ceph.com 的可能性。

2. **Ceph 官网**：
   - 讨论了 Ceph 官网的重构计划。

**行动计划**：

1. John Gregor 和 Sage 负责推进 Crush 管理功能的开发。
2. Sage 负责清理使用 Salt 私有接口的代码。
3. Sage 负责将 Diamond 和 Graphite 的分支合并到上游。
4. Sage 负责改进打包方式，简化前端构建过程。
5. Sage 负责移除 DoSulu 插件管理器。
6. 社区成员参与 UI 开发。
7. 讨论文档聚合和 Ceph 官网的重构计划。

**会议总结**：

本次会议讨论了 Calamari 的开发计划、社区合作以及其他相关事项。会议明确了下一步的工作计划和行动计划，为 Calamari 的发展奠定了基础。