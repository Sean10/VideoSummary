---
title: "2018-Jun-20 :: Ceph Testing Weekly"
date: 2018-06-20
updated: 2018-06-21
tags:
  - "Ceph"
  - "OpenStack"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
本次会议主要讨论了Ceph存储系统中Telltale测试框架的更新与改进。会议中涉及的关键细节包括：

* Telltale测试框架目前依赖于OpenStack基础设施，环境搭建复杂，维护成本高，且测试覆盖率有限。
* 讨论了使用OVH实例搭建测试环境，并利用Jenkins进行测试任务调度。
* 创建了特定测试套件，如smoke test和fault test，以验证Telltale的基本功能。
* 探索了更新Telltale测试套件，提高测试覆盖率，并考虑将Telltale拆分为多个模块。
* 讨论了使用Web应用程序管理Telltale的测试和部署，以及研究使用其他测试框架或工具替代Telltale的部分功能。
* 探索了与其他社区合作，共享测试资源和经验。

会议决定的事项包括：

* 使用OVH实例搭建测试环境。
* 使用Jenkins进行测试任务调度。
* 创建特定测试套件。
* 更新Telltale测试套件，提高测试覆盖率。
* 探索使用分支或标签管理Telltale版本。
* 引入更智能的调度器，优化测试资源分配。
* 考虑将Telltale拆分为多个模块。
* 探索使用Web应用程序管理Telltale的测试和部署。
* 研究使用其他测试框架或工具替代Telltale的部分功能。
* 探索与其他社区合作，共享测试资源和经验。

后续行动计划包括：

* Zack将继续开发libcloud后端，以便在OpenStack中创建临时的Telltale部署。
* Mike将尝试运行Telltale测试套件，并查看其是否能够正常运行。
* Greg将整理会议中讨论的所有想法，并将其记录在etherpad中。
* 所有参会人员将继续探讨Telltale测试框架的改进方案。

本次会议内容涵盖了Ceph测试框架的改进，测试环境搭建，测试流程优化，开发模式探索等多个方面，对于Ceph社区的测试工作具有重要意义。