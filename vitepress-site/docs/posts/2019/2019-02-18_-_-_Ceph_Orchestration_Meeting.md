---
title: "2019-02-18:: Ceph Orchestration Meeting"
date: 2019-02-22
updated: 2019-02-23
tags:
  - "Ceph"
  - "分布式存储"
  - "编排"
  - "会议纪要"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议时间**： 2019年2月18日
**会议地点**： [具体地点]
**参会人员**： [列出参会人员名单]
**会议主题**： Ceph分布式存储项目进展及讨论

**会议内容**：

**1. 错误处理进展**
- 项目成员汇报了上周错误处理的进展，已根据反馈进行了改进，命令行界面和异常定义方面均有提升。
- 提出在SAP解释器中传递异常并正确捕获的问题，建议使用pickle和unpickle异常。
- 希望得到更多关于最终实现的反馈。

**2. SSH Orchestrator进展**
- 汇报了添加Toulouse里程碑到SSH Orchestrator的进展，希望尽快合并。
- 讨论了测试模块的依赖问题，由于依赖包未在Ubuntu上提供，测试无法进行。
- 决定先合并Ansible的pull request，确保测试通过，然后再解决依赖问题。

**3. Ceph状态Orchestrator**
- 报告了Ceph状态Orchestrator的进展，在Ubuntu上部署成功。
- 讨论了Rook的PR，包括主机标签设置和节点亲和性等问题。
- 决定先合并PR，解决兼容性问题，然后再讨论更复杂的特性。

**4. Nautilus 41.0和Rook**
- 讨论了Nautilus 41.0和Rook的集成测试，将在Messenger 2 PR合并后进行。
- 报告了Rook模块Orchestrator模块加载问题的解决进展，预计明天将进入稳定版本。
- 讨论了Ganesha实例的扩展和收缩，以及NFS更新等问题。

**5. 其他**
- 讨论了集成测试平台，包括使用bootstrap集群和Behave进行测试。
- 讨论了SSH Orchestrator在OpenSUSE上的测试进展。

**行动计划**：

- 项目成员继续改进错误处理和SSH Orchestrator。
- 解决Rook模块的依赖问题。
- 合并Ceph状态Orchestrator和Nautilus 41.0的PR。
- 进行Nautilus 41.0和Rook的集成测试。
- 完成Ganesha实例的扩展和收缩，以及NFS更新。
- 推进集成测试平台的开发。

**备注**：

- 会议中提到了一些计算机科学/ceph相关领域英文关键词，如SAP interpreter, pickle, unpickle, Kubernetes, node affinity, Nautilus, Rook, Ganesha等。