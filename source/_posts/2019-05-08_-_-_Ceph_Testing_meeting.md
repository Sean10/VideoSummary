---
categories:
- 视频总结
date: 2019-05-28
subtitle: 2019-05-08_-_-_Ceph_Testing_meeting
tags:
- Ceph
- 分布式存储
- 测试
- Rook
title: "'2019-05-08 :: Ceph Testing meeting'"
updated: 2019-05-28
---


### 会议纪要

**会议时间**： 2023年11月某日

**参会人员**： Sebastian, Greg

**会议主题**： Ceph项目进展及视频会议字幕翻译相关事宜

**会议内容**：

**1. Ceph项目进展**

* **Look into Totality集成**： Greg指出，目前将Look集成到Totality的计划不可行，但从长远来看，这是一个值得考虑的方向。由于Greg正在忙于另一个Rados相关项目，短期内不会继续推进集成工作。
* **Rook集成测试**： Sebastian提到，计划通过集成测试将Rook集成到Ceph环境中。他将使用最新的self容器构建，并在Jenkins中运行测试。
* **Jenkins集成**： Greg表示，为了在Jenkins中实现Rook测试，需要为Pull Requests构建容器镜像，但目前该功能尚未实现。
* **Rook集群**： Sebastian询问是否有可用的Rook集群进行测试，David Galloway等人可能在使用一个Rook集群，但具体位置不明。
* **Jenkins运行环境**： Greg不确定Jenkins运行环境是否有权限访问相关基础设施，需要进一步调查。

**2. 视频会议字幕翻译**

* **字幕翻译**： Sebastian负责英译中的字幕翻译工作。
* **测试orchestrator**： Greg询问Sebastian关于某个测试orchestrator的事情，Sebastian表示他将会推进这个项目。

**3. 决定事项**

* 暂时搁置集成Look into Totality的计划。
* 推进Rook集成测试，并在Jenkins中实现。
* 调查Rook集群的可用性。
* 进一步调查Jenkins运行环境的权限问题。
* Sebastian将继续推进字幕翻译工作。

**4. 后续行动计划**

* Greg将调查Rook集群的可用性，并与David Galloway等人联系。
* Greg将调查Jenkins运行环境的权限问题，并尝试解决。
* Sebastian将继续推进Rook集成测试和字幕翻译工作。

**5. 其他事项**

* 会议中提到了一些计算机科学/ceph相关领域英文关键词，例如：
    * Rados
    * systemd
    * Rook
    * Jenkins
    * Pull Requests
    * Container
    * Terraform
    * Vagrant

**备注**：

* 会议中提到的项目名称和术语可能需要根据实际情况进行调整。