---
title: "2019-10-21 :: Ceph Orchestration Meeting"
date: 2019-10-21
updated: 2019-10-22
tags:
  - "编排"
  - "Rook"
  - "OSD"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2019年10月21日（具体日期未提及）

**会议地点**： 线上会议

**参会人员**： 未知（会议纪要中未提及具体姓名）

**会议主题**：

*   Ceph Orchestrator相关议题
*   Rook项目进展
*   安全守护进程（sage daemon）相关讨论

### 关键细节

**Ceph Orchestrator相关议题**

*   **预览驱动器组功能**： 新的Pull Request允许在仪表板和编排器中预览驱动器组，但需要依赖Rook的卷库存功能。
*   **Rook项目进展**： 讨论了Rook 1.1.3版本，计划修复OSD配置和升级问题。
*   **安全守护进程（sage daemon）**： 讨论了sage daemon的功能和范围，以及是否将其作为独立项目或集成到Ceph源代码树中。

**Rook项目进展**

*   **Rook 1.1.3版本**： 计划明天发布，主要修复了OSD配置和升级问题。
*   **OSD配置问题**： 配置覆盖没有被正确应用，需要进一步调查和修复。
*   **OSD升级问题**： 需要确保在升级过程中始终进行OSD pod的同步。

**安全守护进程（sage daemon**）

*   **功能**： sage daemon用于启动和管理安全守护进程，包括创建密钥环、配置守护进程等。
*   **范围**： 讨论了sage daemon的功能和范围，以及是否将其作为独立项目或集成到Ceph源代码树中。
*   **独立项目**： 一些参与者认为sage daemon应该作为一个独立项目进行开发，以便更好地控制其版本和功能。
*   **集成到Ceph源代码树中**： 一些参与者认为sage daemon应该集成到Ceph源代码树中，以便更好地与Ceph生态系统整合。

### 决定的事项

*   **Rook 1.1.3版本**： 计划明天发布。
*   **sage daemon**： 需要进一步讨论和决策。

### 后续行动计划

*   **Rook 1.1.3版本**： 发布Rook 1.1.3版本。
*   **sage daemon**： 
    *   发布sage daemon的设计文档。
    *   讨论sage daemon的集成方案。
    *   确定sage daemon的开发和发布计划。

### 计算机科学/ceph相关领域英文原文关键词

*   Ceph Orchestrator
*   Rook
*   sage daemon
*   Pull Request
*   Inventory
*   OSD
*   Upgrade
*   Configuration
*   Dependency
*   Scope
*   Integration