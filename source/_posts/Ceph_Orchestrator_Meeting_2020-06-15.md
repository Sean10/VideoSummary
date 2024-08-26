---
title: "Ceph Orchestrator Meeting 2020-06-15"
date: 2020-06-15
updated: 2020-06-16
tags:
categories:
- "视频总结"
subtitle: tech
---


### 会议纪要

#### 会议概要
- **日期**: [具体日期]
- **参会人员**: [参会人员名单]
- **主持人**: [主持人姓名]

#### 主要议题
1. **Sofia Morgan的新需求**
   - 提出了一个新的需求，具体细节待补充。

2. **新增Tautology测试**
   - 讨论了如何轻松添加新的Tautology测试到Ceph中，希望未来能广泛应用。

3. **ETCD配置管理**
   - 正在研究ETCD配置管理，认为这是一个重要的功能。

4. **Drive Groups规范**
   - 通过邮件已经基本解决了Drive Groups的规范问题，会议上再次确认了相关细节。
   - 讨论了如何在Rook中处理Drive Groups，特别是如何将Drive Groups转换为Kubernetes的Placement规范。

5. **开发环境讨论**
   - 讨论了多种开发环境的优缺点，包括使用restart、bootstrap和C start等。
   - 提出了使用Kay CLI工具来创建和管理开发环境，该工具能够快速设置虚拟机并映射开发文件夹到主机，以便于开发和测试。

6. **每日测试运行**
   - 讨论了设置每日自动运行Rook测试的计划，目前正在准备相关的基础设施。

#### 决定事项
- **Drive Groups处理**：确认了将Drive Groups转换为Kubernetes Placement规范的方法，并将在Rook中实施。
- **开发环境**：鼓励使用Kay CLI工具来设置开发环境，并计划进一步完善相关文档和演示。
- **每日测试**：将继续推进每日自动运行Rook测试的计划，确保测试的持续性和可靠性。

#### 后续行动计划
- **Drive Groups实施**：Sebastian将跟进Drive Groups的实施细节，并确保与Kubernetes Placement规范的正确转换。
- **开发环境优化**：Sumukha将准备一个关于使用Kay CLI工具的演示，并更新开发文档。
- **每日测试设置**：Paul Miguel将继续推进每日测试的自动化设置，并与Adam讨论CI的相关事宜。

#### 其他
- 会议中还讨论了一些其他小议题，但未形成具体决议。

#### 会议结束
- 会议在确认无其他议题后结束，并约定下周再次开会。

---

**备注**: 本次会议记录涵盖了会议的关键细节、讨论的主要议题、决定的事项以及后续的行动计划，确保了会议内容的完整性和准确性。