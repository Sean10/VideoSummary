---
title: "2018-Jun-13 :: Ceph Testing Weekly"
date: 2018-06-19
updated: 2018-06-20
tags:
  - "RGW"
categories:
  - "视频总结"
outline: deep
---
**会议纪要**

**会议时间**： 2023年11月（具体日期未提及）

**参会人员**： 多位Ceph社区成员，包括Zach、Greg、Rick、Ally、Tatiana、Yuri等。

**会议主题**：

* 检查上次会议的行动项完成情况
* 讨论Ceph测试框架Tautology的改进和扩展
* 探索使用Libcloud进行测试的可能性
* 讨论Ceph RGW功能测试的改进
* 讨论Ceph安全仪表板的测试

**关键细节**：

* **上次会议行动项**：
    * 红帽工程师创建的Redmine工单尚未创建。
    * 需要更多PR以便进行审查和测试。
    * 需要为Tautology编写开发指南文档。
    * 需要为Tautology集成测试环境编写Ansible脚本。
* **Tautology改进**：
    * 讨论了将Asuza的OpenStack后端补丁合并到Tautology中，并使用Libcloud进行测试。
    * 讨论了使用Tautology进行测试时的节点分配问题。
    * 讨论了为Tautology编写文档，以帮助开发者编写任务。
    * 讨论了将Tautology部署到Jenkins以进行测试。
* **Ceph RGW功能测试**：
    * 讨论了使用Tautology对RGW进行测试，包括S3测试和RGW管理员套件测试。
    * 讨论了为RGW测试编写Ansible脚本。
    * 讨论了使用Tautology进行升级测试，例如将Ceph集群从Luminous升级到Mimic。
* **Ceph安全仪表板的测试**：
    * Tatiana介绍了Red Hat的Ceph安全仪表板（Set Metrics），并讨论了如何对其进行测试。

**决定的事项**：

* 红帽工程师将继续创建Redmine工单。
* 红帽工程师将审查和合并更多PR。
* 红帽工程师将为Tautology编写开发指南文档。
* 红帽工程师将为Tautology集成测试环境编写Ansible脚本。
* 红帽工程师将与社区成员合作，改进和扩展Tautology。
* 红帽工程师将使用Tautology进行Ceph RGW功能测试和升级测试。
* 红帽工程师将探索使用Libcloud进行测试的可能性。

**后续行动计划**：

* 红帽工程师将在下次会议之前完成上述行动项。
* 红帽工程师将参加RGW站立会议，讨论Ceph RGW功能测试的改进。
* 红帽工程师将与社区成员合作，改进和扩展Tautology。

**其他**：

* 会议中讨论了一些其他话题，例如Ceph社区会议的安排和Ceph安全仪表板的开发。
* 会议结束时，红帽工程师将整理会议纪要并发送给参会人员。