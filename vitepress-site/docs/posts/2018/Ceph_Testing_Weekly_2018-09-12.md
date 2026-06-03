---
title: "Ceph Testing Weekly 2018-09-12"
date: 2018-09-12
updated: 2018-09-13
tags:
  - "Ceph"
  - "分布式存储"
categories:
  - "视频总结"
outline: deep
---
### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Greg, Zack, Nathan, Kier, David等

**会议主题**： Ceph分布式存储项目开发与测试进展讨论

**关键细节与讨论议题**：

* **人员情况**： 
    * 由于地理原因和紧急家庭事务，Red Hat的同事无法参加本次会议。
    * Greg因产品工作和个人休假未能积极参与，但仍在跟进相关工作。
    * Nathan和Kier讨论了Ceph CI Ansible项目的进展和优化方案。
    * David分享了OpenSUSE镜像制作的情况。
* **Ceph CI Ansible项目**：
    * **工作流程优化**：
        * 讨论了Ceph CI Ansible项目的工作流程，包括部署测试实例、管理worker进程等。
        * 认为当前的工作流程存在问题，需要改进。
        * 讨论了使用Systemd服务、独立应用、Ansible模块等方式来优化工作流程。
    * **版本控制和集成测试**：
        * 讨论了Ceph CI Ansible项目的版本控制和集成测试问题。
        * 认为需要将Ceph、Paddle、Papito等项目拆分成独立的Python库或项目，并使用pip进行安装和管理。
        * 讨论了使用Ansible模块、聚合仓库等方式来实现集成测试。
    * **OpenSUSE镜像制作**：
        * 讨论了OpenSUSE镜像制作的情况，包括镜像制作工具和部署过程。
        * 认为需要将OpenSUSE镜像提供给David，以便用于测试环境搭建。
* **其他议题**：
    * 讨论了Ceph项目的Python 3迁移和flake8代码风格检查工具的使用。

**决定的事项**：

* Nathan将跟进Ceph CI Ansible项目的优化工作，包括改进工作流程、实现版本控制和集成测试等。
* David将尝试使用OpenSUSE镜像搭建测试环境。
* 讨论了使用Ansible模块、聚合仓库等方式来实现集成测试的可行性。

**后续行动计划**：

* Nathan将整理Ceph CI Ansible项目的优化方案，并与团队讨论。
* David将尝试使用OpenSUSE镜像搭建测试环境，并反馈结果。
* 团队将讨论集成测试的实现方案。

**关键词**：

* Ceph CI Ansible
* Systemd
* 独立应用
* Python库
* pip
* OpenSUSE
* 集成测试
* flake8
* Ceph
* 分布式存储
* 自动化测试
* CI/CD
* DevOps