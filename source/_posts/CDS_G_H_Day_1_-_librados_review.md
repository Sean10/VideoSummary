---
title: "CDS G/H (Day 1) - librados review"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议主题**： Ceph 分布式存储项目会议，重点讨论 Liberatos 代码库的审查、开发流程、技术领导角色引入、发布周期以及 OSD 审查。

**会议关键细节**：

* **开发流程与参与方式**：
    * 通过邮件列表（如 self-dev@ceph.com、calamari-dev@ceph.com、packaging-maintainers@ceph.com）和 IRC（irc.otc.net）参与开发讨论。
    * 使用 GitHub 提交代码和 pull request。
    * 利用 feature tracker 寻找工作机会并报告 bug。
    * 技术领导角色引入：为特定组件指定技术架构负责人，负责代码审查、优先级排序和项目方向。
    * 关键人员：
        * 核心 Rados：Sam Jess
        * Rados 块设备：Josh Durkin
        * Rados Gateway：Yehuda
        * 文件系统：Greg、Jung Yan
        * Calamari：Gregory Amino
        * 测试框架：Zach
        * 部署工具：Deza
        * Chef cookbooks：Gilham Electron
    * 测试基础设施：
        * Get：构建和测试不同发行版和软件包。
        * Popit：集成测试基础设施的 Web 前端。
* **发布周期**：
    * 过去采用每季度一次的命名版本发布，包含两个月编码和一个月 QA。
    * 最近采用每季度一次的 Firefighter 版本，由于新功能集成挑战，导致时间表延迟。
    * 未来考虑采用定期发布，稳定现有功能，不急于合并新功能。
    * 是否继续每季度一次的命名发布存在争议，需要进一步讨论。
* **Liberatos 审查**：
    * 内部线程模型更改：为提高 IOPS 性能，将全局锁分解为多个更小的锁，使用读写锁和原子操作。
    * 并行读取：通过并行读取副本以减少延迟。
    * 跟踪：捕获和回放 Liberatos 级别的跟踪，以便在开发过程中模拟实际工作负载。
* **OSD 审查**：
    * 会议中未详细讨论，需要进一步了解。

**讨论的主要议题**：

* 如何吸引更多开发者参与 Ceph 项目。
* 引入技术领导角色，明确责任和职责。
* 确定发布周期，平衡稳定性和新功能。
* 改进 Liberatos 和 OSD 的性能和功能。

**决定的事项**：

* 继续讨论发布周期，并在邮件列表上提出意见。
* 继续推进 Liberatos 和 OSD 的改进工作。
* 鼓励更多开发者参与 Ceph 项目。

**后续行动计划**：

* 继续讨论发布周期，并在邮件列表上提出意见。
* 完成 Liberatos 和 OSD 的改进工作。
* 鼓励更多开发者参与 Ceph 项目，并为他们提供支持。

**备注**：

* 会议中提到的一些英文关键词：
    * Ceph
    * Liberatos
    * OSD
    * Rados
    * Calamari
    * GitHub
    * pull request
    * feature tracker
    * CI/CD
    * IOPS
    * latency
    * consistency
    * scrubbing
    * repair
    * blueprint
    * trace
    * replay