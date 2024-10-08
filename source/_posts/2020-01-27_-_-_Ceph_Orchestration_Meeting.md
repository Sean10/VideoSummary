---
title: "2020-01-27 :: Ceph Orchestration Meeting"
date: 2020-01-30
updated: 2020-01-30
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 参会人员
- Josh（未参加）
- Petrus
- 其他相关人员

#### 会议时间
- 会议开始时间：待定（等待Josh加入）

#### 主要议题
1. **Ceph Python客户端库的存储位置**
   - **讨论内容**：
     - Ostia提出将Ceph Python客户端库作为外部依赖，而不是合并到Rook项目中。
     - 讨论了将库放在Rook组织下的单独仓库的利弊。
     - 讨论了版本管理和CI的复杂性。
   - **决定**：
     - 同意将Ceph Python客户端库作为一个独立的仓库，以增加灵活性并减少问题。
     - 将创建一个新的仓库在Rook组织下，并由Sebastian负责管理。

2. **Rook项目的其他更新**
   - **Ceph客户端库的发布方式**：
     - 讨论了使用pip安装和后续的RPM包创建。
   - **Rook项目的其他进展**：
     - 讨论了EUR/USD重构、Raw模式支持、PVC模型扩展等技术细节。

3. **CI和日志管理**
   - **CI改进**：
     - 讨论了使用GitHub Actions来同步两个仓库，确保客户端代码的更新与CRD的变更同步。
   - **日志管理**：
     - 讨论了改进日志管理，以便更好地监控和调试部署过程中的问题。

#### 后续行动计划
- 创建新的Ceph Python客户端库仓库。
- 继续改进CI流程，确保客户端代码的自动更新。
- 进一步讨论和实施日志管理的改进措施。

#### 其他事项
- 确认Trello板上的任务已迁移到Tracker。
- 讨论了使用Podman来优化容器元数据的获取。

#### 会议结束
- 会议在讨论了所有议题后结束，期待后续的进展和实施。

---

以上是本次会议的详细纪要，涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划。