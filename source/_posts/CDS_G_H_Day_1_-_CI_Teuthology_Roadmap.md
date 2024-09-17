---
title: "CDS G/H (Day 1) - CI & Teuthology Roadmap"
date: 2014-06-24
updated: 2014-06-25
tags:
categories:
- "视频总结"
subtitle: tech
---



**会议纪要**

**会议主题**： Ceph CI和Tutorials路线图讨论

**参会人员**： Sage, Zach, Alfredo, L, Greg, Luis等

**会议内容**：

**1. Toothology路线图**

* Zach介绍了Toothology的最新进展，包括：
    * 将Toothology任务从框架工作中分离出来，以便更好地扩展和维护。
    * 将队列和锁定机制迁移到一个新的服务Paddles，并使用Bito作为UI。
    * 对Toothology内部作业调度方式进行改进。
    * 计划使用OpenStack作为后端来部署虚拟机，以简化Toothology的安装和设置。
* 讨论了Toothology测试套件对裸金属机器的依赖性，以及如何使用虚拟机进行测试。
* 讨论了如何使Toothology更具通用性，以便测试其他分布式系统。

**2. CI流程改进**

* 讨论了如何改进Ceph的CI流程，以确保所有代码更改在合并到主分支之前都经过充分测试。
* 提出了使用类似Linux Next的方法，通过建立一个每晚构建的临时分支，并在此分支上运行完整测试套件。
* 讨论了如何使用Jenkins或Travis CI等工具来实现这一目标，并确保测试结果能够及时反馈给开发者。
* 讨论了如何处理失败的构建，以及如何将测试结果注释到相关的Pull Request中。

**3. 其他讨论**

* 讨论了如何命名集成分支，以及如何管理历史构建。
* 讨论了是否使用Jenkins或Travis CI作为CI工具，并考虑了各自的优缺点。
* 讨论了如何改进Jenkins配置，以提高其效率和可维护性。

**行动计划**：

* Zach继续推进Toothology的开发工作。
* 讨论组将制定详细的CI流程改进计划，并选择合适的工具和策略。
* 相关人员将负责实现CI流程改进计划，并进行测试和验证。

**备注**：

* 会议中提到了一些关键的技术术语，如Toothology、Paddles、Bito、OpenStack、Jenkins、Travis CI等。
* 会议中讨论了一些具体的实现细节，如分支命名、测试结果反馈等。